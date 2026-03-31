# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:28:38 2024

@author: sarlo
"""

# import sys
# import os
# Añadir la carpeta raíz del proyecto al sys.path
#sys.path.append(os.path.abspath(r'C:\Users\sarlo\OneDrive\Escritorio\Work'))
#import Papers.PyNNK_graph_construction as pkg
#from Papers.PyNNK_graph_construction import graph_utils as utils
#from Papers.PyNNK_graph_construction.graph_construction import knn_graph, nnk_graph

# %% BGSRP (Tik, Var, Samp, Pocs, Psd)
import numpy as np
from pygsp2 import graphs

def gsp_BGSRP_recon(G, x0, y0, param):
    """
    Reconstrucción de señales en grafos mediante BGSRP.

    Parámetros:
    ----------
    G : objeto de la clase Graph de pygsp
        Estructura del grafo.
    x0 : array-like
        Índices de los nodos con etiquetas conocidas.
    y0 : array-like
        Etiquetas conocidas.
    param : dict
        Parámetros adicionales (bandw, gamma, basis).
%   Example:
        G = graphs.Sensor(500)
        G.compute_fourier_basis()
        
        x = 2 * np.random.rand(G.N) - 1
        fx = G.U.T @ x
        f = G.U[:, :G.N // 10] @ fx[:G.N // 10]
        
        p = np.random.permutation(G.N)
        labs = int(0.2 * G.N)
        x0 = p[:labs]
        y0 = f[x0]
        
        param = {'bandw': G.N // 5, 'gamma': 0.1, 'basis': 'lp-ture'}
        y = gsp_BGSRP_recon(G, x0, y0, param)
        error = np.mean(np.abs(f - y))
        print(f"Error: {error}")
Error entre la señal original (x) y la reconstrucción (y)
error_x = np.mean(np.abs(x - y))
%          
%       
%
%   Additional parameters
%   ---------------------
%    param.bandw  : The bandwidth coeffcient n in the algorithm. 
%    param.gamma  : The regularization parameter used to balance the weight 
%                   between the error and the quality index
%    param.basis  : Select the Fourier basis to be used for the computation. 
%      'lp-ture'   : Use the accurate Fourier basis of graph Laplacian
%      'lp-FEARS'  : Use the approximate Fourier basis by FEARS method
    Retorna:
    -------
    y : ndarray
        Señal reconstruida.
    """
    ell = len(x0)
    n = param.get("bandw", 10)  # Default bandwidth
    basis_type = param.get("basis", "lp-ture")
    gamma = param.get("gamma", 0.1)

    if basis_type == "lp-ture":
        # Base de Fourier exacta
        G.compute_fourier_basis()
        Un = G.U[:, 1:n]
        mu = G.e
    elif basis_type == "lp-FEARS":
        # Base aproximada usando FEARS
        basis = G.estimate_lmax()  # Estimación para FEARS
        G.compute_fourier_basis()  # Para obtener G.L si no está
        L = G.L
        Un = basis[:, 1:n]
        mu = np.array([basis[:, i].T @ L @ basis[:, i] for i in range(1, n)])
    else:
        raise ValueError("¡La base de Fourier no está especificada correctamente!")

    Phin = np.diag(1 / mu[1:n])
    A = np.eye(ell) - np.ones((ell, ell)) / ell
    B = Un[x0, :]

    GG = B @ (gamma * Phin + Phin @ B.T @ A @ B @ Phin) @ B.T
    d = B @ Phin @ B.T @ A @ y0

    xi = np.linalg.pinv(GG) @ d
    g = Un @ Phin @ B.T @ xi
    z = -np.ones(ell) @ (g[x0] - y0) * np.sqrt(G.N) / ell
    y = z * np.ones(G.N) / np.sqrt(G.N) + g

    return y

# %%

import numpy as np
from scipy.sparse import lil_matrix

def vkNNG(Z, k_min, k_max, beta_factor=0.1):
    """
    Algoritmo para construir un grafo vkNNG a partir de una matriz de distancias.

    Parámetros:
    Z : np.ndarray
        Matriz de distancias Euclidianas de tamaño (N, N)
    k_min : int
        Número mínimo de vecinos a considerar para cada nodo
    k_max : int
        Número máximo de vecinos a considerar para cada nodo
    beta_factor : float, opcional
        Factor para ajustar los valores de beta_i, por defecto 0.1

    Retorna:
    graph_sparse_csr : scipy.sparse.csr_matrix
        Matriz dispersa en formato CSR representando el grafo
    k_values : np.ndarray
        Array de tamaño N con el número de vecinos para cada nodo
    """
    N = Z.shape[0]  # Número de nodos
    #beta = beta_factor * np.sum(Z, axis=1)/N  Le agrego el /N para hacer la media
    beta = beta_factor * np.sum(Z, axis=1) # Calcular beta_i 
    # Grafo disperso para almacenar las conexiones
    graph_sparse = lil_matrix((N, N))
    k_values = np.zeros(N, dtype=int)  # Almacenar k_i para cada nodo

    for i in range(N):
        # Ordenar las distancias y obtener índices de los vecinos más cercanos
        indices_sorted = np.argsort(Z[i, :])
        Z_sorted = Z[i, indices_sorted]
        
        # Inicializar variables
        delta_i = Z_sorted[k_min]  # Inicia con la distancia al vecino más cercano
        k_i = k_min

        # Ajustar el número de vecinos según el algoritmo
        while delta_i < beta[i] and k_i < k_max:
            k_i += 1
            delta_i += Z_sorted[k_i]
        
        # Guardar el valor final de k_i
        k_values[i] = k_i
        
        # Añadir las aristas a la matriz dispersa
        neighbors = indices_sorted[1:k_i + 1]  # Ignorar el nodo mismo (índice 0)
        for neighbor in neighbors:
            graph_sparse[i, neighbor] = Z[i, neighbor]  # Guardar la distancia como peso de la arista

    # Convertir la matriz dispersa a formato CSR para eficiencia
    graph_sparse_csr = graph_sparse.tocsr()

    return graph_sparse_csr, k_values

# %%
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import kneighbors_graph, radius_neighbors_graph
from scipy.sparse import lil_matrix

def gaussian_kernel(distances, sigma):
    """
    Calcula los pesos usando un kernel gaussiano.
    :param distances: Distancias entre los puntos
    :param sigma: Parámetro sigma del kernel gaussiano
    :return: Pesos calculados con el kernel gaussiano
    """
    return np.exp(-distances**2 / (2 * sigma**2))

def adjacency_matrix(X, k=None, radius=None, sigma=1.0, method='knn'):
    """
    Crea una matriz de adyacencia para un grafo dado un conjunto de coordenadas.
    :param X: Matriz de coordenadas (n_samples x n_features)
    :param k: Número de vecinos (solo se usa si method='knn')
    :param radius: Radio de vecinos (solo se usa si method='radius_neighbors')
    :param sigma: Parámetro sigma del kernel gaussiano
    :param method: 'knn' para vecinos más cercanos k-nn, 'radius_neighbors' para radio de vecinos
    :param return_dense: Si es True, convierte la matriz a densa
    :return: Matriz de adyacencia (densa o dispersa) y matriz de distancias
    """
    N, d = X.shape  # Número de puntos y dimensionalidad
    X = X - np.mean(X, axis=0)
    bounding_radius = 0.5 * np.linalg.norm(np.amax(X, axis=0) - np.amin(X, axis=0), 2)
    scale = np.power(N, 1. / float(min(d, 3))) / 10.
    X *= scale / bounding_radius
    n_samples = X.shape[0]
    adj_matrix = lil_matrix((n_samples, n_samples))  # Matriz dispersa
    


    # Calculamos las distancias entre todos los puntos
    distances = euclidean_distances(X, X)
    #pairwise = pairwise_distances(X)
    
    if method == 'knn':
        # Usar la función de sklearn para obtener la matriz de adyacencia de k-nn
        adj_matrix_sk = kneighbors_graph(X, k, mode='distance', include_self=False)
    elif method == 'radius_neighbors':
        # Usar la función de sklearn para obtener la matriz de adyacencia de radius_neighbors
        adj_matrix_sk = radius_neighbors_graph(X, radius, mode='distance', include_self=False)

    # Llenar la matriz de adyacencia con los pesos gaussianos
    for i in range(n_samples):
        for j in range(n_samples):
            if adj_matrix_sk[i, j] > 0:
                weight = gaussian_kernel(distances[i, j], sigma)
                adj_matrix[i, j] = weight
                adj_matrix[j, i] = weight  # Grafo no dirigido

    
    return adj_matrix, distances

# %%
import pandas as pd
import numpy as np
from scipy.spatial.distance import squareform, pdist
from pygsp2 import graphs, graph_learning, learning
import matplotlib.pyplot as plt

#lectura archivos
df_pos = pd.read_pickle(r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis\code\filt0-40.pkl")
df_pos = df_pos.drop(index='EEG 053')
df_100 = pd.read_pickle(r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis\code\df_100.pkl")

#Señales
signal = df_100.iloc[0, 1:].to_numpy()
X = df_pos[['x', 'y','z']].to_numpy()
# Escala si es necesario

N, d = X.shape  # Número de puntos y dimensionalidad
X_scaled = X - np.kron(np.ones((N, 1)), np.mean(X, axis=0)) # Center
bounding_radius = 0.5 * np.linalg.norm(np.amax(X_scaled, axis=0) - np.amin(X_scaled, axis=0), 2)
scale = np.power(N, 1. / float(min(d, 3))) / 10. 
X_scaled *= scale / bounding_radius # Rescale

# Matriz de distnacias
Z = squareform(pdist(X))
Z_scaled = squareform(pdist(X_scaled))

# Mascara para datos faltantes
missing_ratio = 0.3
rng = np.random.default_rng(42)
mask = rng.uniform(0, 1, N) > missing_ratio
y = signal[~mask]
# Señal con datos faltantes.
measures = signal.copy()
measures[~mask] = np.nan

# Hiperparametros
### Variance of d
### mean of d
### 1/3 mean of d
### k_th Neighbour within 3*sigma
sigma = np.mean(Z)/3
radius = np.mean(Z)
k = 5
# %% Construccion grafo Pygsp2
Gk_pygsp = graphs.NNGraph(X, k = k, sigma = sigma)
#Gk.set_coordinates(X/np.amax(X))
Gk_pygsp.compute_fourier_basis()
Gr_pygsp = graphs.NNGraph(X, "radius", epsilon = radius,sigma = sigma)
Gr_pygsp.compute_fourier_basis()
Wk_pygsp = Gk_pygsp.W.toarray()
Wr_pygsp = Gr_pygsp.W.toarray()

# %% Construcction skl
Wk_skl, _ = adjacency_matrix(X,k,sigma = sigma, method = 'knn')
Gk_skl = graphs.Graph(Wk_skl)
Gk_skl.compute_fourier_basis()
Wr_skl, _ = adjacency_matrix(X,radius = radius,sigma = sigma, method = "radius_neighbors")
Gr_skl = graphs.Graph(Wr_skl)
Gr_skl.compute_fourier_basis()
Wk_skl = Wk_skl.toarray()
Wr_skl = Wr_skl.toarray()

# %% Construccion vKNN
#from sklearn.metrics.pairwise import rbf_kernel
#rbf = rbf_kernel(X, gamma = 1/sigma)
W_vknn, k_values = vkNNG(Z,k_min = 2, k_max = 5, beta_factor=0.01)
G_vknn = graphs.Graph(W_vknn)
G_vknn.compute_fourier_basis()
W_vknn = W_vknn.toarray()

# %% Kaliofolias
a=0.34
b=0.4
gamma = 0.04
W_kaliofolias = graph_learning.graph_log_degree(Z, a, b, gamma= gamma)
W_kaliofolias[W_kaliofolias < 1e-5] = 0
G_kaliofolias = graphs.Graph(W_kaliofolias)
G_kaliofolias.compute_fourier_basis()

# %% NNK FALTA
# correr nnk_demo.py
# G_knn_nnk = graphs.Graph(W_knn_nnk)
# G_knn_nnk.compute_fourier_basis()
# W_knn_nnk = W_knn_nnk.toarray()
# G_nnk = graphs.Graph(W_nnk)
# G_nnk.compute_fourier_basis()
# W_nnk = W_nnk.toarray()

# %% AEW FALTA

# %% LLE FALTA

# %% Interpolación sin grafo
from scipy.interpolate import NearestNDInterpolator, RBFInterpolator
NNI = NearestNDInterpolator(X[mask], measures[mask])
y_NNI = NNI(X[~mask])
RBFI = RBFInterpolator(X[mask], measures[mask])
y_RBFI = RBFI(X[~mask])

# %% Interpolacion Tikhonov 
tau = 0 ##Verificar
#pygsp
y_tik_k_pygsp = learning.regression_tikhonov(Gk_pygsp, measures, mask, tau)
y_tik_r_pygsp = learning.regression_tikhonov(Gr_pygsp, measures, mask, tau)
#skl
y_tik_k_skl = learning.regression_tikhonov(Gk_skl, measures, mask, tau)
y_tik_r_skl = learning.regression_tikhonov(Gr_skl, measures, mask, tau)
#vknn
y_tik_vknn = learning.regression_tikhonov(G_vknn, measures, mask, tau)
#Kaliofolias
y_tik_kaliofolias = learning.regression_tikhonov(G_kaliofolias, measures, mask, tau)
#NNK
y_tik_knn_nnk = learning.regression_tikhonov(G_knn_nnk, measures, mask, tau)
y_tik_nnk = learning.regression_tikhonov(G_nnk, measures, mask, tau)

# %% BGSRP
x = signal ##Reemplazar por señal conocida
p = np.random.permutation(N)
sampling_rate = 0.3
labs = int(sampling_rate * N)
x0 = p[:labs]
param = {'bandw': N // 5, 'gamma': 0.1, 'basis': 'lp-ture'}

# fx = G.U.T @ x
# f = G.U[:, :G.N // 10] @ fx[:G.N // 10]
# y0 = f[x0]

# y = gsp_BGSRP_recon(G, x0, y0, param)

# %% Error MAE
err_NNI = np.mean(np.abs(y_NNI - y))
err_RBFI = np.mean(np.abs(y_RBFI - y))
err_tik_k_pygsp = np.mean(np.abs(y_tik_k_pygsp[~mask] - y))
err_tik_r_pygsp = np.mean(np.abs(y_tik_r_pygsp[~mask] - y))
err_tik_k_skl = np.mean(np.abs(y_tik_k_skl[~mask] - y))
err_tik_r_skl = np.mean(np.abs(y_tik_r_skl[~mask] - y))
err_tik_vknn = np.mean(np.abs(y_tik_vknn[~mask] - y))
err_tik_kaliofolias = np.mean(np.abs(y_tik_kaliofolias[~mask] - y))
err_tik_knn_nnk = np.mean(np.abs(y_tik_knn_nnk[~mask] - y))
err_tik_nnk = np.mean(np.abs(y_tik_nnk[~mask] - y))

# %%
## Visualizacion

# fig = plt.figure(figsize=(10, 7))
# plt.subplot(1,2,1)
# plt.imshow(Wkpygsp)
# plt.subplot(1,2,2)
# plt.imshow(Wrpygsp)
# plt.show()

# AEW No
# Time-Varing aun no
# LLE no sé hacerlo
# 




