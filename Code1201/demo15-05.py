from scipy.stats import pearsonr
from scipy.interpolate import interp1d
from matplotlib.backends.backend_pdf import PdfPages
from scipy.interpolate import NearestNDInterpolator, RBFInterpolator
from pygsp2 import graphs, learning
from scipy.spatial.distance import squareform, pdist
import pandas as pd
import mne
import os
import datetime
from mne.channels import read_custom_montage
import matplotlib.pyplot as plt
import numpy as np
from itertools import product
from collections import defaultdict
import seaborn as sns

# Intentar importar joypy, si no está, se omitirá el ridgeline plot
try:
    import joypy
    JOYPY_AVAILABLE = True
except ImportError:
    JOYPY_AVAILABLE = False
    print("Advertencia: La librería 'joypy' no está instalada. El Ridgeline Plot para MAE no se generará.")

plt.close('all')

# =============================================================================
# Placeholder for custom modules (debes tener interpolation.py y construction.py)
# =============================================================================
try:
    from interpolation import spherical_spline_interpolation, gsp_BGSRP_recon
except ImportError:
    print("Advertencia: Módulo 'interpolation' no encontrado. Spherical Spline y BGSRP podrían fallar o usar dummies.")

    # Mantener firma actualizada
    def spherical_spline_interpolation(X, values, s_initial=1.0, s_retry_factor=5, max_s_retry=10000.0):
        print(f"spherical_spline_interpolation ({
              s_initial=}) llamada (dummy).")
        nan_indices = np.isnan(values)
        result = np.zeros_like(values)
        result[nan_indices] = np.nan
        return result

    def gsp_BGSRP_recon(graph, missing_idx, y0, param_BGSRP):
        print("gsp_BGSRP_recon llamada (dummy).")
        return [np.full_like(y0, np.nan)]

try:
    from construction import vkNNG, adjacency_matrix, adaptive_edge_weighting, NNK, kaliofolias
except ImportError:
    print("Advertencia: Módulo 'construction' no encontrado. Métodos de construcción de grafos podrían fallar o usar dummies.")

    def dummy_adjacency_matrix(X, k_or_radius, sigma, method):
        N_adj = X.shape[0]
        print(f"dummy_adjacency_matrix for {method} llamada (dummy).")
        # Importar lil_matrix aquí para evitar error si scipy no está completamente importado aún
        from scipy.sparse import lil_matrix
        return lil_matrix((N_adj, N_adj)), None

    def vkNNG_fallback(Z_scaled, k_min, k_max, beta_factor): return (
        dummy_adjacency_matrix(Z_scaled, k_min, 0, 'vkNNG_dummy')[0].toarray(), None)

    def adaptive_edge_weighting_fallback(X, W_knn, sigma): return dummy_adjacency_matrix(
        X, 0, sigma, 'AEW_dummy')[0].toarray()

    def NNK_fallback(X, k): return (dummy_adjacency_matrix(X, k, 0, 'NNK_dummy')[
        0].toarray(), dummy_adjacency_matrix(X, k, 0, 'NNK_knn_dummy')[0].toarray())

    def kaliofolias_fallback(Z_scaled, a, b, gamma): return dummy_adjacency_matrix(
        Z_scaled, 0, 0, 'Kaliofolias_dummy')[0].toarray()

    adjacency_matrix = dummy_adjacency_matrix
    vkNNG = vkNNG_fallback
    adaptive_edge_weighting = adaptive_edge_weighting_fallback
    NNK = NNK_fallback
    kaliofolias = kaliofolias_fallback
# =============================================================================

# Configuración de datos MNE
data_path = mne.datasets.sample.data_path()
subjects_dir = data_path / "subjects"
fname_raw = data_path / "MEG" / "sample" / "sample_audvis_raw.fif"
misc_path = mne.datasets.misc.data_path()
fname_mon = misc_path / "sample_eeg_mri" / "sample_mri_montage.elc"

dig_montage = read_custom_montage(
    fname_mon, head_size=None, coord_frame="mri", verbose="error")
