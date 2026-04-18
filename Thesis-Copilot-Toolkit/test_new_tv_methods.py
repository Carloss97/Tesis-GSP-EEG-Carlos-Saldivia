#!/usr/bin/env python
# Aviso de artefacto histórico: este script de pruebas menciona métodos/datasets que han sido excluidos de ejecuciones activas. Ver Thesis-Copilot-Toolkit/docs/HISTORICAL_ARTIFACTS_NOTICE.md
"""Test script for new TV-based interpolation methods."""

import os
import sys

# PYTHONPATH setup
repo_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, repo_root)

import numpy as np
from src.data.data_loader import load_synthetic_eeg
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from src.evaluation.evaluation import evaluate_signals

def test_new_tv_methods():
    """Test all new TV methods with synthetic EEG."""
    print("=" * 70)
    print("TESTING NEW TV METHODS (Bibliography-based)")
    print("=" * 70)
    
    # Load synthetic data
    print("\n[1] Loading synthetic EEG data...")
    data_dict = load_synthetic_eeg(n_channels=10, n_times=50, random_state=42)
    signals = data_dict['signals']
    positions = data_dict['positions']
    print(f"   Signals shape: {signals.shape}")
    print(f"   Positions shape: {positions.shape}")
    
    # Introduce missing channels
    print("\n[2] Introducing missing channels...")
    obs_mask = signals.copy()
    np.random.seed(42)
    missing_idx = np.random.choice(10, size=3, replace=False)
    missing_times = np.random.choice(50, size=20, replace=False)
    signals_masked = signals.copy()
    signals_masked[np.ix_(missing_times, missing_idx)] = np.nan
    print(f"   Missing channels: {missing_idx.tolist()}")
    print(f"   Missing times (20 out of 50): {missing_times.shape[0]}")
    
    # Build graph
    print("\n[3] Building graph...")
    graph_result = build_graph("aew", positions, signals=signals)
    adjacency = graph_result["adjacency"]
    print(f"   Graph method: aew")
    print(f"   Adjacency shape: {adjacency.shape}")
    
    # Test new TV methods
    new_tv_methods = [
        ("sobolev_temporal", {"alpha": 0.5, "beta": 0.2, "n_iter": 50}),
        ("temporal_laplacian", {"alpha": 0.7, "beta": 0.25}),
        ("heat_diffusion_temporal", {"alpha": 0.5, "beta": 0.3, "n_iter": 40}),
        ("spline_temporal", {"alpha": 0.6, "s_temporal": 0.1}),
        ("wavelet_temporal", {"alpha": 0.65, "wavelet_level": 2}),
        ("directed_tv", {"alpha": 0.5, "beta": 0.15, "n_iter": 30, "eps": 1e-5}),
        ("adaptive_temporal", {"alpha": 0.55, "beta": 0.2, "gamma": 0.05, "n_iter": 50}),
    ]
    
    print("\n[4] Testing new TV methods...")
    print("-" * 70)
    
    results = {}
    for method_name, params in new_tv_methods:
        try:
            print(f"\n   Testing {method_name}...")
            result = interpolate_signals(
                method_name,
                signals_masked,
                adjacency=adjacency,
                **params
            )
            reconstructed = result["reconstructed"]
            
            # Evaluate
            metrics = evaluate_signals(
                signals[missing_times][:, missing_idx],
                reconstructed[missing_times][:, missing_idx],
                metrics=["mae", "rmse"]
            )
            
            mae = metrics["mae"]
            rmse = metrics["rmse"]
            
            results[method_name] = {"mae": mae, "rmse": rmse, "params": params}
            print(f"      ✓ MAE: {mae:.6f}, RMSE: {rmse:.6f}")
            
        except Exception as e:
            print(f"      ✗ ERROR: {str(e)}")
            results[method_name] = {"error": str(e)}
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    valid_results = {k: v for k, v in results.items() if "error" not in v}
    error_results = {k: v for k, v in results.items() if "error" in v}
    
    print(f"\nSuccessful methods: {len(valid_results)}/{len(new_tv_methods)}")
    if valid_results:
        print("\nPerformance ranking (by MAE):")
        sorted_by_mae = sorted(valid_results.items(), key=lambda x: x[1]["mae"])
        for i, (method, metrics) in enumerate(sorted_by_mae, 1):
            print(f"  {i}. {method:25s} MAE={metrics['mae']:.6f}, RMSE={metrics['rmse']:.6f}")
    
    if error_results:
        print(f"\nFailed methods: {len(error_results)}")
        for method, err_info in error_results.items():
            print(f"  - {method}: {err_info['error']}")
    
    print("\n" + "=" * 70)
    print("TEST COMPLETED")
    print("=" * 70)

if __name__ == "__main__":
    test_new_tv_methods()
