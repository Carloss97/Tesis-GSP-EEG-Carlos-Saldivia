# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 08:15:15 2025

@author: sarlo
"""
# %%
from interpolation import spherical_spline_interpolation, gsp_BGSRP_recon
from construction import vkNNG, adjacency_matrix, adaptive_edge_weighting, NNK, kaliofolias
from scipy.interpolate import NearestNDInterpolator, RBFInterpolator
from pygsp2 import graphs, learning
from scipy.spatial.distance import squareform, pdist
import pandas as pd
import mne
from mne.channels import compute_native_head_t, read_custom_montage
import matplotlib.pyplot as plt
import numpy as np
from itertools import product
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
dig_montage.plot()
raw = mne.io.read_raw_fif(fname_raw)
raw.pick(picks=["eeg", "stim"]).load_data()
raw.set_montage(dig_montage)
raw.plot_sensors(show_names=True)

raw.set_eeg_reference(projection=True)
events = mne.find_events(raw)
epochs = mne.Epochs(raw, events)
cov = mne.compute_covariance(epochs, tmax=0.0)
evoked = epochs["1"].average()  # trigger 1 in auditory/left
evoked.plot_joint()
df = evoked.to_data_frame()
times = df.to_numpy()[:, 0]
signals = df.to_numpy()[:, 1:]
# df_100 = df.loc[df['time'] == 100]
sensor_pos = dig_montage.get_positions()['ch_pos']
X = np.stack(list(sensor_pos.values()))[1:, :]

# %%

# lectura archivos
# df_pos = pd.read_pickle(r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis\code\filt0-40.pkl")
# df_pos = df_pos.drop(index='EEG 053')
# df_100 = pd.read_pickle(r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis\code\df_100.pkl")
# #Señales
# signal = df_100.iloc[0, 1:].to_numpy()
# X = df_pos[['x', 'y','z']].to_numpy()
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
missing_ratio = 0.02  # 0.02 para 1 faltante
rng = np.random.default_rng(42)
mask = rng.uniform(0, 1, N) > missing_ratio
missing_idx = np.where(mask == False)[0]
# y = signal[~mask]
# # Señal con datos faltantes.
# measures = signal.copy()
# measures[~mask] = np.nan

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
epsilon_MQ = 0.1
s_SSI = 10.0  # SSI
tau_tik = 0
param_BGSRP = {'bandw': N // 5, 'gamma': 0.1, 'basis': 'lp-ture'}
# === Definición de rangos de hiperparámetros ===
# param_grid = {
#     "Tikhonov": {
#         "tau_tik": [0, 0.001, 0.01, 0.1]
#     },
#     "BGSRP": {
#         "bandw": [N // 10, N // 5, N // 2],
#         "gamma": [0.01, 0.1, 1]
#     },
#     "RBFI MQ": {
#         "epsilon_MQ": [0.01, 0.1, 0.5, 1.0]
#     },
#     "Spline Superficie": {
#         "s_SSI": [1.0, 5.0, 10.0, 20.0]
#     }
# }
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
# Diccionario para almacenar resultados de interpolación
# %% Configuración de almacenamiento de resultados
# methods_errors = {key: [] for key in list(interpolations.keys()) +
#                   [f"Tikhonov({name},τ={tau_tik})" for name in graphs_dict.keys()] +
#                   [f"BGSRP({name},bandw={param_BGSRP['bandw']},γ={param_BGSRP['gamma']})"
#                    for name in graphs_dict.keys()]}
# %% Interpolación.

# %% Procesamiento iterativo
for time_idx in range(signals.shape[0]):
    print(f"Procesando time point {time_idx+1}/{signals.shape[0]}")

    # Obtener señal actual
    signal = signals[time_idx, :]
    y = signal[~mask]
    measures = signal.copy()
    measures[~mask] = np.nan
    # Crear medidas con valores faltantes
    # measures = current_signal.copy()
    # measures[missing_idx] = np.nan
    # y_true = current_signal[missing_idx]

    current_errors = {}

    # Métodos sin grafo
    interpolators = {
        "NNI": NearestNDInterpolator(X[mask], measures[mask])(X[~mask]),
        "RBFI TPS": RBFInterpolator(X[mask], measures[mask])(X[~mask]),
        f"RBFI MQ(ε={epsilon_MQ})": RBFInterpolator(X[mask], measures[mask], kernel='multiquadric', epsilon=epsilon_MQ)(X[~mask]),
        f"Spline Superficie(s={s_SSI})": spherical_spline_interpolation(X, measures, s_SSI)[~mask],
    }

    for name, y_hat in interpolators.items():
        current_errors[name] = np.mean(np.abs(y_hat - y))

    # Métodos con grafo
    for name, graph in graphs_dict.items():
        # Tikhonov
        y_tikh = learning.regression_tikhonov(
            graph, measures, mask, tau_tik)
        current_errors[f"Tikhonov({name},τ={tau_tik})"] = np.mean(
            np.abs(y_tikh[~mask] - y))

        # BGSRP
        fx = graph.U.T @ signal
        f = graph.U[:, :param_BGSRP['bandw']] @ fx[:param_BGSRP['bandw']]
        y0 = f[missing_idx]
        y_BGSRP = gsp_BGSRP_recon(graph, missing_idx, y0, param_BGSRP)
        current_errors[f"BGSRP({name},bandw={param_BGSRP['bandw']},γ={param_BGSRP['gamma']})"] = \
            np.mean(np.abs(signal - y_BGSRP))

    # Acumular errores
    for method, error in current_errors.items():
        if time_idx == 0:
            methods_errors = {key: [] for key in list(interpolators.keys()) +
                              [f"Tikhonov({name},τ={tau_tik})" for name in graphs_dict.keys()] +
                              [f"BGSRP({name},bandw={param_BGSRP['bandw']},γ={param_BGSRP['gamma']})"
                               for name in graphs_dict.keys()]}
        methods_errors[method].append(error)
# best_results = {}

# # === Iterar sobre grafos ===
# for graph_name, graph in graphs_dict.items():
#     print(f"\nEvaluando sobre grafo: {graph_name}")

#     # === Tikhonov ===
#     for tau in param_grid["Tikhonov"]["tau_tik"]:
#         maes = []
#         for time_idx in range(signals.shape[0]):
#             signal = signals[time_idx, :]
#             measures = signal.copy()
#             measures[~mask] = np.nan
#             y = signal[~mask]

#             y_hat = learning.regression_tikhonov(graph, measures, mask, tau)
#             maes.append(np.mean(np.abs(y_hat[~mask] - y)))

#         avg_mae = np.mean(maes)
#         key = f"Tikhonov(tau={tau}, graph={graph_name})"
#         best_results[key] = avg_mae

#     # === BGSRP ===
#     for bandw, gamma in product(param_grid["BGSRP"]["bandw"], param_grid["BGSRP"]["gamma"]):
#         maes = []
#         for time_idx in range(signals.shape[0]):
#             signal = signals[time_idx, :]
#             fx = graph.U.T @ signal
#             f = graph.U[:, :bandw] @ fx[:bandw]
#             y0 = f[missing_idx]
#             y_hat = gsp_BGSRP_recon(graph, missing_idx, y0, {
#                                     'bandw': bandw, 'gamma': gamma})
#             maes.append(np.mean(np.abs(signal - y_hat)))

#         avg_mae = np.mean(maes)
#         key = f"BGSRP(bandw={bandw}, gamma={gamma}, graph={graph_name})"
#         best_results[key] = avg_mae

# # === Métodos sin grafo (solo una vez) ===
# for eps in param_grid["RBFI MQ"]["epsilon_MQ"]:
#     maes = []
#     for time_idx in range(signals.shape[0]):
#         signal = signals[time_idx, :]
#         y = signal[~mask]
#         measures = signal.copy()
#         measures[~mask] = np.nan

#         y_hat = RBFInterpolator(
#             X[mask], measures[mask], kernel='multiquadric', epsilon=eps)(X[~mask])
#         maes.append(np.mean(np.abs(y_hat - y)))

#     avg_mae = np.mean(maes)
#     best_results[f"RBFI MQ(ε={eps})"] = avg_mae

# for s in param_grid["Spline Superficie"]["s_SSI"]:
#     maes = []
#     for time_idx in range(signals.shape[0]):
#         signal = signals[time_idx, :]
#         y = signal[~mask]
#         measures = signal.copy()
#         measures[~mask] = np.nan

#         y_hat = spherical_spline_interpolation(X, measures, s)[~mask]
#         maes.append(np.mean(np.abs(y_hat - y)))

#     avg_mae = np.mean(maes)
#     best_results[f"Spline Superficie(s={s})"] = avg_mae

# # === Mostrar resultados ordenados ===
# sorted_best = sorted(best_results.items(), key=lambda x: x[1])
# print("\n=== Resultados ordenados por MAE promedio ===")
# for name, mae in sorted_best:
#     print(f"{name}: {mae:.4f}")
# %% Post-procesamiento y visualización
# Calcular promedios
average_errors = {}
nan_counts = {}
for method, errors in methods_errors.items():
    # Convert list to numpy array for vectorized operations
    errors_array = np.array(errors)

    # Compute mean (ignoring nan)
    average_errors[method] = np.nanmean(errors_array)

    # Count number of nan values in the list
    nan_counts[method] = np.isnan(errors_array).sum()
for method, count in nan_counts.items():
    if count > 0:
        print(f"Method '{method}' had {count} NaN value(s)")
# Ordenar métodos por error
sorted_errors = sorted(average_errors.items(), key=lambda x: x[1])

# Visualización
plt.figure(figsize=(14, 8))
bars = plt.barh([method for method, _ in sorted_errors],
                [error for _, error in sorted_errors],
                color='skyblue')
plt.xlabel("Error MAE Promedio")
plt.title("Comparación de Métodos de Interpolación (Promedio Temporal)")
plt.grid(axis='x', linestyle='--', alpha=0.7)

for bar, (method, error) in zip(bars, sorted_errors):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
             f'{error:.4f}', va='center', ha='left', fontsize=9)

plt.tight_layout()
plt.show()


# # %%Visualizacion
# # Visualización
# fig0 = plt.figure(figsize=(13, 8))
# bars = plt.bar(errors.keys(), errors.values(), color='skyblue')
# plt.ylabel("Error MAE")
# plt.title("Comparación de Errores MAE con Parámetros")
# plt.xticks(rotation=75, ha="right")
# plt.grid(axis='y', linestyle='--', alpha=0.7)

# for bar, valor in zip(bars, errors.values()):
#     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{valor:.3f}',
#              ha='center', va='bottom', fontsize=9, fontweight='bold')

# plt.tight_layout()
# plt.show()

fig1 = plt.figure(figsize=(10, 7))

plt.subplot(2, 4, 1)
plt.imshow(W_knn)
plt.title('Sklearn KNN')  # Título para la quinta gráfica

plt.subplot(2, 4, 2)
plt.imshow(W_enn)
plt.title('Sklearn Radius')  # Título para la sexta gráfica

plt.subplot(2, 4, 3)
plt.imshow(W_knn_nnk)
plt.title('KNN(NNK)')  # Título para la primera gráfica

plt.subplot(2, 4, 4)
plt.imshow(W_nnk)
plt.title('NNK')  # Título para la segunda gráfica

plt.subplot(2, 4, 5)
plt.imshow(W_vknn)
plt.title('VKNN')  # Título para la tercera gráfica

plt.subplot(2, 4, 6)
plt.imshow(W_kaliofolias)
plt.title('Kaliofolias')  # Título para la cuarta gráfica

plt.subplot(2, 4, 7)
plt.imshow(W_aew)
plt.title('AEW')  # Título para la sexta gráfica

plt.show()
# Falta Time-Varing
# SS MNE
# Falta iterar sobre cantidad de electrodos faltantes
# Falta cambiar dataset
# Falta verificar cada metodo con su dataset.
# Falta optimizar hyperparametros de cada metodo de construccion + interpolación
# pyunlockbox