raw = mne.io.read_raw_fif(fname_raw, preload=True)
raw.pick(picks=["eeg", "stim"])
raw.set_montage(dig_montage)
raw.set_eeg_reference(projection=True)
events = mne.find_events(raw)
epochs = mne.Epochs(raw, events)
evoked = epochs["1"].average()
# Renombrado para evitar confusión con pd más adelante
df_evoked = evoked.to_data_frame()
times = df_evoked.to_numpy()[:, 0]
signals = df_evoked.to_numpy()[:, 1:]
sensor_pos_dict = dig_montage.get_positions()['ch_pos']
ch_names_from_evoked = evoked.ch_names
X = np.array([sensor_pos_dict[ch]
             for ch in ch_names_from_evoked if ch in sensor_pos_dict])
original_signal_ch_names = df_evoked.columns[1:]
valid_ch_indices = [i for i, name in enumerate(
    original_signal_ch_names) if name in sensor_pos_dict]
signals = signals[:, valid_ch_indices]
N, d = X.shape
T = signals.shape[0]
print(f"Número de canales (N): {N}, Puntos de tiempo (T): {
      T}, Forma de señales: {signals.shape}")

# Escalado de posiciones de sensores
X_scaled = X - np.mean(X, axis=0)
bounding_radius = 0.5 * \
    np.linalg.norm(np.amax(X_scaled, axis=0) - np.amin(X_scaled, axis=0), 2)
scale = np.power(N, 1. / float(min(d, 3))) / 10.
if bounding_radius > 1e-9:  # Evitar división por cero si todos los puntos son iguales
    X_scaled *= scale / bounding_radius
else:
    print("Advertencia: Bounding radius es cero o muy pequeño. Escalado de X no se aplicó como se esperaba.")
Z_scaled = squareform(pdist(X_scaled))

# Hiperparámetros para construcción de grafos
# Evitar NaN/cero si Z_scaled es problemático
sigma = np.mean(Z_scaled[Z_scaled > 0]) / 3 if np.any(Z_scaled > 0) else 0.1
radius = np.mean(Z_scaled[Z_scaled > 0]) if np.any(Z_scaled > 0) else 0.3
k = 5
k_min, k_max, beta_factor = 2, 10, 0.01
a_kal, b_kal, gamma_kal = 0.34, 0.4, 0.04

# Hiperparámetros de interpolación
param_grid = {
    "Tikhonov": {"tau_tik": [0.01, 0.1, 1]},
    # Asegurar bandw > 0
    "BGSRP": {"bandw": [N // 10 if N // 10 > 0 else 1, N // 4 if N // 4 > 0 else 2], "gamma_bgsrp": [0.01, 1]},
    "RBFI MQ": {"epsilon_MQ": [1.0, 1.1]},
    "Spline Superficie": {"s_SSI": [10.0, 50.0, 100.0]}
}

# Construcción de Grafos (una vez)
print("Construyendo grafos...")
graphs_dict = {}
weights_dict = {}
try:
    W_knn, _ = adjacency_matrix(X_scaled, k, sigma=sigma, method="knn")
    G_knn = graphs.Graph(W_knn.toarray() if not isinstance(
        W_knn, np.ndarray) else W_knn)
    G_knn.compute_fourier_basis()
    weights_dict[f"KNN(k={k},σ={sigma:.2f})"] = G_knn.W.toarray()
    graphs_dict[f"KNN(k={k},σ={sigma:.2f})"] = G_knn

    # Añadir otros constructores de grafos aquí como antes...
    # Ejemplo:
    W_enn, _ = adjacency_matrix(
        X_scaled, radius=radius, sigma=sigma, method="radius_neighbors")
    G_enn = graphs.Graph(W_enn.toarray() if not isinstance(
        W_enn, np.ndarray) else W_enn)
    G_enn.compute_fourier_basis()
    weights_dict[f"Radius(r={radius:.2f},σ={sigma:.2f})"] = G_enn.W.toarray()
    graphs_dict[f"Radius(r={radius:.2f},σ={sigma:.2f})"] = G_enn

    # ... (VKNN, AEW, NNK, Kaliofolias, asegurando que devuelven arrays y G.compute_fourier_basis() se llama)
    W_vknn_val, _ = vkNNG(Z_scaled, k_min, k_max, beta_factor)
    G_vknn = graphs.Graph(W_vknn_val)
    G_vknn.compute_fourier_basis()
    weights_dict[f"VKNN(k_min={k_min},k_max={k_max},β={
        beta_factor})"] = G_vknn.W.toarray()
    graphs_dict[f"VKNN(k_min={k_min},k_max={k_max},β={beta_factor})"] = G_vknn

    W_aew_val = adaptive_edge_weighting(
        X_scaled, G_knn.W.toarray(), sigma)  # AEW usa W_knn
    G_aew = graphs.Graph(W_aew_val)
    G_aew.compute_fourier_basis()
    weights_dict[f"AEW(k={k},σ={sigma:.2f})"] = G_aew.W.toarray()
    graphs_dict[f"AEW(k={k},σ={sigma:.2f})"] = G_aew

    W_nnk_val, W_knn_nnk_val = NNK(X_scaled, k)
    G_nnk = graphs.Graph(W_nnk_val)
    G_nnk.compute_fourier_basis()
    weights_dict[f"NNK(k={k})"] = G_nnk.W.toarray()
    graphs_dict[f"NNK(k={k})"] = G_nnk
    # weights_dict[f"KNN_sub(NNK, k={k})"] = W_knn_nnk_val # Opcional: para visualizar el KNN usado en NNK

    W_kaliofolias_val = kaliofolias(Z_scaled, a_kal, b_kal, gamma_kal)
    G_kaliofolias = graphs.Graph(W_kaliofolias_val)
    G_kaliofolias.compute_fourier_basis()
    weights_dict[f"Kaliofolias(a={a_kal},b={b_kal},γ={
        gamma_kal:.2f})"] = G_kaliofolias.W.toarray()
    graphs_dict[f"Kaliofolias(a={a_kal},b={b_kal},γ={
        gamma_kal:.2f})"] = G_kaliofolias

    print("Grafos construidos.")
