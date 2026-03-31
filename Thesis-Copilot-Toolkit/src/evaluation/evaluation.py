"""
evaluation.py
Funciones para calcular métricas de evaluación de reconstrucción/interpolación.
"""

from typing import Dict, Any
import numpy as np

# Interfaz estándar para evaluación de reconstrucción

import numpy as np

def evaluate_reconstruction(signals_true: np.ndarray, signals_reconstructed: np.ndarray, metrics: list = None) -> Dict[str, Any]:
    """
    Calcula métricas de error entre señales originales y reconstruidas.
    - signals_true: señales originales (vector o matriz)
    - signals_reconstructed: señales reconstruidas (mismo shape)
    - metrics: lista de métricas a calcular ("mae", "rmse", ...)
    Retorna un diccionario con los resultados de cada métrica.
    """
    results = {}
    if metrics is None or "mae" in metrics:
        # MAE solo en posiciones donde había NaN en la entrada
        mask = np.isnan(signals_true)
        mae = np.nanmean(np.abs(signals_true[mask] - signals_reconstructed[mask]))
        results["mae"] = mae
    # Otros métricas pueden agregarse aquí
    return results
