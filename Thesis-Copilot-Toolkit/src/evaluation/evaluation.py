"""Funciones de evaluacion para reconstruccion/interpolacion EEG."""

import os
from typing import Any, Dict

import numpy as np


def _downsample_1d(arr: np.ndarray, max_points: int) -> np.ndarray:
    if max_points <= 0 or arr.size <= max_points:
        return arr
    idx = np.linspace(0, arr.size - 1, num=max_points, dtype=int)
    return arr[idx]


def evaluate_signals(original: np.ndarray, reconstructed: np.ndarray, metrics: list = None) -> Dict[str, Any]:
    if metrics is None:
        metrics = ["mae", "rmse", "dtw", "snr"]

    results: Dict[str, Any] = {}
    for metric in metrics:
        key = metric.lower()
        if key == "mae":
            results["mae"] = mean_absolute_error(original, reconstructed)
        elif key == "rmse":
            results["rmse"] = root_mean_squared_error(original, reconstructed)
        elif key == "dtw":
            results["dtw"] = dtw_distance(original, reconstructed)
        elif key == "snr":
            results["snr"] = snr(original, reconstructed)
    return results


def evaluate_reconstruction(signals_true: np.ndarray, signals_reconstructed: np.ndarray, metrics: list = None) -> Dict[str, Any]:
    return evaluate_signals(signals_true, signals_reconstructed, metrics=metrics)


def mean_absolute_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    mask = ~np.isnan(y_true)
    return float(np.mean(np.abs(y_true[mask] - y_pred[mask])))


def root_mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    mask = ~np.isnan(y_true)
    return float(np.sqrt(np.mean((y_true[mask] - y_pred[mask]) ** 2)))


def dtw_distance(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    max_points = int(os.environ.get("B2_DTW_MAX_POINTS", "80"))

    try:
        from dtaidistance import dtw
    except ImportError as exc:
        raise ImportError("Instale dtaidistance para usar DTW") from exc

    # Soporta entrada 1D (vector) o 2D (matriz)
    if y_true.ndim == 1:
        mask = ~np.isnan(y_true)
        if np.sum(mask) < 2:
            return float("nan")
        a = _downsample_1d(y_true[mask], max_points=max_points)
        b = _downsample_1d(y_pred[mask], max_points=max_points)
        return float(dtw.distance(a, b))
    else:
        _, n_channels = y_true.shape
        dist = 0.0
        count = 0
        for d in range(n_channels):
            mask = ~np.isnan(y_true[:, d])
            if np.sum(mask) < 2:
                continue
            a = _downsample_1d(y_true[mask, d], max_points=max_points)
            b = _downsample_1d(y_pred[mask, d], max_points=max_points)
            dist += dtw.distance(a, b)
            count += 1
        return float(dist / count) if count > 0 else float("nan")


def snr(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    # Soporta entrada 1D (vector) o 2D (matriz)
    if y_true.ndim == 1:
        mask = ~np.isnan(y_true)
        signal = y_true[mask]
        noise = y_true[mask] - y_pred[mask]
        noise_var = np.var(noise)
        if noise_var == 0:
            return float("nan")
        return float(10.0 * np.log10(np.var(signal) / noise_var))
    else:
        _, n_channels = y_true.shape
        snr_vals = []
        for d in range(n_channels):
            mask = ~np.isnan(y_true[:, d])
            signal = y_true[mask, d]
            noise = y_true[mask, d] - y_pred[mask, d]
            noise_var = np.var(noise)
            if noise_var == 0:
                continue
            snr_vals.append(10.0 * np.log10(np.var(signal) / noise_var))
        return float(np.mean(snr_vals)) if snr_vals else float("nan")