except Exception as e_graph:
    print(f"Error durante la construcción de grafos: {
          e_graph}. Métodos basados en grafos podrían fallar.")
    # Crear dummies si falla la construcción
    from scipy.sparse import csgraph, diags
    dummy_W = diags(np.random.rand(N), 0, shape=(N, N), format="csr")
    dummy_W = dummy_W + dummy_W.T  # Simetrizar
    dummy_G = graphs.Graph(dummy_W)
    try:
        dummy_G.compute_fourier_basis()
    except Exception:
        print("Fallo al calcular base de Fourier para grafo dummy")

    graph_names_fallback = [f"KNN(k={k},σ={sigma:.2f})", f"Radius(r={radius:.2f},σ={sigma:.2f})",
                            f"VKNN(k_min={k_min},k_max={k_max},β={
        beta_factor})", f"AEW(k={k},σ={sigma:.2f})",
        f"NNK(k={k})", f"Kaliofolias(a={a_kal},b={b_kal},γ={gamma_kal:.2f})"]
    for name in graph_names_fallback:
        if name not in graphs_dict:
            graphs_dict[name] = dummy_G
        if name not in weights_dict:
            weights_dict[name] = dummy_W.toarray()


# Almacenamiento de resultados MAE
all_scenarios_mae_results = defaultdict(list)
pdf_figs = []  # Para guardar figuras en PDF

