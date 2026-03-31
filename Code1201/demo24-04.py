from scipy.stats import pearsonr
from scipy.interpolate import interp1d
from matplotlib.backends.backend_pdf import PdfPages
from interpolation import spherical_spline_interpolation, gsp_BGSRP_recon
from construction import vkNNG, adjacency_matrix, adaptive_edge_weighting, NNK, kaliofolias
from scipy.interpolate import NearestNDInterpolator, RBFInterpolator
from pygsp2 import graphs, learning
from scipy.spatial.distance import squareform, pdist
import pandas as pd
import mne
import os
import datetime
from mne.channels import compute_native_head_t, read_custom_montage
import matplotlib.pyplot as plt
import numpy as np
from itertools import product
from collections import defaultdict
from dtaidistance import dtw
plt.close('all')

# Setup for reading the raw data
data_path = mne.datasets.sample.data_path()
subjects_dir = data_path / "subjects"
fname_raw = data_path / "MEG" / "sample" / "sample_audvis_raw.fif"
bem_dir = subjects_dir / "sample" / "bem"
fname_bem = bem_dir / "sample-5120-5120-5120-bem-sol.fif"
fname_src = bem_dir / "sample-oct-6-src.fif"

misc_path = mne.datasets.misc.data_path()
fname_T1_electrodes = misc_path / "sample_eeg_mri" / "T1_electrodes.mgz"
fname_mon = misc_path / "sample_eeg_mri" / "sample_mri_montage.elc"

dig_montage = read_custom_montage(
    fname_mon,
    head_size=None,
    coord_frame="mri",
    verbose="error",  # because it contains a duplicate point
)
# dig_montage.plot()
raw = mne.io.read_raw_fif(fname_raw)
raw.pick(picks=["eeg", "stim"]).load_data()
raw.set_montage(dig_montage)
# raw.plot_sensors(show_names=True)

raw.set_eeg_reference(projection=True)
events = mne.find_events(raw)
epochs = mne.Epochs(raw, events)
cov = mne.compute_covariance(epochs, tmax=0.0)
evoked = epochs["1"].average()  # trigger 1 in auditory/left
# evoked.plot_joint()
df = evoked.to_data_frame()
times = df.to_numpy()[:, 0]
signals = df.to_numpy()[:, 1:]
sensor_pos = dig_montage.get_positions()['ch_pos']
X = np.stack(list(sensor_pos.values()))[1:, :]

# %%
# Escala si es necesario
N, d = X.shape
X_scaled = X - np.kron(np.ones((N, 1)), np.mean(X, axis=0))
bounding_radius = 0.5 * \
    np.linalg.norm(np.amax(X_scaled, axis=0) - np.amin(X_scaled, axis=0), 2)
scale = np.power(N, 1. / float(min(d, 3))) / 10.
X_scaled *= scale / bounding_radius
Z = squareform(pdist(X))
Z_scaled = squareform(pdist(X_scaled))
# Mascara para datos faltantes
missing_ratio = 0.045  # 0.02 para 1 faltante
rng = np.random.default_rng(40)
mask = rng.uniform(0, 1, N) > missing_ratio
missing_idx = np.where(mask == False)[0]

