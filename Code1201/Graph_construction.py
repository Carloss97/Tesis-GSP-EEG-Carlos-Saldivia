# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:10:41 2024

@author: sarlo
"""

# %% Similarity Kernels

# Gaussian Kernel

## Selection of sigma
### Variance of d
### mean of d
### 1/3 mean of d
### k_th Neighbour within 3*sigma

# Cosine similarity.
from sklearn.metrics.pairwise import cosine_similarity
###cosine_similarity(X, Y)

 
# %% Adaptative Edge Weighting (AEW) ????
import numpy as np
from scipy.spatial.distance import pdist, squareform

def generate_nngraph(X, k, sigma):
    """
    Construye el grafo kNN.
    
    Parámetros:
      X: Matriz de datos de forma (n, d) (n instancias, d características)
      k: Número de vecinos
      sigma: Estrategia para definir el parámetro de anchura ('median' o 'local-scaling')
      
    Retorna:
      W: Matriz de adyacencia ponderada (n, n)
      sigma: Parámetro de anchura (escala global o vector, según la opción)
    """
    n = X.shape[0]
    # Calcula las distancias cuadráticas entre instancias
    D = squareform(pdist(X, metric='euclidean')**2)
    sort_idx = np.argsort(D, axis=1)
    sort_D = np.sort(D, axis=1)
    
    # Selecciona los k vecinos más cercanos (excluyendo la misma instancia)
    knn_idx = sort_idx[:, 1:k+1]
    kD = sort_D[:, 1:k+1]
    
    W = np.zeros((n, n))
    if sigma == 'median':
        sigma_val = np.median(np.sqrt(kD.flatten()))
        sigma_val = max(sigma_val, 1e-6)
        for i in range(n):
            W[i, knn_idx[i]] = np.exp(-kD[i] / (2 * sigma_val**2))
        sigma_out = sigma_val  # Escalar
    elif sigma == 'local-scaling':
        # Utiliza el vecino 7 (o el último disponible si k < 7)
        idx = min(6, k-1)
        sigma_vec = np.sqrt(kD[:, idx])
        sigma_vec[sigma_vec == 0] = 1
        for i in range(n):
            W[i, knn_idx[i]] = np.exp(-kD[i] / (sigma_vec[i] * sigma_vec[knn_idx[i]]))
        sigma_out = sigma_vec  # Vector de escala
    else:
        raise ValueError('Unknown option for sigma')
    
    # Forzamos la simetría
    W = np.maximum(W, W.T)
    return W, sigma_out

def adaptive_edge_weighting(X, param):
    """
    Implementa el método Adaptive Edge Weighting para propagación de etiquetas.
    
    Parámetros:
      X: Matriz de datos con forma (n, d), donde n = número de instancias y d = número de características.
      param: Diccionario con:
         - 'k': número de vecinos en el grafo kNN.
         - 'sigma': opción para definir el parámetro de anchura ('median' o 'local-scaling').
         - 'max_iter': número máximo de iteraciones para el descenso de gradiente.
         
    Retorna:
      W: Matriz de adyacencia optimizada.
      W0: Matriz de adyacencia inicial.
    """
    n, d = X.shape  # X está en forma (n, d)
    tol = 1e-4
    beta = 0.1
    beta_p = 0
    max_beta_p = 8
    rho = 1e-3

    # Genera el grafo inicial (W0) y el parámetro sigma0
    W0, sigma0 = generate_nngraph(X, param['k'], param['sigma'])
    L = np.eye(d)  # Matriz L (inicialmente identidad)

    Xori = X.copy()  # Conserva la versión original de X

    # Calcula la matriz de distancias (entre instancias)
    dist = squareform(pdist(X, metric='euclidean')**2)
    if np.isscalar(sigma0):
        # Si sigma0 es escalar, se escala X
        X = X / (np.sqrt(2) * sigma0)
    else:
        sigma0 = sigma0.reshape(-1, 1)  # Aseguramos que sigma0 sea columna
        dist = dist / (sigma0 @ sigma0.T)

    # Construye la matriz W inicial a partir de W0 y distancias
    edge_idx = np.where(W0 > 0)
    W = np.zeros((n, n))
    W[edge_idx] = np.exp(-dist[edge_idx])

    # Calcula la matriz Gd: para cada par (i, j) con conexión, se guarda -(X[i]-X[j])^2
    Gd = np.zeros((n, n, d))
    W_idx = {i: np.where(W[i, :] > 0)[0] for i in range(n)}
    for i in range(n):
        for j in W_idx[i]:
            Gd[i, j, :] = -(X[i, :] - X[j, :]) ** 2
            if not np.isscalar(sigma0):
                Gd[i, j, :] /= (sigma0[i] * sigma0[j])
    
    # Inicializa las matrices para derivadas parciales
    d_W = np.zeros((n, n, d))
    d_WDi = np.zeros((n, n, d))

    # --- Bucle principal de optimización ---
    for iter in range(param['max_iter']):
        # Calcula D = suma de los pesos en cada fila (grado de cada nodo)
        D = W.sum(axis=1, keepdims=True)
        D[D == 0] = 1

        # Calcula d_W para cada nodo i y sus vecinos
        for i in range(n):
            # Aquí se emula: d_W(i, W_idx{i}, :) = 2*diag(W(i, W_idx{i}))*Gd(i, W_idx{i}, :) .* (ones(length(W_idx{i}),1)*diag(L)')
            # Tomamos diag(L) (vector de longitud d)
            L_diag = np.diag(L)  # forma (d,)
            # Multiplicación elemento a elemento:
            d_W[i, W_idx[i], :] = 2 * W[i, W_idx[i]].reshape(-1, 1) * Gd[i, W_idx[i], :] * L_diag

        # Suma de d_W en la dimensión de vecinos (para cada i, suma a lo largo de j)
        sum_d_W = np.sum(d_W, axis=1)  # forma (n, d)
        for i in range(n):
            # d_WDi(i, W_idx{i}, :) = d_W(i, W_idx{i}, :) / D[i] - (W(i, W_idx{i})/(D[i]^2)) * sum_d_W(i, :)
            d_WDi[i, W_idx[i], :] = d_W[i, W_idx[i], :] / D[i] - (W[i, W_idx[i]].reshape(-1, 1) / (D[i] ** 2)) @ sum_d_W[i, :].reshape(1, d)

        # Calcula Xest según la fórmula: Xest = (diag(1./D) * W * Xori) 
        # Aquí, diag(1./D) es (n, n), W es (n, n) y Xori es (n, d)
        Xest = np.diag(1.0 / D.flatten()) @ W @ Xori  # Resultado en (n, d)

        err = Xori - Xest  # Error (n, d)
        sqerr = np.sum(err ** 2)

        # === Cálculo del gradiente ===
        # En MATLAB, se hace:
        # grad = -(reshape(d_WDi, n^2, d)' * vec(err' * Xori))';
        #
        # Para emularlo, debemos considerar que MATLAB trata Xori como (d, n).
        # Por ello, definimos:
        X_m = Xori.T      # X_m es Xori en formato MATLAB, forma (d, n)
        Xest_m = Xest.T   # Xest_m es (d, n)
        err_m = X_m - Xest_m  # error en formato MATLAB, forma (d, n)
        # MATLAB hace: err' * Xori, es decir (err_m)' * X_m, donde (err_m)' tiene forma (n, d)
        temp = err_m.T @ X_m  # Resultado: (n, d) @ (d, n) = (n, n)
        vec_temp = temp.flatten()  # Aplanamos a un vector de longitud n*n

        # Reorganizamos d_WDi: reshape a (n^2, d) y luego transponemos para obtener (d, n^2)
        grad = -np.dot(d_WDi.reshape(n ** 2, d).T, vec_temp)  # Resultado: (d,)
        grad /= np.linalg.norm(grad)

        print(f'Iter = {iter}, MSE = {sqerr / (d * n):.6e}')

        # --- Descenso de gradiente con búsqueda de línea ---
        step = beta ** beta_p
        sqerr_prev = sqerr
        L_prev = L.copy()

        while True:
            # Actualiza L en función del gradiente (solo en la diagonal)
            L = L_prev - step * np.diag(grad)
            # Calcula la nueva matriz de distancias con la transformación L
            dist = squareform(pdist((X @ L), metric='euclidean')**2)
            if not np.isscalar(sigma0):
                dist /= (sigma0 @ sigma0.T)
            W[edge_idx] = np.exp(-dist[edge_idx])

            D = W.sum(axis=1, keepdims=True)
            D[D == 0] = 1
            Xest = np.diag(1.0 / D.flatten()) @ W @ Xori
            err = Xori - Xest
            sqerr_temp = np.sum(err ** 2)

            if sqerr_temp - sqerr_prev <= -rho * step * np.dot(grad, grad):
                break

            beta_p += 1
            if beta_p > max_beta_p:
                return W, W0
            step *= beta

        if (sqerr_prev - sqerr_temp) / sqerr_prev < tol:
            break

    return W, W0


# Ejemplo de uso
#X = np.random.rand(50, 10)  # Matriz de datos de entrada (50 instancias, 10 características)
# param = {
#     'max_iter': 100,
#     'k': 10,
#     'sigma': 'median'  # o 'local-scaling'
# }
# W, W0 = adaptive_edge_weighting(X, param)
# %% k*NN no lo encuentro
# %% k/e - NN sparsification (Thresholding techniques)
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


# %% Non-Negative Kernel (NNK) regression
import os
import numpy as np
import sys

# Añadir la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(r'C:\Users\sarlo\OneDrive\Escritorio\Work'))
from Papers.PyNNK_graph_construction import graph_utils as utils
from Papers.PyNNK_graph_construction.graph_construction import knn_graph, nnk_graph
import matplotlib.pyplot as plt


def NNK(X, knn_param=5, thresh=1e-6, metric='rbf', p=2):
    """
    Constructs the KNN and NNK graphs from the input matrix X.
    
    Args:
    - X: numpy array of shape (n_samples, n_features), the data points.
    - knn_param: number of neighbors to use for KNN.
    - thresh: threshold for minimum edge weights.
    - metric: similarity metric ('cosine' or 'rbf').
    - p: the Lp distance type to use for distance calculations (only if 'rbf' is chosen).
    
    Returns:
    - W_knn: KNN graph (sparse matrix).
    - W_nnk: NNK graph (sparse matrix).
    """
    
    if metric == 'cosine':
        # Normalize the data for cosine similarity
        X_normalized = X / np.linalg.norm(X, axis=1)[:, None]
        # Compute the similarity matrix
        G = 0.5 + np.dot(X_normalized, X_normalized.T) / 2.0
        # Create KNN mask based on similarity
        knn_mask = utils.create_directed_KNN_mask(D=G, knn_param=knn_param, D_type='similarity')
        
    elif metric == 'rbf':
        # Compute the distance matrix for RBF kernel
        D = utils.create_distance_matrix(X=X, p=p)
        # Create KNN mask based on distance
        knn_mask = utils.create_directed_KNN_mask(D=D, knn_param=knn_param, D_type='distance')
        # Compute sigma for RBF kernel
        sigma = np.mean(D[:, knn_mask[:, -1]]) / 3
        # Compute the RBF similarity matrix
        G = np.exp(-(D ** 2) / (2 * sigma ** 2))
    else:
        raise Exception("Unknown metric: " + metric)
    
    # Construct KNN graph
    W_knn = knn_graph(G, knn_mask, knn_param, thresh)
    
    # Construct NNK graph
    W_nnk = nnk_graph(G, knn_mask, knn_param, thresh)
    
    return W_knn, W_nnk

# %% Kaliofolias

##EEGraSP.learn_graph
## pygs2. W = graph_learning.graph_log_degree(
 #     Z, a, b, gamma=gamma, w_max=w_max, maxiter=maxiter)
 # W[W < 1e-5] = 0
# %% vKNNs

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

