"""
graph_constructors.py
Funciones generales para construir grafos a partir de posiciones y/o señales EEG.
"""

from typing import Any, Dict
import numpy as np

# Interfaz estándar para construcción de grafo
def build_graph(method: str, positions: np.ndarray, signals: np.ndarray = None, **kwargs) -> Dict[str, Any]:
    """
    Construye un grafo según el método especificado.
    - method: nombre del método ("knn", "gaussian", "vkNNG", etc.)
    - positions: shape (N_electrodos, 3)
    - signals: opcional, shape (N_instantes, N_electrodos)
    - kwargs: parámetros específicos del método
    Retorna un diccionario con:
      - 'adjacency': matriz de adyacencia (N_electrodos, N_electrodos)
      - 'info': metadatos del grafo
    """
    raise NotImplementedError("Implementar construcción para: " + method)