# %%Hiperparametros
# Variance of d
# mean of d
# 1/3 mean of d
# k_th Neighbour within 3*sigma
# construction
sigma = np.mean(Z_scaled)/3
radius = np.mean(Z_scaled)
k = 5
# vknn
k_min = 2
k_max = 10
beta_factor = 0.01
# Kaliofolias
a = 0.34
b = 0.4
gamma = 0.04
# interpolation
# === Definición de rangos de hiperparámetros ===
param_grid = {
    "Tikhonov": {
        "tau_tik": [0, 0.1, 1]
    },
    "BGSRP": {
        "bandw": [N // 10,  N // 4],
        "gamma": [0.01, 1]
    },
    "RBFI MQ": {
        "epsilon_MQ": [0.9, 1.0, 1.1]
    },
    "Spline Superficie": {
        "s_SSI": [10.0, 50.0, 100.0]
    }
}
# %% Construccion
# knn /e-nn
W_knn, _ = adjacency_matrix(X, k, sigma=sigma, method="knn")
W_knn = W_knn.toarray()
G_knn = graphs.Graph(W_knn)
G_knn.compute_fourier_basis()

W_enn, _ = adjacency_matrix(
    X, radius=radius, sigma=sigma, method="radius_neighbors")
W_enn = W_enn.toarray()
G_enn = graphs.Graph(W_enn)
G_enn.compute_fourier_basis()

# vKnn
W_vknn, k_values = vkNNG(Z_scaled, k_min, k_max, beta_factor)
W_vknn = W_vknn.toarray()
G_vknn = graphs.Graph(W_vknn)
G_vknn.compute_fourier_basis()

# AEW
W_aew = adaptive_edge_weighting(X, W_knn, sigma)
G_aew = graphs.Graph(W_aew)
G_aew.compute_fourier_basis()

# NNK
W_nnk, W_knn_nnk = NNK(X, k)
W_nnk = W_nnk.toarray()
W_knn_nnk = W_knn_nnk.toarray()
G_nnk = graphs.Graph(W_nnk)
G_nnk.compute_fourier_basis()

# Kaliofolias
W_kaliofolias = kaliofolias(Z_scaled, a, b, gamma)
G_kaliofolias = graphs.Graph(W_kaliofolias)
G_kaliofolias.compute_fourier_basis()

weights_dict = {
    f"KNN(k={k},σ={sigma:.4f}, n_edge={G_knn.n_edges})": W_knn,
    f"Radius(r={radius:.4f},σ={sigma:.4f}, n_edge={G_enn.n_edges})": W_enn,
    f"VKNN(k_min={k_min},k_max={k_max},β={beta_factor}, n_edge={G_vknn.n_edges})": W_vknn,
    f"Kaliofolias(a={a},b={b},γ={gamma}, n_edge={G_kaliofolias.n_edges})": W_kaliofolias,
    f"NNK(k={k}, n_edge={G_nnk.n_edges})": W_nnk,
    f"AEW(k={k},σ={sigma}, n_edge={G_aew.n_edges})": W_aew,
}
graphs_dict = {
    f"KNN(k={k},σ={sigma:.4f}, n_edge={G_knn.n_edges})": G_knn,
    f"Radius(r={radius:.4f},σ={sigma:.4f}, n_edge={G_enn.n_edges})": G_enn,
    f"VKNN(k_min={k_min},k_max={k_max},β={beta_factor}, n_edge={G_vknn.n_edges})": G_vknn,
    f"Kaliofolias(a={a},b={b},γ={gamma}, n_edge={G_kaliofolias.n_edges})": G_kaliofolias,
    f"NNK(k={k}, n_edge={G_nnk.n_edges})": G_nnk,
    f"AEW(k={k},σ={sigma}, n_edge={G_aew.n_edges})": G_aew,
}
# %% Procesamiento iterativo
mae_results = defaultdict(dict)
T = signals.shape[0]
interpolation_results = defaultdict(dict)
for t in range(T):
    signal = signals[t, :]
    y = signal[~mask]
    measures = signal.copy()
    measures[~mask] = np.nan
    # Crear medidas con valores

    # Métodos sin grafo
    for method, params in param_grid.items():
        if method == "RBFI MQ":
            for epsilon in params["epsilon_MQ"]:
                label = f"RBFI MQ(ε={epsilon})"
                y_hat = RBFInterpolator(
                    X[mask], measures[mask], kernel='multiquadric', epsilon=epsilon)(X[~mask])
                interpolation_results[label][t] = y_hat
                error = np.mean(np.abs(y_hat - y))
                mae_results[label][t] = error

        elif method == "Spline Superficie":
            for s in params["s_SSI"]:
                label = f"Spline Superficie(s={s})"
                y_hat = spherical_spline_interpolation(X, measures, s)[~mask]
                interpolation_results[label][t] = y_hat
                error = np.mean(np.abs(y_hat - y))
                mae_results[label][t] = error

    # Interpoladores básicos (sin parámetros)
    y_hat = NearestNDInterpolator(X[mask], measures[mask])(X[~mask])
    interpolation_results["NNI"][t] = y_hat
    mae_results["NNI"][t] = np.mean(np.abs(y_hat - y))

    y_hat = RBFInterpolator(X[mask], measures[mask])(X[~mask])
    mae_results["RBFI TPS"][t] = np.mean(np.abs(y_hat - y))
    interpolation_results["RBFI TPS"][t] = y_hat

    # Métodos con grafo
    for graph_name, graph in graphs_dict.items():
        if "Tikhonov" in param_grid:
            for tau in param_grid["Tikhonov"]["tau_tik"]:
                y_tikh = learning.regression_tikhonov(
                    graph, measures, mask, tau)
                label = f"Tikhonov({graph_name},τ={tau})"
                interpolation_results[label][t] = y_tikh[~mask]
                mae_results[label][t] = np.mean(
                    np.abs(y_tikh[~mask] - y))

        if "BGSRP" in param_grid:
            fx = graph.U.T @ signal
            for bandw, gamma in product(param_grid["BGSRP"]["bandw"], param_grid["BGSRP"]["gamma"]):
                f_hat = graph.U[:, :bandw] @ fx[:bandw]
                y0 = f_hat[missing_idx]
                param_BGSRP = {"bandw": bandw, "gamma": gamma,
                               'basis': 'lp-ture'}
                y_BGSRP = gsp_BGSRP_recon(graph, missing_idx, y0, param_BGSRP)
                label = f"BGSRP({graph_name},bandw={bandw},γ={gamma})"
                interpolation_results[label][t] = y_BGSRP[0]
                mae_results[label][t] = np.mean(
                    np.abs(y_BGSRP[0] - y))
avg_mae = {label: np.nanmean(list(errors.values()))
           for label, errors in mae_results.items()}
sorted_results = sorted(avg_mae.items(), key=lambda x: x[1])

# for label, error in sorted_results:
#     print(f"{label}: MAE promedio = {error:.4f}")
labels, errors = zip(*sorted_results)
# %%  visualización
# Agrupar interpolaciones
grupos = defaultdict(list)
for label, series in interpolation_results.items():
    if "Tikhonov" in label:
        grupo = "Tikhonov"
    elif "BGSRP" in label:
        grupo = "BGSRP"
    else:
        grupo = "Otros"
    grupos[grupo].append((label, series))
# === Crear figura 1: Matrices de pesos ===
fig1 = plt.figure(figsize=(10, 7))

plt.subplot(2, 4, 1)
plt.imshow(W_knn)
plt.title('Sklearn KNN')

plt.subplot(2, 4, 2)
plt.imshow(W_enn)
plt.title('Sklearn Radius')

plt.subplot(2, 4, 3)
plt.imshow(W_knn_nnk)
plt.title('KNN(NNK)')

plt.subplot(2, 4, 4)
plt.imshow(W_nnk)
plt.title('NNK')

plt.subplot(2, 4, 5)
plt.imshow(W_vknn)
plt.title('VKNN')

plt.subplot(2, 4, 6)
plt.imshow(W_kaliofolias)
plt.title('Kaliofolias')

plt.subplot(2, 4, 7)
plt.imshow(W_aew)
plt.title('AEW')

plt.tight_layout()

# === Crear figura de MAE ===
fig_mae = plt.figure(figsize=(12, 6))
bars = plt.barh(range(len(labels)), errors, color='skyblue')
plt.yticks(range(len(labels)), labels, fontsize=8)
plt.xlabel("MAE Promedio", fontsize=12)
plt.title(
    f"Comparación de Métodos de Interpolación EEG, idx = {missing_idx}", fontsize=14)
plt.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.gca().invert_yaxis()

# === Función para graficar por grupo ===

results_df = pd.DataFrame()


def graficar_grupo(grupo_nombre, metodos, max_por_figura=6):
    global results_df  # <<< Necesario para modificar la variable global
    for i in range(0, len(metodos), max_por_figura):
        fig, axs = plt.subplots(2, 3, figsize=(15, 8))
        fig.suptitle(f"Interpolaciones - {grupo_nombre}", fontsize=16)
        axs = axs.flatten()
        for j, (label, series_dict) in enumerate(metodos[i:i + max_por_figura]):
            interpol = np.vstack([v for v in series_dict.values()])
            axs[j].plot(signals[:, missing_idx], label='Original', alpha=0.5)
            axs[j].plot(interpol, label='Interpolado')
            axs[j].set_title(label, fontsize=9)
            axs[j].legend(fontsize=6)
            distance, paths = dtw.warping_paths(
                signals[:, missing_idx], interpol, use_c=False)
            best_path = dtw.best_path(paths)
            similarity_score = distance / len(best_path)
            new_row = pd.DataFrame(
                {'Method': [label], 'Value': [similarity_score]})
            results_df = pd.concat([results_df, new_row], ignore_index=True)

        for j in range(len(metodos[i + max_por_figura:i + 6])):
            axs[-(j+1)].axis('off')
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        pdf.savefig(fig)
        plt.close(fig)


# === Nombre del archivo con fecha y hora ===
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
pdf_path = f"interpolaciones_EEG_{timestamp}.pdf"

# === Guardar todo en PDF ===
with PdfPages(pdf_path) as pdf:
    pdf.savefig(fig_mae)
    plt.close(fig_mae)

    pdf.savefig(fig1)
    plt.close(fig1)

    for grupo, metodos in grupos.items():
        graficar_grupo(grupo, metodos)

# === Abrir automáticamente en Windows ===
if os.name == "nt":
    os.startfile(pdf_path)

results_df = results_df.sort_values(
    by='Value', ascending=True).reset_index(drop=True)
results_df
# Falta Time-Varing
# SS MNE
# Falta iterar sobre cantidad de electrodos faltantes
# Falta cambiar dataset
# Falta verificar cada metodo con su dataset.
# Falta optimizar hyperparametros de cada metodo de construccion + interpolación
# pyunlockbox
# Añadir Time-it
