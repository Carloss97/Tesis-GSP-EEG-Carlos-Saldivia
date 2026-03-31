from scipy.stats import pearsonr  # No usado actualmente
from scipy.interpolate import interp1d  # No usado actualmente
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
from dtaidistance import dtw  # <--- AÑADIDO PARA DTW

# Intentar importar joypy (no se usará en esta versión, pero se mantiene la estructura)
try:
    import joypy
    JOYPY_AVAILABLE = True
except ImportError:
    JOYPY_AVAILABLE = False
    # print("Advertencia: La librería 'joypy' no está instalada. El Ridgeline Plot no se generará.")

plt.close('all')

# =============================================================================
# Placeholder for custom modules
# =============================================================================
try:
    from interpolation import spherical_spline_interpolation, gsp_BGSRP_recon
except ImportError:
    print("Advertencia: Módulo 'interpolation' no encontrado. Spherical Spline y BGSRP podrían fallar o usar dummies.")

    def spherical_spline_interpolation(X, values, s_initial=1.0, s_retry_factor=5, max_s_retry=10000.0):
        # print(f"spherical_spline_interpolation ({s_initial=}) llamada (dummy).")
        result = values.copy()  # Devolver NaNs originales si falla
        return result

    def gsp_BGSRP_recon(graph, missing_idx, y0, param_BGSRP):
        # print("gsp_BGSRP_recon llamada (dummy).")
        # y0 puede ser un array o escalar
        return [np.full_like(np.array(y0), np.nan)]

try:
    from construction import vkNNG, adjacency_matrix, adaptive_edge_weighting, NNK, kaliofolias
except ImportError:
    print("Advertencia: Módulo 'construction' no encontrado. Métodos de construcción de grafos podrían fallar o usar dummies.")
    from scipy.sparse import lil_matrix

    def dummy_adjacency_matrix(X_dummy, k_or_radius, sigma, method):
        N_adj = X_dummy.shape[0]
        return lil_matrix((N_adj, N_adj)), None

    def vkNNG(Z_s, k_m, k_mx, bf): return (dummy_adjacency_matrix(
        Z_s, k_m, 0, 'vkNNG_dummy')[0].toarray(), None)

    def adaptive_edge_weighting(X_s, W_k, sig): return dummy_adjacency_matrix(
        X_s, 0, sig, 'AEW_dummy')[0].toarray()

    def NNK(X_s, k_nn): return (dummy_adjacency_matrix(X_s, k_nn, 0, 'NNK_dummy')[
        0].toarray(), dummy_adjacency_matrix(X_s, k_nn, 0, 'NNK_knn_dummy')[0].toarray())

    def kaliofolias(Z_s, a_k, b_k, g_k): return dummy_adjacency_matrix(
        Z_s, 0, 0, 'Kaliofolias_dummy')[0].toarray()
    adjacency_matrix = dummy_adjacency_matrix
# =============================================================================

# Configuración de datos MNE (sin cambios)
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
print(f"Canales (N): {N}, Tiempos (T): {T}, Señales: {signals.shape}")

# Escalado de posiciones (sin cambios)
X_scaled = X - np.mean(X, axis=0)
bounding_radius = 0.5 * \
    np.linalg.norm(np.amax(X_scaled, axis=0) - np.amin(X_scaled, axis=0), 2)
scale = np.power(N, 1. / float(min(d, 3))) / 10.
if bounding_radius > 1e-9:
    X_scaled *= scale / bounding_radius
else:
    print("Advertencia: Bounding radius cero. Escalado no aplicado.")
Z_scaled = squareform(pdist(X_scaled))

# Hiperparámetros de grafos (sin cambios)
sigma = np.mean(Z_scaled[Z_scaled > 0]) / 3 if np.any(Z_scaled > 0) else 0.1
radius = np.mean(Z_scaled[Z_scaled > 0]) if np.any(Z_scaled > 0) else 0.3
k = 5
k_min, k_max, beta_factor = 2, 10, 0.01
a_kal, b_kal, gamma_kal = 0.34, 0.4, 0.04

