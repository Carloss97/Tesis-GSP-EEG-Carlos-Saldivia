# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:46:21 2025

@author: sarlo
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:28:38 2024

@author: sarlo
"""
# %% MNE Spherical Spline

##raw.interpolate_bads()

import numpy as np
def spherical_spline_interpolation(positions, values):
    # Creamos una copia de los valores para no modificar el array original
    interp_values = values.copy()
    
    # Normalizar posiciones a la esfera unitaria
    positions_unit = positions / np.linalg.norm(positions, axis=1, keepdims=True)
    
    # Calcular la matriz de cosenos angulares
    cos_theta = np.dot(positions_unit, positions_unit.T)
    epsilon = 1e-10  # Para evitar problemas numéricos
    cos_theta = np.clip(cos_theta, -1 + epsilon, 1 - epsilon)
    
    # Calcular la matriz G según la fórmula de la interpolación spline esférica
    G = 2 * np.log(1 / np.sqrt(np.maximum(1 - cos_theta**2, epsilon)))
    np.fill_diagonal(G, 0)  # Establecer la diagonal en 0 para evitar autointerpolación
    
    # Identificar electrodos conocidos y faltantes
    known = ~np.isnan(interp_values)
    unknown = np.isnan(interp_values)
    
    # Resolver el sistema lineal para obtener los coeficientes de interpolación
    G_known = G[np.ix_(known, known)]
    V_known = interp_values[known]
    coeffs = np.linalg.solve(G_known, V_known)
    
    # Interpolación para valores faltantes
    G_interp = G[np.ix_(unknown, known)]
    V_interp = np.dot(G_interp, coeffs)
    
    # Reemplazar valores faltantes en la copia
    interp_values[unknown] = V_interp
    return interp_values


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
missing_ratio = 0.1 # 0.02 para 1 faltante
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
#Gr_pygsp = graphs.NNGraph(X, "radius", epsilon = radius,sigma = sigma)
#Gr_pygsp.compute_fourier_basis()
#Wk_pygsp = Gk_pygsp.W.toarray()
#Wr_pygsp = Gr_pygsp.W.toarray()

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

# %% NNK
import sys
import os
# Obtener el directorio actual del script
if hasattr(sys, "frozen"):  # En caso de que el script esté congelado (por ejemplo, con PyInstaller)
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))

# Añadir el directorio principal del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(current_dir, 'PyNNK_graph_construction')))
import numpy as np
import matplotlib.pyplot as plt
from absl import flags, app
from graph_construction import knn_graph, nnk_graph
import graph_utils as utils

# FLAGS = flags.FLAGS
# # Algorithm specific parameters
# flags.DEFINE_integer('knn_param', 5, 'number of neighbors to use for NNK')
# flags.DEFINE_float('thresh', 1e-6, 'threshold corresponding to minimum value of edge weights')
# flags.DEFINE_string('metric', 'rbf', 'Similarity metric to use for finding neighbors: cosine, rbf')
# flags.DEFINE_float('p', 2, 'type of Lp distance to use (if used)')
D = utils.create_distance_matrix(X=X, p=2)
knn_mask = utils.create_directed_KNN_mask(D=D, knn_param=5, D_type='distance')
sigma = np.mean(D[:, knn_mask[:, -1]]) / 3
G = np.exp(-(D ** 2) / (2 * sigma ** 2))
W_knn_nnk = knn_graph(G, knn_mask, 5, 1e-6)
W_nnk = nnk_graph(G, knn_mask, 5, 1e-6)
G_knn_nnk = graphs.Graph(W_knn_nnk)
G_knn_nnk.compute_fourier_basis()
W_knn_nnk = W_knn_nnk.toarray()
G_nnk = graphs.Graph(W_nnk)
G_nnk.compute_fourier_basis()
W_nnk = W_nnk.toarray()

# %% AEW
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
param = {
    'max_iter': 100,
    'k': 10,
    'sigma': 'median'  # o 'local-scaling'
}
W_aew, W0_aew = adaptive_edge_weighting(X, param)
G_aew = graphs.Graph(W_aew)
G0_aew = graphs.Graph(W0_aew)
# %% Interpolación sin grafo
from scipy.interpolate import NearestNDInterpolator, RBFInterpolator
#ND
NNI = NearestNDInterpolator(X[mask], measures[mask])
y_NNI = NNI(X[~mask])
#TPS
RBFI_TPS = RBFInterpolator(X[mask], measures[mask])
y_RBFI_TPS = RBFI_TPS(X[~mask])
#MQ
RBFI_MQ = RBFInterpolator(X[mask], measures[mask], kernel= 'multiquadric', epsilon=0.07)
y_RBFI_MQ = RBFI_MQ(X[~mask])
#SS
y_SSI = spherical_spline_interpolation(X,measures)
# %% Interpolacion Tikhonov 
tau = 0 ##Verificar
#pygsp
y_tik_k_pygsp = learning.regression_tikhonov(Gk_pygsp, measures, mask, tau)
#y_tik_r_pygsp = learning.regression_tikhonov(Gr_pygsp, measures, mask, tau)
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
#AEW
y_tik_aew = learning.regression_tikhonov(G_aew, measures, mask, tau)
y_tik_aew0 = learning.regression_tikhonov(G0_aew, measures, mask, tau)
# %% BGSRP
x = signal ##Reemplazar por señal conocida
x0 = np.where(mask == False)[0]
param = {'bandw': N // 5, 'gamma': 0.1, 'basis': 'lp-ture'}

fx = Gk_skl.U.T @ x
f = Gk_skl.U[:, :N // 10] @ fx[:N // 10]
y0 = f[x0]

y_BGSRP_k_skl = gsp_BGSRP_recon(Gk_skl, x0, y0, param)

err_BGSRP_k_skl = np.mean(np.abs(f - y_BGSRP_k_skl))
err_x_BGSRP_k_skl = np.mean(np.abs(x - y_BGSRP_k_skl))

# %% Error MAE
err_NNI = np.mean(np.abs(y_NNI - y))
err_RBFI_TPS = np.mean(np.abs(y_RBFI_TPS - y))
err_RBFI_MQ = np.mean(np.abs(y_RBFI_MQ - y))
err_SS = np.mean(np.abs(y_SSI[~mask] - y))
err_tik_k_pygsp = np.mean(np.abs(y_tik_k_pygsp[~mask] - y))
#err_tik_r_pygsp = np.mean(np.abs(y_tik_r_pygsp[~mask] - y))
err_tik_k_skl = np.mean(np.abs(y_tik_k_skl[~mask] - y))
err_tik_r_skl = np.mean(np.abs(y_tik_r_skl[~mask] - y))
err_tik_vknn = np.mean(np.abs(y_tik_vknn[~mask] - y))
err_tik_kaliofolias = np.mean(np.abs(y_tik_kaliofolias[~mask] - y))
err_tik_knn_nnk = np.mean(np.abs(y_tik_knn_nnk[~mask] - y))
err_tik_nnk = np.mean(np.abs(y_tik_nnk[~mask] - y))
err_tik_aew = np.mean(np.abs(y_tik_aew[~mask] - y))
err_tik_aew0 = np.mean(np.abs(y_tik_aew0[~mask] - y))



# %%
## Visualizacion

fig = plt.figure(figsize=(10, 7))

plt.subplot(2, 4, 1)
plt.imshow(W_knn_nnk)
plt.title('KNN(NNK)')  # Título para la primera gráfica

plt.subplot(2, 4, 2)
plt.imshow(W_nnk)
plt.title('NNK')  # Título para la segunda gráfica

plt.subplot(2, 4, 3)
plt.imshow(W_vknn)
plt.title('VKNN')  # Título para la tercera gráfica

plt.subplot(2, 4, 4)
plt.imshow(W_kaliofolias)
plt.title('Kaliofolias')  # Título para la cuarta gráfica

plt.subplot(2, 4, 5)
plt.imshow(Wk_skl)
plt.title('Sklearn KNN')  # Título para la quinta gráfica

plt.subplot(2, 4, 6)
plt.imshow(Wr_skl)
plt.title('Sklearn Radius')  # Título para la sexta gráfica

plt.subplot(2, 4, 7)
plt.imshow(W_aew)
plt.title('AEW')  # Título para la sexta gráfica

plt.subplot(2, 4, 8)
plt.imshow(W0_aew)
plt.title('AEW0')  # Título para la sexta gráfica

plt.show()

# %% Visualizacion Errores
# Definir los errores con nombres descriptivos
errores = {
    "NNI": err_NNI,
    "RBFI TPS": err_RBFI_TPS,
    "RBFI MQ": err_RBFI_MQ,
    "Spline Superficie": err_SS,
    "Tikhonov Kernel Pygsp": err_tik_k_pygsp,
    "Tikhonov Kernel SKL": err_tik_k_skl,
    "Tikhonov Regularización SKL": err_tik_r_skl,
    "Tikhonov VKNN": err_tik_vknn,
    "Tikhonov Kaliofolias": err_tik_kaliofolias,
    "Tikhonov KNN+NNK": err_tik_knn_nnk,
    "Tikhonov NNK": err_tik_nnk,
    "AEW": err_tik_aew,
    "AEW0": err_tik_aew0,
    "BGSRP k-NN": err_x_BGSRP_k_skl,
}

# Crear la gráfica
plt.figure(figsize=(10, 5))
bars = plt.bar(errores.keys(), errores.values(), color='skyblue')
plt.ylabel("Error MAE")
plt.title("Comparación de Errores MAE de Diferentes Métodos")
plt.xticks(rotation=45, ha="right")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Añadir los valores de los errores en las barras
for bar, valor in zip(bars, errores.values()):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{valor:.3f}', 
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.show()
# Falta Time-Varing 
# Falta BGSRP con resto
# Falta iterar sobre cantidad de electrodos faltantes
# Falta optimizar hyperparametros de cada metodo de construccion + interpolación