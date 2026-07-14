"""
interpolators.py
Funciones generales para interpolar/reconstruir señales EEG a partir de un grafo.
"""

from typing import Any, Dict
import numpy as np

# Interfaz estándar para interpolación/reconstrucción

import numpy as np

def interpolate(method: str, signals_incomplete: np.ndarray, adjacency: np.ndarray, **kwargs) -> Dict[str, Any]:
    """
    Interpola/reconstruye señales EEG usando el método especificado.
    - method: nombre del método ("laplacian", "tikhonov", "rbf", etc.)
    - signals_incomplete: vector o matriz con NaN en canales faltantes
    - adjacency: matriz de adyacencia del grafo
    - kwargs: parámetros específicos del método
    Retorna un diccionario con:
      - 'signals_reconstructed': señales reconstruidas (mismo shape que entrada)
      - 'info': metadatos/resultados del método
    """
    if method == "dummy_mean":
      # Interpolación simple: reemplaza NaN por la media de los canales presentes en cada instante
      signals_rec = signals_incomplete.copy()
      for i in range(signals_rec.shape[0]):
        row = signals_rec[i]
        isnan = np.isnan(row)
        if np.any(isnan):
          mean_val = np.nanmean(row)
          row[isnan] = mean_val
          signals_rec[i] = row
      return {"signals_reconstructed": signals_rec, "info": {"method": "dummy_mean"}}
    elif method == "laplacian":
        # Interpolación Laplaciana (GSP) para cada instante de tiempo
        import warnings
        signals_rec = signals_incomplete.copy()
        A = adjacency
        if not isinstance(A, np.ndarray):
            A = A.toarray() if hasattr(A, 'toarray') else np.array(A)
        D = np.diag(A.sum(axis=1))
        L = D - A
        for t in range(signals_rec.shape[0]):
            y = signals_rec[t]
            mask_known = ~np.isnan(y)
            mask_missing = np.isnan(y)
            if np.sum(mask_missing) == 0:
                continue
            L_uu = L[np.ix_(mask_missing, mask_missing)]
            L_uk = L[np.ix_(mask_missing, mask_known)]
            y_k = y[mask_known]
            # Resolver L_uu y_u = -L_uk y_k
            try:
                y_u = np.linalg.solve(L_uu, -L_uk @ y_k)
                y[mask_missing] = y_u
            except Exception as e:
                warnings.warn(f"Laplacian interpolation: L_uu singular en t={t}, se rellena con 0. Error: {e}")
                y[mask_missing] = 0  # fallback si L_uu singular
            signals_rec[t] = y
        return {"signals_reconstructed": signals_rec, "info": {"method": "laplacian"}}
    raise NotImplementedError("Implementar interpolación para: " + method)
