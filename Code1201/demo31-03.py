# Asd.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist
from pygsp2 import graphs, learning
from scipy.interpolate import NearestNDInterpolator, RBFInterpolator
from construction import vkNNG, adjacency_matrix, adaptive_edge_weighting, NNK, kaliofolias
from interpolation import spherical_spline_interpolation, gsp_BGSRP_recon

# lectura archivos
df_pos = pd.read_pickle(
    r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis\code\filt0-40.pkl")
df_pos = df_pos.drop(index='EEG 053')
df_100 = pd.read_pickle(
    r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis\code\df_100.pkl")
# Señales
signal = df_100.iloc[1:].to_numpy()
X = df_pos[['x', 'y', 'z']].to_numpy()
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
missing_ratio = 0.1  # 0.02 para 1 faltante
rng = np.random.default_rng(42)
mask = rng.uniform(0, 1, N) > missing_ratio
missing_idx = np.where(mask == False)[0]
y = signal[~mask]
# Señal con datos faltantes.
measures = signal.copy()
measures[~mask] = np.nan

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
epsilon_MQ = 0.06
s_SSI = 20.0  # SSI
tau_tik = 0
param_BGSRP = {'bandw': N // 5, 'gamma': 0.1, 'basis': 'lp-ture'}
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
interpolations = {}
errors = {}
# %% Interpolación.
# Métodos sin grafo con sus parámetros
interpolations = {
    "NNI": NearestNDInterpolator(X[mask], measures[mask])(X[~mask]),
    "RBFI TPS": RBFInterpolator(X[mask], measures[mask])(X[~mask]),
    f"RBFI MQ(ε={epsilon_MQ})": RBFInterpolator(X[mask], measures[mask], kernel='multiquadric', epsilon=epsilon_MQ)(X[~mask]),
    f"Spline Superficie(s={s_SSI})": spherical_spline_interpolation(X, measures, s_SSI)[~mask],
}
# Cálculo de errores para métodos sin grafo
errors = {
    name: np.mean(np.abs(y_hat - y))
    for name, y_hat in interpolations.items()
}
for name, graph in graphs_dict.items():
    # Métodos con grafo (Tikhonov)
    y_tikh = learning.regression_tikhonov(graph, measures, mask, tau_tik)
    label = f"Tikhonov({name},τ={tau_tik})"
    interpolations[label] = y_tikh[~mask]
    errors[label] = np.mean(np.abs(y_tikh[~mask] - y))

    # Espectro y reconstrucción parcial
    fx = graph.U.T @ signal
    f = graph.U[:, :param_BGSRP['bandw']] @ fx[:param_BGSRP['bandw']]
    y0 = f[missing_idx]
    y_BGSRP = gsp_BGSRP_recon(graph, missing_idx, y0, param_BGSRP)

    label = (
        f"BGSRP({name},"
        f"bandw={param_BGSRP['bandw']},γ={param_BGSRP['gamma']},"
        f"basis={param_BGSRP['basis']})"
    )
    interpolations[label] = y_BGSRP
    errors[label] = np.mean(np.abs(signal - y_BGSRP))


# %%Visualizacion
# Visualización
fig0 = plt.figure(figsize=(13, 8))
bars = plt.bar(errors.keys(), errors.values(), color='skyblue')
plt.ylabel("Error MAE")
plt.title("Comparación de Errores MAE con Parámetros")
plt.xticks(rotation=75, ha="right")
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar, valor in zip(bars, errors.values()):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{valor:.3f}',
             ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()

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