# Iterar sobre cada electrodo como faltante
for missing_electrode_idx in range(N):
    print(f"Procesando escenario: Electrodo {
          missing_electrode_idx+1}/{N} faltante...")
    mask = np.ones(N, dtype=bool)
    mask[missing_electrode_idx] = False

    mae_values_at_each_t_current_scenario = defaultdict(list)

    for t in range(T):  # Iterar sobre instantes de tiempo
        signal_at_t = signals[t, :]
        true_value_at_missing_electrode = signal_at_t[missing_electrode_idx]
        measures_at_t = signal_at_t.copy()
        measures_at_t[missing_electrode_idx] = np.nan
        known_values = measures_at_t[mask]
        known_positions = X[mask, :]
        missing_position = X[[missing_electrode_idx], :]
        y_hat = np.nan  # Valor de interpolación por defecto

        # --- Métodos sin grafo ---
        # NNI
        label_nni = "NNI"
        y_hat_nni = np.nan
        try:
            interpolator_nni = NearestNDInterpolator(
                known_positions, known_values)
            y_hat_nni_arr = interpolator_nni(missing_position)
            y_hat_nni = y_hat_nni_arr[0]
            mae_values_at_each_t_current_scenario[label_nni].append(
                np.abs(y_hat_nni - true_value_at_missing_electrode))
        except Exception:
            mae_values_at_each_t_current_scenario[label_nni].append(np.nan)

        # RBFI TPS
        label_rbf_tps = "RBFI TPS"
        y_hat_rbf_tps = np.nan
        try:
            # kernel='thin_plate_spline' por defecto
            interpolator_rbf_tps = RBFInterpolator(
                known_positions, known_values)
            y_hat_rbf_tps_arr = interpolator_rbf_tps(missing_position)
            y_hat_rbf_tps = y_hat_rbf_tps_arr[0]
            mae_values_at_each_t_current_scenario[label_rbf_tps].append(
                np.abs(y_hat_rbf_tps - true_value_at_missing_electrode))
        except Exception:
            mae_values_at_each_t_current_scenario[label_rbf_tps].append(np.nan)

        # RBFI MQ (con bucle de parámetros)
        for epsilon in param_grid["RBFI MQ"]["epsilon_MQ"]:
            label_rbf_mq = f"RBFI MQ(ε={epsilon})"
            y_hat_rbf_mq = np.nan
            try:
                interpolator_rbf_mq = RBFInterpolator(
                    known_positions, known_values, kernel='multiquadric', epsilon=epsilon)
                y_hat_rbf_mq_arr = interpolator_rbf_mq(missing_position)
                y_hat_rbf_mq = y_hat_rbf_mq_arr[0]
                mae_values_at_each_t_current_scenario[label_rbf_mq].append(
                    np.abs(y_hat_rbf_mq - true_value_at_missing_electrode))
            except Exception:
                mae_values_at_each_t_current_scenario[label_rbf_mq].append(
                    np.nan)

        # Spline Superficie (con bucle de parámetros)
        for s_param in param_grid["Spline Superficie"]["s_SSI"]:
            label_spline = f"Spline Superficie(s={s_param})"
            y_hat_spline = np.nan
            try:
                interpolated_signal_full = spherical_spline_interpolation(
                    X, measures_at_t, s_initial=s_param)
                y_hat_spline = interpolated_signal_full[missing_electrode_idx]
                if pd.notna(y_hat_spline):  # Solo calcular error si la interpolación no fue NaN
                    mae_values_at_each_t_current_scenario[label_spline].append(
                        np.abs(y_hat_spline - true_value_at_missing_electrode))
                else:
                    mae_values_at_each_t_current_scenario[label_spline].append(
                        np.nan)
            except Exception:
                mae_values_at_each_t_current_scenario[label_spline].append(
                    np.nan)

        # --- Métodos con grafo ---
        for graph_name, graph_obj in graphs_dict.items():
            if not hasattr(graph_obj, 'U') or graph_obj.U is None:
                continue  # Saltar si el grafo no tiene base de Fourier

            # Tikhonov (con bucle de parámetros)
            for tau in param_grid["Tikhonov"]["tau_tik"]:
                label_tikh = f"Tikhonov({graph_name},τ={tau})"
                y_hat_tikh = np.nan
                try:
                    y_tikh_full = learning.regression_tikhonov(
                        graph_obj, measures_at_t, mask, tau)
                    y_hat_tikh = y_tikh_full[missing_electrode_idx]
                    mae_values_at_each_t_current_scenario[label_tikh].append(
                        np.abs(y_hat_tikh - true_value_at_missing_electrode))
                except Exception:
                    mae_values_at_each_t_current_scenario[label_tikh].append(
                        np.nan)

            # BGSRP (con bucle de parámetros)
            # Asegurar que bandw no sea mayor que el número de eigenvectores disponibles
            max_possible_bandw = graph_obj.U.shape[1] if hasattr(
                graph_obj, 'U') and graph_obj.U is not None else 0
            if max_possible_bandw > 0:  # Solo si hay eigenvectores
                # Usar señal completa sin NaN para transformar
                current_signal_at_t_for_transform = signal_at_t
                if np.all(np.isfinite(current_signal_at_t_for_transform)):  # Chequeo de finitud
                    try:
                        fx = graph_obj.U.T @ current_signal_at_t_for_transform
                        for bandw_param, gamma_bgsrp_param in product(param_grid["BGSRP"]["bandw"], param_grid["BGSRP"]["gamma_bgsrp"]):
                            actual_bandw = min(
                                bandw_param, max_possible_bandw)  # Ajustar bandw
                            if actual_bandw <= 0:
                                continue  # Saltar si bandw es 0 o negativo

                            label_bgsrp = f"BGSRP({graph_name},bandw={
                                actual_bandw},γ={gamma_bgsrp_param})"
                            y_hat_bgsrp = np.nan
                            try:
                                f_hat = graph_obj.U[:,
                                                    :actual_bandw] @ fx[:actual_bandw]
                                y0_bgsrp = f_hat[[missing_electrode_idx]]
                                params_bgsrp_call = {
                                    "bandw": actual_bandw, "gamma": gamma_bgsrp_param, 'basis': 'lp-ture'}
                                y_BGSRP_arr = gsp_BGSRP_recon(
                                    graph_obj, [missing_electrode_idx], y0_bgsrp, params_bgsrp_call)
                                y_hat_bgsrp = y_BGSRP_arr[0]
                                mae_values_at_each_t_current_scenario[label_bgsrp].append(
                                    np.abs(y_hat_bgsrp - true_value_at_missing_electrode))
                            except Exception:
                                mae_values_at_each_t_current_scenario[label_bgsrp].append(
                                    np.nan)
                    # Error en fx = graph_obj.U.T @ ... (ej. si signal_at_t no es finita)
                    except Exception:
                        # Asignar NaN a todas las combinaciones de BGSRP para este grafo y tiempo t
                        for bandw_param, gamma_bgsrp_param in product(param_grid["BGSRP"]["bandw"], param_grid["BGSRP"]["gamma_bgsrp"]):
                            actual_bandw = min(bandw_param, max_possible_bandw)
                            if actual_bandw <= 0:
                                continue
                            label_bgsrp = f"BGSRP({graph_name},bandw={
                                actual_bandw},γ={gamma_bgsrp_param})"
                            mae_values_at_each_t_current_scenario[label_bgsrp].append(
                                np.nan)
                else:  # signal_at_t no era finita, asignar NaN a BGSRP
                    for bandw_param, gamma_bgsrp_param in product(param_grid["BGSRP"]["bandw"], param_grid["BGSRP"]["gamma_bgsrp"]):
                        actual_bandw = min(bandw_param, max_possible_bandw)
                        if actual_bandw <= 0:
                            continue
                        label_bgsrp = f"BGSRP({graph_name},bandw={
                            actual_bandw},γ={gamma_bgsrp_param})"
                        mae_values_at_each_t_current_scenario[label_bgsrp].append(
                            np.nan)

    # Después del bucle de tiempo 't': calcular MAE promedio para este escenario de electrodo faltante
    for label, maes_at_each_t in mae_values_at_each_t_current_scenario.items():
        if maes_at_each_t:
            avg_mae_this_scenario = np.nanmean(maes_at_each_t)
            all_scenarios_mae_results[label].append(avg_mae_this_scenario)
        else:
            all_scenarios_mae_results[label].append(np.nan)