# Hiperparámetros de interpolación (sin cambios)
param_grid = {
    "Tikhonov": {"tau_tik": [0.01, 0.1, 1]},
    "BGSRP": {"bandw": [N // 10 if N // 10 > 0 else 1, N // 4 if N // 4 > 0 else max(2, N//10 + 1)], "gamma_bgsrp": [0.01, 1]},
    "RBFI MQ": {"epsilon_MQ": [0.9, 1.0, 1.1]},  # Restaurado 0.9
    "Spline Superficie": {"s_SSI": [10.0, 50.0, 100.0]}
}

# Construcción de Grafos (sin cambios)
# ... (tu código de construcción de grafos aquí, igual al que proporcionaste)...
print("Construyendo grafos...")
graphs_dict = {}
weights_dict = {}
try:
    W_knn_sparse, _ = adjacency_matrix(X_scaled, k, sigma=sigma, method="knn")
    W_knn = W_knn_sparse.toarray() if hasattr(
        W_knn_sparse, 'toarray') else W_knn_sparse
    G_knn = graphs.Graph(W_knn)
    G_knn.compute_fourier_basis()
    weights_dict[f"KNN(k={k},σ={sigma:.2f})"] = W_knn
    graphs_dict[f"KNN(k={k},σ={sigma:.2f})"] = G_knn

    W_enn_sparse, _ = adjacency_matrix(
        X_scaled, radius=radius, sigma=sigma, method="radius_neighbors")
    W_enn = W_enn_sparse.toarray() if hasattr(
        W_enn_sparse, 'toarray') else W_enn_sparse
    G_enn = graphs.Graph(W_enn)
    G_enn.compute_fourier_basis()
    weights_dict[f"Radius(r={radius:.2f},σ={sigma:.2f})"] = W_enn
    graphs_dict[f"Radius(r={radius:.2f},σ={sigma:.2f})"] = G_enn

    W_vknn_val, _ = vkNNG(Z_scaled, k_min, k_max, beta_factor)
    G_vknn = graphs.Graph(W_vknn_val)
    G_vknn.compute_fourier_basis()
    weights_dict[f"VKNN(k_min={k_min},k_max={k_max},β={
        beta_factor})"] = W_vknn_val
    graphs_dict[f"VKNN(k_min={k_min},k_max={k_max},β={beta_factor})"] = G_vknn

    W_aew_val = adaptive_edge_weighting(X_scaled, W_knn, sigma)
    G_aew = graphs.Graph(W_aew_val)
    G_aew.compute_fourier_basis()
    weights_dict[f"AEW(k={k},σ={sigma:.2f})"] = W_aew_val
    graphs_dict[f"AEW(k={k},σ={sigma:.2f})"] = G_aew

    # W_knn_for_nnk_val no se usa directamente en graphs_dict
    W_nnk_val, _ = NNK(X_scaled, k)
    G_nnk = graphs.Graph(W_nnk_val)
    G_nnk.compute_fourier_basis()
    weights_dict[f"NNK(k={k})"] = W_nnk_val
    graphs_dict[f"NNK(k={k})"] = G_nnk

    W_kaliofolias_val = kaliofolias(Z_scaled, a_kal, b_kal, gamma_kal)
    G_kaliofolias = graphs.Graph(W_kaliofolias_val)
    G_kaliofolias.compute_fourier_basis()
    weights_dict[f"Kaliofolias(a={a_kal},b={b_kal},γ={
        gamma_kal:.2f})"] = W_kaliofolias_val
    graphs_dict[f"Kaliofolias(a={a_kal},b={b_kal},γ={
        gamma_kal:.2f})"] = G_kaliofolias
    print("Grafos construidos.")
except Exception as e_graph_constr:
    print(f"Error crítico durante construcción de grafos: {e_graph_constr}.")
    from scipy.sparse import diags  # Mover importación aquí por si falla antes
    dummy_W_arr = diags(np.random.rand(N), 0, shape=(N, N),
                        format="csr").toarray()
    dummy_G = graphs.Graph(dummy_W_arr)
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
            weights_dict[name] = dummy_W_arr


# --- Almacenamiento de resultados ---
all_scenarios_mae_results = defaultdict(list)
all_scenarios_dtw_results = defaultdict(list)  # <--- AÑADIDO PARA DTW
pdf_figs = []

