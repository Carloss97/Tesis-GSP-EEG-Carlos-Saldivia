# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 14:47:15 2025

@author: sarlo
"""
from scipy.interpolate import SmoothSphereBivariateSpline  # Asegúrate que está importada
from pygsp2 import graphs
import numpy as np
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# %% BGSRP (Tik, Var, Samp, Pocs, Psd)


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
        raise ValueError(
            "¡La base de Fourier no está especificada correctamente!")

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


def spherical_spline_interpolation(X, values, s_initial=1.0, s_retry_factor=5, max_s_retry=10000.0):
    """
    Interpola valores en una esfera usando splines bivariados esféricos.

    Parámetros:
    X (np.ndarray): Coordenadas cartesianas de los sensores (N_sensores, 3).
    values (np.ndarray): Valores en los sensores (N_sensores,). Puede contener NaNs.
    s_initial (float): Parámetro de suavizado inicial para el spline.
    s_retry_factor (float): Factor por el cual se multiplica s si el ajuste inicial falla.
    max_s_retry (float): Valor máximo de s para reintentar en caso de error.

    Retorna:
    np.ndarray: Array de valores con los NaNs interpolados.
                Si la interpolación falla repetidamente, los NaNs originales pueden persistir.
    """
    values_interpolated = values.copy()

    # Normalizar a la esfera unitaria solo si no son ya unitarios (o casi)
    # Esto es importante si X ya representa puntos en una esfera (ej. de un forward model)
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    if np.any(np.abs(norms - 1.0) > 1e-6):  # Si no están ya en la esfera unitaria
        X_unit = X / norms
    else:
        X_unit = X.copy()

    x, y, z = X_unit[:, 0], X_unit[:, 1], X_unit[:, 2]

    # Coordenadas esféricas
    # theta es la colatitud (ángulo polar) [0, pi]
    # phi es la longitud (ángulo azimutal) [0, 2pi]
    theta = np.arccos(np.clip(z, -1.0, 1.0))
    phi = np.mod(np.arctan2(y, x), 2 * np.pi)

    known_mask = ~np.isnan(values)
    unknown_mask = np.isnan(values)

    if not np.any(known_mask) or not np.any(unknown_mask):
        # No hay nada que interpolar o no hay datos conocidos para interpolar
        return values_interpolated

    theta_known = theta[known_mask]
    phi_known = phi[known_mask]
    values_known = values[known_mask]

    theta_unknown = theta[unknown_mask]
    phi_unknown = phi[unknown_mask]

    current_s = s_initial
    spline_fitted = False

    # Intentar ajustar con s_initial
    try:
        # Verificar si hay suficientes puntos para el spline
        # SmoothSphereBivariateSpline requiere al menos (k+1)**2 puntos, donde k es el grado (defecto 3)
        # es decir, al menos 16 puntos.
        # (3+1)**2 = 16. Ajustar según grado si se cambia.
        if len(values_known) < 16:
            # print(f"Advertencia Spline: No hay suficientes puntos conocidos ({len(values_known)}) para ajustar el spline. Se requieren al menos 16. Saltando interpolación para s={current_s:.2f}.")
            # En este caso, no se puede ajustar el spline, se devuelven los NaNs.
            return values_interpolated

        spline = SmoothSphereBivariateSpline(
            theta_known, phi_known, values_known, s=current_s)
        values_interpolated[unknown_mask] = spline(
            theta_unknown, phi_unknown, grid=False)
        spline_fitted = True
    except ValueError as e:
        # print(f"Error al ajustar el spline con s={current_s:.2f}: {e}")
        # Intentar con un s mayor si el error es el esperado
        if "nxest" in str(e) or "nyest" in str(e) or "s too small" in str(e).lower():
            # print(f"Reintentando spline con s más grande...")
            current_s_retry = current_s * s_retry_factor
            if current_s_retry <= max_s_retry:
                try:
                    if len(values_known) < 16:
                        # print(f"Advertencia Spline (reintento): No hay suficientes puntos conocidos ({len(values_known)}) para ajustar el spline. Se requieren al menos 16. Saltando interpolación para s={current_s_retry:.2f}.")
                        return values_interpolated  # Devuelve NaNs

                    spline = SmoothSphereBivariateSpline(
                        theta_known, phi_known, values_known, s=current_s_retry)
                    values_interpolated[unknown_mask] = spline(
                        theta_unknown, phi_unknown, grid=False)
                    spline_fitted = True
                    # print(f"Spline ajustado exitosamente en reintento con s={current_s_retry:.2f}")
                except ValueError as e_retry:
                    # print(f"Error al ajustar el spline en reintento con s={current_s_retry:.2f}: {e_retry}. Devolviendo NaNs.")
                    # Asegurar que son NaN si falla
                    values_interpolated[unknown_mask] = np.nan
                except Exception as e_generic_retry:
                    # print(f"Error genérico al ajustar el spline en reintento con s={current_s_retry:.2f}: {e_generic_retry}. Devolviendo NaNs.")
                    values_interpolated[unknown_mask] = np.nan
            else:
                # print(f"El valor de s para reintento ({current_s_retry:.2f}) excede el máximo ({max_s_retry:.2f}). Devolviendo NaNs.")
                values_interpolated[unknown_mask] = np.nan
        else:
            # Otro ValueError no esperado
            # print(f"ValueError no manejado específicamente: {e}. Devolviendo NaNs.")
            values_interpolated[unknown_mask] = np.nan
    # Captura cualquier otra excepción (ej. LinAlgError)
    except Exception as e_generic:
        # print(f"Error genérico (no ValueError) al ajustar el spline con s={current_s:.2f}: {e_generic}. Devolviendo NaNs.")
        values_interpolated[unknown_mask] = np.nan

    # Si después de todos los intentos, los valores siguen siendo NaN (porque el spline falló),
    # se devolverán como NaN.
    if not spline_fitted:
        values_interpolated[unknown_mask] = np.nan

    return values_interpolated
