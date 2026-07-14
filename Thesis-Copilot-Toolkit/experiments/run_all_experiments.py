"""
run_all_experiments.py
Script para ejecutar todas las combinaciones de dataset, grafo e interpolador según el backlog.
"""
import os

from src.data.data_loader import load_synthetic_eeg, load_mne_sample_dataset, simulate_missing_channels
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from src.evaluation import evaluate_signals
from src.reporting import results_to_table, plot_metric_comparison, summary_report

# Definir datasets y funciones de carga
DATASETS = {
    'synthetic': lambda: load_synthetic_eeg(n_channels=16, n_times=500),
    'mne_sample': load_mne_sample_dataset
}

if os.environ.get('FAST_SYNTHETIC_ONLY', '0') == '1':
    DATASETS = {'synthetic': DATASETS['synthetic']}

# Métodos de grafo y sus parámetros
GRAPH_METHODS = [
    ('knn', {'k': 4}),
    ('knng', {'k': 4, 'sigma': 1.0}),
    ('vknng', {'k': 4, 'alpha': 1.0, 'k_min': 2, 'k_max': 8}),
    ('gaussian', {'sigma': 1.0}),
    ('aew', {'k': 4, 'sigma_dist': 1.0, 'sigma_corr': 0.5}),
    ('kalofolias', {}),
    ('nnk', {'k': 4}),
]

# Métodos de interpolación
INTERPOLATORS = [
    'linear',
    'gsp',
    'tikhonov',
    'bgsrp',
    'gsmooth',
    'graph_time_tikhonov',
    'puy',
    'sobolev',
    'spherical_spline',
    'rbfi_tps',
    'rbfi_mq',
    'spline_surface',
    'random',
    'idw',
]

results = []

GRAPH_BASED_INTERPOLATORS = {
    'gsp',
    'tikhonov',
    'bgsrp',
    'gsmooth',
    'graph_time_tikhonov',
    'puy',
    'sobolev',
}

POSITION_BASED_INTERPOLATORS = {
    'idw',
    'spherical_spline',
    'rbfi_tps',
    'rbfi_mq',
    'spline_surface',
}

for ds_name, ds_loader in DATASETS.items():
    sample = ds_loader()
    signals = sample['signals']
    positions = sample['positions']
    # Simular canales faltantes
    signals_missing = simulate_missing_channels(signals, missing_ratio=0.2)
    for g_method, g_params in GRAPH_METHODS:
        try:
            graph = build_graph(g_method, positions, signals=signals, **g_params)
            adjacency = graph['adjacency'].toarray() if hasattr(graph['adjacency'], 'toarray') else graph['adjacency']
        except Exception as exc:
            print(f"[WARN] Fallo en grafo {g_method} ({ds_name}): {exc}")
            continue
        for interp in INTERPOLATORS:
            try:
                if interp in GRAPH_BASED_INTERPOLATORS:
                    rec = interpolate_signals(interp, signals_missing, adjacency=adjacency)
                elif interp in POSITION_BASED_INTERPOLATORS:
                    rec = interpolate_signals(interp, signals_missing, positions=positions, power=2.0)
                else:
                    rec = interpolate_signals(interp, signals_missing)
                metrics = evaluate_signals(signals, rec['reconstructed'])
                metrics['method'] = interp
                metrics['graph'] = g_method
                metrics['dataset'] = ds_name
                results.append(metrics)
            except Exception as exc:
                print(f"[WARN] Fallo en interpolador {interp} con grafo {g_method} ({ds_name}): {exc}")
                continue

# Guardar y mostrar resultados
df = results_to_table(results, filename='results_all_experiments.csv')
print(df)
plot_metric_comparison(df, metric='mae')
print(summary_report(df))
