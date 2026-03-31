"""
interpolation_methods.py
Métodos de interpolación/reconstrucción para señales EEG con canales faltantes.
"""

from typing import Any, Dict
import numpy as np
from scipy.interpolate import interp1d


def interpolate_signals(method: str, signals: np.ndarray, adjacency: np.ndarray = None, **kwargs) -> Dict[str, Any]:
    """
    Wrapper para interpolar señales EEG con canales faltantes.
    - method: 'linear', 'gsp', etc.
    - signals: matriz (N_instantes, N_electrodos) con NaN en canales faltantes
    - adjacency: matriz de adyacencia (opcional, para métodos GSP)
    Retorna un diccionario con:
      - 'reconstructed': señales reconstruidas (N_instantes, N_electrodos)
      - 'info': metadatos
    """
    if method == 'linear':
        reconstructed = interpolate_linear(signals)
        info = {'method': 'linear'}
        return {'reconstructed': reconstructed, 'info': info}
    elif method == 'gsp':
        if adjacency is None:
            raise ValueError('Se requiere matriz de adyacencia para interpolación GSP')
        reconstructed = interpolate_gsp(signals, adjacency)
        info = {'method': 'gsp'}
        return {'reconstructed': reconstructed, 'info': info}
    else:
        raise NotImplementedError(f"Método de interpolación no implementado: {method}")


def interpolate_linear(signals: np.ndarray) -> np.ndarray:
    """
    Interpolación lineal simple a lo largo de los canales (por instante).
    """
    reconstructed = signals.copy()
    N, D = signals.shape
    for i in range(N):
        row = signals[i]
        mask = ~np.isnan(row)
        if np.sum(mask) < 2:
            continue  # No se puede interpolar
        x = np.arange(D)
        reconstructed[i] = np.interp(x, x[mask], row[mask])
    return reconstructed


def interpolate_gsp(signals: np.ndarray, adjacency: np.ndarray) -> np.ndarray:
    """
    Interpolación basada en Laplaciano de grafo (mínima energía).
    """
    from scipy.sparse import csgraph
    reconstructed = signals.copy()
    N, D = signals.shape
    L = csgraph.laplacian(adjacency, normed=False)
    for i in range(N):
        y = signals[i]
        mask = ~np.isnan(y)
        if np.all(mask):
            continue  # No hay faltantes
        # Resolver L_uu x = -L_uk y_k
        known_idx = np.where(mask)[0]
        unknown_idx = np.where(~mask)[0]
        L_uu = L[np.ix_(unknown_idx, unknown_idx)]
        L_uk = L[np.ix_(unknown_idx, known_idx)]
        y_k = y[known_idx]
        try:
            x = np.linalg.solve(L_uu, -L_uk @ y_k)
            y_rec = y.copy()
            y_rec[unknown_idx] = x
            reconstructed[i] = y_rec
        except np.linalg.LinAlgError:
            pass  # Si el sistema es singular, dejar NaN
    return reconstructed
