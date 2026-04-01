"""
experiment_mne_pipeline.py
Pipeline completo usando el dataset MNE Sample.
"""

from src.data.data_loader import load_mne_sample_dataset, simulate_missing_channels
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals
from src.evaluation import evaluate_signals
from src.reporting import results_to_table, plot_metric_comparison, summary_report

# 1. Cargar datos MNE
sample = load_mne_sample_dataset()
signals = sample['signals']
positions = sample['positions']

# 2. Simular canales faltantes (aleatorio)
signals_missing = simulate_missing_channels(signals, missing_ratio=0.2)

# 3. Construir grafo (kNN y gaussian)
graph_knn = build_graph('knn', positions, k=5)
graph_gauss = build_graph('gaussian', positions, sigma=1.0)
adj_knn = graph_knn['adjacency'].toarray() if hasattr(graph_knn['adjacency'], 'toarray') else graph_knn['adjacency']
adj_gauss = graph_gauss['adjacency']

# 4. Interpolación (lineal y GSP)
recon_linear = interpolate_signals('linear', signals_missing)
recon_gsp_knn = interpolate_signals('gsp', signals_missing, adjacency=adj_knn)
recon_gsp_gauss = interpolate_signals('gsp', signals_missing, adjacency=adj_gauss)

# 5. Evaluación
results = []
for method, rec in [
    ('linear', recon_linear['reconstructed']),
    ('gsp_knn', recon_gsp_knn['reconstructed']),
    ('gsp_gauss', recon_gsp_gauss['reconstructed'])
]:
    metrics = evaluate_signals(signals, rec)
    metrics['method'] = method
    metrics['dataset'] = 'mne_sample'
    results.append(metrics)

df = results_to_table(results, filename=None)
print(df)

# 6. Visualización y resumen
plot_metric_comparison(df, metric='mae')
print(summary_report(df))
