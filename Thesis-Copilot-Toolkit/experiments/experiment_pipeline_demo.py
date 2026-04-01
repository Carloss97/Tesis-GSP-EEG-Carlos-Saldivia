"""
experiment_pipeline_demo.py
Script de ejemplo: pipeline completo de reconstrucción EEG-GSP.
"""

from src.data.data_loader import load_synthetic_eeg, simulate_missing_channels
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from src.evaluation import evaluate_signals
from src.reporting import results_to_table, plot_metric_comparison, summary_report

# 1. Cargar datos sintéticos
sample = load_synthetic_eeg(n_channels=16, n_times=500)
signals = sample['signals']
positions = sample['positions']

# 2. Simular canales faltantes (aleatorio)
signals_missing = simulate_missing_channels(signals, missing_ratio=0.2)

# 3. Construir grafo (kNN)
graph = build_graph('knn', positions, k=4)
adjacency = graph['adjacency'].toarray() if hasattr(graph['adjacency'], 'toarray') else graph['adjacency']

# 4. Interpolación (lineal y GSP)
recon_linear = interpolate_signals('linear', signals_missing)
recon_gsp = interpolate_signals('gsp', signals_missing, adjacency=adjacency)

# 5. Evaluación
results = []
for method, rec in [('linear', recon_linear['reconstructed']), ('gsp', recon_gsp['reconstructed'])]:
    metrics = evaluate_signals(signals, rec)
    metrics['method'] = method
    metrics['dataset'] = 'synthetic'
    results.append(metrics)

df = results_to_table(results, filename=None)
print(df)

# 6. Visualización y resumen
plot_metric_comparison(df, metric='mae')
print(summary_report(df))