# --- Bucle Principal de Procesamiento ---
for missing_electrode_idx in range(N):
    print(f"Procesando escenario: Electrodo {
          missing_electrode_idx+1}/{N} faltante...")
    mask = np.ones(N, dtype=bool)
    mask[missing_electrode_idx] = False

    mae_values_at_each_t_current_scenario = defaultdict(list)
    interpolated_series_for_dtw_current_scenario = defaultdict(
        list)  # <--- AÑADIDO PARA DTW

    for t in range(T):
        signal_at_t = signals[t, :]
        true_value_at_missing_electrode = signal_at_t[missing_electrode_idx]
        measures_at_t = signal_at_t.copy()
        measures_at_t[missing_electrode_idx] = np.nan
        known_values = measures_at_t[mask]
        known_positions = X[mask, :]
        missing_position = X[[missing_electrode_idx], :]
        # y_hat fue eliminado, usar variables específicas por método

        # --- Métodos sin grafo ---
        # NNI
        label_nni = "NNI"
        y_hat_nni = np.nan
        try:
            interpolator_nni = NearestNDInterpolator(
                known_positions, known_values)
            y_hat_nni = interpolator_nni(missing_position)[0]
            mae_values_at_each_t_current_scenario[label_nni].append(
                np.abs(y_hat_nni - true_value_at_missing_electrode))
        except Exception:
            mae_values_at_each_t_current_scenario[label_nni].append(np.nan)
        interpolated_series_for_dtw_current_scenario[label_nni].append(
            y_hat_nni)  # <--- AÑADIDO PARA DTW

        # RBFI TPS
        label_rbf_tps = "RBFI TPS"
        y_hat_rbf_tps = np.nan
        try:
            interpolator_rbf_tps = RBFInterpolator(
                known_positions, known_values)
            y_hat_rbf_tps = interpolator_rbf_tps(missing_position)[0]
            mae_values_at_each_t_current_scenario[label_rbf_tps].append(
                np.abs(y_hat_rbf_tps - true_value_at_missing_electrode))
        except Exception:
            mae_values_at_each_t_current_scenario[label_rbf_tps].append(np.nan)
        interpolated_series_for_dtw_current_scenario[label_rbf_tps].append(
            y_hat_rbf_tps)  # <--- AÑADIDO PARA DTW

        # RBFI MQ
        for epsilon in param_grid["RBFI MQ"]["epsilon_MQ"]:
            label_rbf_mq = f"RBFI MQ(ε={epsilon})"
            y_hat_rbf_mq = np.nan
            try:
                interpolator_rbf_mq = RBFInterpolator(
                    known_positions, known_values, kernel='multiquadric', epsilon=epsilon)
                y_hat_rbf_mq = interpolator_rbf_mq(missing_position)[0]
                mae_values_at_each_t_current_scenario[label_rbf_mq].append(
                    np.abs(y_hat_rbf_mq - true_value_at_missing_electrode))
            except Exception:
                mae_values_at_each_t_current_scenario[label_rbf_mq].append(
                    np.nan)
            interpolated_series_for_dtw_current_scenario[label_rbf_mq].append(
                y_hat_rbf_mq)  # <--- AÑADIDO PARA DTW

        # Spline Superficie
        for s_param in param_grid["Spline Superficie"]["s_SSI"]:
            label_spline = f"Spline Superficie(s={s_param})"
            y_hat_spline = np.nan
            try:
                interpolated_signal_full = spherical_spline_interpolation(
                    X, measures_at_t, s_initial=s_param)
                y_hat_spline = interpolated_signal_full[missing_electrode_idx]
                if pd.notna(y_hat_spline):
                    mae_values_at_each_t_current_scenario[label_spline].append(
                        np.abs(y_hat_spline - true_value_at_missing_electrode))
                else:
                    mae_values_at_each_t_current_scenario[label_spline].append(
                        np.nan)
            except Exception:
                mae_values_at_each_t_current_scenario[label_spline].append(
                    np.nan)
            interpolated_series_for_dtw_current_scenario[label_spline].append(
                y_hat_spline)  # <--- AÑADIDO PARA DTW

        # --- Métodos con grafo ---
        for graph_name, graph_obj in graphs_dict.items():
            # Chequeo robusto de base de Fourier
            valid_fourier_basis = hasattr(graph_obj, 'U') and graph_obj.U is not None and \
                graph_obj.U.shape[0] == N and graph_obj.U.shape[1] > 0

            if not valid_fourier_basis:
                # Fallback: Llenar con NaNs para este grafo si la base no es válida
                for tau_f in param_grid["Tikhonov"]["tau_tik"]:
                    label_tikh_f = f"Tikhonov({graph_name},τ={tau_f})"
                    mae_values_at_each_t_current_scenario[label_tikh_f].append(
                        np.nan)
                    interpolated_series_for_dtw_current_scenario[label_tikh_f].append(
                        np.nan)  # <--- DTW
                if "BGSRP" in param_grid:
                    max_possible_bandw_f = 1  # Dummy value if U invalid
                    for bandw_param_f, gamma_bgsrp_param_f in product(param_grid["BGSRP"]["bandw"], param_grid["BGSRP"]["gamma_bgsrp"]):
                        actual_bandw_f = min(
                            bandw_param_f, max_possible_bandw_f)
                        if actual_bandw_f <= 0:
                            actual_bandw_f = 1  # Evitar bandw no positivo
                        label_bgsrp_f = f"BGSRP({graph_name},bandw={actual_bandw_f},γ={
                            gamma_bgsrp_param_f})"
                        mae_values_at_each_t_current_scenario[label_bgsrp_f].append(
                            np.nan)
                        interpolated_series_for_dtw_current_scenario[label_bgsrp_f].append(
                            np.nan)  # <--- DTW
                continue  # Saltar al siguiente grafo

            # Tikhonov
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
                interpolated_series_for_dtw_current_scenario[label_tikh].append(
                    y_hat_tikh)  # <--- AÑADIDO PARA DTW

            # BGSRP
            current_signal_at_t_for_transform = signal_at_t
            # Ya sabemos que U es válido aquí
            max_possible_bandw_bg = graph_obj.U.shape[1]

            if not np.all(np.isfinite(current_signal_at_t_for_transform)):
                # Fallback si la señal no es finita: llenar NaNs para BGSRP
                for bandw_param_bg, gamma_bgsrp_param_bg in product(param_grid["BGSRP"]["bandw"], param_grid["BGSRP"]["gamma_bgsrp"]):
                    actual_bandw_bg = min(
                        bandw_param_bg, max_possible_bandw_bg)
                    if actual_bandw_bg <= 0:
                        actual_bandw_bg = 1
                    label_bgsrp_bg = f"BGSRP({graph_name},bandw={actual_bandw_bg},γ={
                        gamma_bgsrp_param_bg})"
                    mae_values_at_each_t_current_scenario[label_bgsrp_bg].append(
                        np.nan)
                    interpolated_series_for_dtw_current_scenario[label_bgsrp_bg].append(
                        np.nan)  # <--- DTW
                continue  # Saltar al siguiente método o grafo si es el final del bloque BGSRP

            try:  # Intento para calcular fx
                fx = graph_obj.U.T @ current_signal_at_t_for_transform
                for bandw_param, gamma_bgsrp_param in product(param_grid["BGSRP"]["bandw"], param_grid["BGSRP"]["gamma_bgsrp"]):
                    actual_bandw = min(bandw_param, max_possible_bandw_bg)
                    if actual_bandw <= 0:
                        actual_bandw = 1

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

                        if isinstance(y_BGSRP_arr, list) and len(y_BGSRP_arr) > 0:
                            y_hat_bgsrp = y_BGSRP_arr[0]
                            if isinstance(y_hat_bgsrp, (np.ndarray, list)) and len(y_hat_bgsrp) == 1:
                                y_hat_bgsrp = y_hat_bgsrp[0]

                        if pd.notna(y_hat_bgsrp):
                            mae_values_at_each_t_current_scenario[label_bgsrp].append(
                                np.abs(y_hat_bgsrp - true_value_at_missing_electrode))
                        else:
                            mae_values_at_each_t_current_scenario[label_bgsrp].append(
                                np.nan)
                    except Exception:
                        mae_values_at_each_t_current_scenario[label_bgsrp].append(
                            np.nan)
                    interpolated_series_for_dtw_current_scenario[label_bgsrp].append(
                        y_hat_bgsrp)  # <--- AÑADIDO PARA DTW
            except Exception as e_fx_calc:
                # Fallback si fx falla: llenar NaNs para todas las combinaciones BGSRP
                for bandw_param_e, gamma_bgsrp_param_e in product(param_grid["BGSRP"]["bandw"], param_grid["BGSRP"]["gamma_bgsrp"]):
                    actual_bandw_e = min(bandw_param_e, max_possible_bandw_bg)
                    if actual_bandw_e <= 0:
                        actual_bandw_e = 1
                    label_bgsrp_e = f"BGSRP({graph_name},bandw={actual_bandw_e},γ={
                        gamma_bgsrp_param_e})"
                    mae_values_at_each_t_current_scenario[label_bgsrp_e].append(
                        np.nan)
                    interpolated_series_for_dtw_current_scenario[label_bgsrp_e].append(
                        np.nan)  # <--- DTW

    # --- FIN del bucle for t in range(T) ---

    # 1. Procesar y guardar el MAE promedio para este escenario
    for label, maes_at_each_t in mae_values_at_each_t_current_scenario.items():
        all_scenarios_mae_results[label].append(
            np.nanmean(maes_at_each_t) if maes_at_each_t else np.nan)

    # 2. Calcular y guardar DTW para este escenario (REINCORPORADO)
    original_signal_series = signals[:, missing_electrode_idx]
    s1_original = np.ascontiguousarray(original_signal_series, dtype=np.double)
    original_signal_valid_for_dtw = np.all(np.isfinite(s1_original))

    for label, interpolated_points in interpolated_series_for_dtw_current_scenario.items():
        dtw_distance_to_store = np.nan
        if original_signal_valid_for_dtw and len(interpolated_points) == T:
            interpolated_s_arr = np.array(interpolated_points)
            if not (np.any(np.isnan(interpolated_s_arr)) or not np.all(np.isfinite(interpolated_s_arr))):
                try:
                    s2_interpolated = np.ascontiguousarray(
                        interpolated_s_arr, dtype=np.double)
                    # Usar dtw.distance_fast para velocidad si la normalización por path no es crítica,
                    # o si puedes normalizar de otra forma (ej. por T)
                    # dtw_distance_to_store = dtw.distance_fast(s1_original, s2_interpolated, use_pruning=True) / T # Ejemplo normalización por T

                    distance_val, paths_val = dtw.warping_paths(
                        s1_original, s2_interpolated, use_c=False, psi=0)
                    if distance_val != np.inf and paths_val.any():  # paths_val.any() es una forma de chequear si no está vacío
                        best_path_val = dtw.best_path(paths_val)
                        if len(best_path_val) > 0:
                            dtw_distance_to_store = distance_val / \
                                len(best_path_val)
                except Exception:
                    pass
        all_scenarios_dtw_results[label].append(dtw_distance_to_store)