# --- FIN del bucle for missing_electrode_idx ---

# Post-procesamiento MAE
median_maes_for_sorting = {
    label: np.nanmedian(maes) for label, maes in all_scenarios_mae_results.items() if maes and np.sum(~np.isnan(maes)) > 0
}
valid_labels_for_plot = [
    label for label, median_val in median_maes_for_sorting.items() if not np.isnan(median_val)]

if not valid_labels_for_plot:
    print("No hay datos MAE válidos para generar gráficos o ranking.")
    df_mae_results_long = pd.DataFrame()  # DataFrame vacío
else:
    sorted_labels_for_boxplot = sorted(
        valid_labels_for_plot, key=lambda label: median_maes_for_sorting[label])
    mae_data_list_for_df = []
    for label in sorted_labels_for_boxplot:
        maes_for_label = all_scenarios_mae_results[label]
        for mae_value in maes_for_label:
            if not np.isnan(mae_value):
                mae_data_list_for_df.append(
                    {'Method': label, 'MAE': mae_value})

    if not mae_data_list_for_df:
        print(
            "Advertencia: Lista de datos MAE para DataFrame vacía después de filtrar NaNs.")
        df_mae_results_long = pd.DataFrame()
    else:
        df_mae_results_long = pd.DataFrame(mae_data_list_for_df)
        df_mae_results_long['Method'] = pd.Categorical(
            df_mae_results_long['Method'], categories=sorted_labels_for_boxplot, ordered=True)
        df_mae_results_long = df_mae_results_long.sort_values('Method')

