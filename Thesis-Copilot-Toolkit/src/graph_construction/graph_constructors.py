"""
graph_constructors.py
Funciones generales para construir grafos a partir de posiciones y/o señales EEG.
"""

from typing import Any, Dict
import numpy as np

# Interfaz estándar para construcción de grafo


from sklearn.neighbors import kneighbors_graph
from scipy.spatial.distance import cdist
import numpy as np

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
    if method == "knn":
      k = kwargs.get("k", 5)
      adjacency = kneighbors_graph(positions, n_neighbors=k, mode='connectivity', include_self=False)
      info = {"method": "knn", "k": k}
      return {"adjacency": adjacency, "info": info}
    elif method == "gaussian":
      sigma = kwargs.get("sigma", 1.0)
      dists = cdist(positions, positions)
      adjacency = np.exp(-dists**2 / (2 * sigma**2))
      np.fill_diagonal(adjacency, 0)
      info = {"method": "gaussian", "sigma": sigma}
      return {"adjacency": adjacency, "info": info}
    raise NotImplementedError("Implementar construcción para: " + method)