# --- FIN del bucle for missing_electrode_idx ---


# --- Post-procesamiento y Visualización ---
# MAE DataFrame y Ranking
median_maes_for_sorting = {label: np.nanmedian(
    maes) for label, maes in all_scenarios_mae_results.items() if maes and np.sum(~np.isnan(maes)) > 0}
valid_labels_for_mae_plot = [
    label for label, median_val in median_maes_for_sorting.items() if not np.isnan(median_val)]
df_mae_results_long = pd.DataFrame()
if valid_labels_for_mae_plot:
    sorted_labels_for_mae_boxplot = sorted(
        valid_labels_for_mae_plot, key=lambda label: median_maes_for_sorting[label])
    mae_data_list_for_df = [{'Method': label, 'MAE': mae_value}
                            for label in sorted_labels_for_mae_boxplot for mae_value in all_scenarios_mae_results[label] if not np.isnan(mae_value)]
    if mae_data_list_for_df:
        df_mae_results_long = pd.DataFrame(mae_data_list_for_df)
        df_mae_results_long['Method'] = pd.Categorical(
            df_mae_results_long['Method'], categories=sorted_labels_for_mae_boxplot, ordered=True)
        df_mae_results_long = df_mae_results_long.sort_values('Method')

print("\n--- Ranking MAE ---")
if not df_mae_results_long.empty:
    ranking_stats_mae = df_mae_results_long.groupby('Method', observed=True)['MAE'].agg(
        ['median', 'mean', 'std', 'min', 'max', lambda x: np.percentile(
            x.dropna(), 25), lambda x: np.percentile(x.dropna(), 75)]
        # Nombres más cortos
    ).rename(columns={'<lambda_0>': '25p_MAE', '<lambda_1>': '75p_MAE'})
    print(ranking_stats_mae.sort_values(by='median'))
    timestamp_csv = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    try:
        ranking_stats_mae.to_csv(f"ranking_mae_EEG_{timestamp_csv}.csv")
        print(f"Ranking MAE guardado.")
    except Exception as e:
        print(f"No se pudo guardar ranking MAE: {e}")
