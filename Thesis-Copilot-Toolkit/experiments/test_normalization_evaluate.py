#!/usr/bin/env python3
"""Quick test for evaluate_signals normalization behavior."""
from __future__ import annotations

import numpy as np
from src.evaluation.evaluation import evaluate_signals


def main():
    # synthetic-like scale (~1)
    original = np.array([0.9, -0.7, 0.3, 0.0, np.nan])
    # reconstructed is scaled differently (e.g., physionet-like microvolts)
    reconstructed = original * 1e-6

    print("Raw metrics (no normalization):")
    print(evaluate_signals(original, reconstructed, metrics=["mae", "rmse", "snr"], normalize=False))

    print("Normalized metrics (rms):")
    print(evaluate_signals(original, reconstructed, metrics=["mae", "rmse", "snr"], normalize=True, norm_method="rms"))

    print("Normalized metrics (median):")
    print(evaluate_signals(original, reconstructed, metrics=["mae", "rmse", "snr"], normalize=True, norm_method="median"))


if __name__ == "__main__":
    main()
