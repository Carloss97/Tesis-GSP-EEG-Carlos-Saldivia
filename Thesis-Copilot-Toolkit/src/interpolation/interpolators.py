"""
interpolators.py
Funciones generales para interpolar/reconstruir señales EEG a partir de un grafo.
"""

from typing import Any, Dict
import numpy as np

# Interfaz estándar para interpolación/reconstrucción
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
    raise NotImplementedError("Implementar interpolación para: " + method)