else:
    print("Sin datos MAE para ranking.")

# DTW DataFrame y Ranking (REINCORPORADO)
median_dtws_for_sorting = {label: np.nanmedian(
    dists) for label, dists in all_scenarios_dtw_results.items() if dists and np.sum(~np.isnan(dists)) > 0}
valid_labels_for_dtw_plot = [
    label for label, median_val in median_dtws_for_sorting.items() if not np.isnan(median_val)]
df_dtw_results_long = pd.DataFrame()
if valid_labels_for_dtw_plot:
    sorted_labels_for_dtw_boxplot = sorted(
        valid_labels_for_dtw_plot, key=lambda label: median_dtws_for_sorting[label])
    dtw_data_list_for_df = [{'Method': label, 'DTW_Normalized': dtw_value}
                            for label in sorted_labels_for_dtw_boxplot for dtw_value in all_scenarios_dtw_results[label] if not np.isnan(dtw_value)]
    if dtw_data_list_for_df:
        df_dtw_results_long = pd.DataFrame(dtw_data_list_for_df)
        df_dtw_results_long['Method'] = pd.Categorical(
            df_dtw_results_long['Method'], categories=sorted_labels_for_dtw_boxplot, ordered=True)
        df_dtw_results_long = df_dtw_results_long.sort_values('Method')