# Ranking de Métodos MAE
print("\n--- Ranking de Métodos de Interpolación por MAE (Mediana MAE ascendente) ---")
if not df_mae_results_long.empty:
    ranking_stats = df_mae_results_long.groupby('Method', observed=True)['MAE'].agg(
        ['median', 'mean', 'std', 'min', 'max',
         lambda x: np.percentile(x.dropna(), 25),
         lambda x: np.percentile(x.dropna(), 75)]
    ).rename(columns={'<lambda_0>': '25th_pctl_MAE', '<lambda_1>': '75th_pctl_MAE'})
    ranking_stats = ranking_stats.sort_values(by='median', ascending=True)
    print(ranking_stats)
    timestamp_csv = datetime.datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S")  # Definir aquí para usar en CSV
    csv_ranking_path = f"ranking_mae_interpolacion_EEG_{timestamp_csv}.csv"
    try:
        ranking_stats.to_csv(csv_ranking_path)
        print(f"\nRanking MAE guardado en: {csv_ranking_path}")
    except Exception as e:
        print(f"\nNo se pudo guardar el ranking MAE en CSV: {e}")
else:
    print("No hay datos MAE para generar el ranking.")

# Visualización
# Figura 1: Matrices de Adyacencia (si weights_dict se llena correctamente)
if weights_dict:
    try:
        # Ajustar altura
        fig1 = plt.figure(
            figsize=(12, max(5, (len(weights_dict) // 3 + 1)*2.5)))
        plot_idx = 1
        cols = 3
        rows = (len(weights_dict) + cols - 1) // cols
        for title_w, W_matrix in weights_dict.items():
            if plot_idx > rows * cols:
                break
            plt.subplot(rows, cols, plot_idx)
            plt.imshow(W_matrix, aspect='auto', cmap='viridis')
            plt.title(title_w.split('(')[0], fontsize=9)
            plot_idx += 1
        plt.suptitle("Matrices de Adyacencia de Grafos", fontsize=16)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        pdf_figs.append(fig1)
    except Exception as e:
        print(f"Error al crear fig1 (matrices de pesos): {e}")
        if 'fig1' in locals() and fig1:
            plt.close(fig1)

# Figura MAE Boxplot
fig_boxplot = None
if not df_mae_results_long.empty:
    try:
        max_label_len = max(
            len(s) for s in sorted_labels_for_boxplot) if sorted_labels_for_boxplot else 0
        left_margin = min(0.1 + max_label_len * 0.0075, 0.45)
        fig_boxplot, ax_boxplot = plt.subplots(
            figsize=(14, max(8, len(sorted_labels_for_boxplot) * 0.4)))
        sns.boxplot(y='Method', x='MAE', data=df_mae_results_long, ax=ax_boxplot, orient='h',
                    order=sorted_labels_for_boxplot, hue='Method', hue_order=sorted_labels_for_boxplot,
                    palette='viridis', showfliers=True, legend=False)
        ax_boxplot.set_xscale('log')
        ax_boxplot.set_xlabel("Log Mean Absolute Error (MAE)", fontsize=12)
        ax_boxplot.set_ylabel("Método de Interpolación", fontsize=12)
        ax_boxplot.set_title(
            f"Distribución de MAE (N={N} escenarios) - Boxplot", fontsize=14)
        ax_boxplot.grid(True, axis='x', linestyle='--', alpha=0.7)
        ax_boxplot.grid(True, axis='y', linestyle=':', alpha=0.4)
        fig_boxplot.subplots_adjust(left=left_margin)
        pdf_figs.append(fig_boxplot)
    except Exception as e:
        print(f"Error al crear fig_boxplot: {e}")
        if fig_boxplot:
            plt.close(fig_boxplot)
            fig_boxplot = None

fig_boxplot = None
if not df_mae_results_long.empty:
    try:
        max_label_len = max(
            len(s) for s in sorted_labels_for_boxplot) if sorted_labels_for_boxplot else 0
        left_margin = min(0.1 + max_label_len * 0.0075, 0.45)
        fig_boxplot, ax_boxplot = plt.subplots(
            figsize=(14, max(8, len(sorted_labels_for_boxplot) * 0.4)))
        sns.boxplot(y='Method', x='MAE', data=df_mae_results_long, ax=ax_boxplot, orient='h',
                    order=sorted_labels_for_boxplot, hue='Method', hue_order=sorted_labels_for_boxplot,
                    palette='viridis', showfliers=False, legend=False)
        ax_boxplot.set_xlabel("Mean Absolute Error (MAE)", fontsize=12)
        ax_boxplot.set_ylabel("Método de Interpolación", fontsize=12)
        ax_boxplot.set_title(
            f"Distribución de MAE (N={N} escenarios) - Boxplot", fontsize=14)
        ax_boxplot.grid(True, axis='x', linestyle='--', alpha=0.7)
        ax_boxplot.grid(True, axis='y', linestyle=':', alpha=0.4)
        fig_boxplot.subplots_adjust(left=left_margin)
        pdf_figs.append(fig_boxplot)
    except Exception as e:
        print(f"Error al crear fig_boxplot: {e}")
        if fig_boxplot:
            plt.close(fig_boxplot)
            fig_boxplot = None


# # Figura MAE Violin Plot
# fig_violin = None
# if not df_mae_results_long.empty:
#     try:
#         max_label_len_v = max(
#             len(s) for s in sorted_labels_for_boxplot) if sorted_labels_for_boxplot else 0
#         left_margin_v = min(0.1 + max_label_len_v * 0.0075, 0.45)
#         fig_violin, ax_violin = plt.subplots(
#             figsize=(14, max(8, len(sorted_labels_for_boxplot) * 0.45)))
#         sns.violinplot(y='Method', x='MAE', data=df_mae_results_long, ax=ax_violin, orient='h',
#                        order=sorted_labels_for_boxplot, hue='Method', hue_order=sorted_labels_for_boxplot,
#                        palette='plasma', inner='quartile', cut=0, legend=False)
#         ax_violin.set_xscale('log')
#         ax_violin.set_xlabel("Log Mean Absolute Error (MAE)", fontsize=12)
#         ax_violin.set_ylabel("Método de Interpolación", fontsize=12)
#         ax_violin.set_title(
#             f"Distribución de MAE (N={N} escenarios) - Violin Plot", fontsize=14)
#         ax_violin.grid(True, axis='x', linestyle='--', alpha=0.7)
#         ax_violin.grid(True, axis='y', linestyle=':', alpha=0.4)
#         fig_violin.subplots_adjust(left=left_margin_v)
#         pdf_figs.append(fig_violin)
#     except Exception as e:
#         print(f"Error al crear fig_violin: {e}")
#         if fig_violin:
#             plt.close(fig_violin)
#             fig_violin = None


# Guardar en PDF
if pdf_figs:
    # Usar timestamp_csv si prefieres consistencia
    timestamp_pdf = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pdf_path = f"reporte_MAE_interpolaciones_EEG_{timestamp_pdf}.pdf"
    print(f"\nIntentando guardar PDF en: {pdf_path}")
    with PdfPages(pdf_path) as pdf:
        for i, fig_to_save in enumerate(pdf_figs):
            if fig_to_save and isinstance(fig_to_save, plt.Figure):
                try:
                    bbox_setting = 'tight' if fig_to_save not in [locals().get(
                        'fig_boxplot'), locals().get('fig_violin')] else None
                    if bbox_setting:
                        pdf.savefig(fig_to_save, bbox_inches=bbox_setting)
                    else:
                        pdf.savefig(fig_to_save)
                    print(f"Figura {i+1} guardada en el PDF.")
                except Exception as e:
                    print(f"Error al guardar figura {
                          i+1} ('{fig_to_save.canvas.get_window_title()}') en PDF: {e}")
                finally:
                    plt.close(fig_to_save)
            else:
                print(f"Figura {i+1} no es válida o es None, no se guardará.")
    print(f"PDF '{pdf_path}' creado.")
    if os.name == "nt":
        try:
            os.startfile(pdf_path)
        except Exception as e:
            print(f"No se pudo abrir el PDF automáticamente: {e}")
else:
    print("\nNo se generaron figuras para guardar en el PDF.")

print("\nProceso completado.")
