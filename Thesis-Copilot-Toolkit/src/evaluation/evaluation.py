"""
evaluation.py
Funciones para calcular métricas de evaluación de reconstrucción/interpolación.
"""

from typing import Dict, Any
import numpy as np

# Interfaz estándar para evaluación de reconstrucción
def evaluate_reconstruction(signals_true: np.ndarray, signals_reconstructed: np.ndarray, metrics: list = None) -> Dict[str, Any]:
    """
    Calcula métricas de error entre señales originales y reconstruidas.
    - signals_true: señales originales (vector o matriz)
    - signals_reconstructed: señales reconstruidas (mismo shape)
    - metrics: lista de métricas a calcular ("mae", "rmse", "dtw", "snr", ...)
    Retorna un diccionario con los resultados de cada métrica.
    """
    raise NotImplementedError("Implementar evaluación de métricas")