print("\n--- Ranking DTW ---")
if not df_dtw_results_long.empty:
    ranking_stats_dtw = df_dtw_results_long.groupby('Method', observed=True)['DTW_Normalized'].agg(
        ['median', 'mean', 'std', 'min', 'max', lambda x: np.percentile(
            x.dropna(), 25), lambda x: np.percentile(x.dropna(), 75)]
    ).rename(columns={'<lambda_0>': '25p_DTW', '<lambda_1>': '75p_DTW'})
    print(ranking_stats_dtw.sort_values(by='median'))
    try:
        ranking_stats_dtw.to_csv(f"ranking_dtw_EEG_{timestamp_csv}.csv")
        print(f"Ranking DTW guardado.")
    except Exception as e:
        print(f"No se pudo guardar ranking DTW: {e}")
else:
    print("Sin datos DTW para ranking.")

# --- Visualización ---
# Figura Matrices de Adyacencia
fig1_adj = None  # Inicializar
if weights_dict:
    try:
        fig1_adj = plt.figure(
            figsize=(12, max(5, (len(weights_dict) // 3 + 1)*2.5)))
        # ... (código de ploteo de matrices sin cambios) ...
        plot_idx = 1
        cols_adj = 3
        rows_adj = (len(weights_dict) + cols_adj - 1) // cols_adj
        for title_w, W_matrix in weights_dict.items():
            if plot_idx > rows_adj * cols_adj:
                break
            plt.subplot(rows_adj, cols_adj, plot_idx)
            plt.imshow(W_matrix, aspect='auto', cmap='viridis')
            plt.title(title_w.split('(')[0], fontsize=9)
            plot_idx += 1
        plt.suptitle("Matrices de Adyacencia de Grafos", fontsize=16)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        pdf_figs.append(fig1_adj)
    except Exception as e:
        print(f"Error creando fig1_adj: {e}")
        plt.close(fig1_adj if fig1_adj else None)


# Boxplot MAE Logarítmico
fig_boxplot_log_mae = None
if not df_mae_results_long.empty:
    try:
        max_label_len_mae = max(len(
            s) for s in sorted_labels_for_mae_boxplot) if sorted_labels_for_mae_boxplot else 0
        left_margin_mae = min(0.1 + max_label_len_mae * 0.0075, 0.45)
        fig_boxplot_log_mae, ax_log = plt.subplots(
            figsize=(14, max(8, len(sorted_labels_for_mae_boxplot) * 0.4)))
        sns.boxplot(y='Method', x='MAE', data=df_mae_results_long, ax=ax_log, orient='h',
                    order=sorted_labels_for_mae_boxplot, hue='Method', hue_order=sorted_labels_for_mae_boxplot,
                    palette='viridis', showfliers=True, legend=False)
        ax_log.set_xscale('log')
        ax_log.set_xlabel("Log Mean Absolute Error (MAE)", fontsize=12)
        ax_log.set_ylabel("Método de Interpolación", fontsize=12)
        ax_log.set_title(f"Distribución de MAE (Log) (N={
                         N} escenarios)", fontsize=14)
        ax_log.grid(True, axis='x', linestyle='--', alpha=0.7)
        ax_log.grid(True, axis='y', linestyle=':', alpha=0.4)
        fig_boxplot_log_mae.subplots_adjust(left=left_margin_mae)
        pdf_figs.append(fig_boxplot_log_mae)
    except Exception as e:
        print(f"Error creando fig_boxplot_log_mae: {e}")
        plt.close(fig_boxplot_log_mae if fig_boxplot_log_mae else None)

# Boxplot MAE Lineal
fig_boxplot_linear_mae = None
if not df_mae_results_long.empty:
    try:
        max_label_len_mae = max(len(
            s) for s in sorted_labels_for_mae_boxplot) if sorted_labels_for_mae_boxplot else 0
        left_margin_mae = min(0.1 + max_label_len_mae * 0.0075, 0.45)
        fig_boxplot_linear_mae, ax_linear = plt.subplots(
            figsize=(14, max(8, len(sorted_labels_for_mae_boxplot) * 0.4)))
        sns.boxplot(y='Method', x='MAE', data=df_mae_results_long, ax=ax_linear, orient='h',
                    order=sorted_labels_for_mae_boxplot, hue='Method', hue_order=sorted_labels_for_mae_boxplot,
                    # showfliers=True para este también
                    palette='viridis', showfliers=False, legend=False)
        ax_linear.set_xscale('linear')  # Escala Lineal explícita
        ax_linear.set_xlabel(
            "Mean Absolute Error (MAE) - Escala Lineal", fontsize=12)
        # Ajuste de límites para el lineal (opcional, como lo pediste)
        if not df_mae_results_long['MAE'].empty:
            q95_mae = df_mae_results_long['MAE'].quantile(0.95)
            min_mae_val = df_mae_results_long['MAE'].min()
            if pd.notna(q95_mae) and pd.notna(min_mae_val):
                ax_linear.set_xlim(
                    left=max(0, min_mae_val - (q95_mae * 0.05)), right=q95_mae * 1.05)
            elif pd.notna(q95_mae):
                ax_linear.set_xlim(left=0, right=q95_mae*1.05)

        ax_linear.set_ylabel("Método de Interpolación", fontsize=12)
        ax_linear.set_title(f"Distribución de MAE (Lineal) (N={
                            N} escenarios)", fontsize=14)
        ax_linear.grid(True, axis='x', linestyle='--', alpha=0.7)
        ax_linear.grid(True, axis='y', linestyle=':', alpha=0.4)
        fig_boxplot_linear_mae.subplots_adjust(left=left_margin_mae)
        pdf_figs.append(fig_boxplot_linear_mae)
    except Exception as e:
        print(f"Error creando fig_boxplot_linear_mae: {e}")
        plt.close(fig_boxplot_linear_mae if fig_boxplot_linear_mae else None)


# Boxplot para DTW (REINCORPORADO)
fig_dtw_boxplot = None
if not df_dtw_results_long.empty:
    try:
        max_label_len_dtw = max(len(
            s) for s in sorted_labels_for_dtw_boxplot) if sorted_labels_for_dtw_boxplot else 0
        left_margin_dtw = min(0.1 + max_label_len_dtw * 0.0075, 0.45)
        fig_dtw_boxplot, ax_dtw_boxplot = plt.subplots(
            figsize=(14, max(8, len(sorted_labels_for_dtw_boxplot) * 0.4)))
        sns.boxplot(y='Method', x='DTW_Normalized', data=df_dtw_results_long, ax=ax_dtw_boxplot, orient='h',
                    order=sorted_labels_for_dtw_boxplot, hue='Method', hue_order=sorted_labels_for_dtw_boxplot,
                    palette='crest', showfliers=True, legend=False)

        use_log_scale_dtw = False  # Determinar si usar escala log para DTW
        positive_dtws = df_dtw_results_long['DTW_Normalized'][df_dtw_results_long['DTW_Normalized'] > 0]
        if not positive_dtws.empty:
            min_dtw, max_dtw = positive_dtws.min(
            ), df_dtw_results_long['DTW_Normalized'].max()
            if pd.notna(min_dtw) and pd.notna(max_dtw) and min_dtw > 0 and (max_dtw / min_dtw) > 50:
                use_log_scale_dtw = True

        xlabel_dtw = "Distancia DTW Normalizada"
        if use_log_scale_dtw:
            ax_dtw_boxplot.set_xscale('log')
            xlabel_dtw = f"Log({xlabel_dtw})"
            min_pos_dtw = positive_dtws.min()  # Ya sabemos que no está vacío y es >0
            ax_dtw_boxplot.set_xlim(
                left=min_pos_dtw * 0.5 if min_pos_dtw * 0.5 > 0 else 1e-9)
        else:
            # Asegurar escala lineal si no es log
            ax_dtw_boxplot.set_xscale('linear')

        ax_dtw_boxplot.set_xlabel(xlabel_dtw, fontsize=12)
        ax_dtw_boxplot.set_ylabel("Método de Interpolación", fontsize=12)
        ax_dtw_boxplot.set_title(
            f"Distribución de Distancia DTW Normalizada (N={N} escenarios)", fontsize=14)
        ax_dtw_boxplot.grid(True, axis='x', linestyle='--', alpha=0.7)
        ax_dtw_boxplot.grid(True, axis='y', linestyle=':', alpha=0.4)
        fig_dtw_boxplot.subplots_adjust(left=left_margin_dtw)
        pdf_figs.append(fig_dtw_boxplot)
    except Exception as e:
        print(f"Error creando fig_dtw_boxplot: {e}")
        plt.close(fig_dtw_boxplot if fig_dtw_boxplot else None)

# Guardar en PDF
# ... (tu código de guardado en PDF, igual al de la versión anterior, que itera sobre pdf_figs) ...
if pdf_figs:
    # timestamp_pdf = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Ya se definió timestamp_csv
    pdf_path = f"reporte_completo_interpolaciones_EEG_{
        timestamp_csv}.pdf"  # Reusar timestamp_csv
    print(f"\nIntentando guardar PDF en: {pdf_path}")
    with PdfPages(pdf_path) as pdf:
        for i, fig_to_save in enumerate(pdf_figs):
            if fig_to_save and isinstance(fig_to_save, plt.Figure):
                try:
                    is_adjusted_plot = fig_to_save in [locals().get('fig_boxplot_log_mae'), locals().get('fig_boxplot_linear_mae'),
                                                       locals().get('fig_violin_mae'), locals().get('fig_dtw_boxplot')]
                    # Usar tight si no se ajustó 'left'
                    bbox_setting = 'tight' if not is_adjusted_plot else None

                    if bbox_setting:
                        pdf.savefig(fig_to_save, bbox_inches=bbox_setting)
                    else:
                        pdf.savefig(fig_to_save)
                    print(f"Figura {i+1} guardada en el PDF.")
                except Exception as e:
                    fig_title_for_error = f"Figura tipo {type(fig_to_save)}"
                    if hasattr(fig_to_save, '_suptitle') and fig_to_save._suptitle is not None:
                        fig_title_for_error = fig_to_save._suptitle.get_text()
                    elif fig_to_save.axes and fig_to_save.axes[0].get_title():
                        fig_title_for_error = fig_to_save.axes[0].get_title()
                    print(f"Error al guardar figura {
                          i+1} ('{fig_title_for_error}') en PDF: {e}")
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
