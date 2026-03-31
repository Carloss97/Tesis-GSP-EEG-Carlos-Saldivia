# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:24:06 2024

@author: sarlo
"""

# Non-Graph specific.

# %%  NNInterpolator
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import NearestNDInterpolator
rng = np.random.default_rng()
x = rng.random(10) - 0.5
y = rng.random(10) - 0.5
z = np.hypot(x, y)
X = np.linspace(min(x), max(x))
Y = np.linspace(min(y), max(y))
X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation
interp = NearestNDInterpolator(list(zip(x, y)), z)
Z = interp(X, Y)
plt.pcolormesh(X, Y, Z, shading='auto')
plt.plot(x, y, "ok", label="input point")
plt.legend()
plt.colorbar()
plt.axis("equal")
plt.show()

# %% RBF
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RBFInterpolator
from scipy.stats.qmc import Halton
rng = np.random.default_rng()
xobs = 2*Halton(2, seed=rng).random(100) - 1
yobs = np.sum(xobs, axis=1)*np.exp(-6*np.sum(xobs**2, axis=1))
xgrid = np.mgrid[-1:1:50j, -1:1:50j]
xflat = xgrid.reshape(2, -1).T
yflat = RBFInterpolator(xobs, yobs)(xflat) #kernel, neighbors (MQ, TPS )ValueError: `epsilon` must be specified if `kernel` is not one of {'quintic', 'linear', 'cubic', 'thin_plate_spline'}.
ygrid = yflat.reshape(50, 50)
fig, ax = plt.subplots()
ax.pcolormesh(*xgrid, ygrid, vmin=-0.25, vmax=0.25, shading='gouraud')
p = ax.scatter(*xobs.T, c=yobs, s=50, ec='k', vmin=-0.25, vmax=0.25)
fig.colorbar(p)
plt.show()

# %% MNE Spherical Spline

##raw.interpolate_bads()

import numpy as np

def spherical_spline_interpolation(positions, values):
    # Normalizar posiciones a la esfera unitaria
    positions_unit = positions / np.linalg.norm(positions, axis=1, keepdims=True)
    
    # Calcular matriz de cosenos angulares
    cos_theta = np.dot(positions_unit, positions_unit.T)
    epsilon = 1e-10  # Para evitar problemas numéricos
    cos_theta = np.clip(cos_theta, -1 + epsilon, 1 - epsilon)
    
    # Calcular matriz G
    G = 2 * np.log(1 / np.sqrt(np.maximum(1 - cos_theta**2, epsilon)))
    np.fill_diagonal(G, 0)  # Establecer la diagonal en 0
    
    # Identificar electrodos conocidos y faltantes
    known = ~np.isnan(values)
    unknown = np.isnan(values)
    
    # Resolver sistema para coeficientes
    G_known = G[np.ix_(known, known)]
    V_known = values[known]
    coeffs = np.linalg.solve(G_known, V_known)
    
    # Interpolación para valores faltantes
    G_interp = G[np.ix_(unknown, known)]
    V_interp = np.dot(G_interp, coeffs)
    
    # Reemplazar valores faltantes
    values[unknown] = V_interp
    return values


# %% Tikhonov Regression

## learning.regression_tikhonov(G, measures, mask, tau=0)

# %% Graph TRSS (Natural NI, TVTRSS, Graph Signal Reconstruction, GR, RSD)



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

# import matplotlib.pyplot as plt
# G = graphs.Sensor(500) #Reemplazar por grafo conocido
# G.compute_fourier_basis()
# x = 2 * np.random.rand(G.N) - 1 ##Reemplazar por señal conocida
# fx = G.U.T @ x
# f = G.U[:, :G.N // 10] @ fx[:G.N // 10]
# p = np.random.permutation(G.N)
# labs = int(0.2 * G.N)
# x0 = p[:labs]
# y0 = f[x0]
# param = {'bandw': G.N // 5, 'gamma': 0.1, 'basis': 'lp-ture'}
# y = gsp_BGSRP_recon(G, x0, y0, param)
# error = np.mean(np.abs(f - y))
# error_x = np.mean(np.abs(x - y))
# print(f"Error: {error}")
# plt.figure(figsize=(10, 6))
# plt.plot(x, label="Señal original (x)", linestyle="--", alpha=0.7)
# plt.plot(f, label="Señal limitada en banda (f)", alpha=0.8)
# plt.plot(y, label="Señal reconstruida (y)", linestyle=":")
# plt.scatter(x0, y0, color="red", label="Etiquetas conocidas", zorder=5)
# plt.legend()
# plt.title("Comparación de señales")
# plt.show()

