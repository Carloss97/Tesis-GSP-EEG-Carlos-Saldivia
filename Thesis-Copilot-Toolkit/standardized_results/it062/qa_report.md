# QA Report: it62_mne_sample_all_graphs

**Status**: ✓ GO
**Fecha**: 2026-04-05 16:07
**Descripción**: MNE Sample proxy, 3 grafos (kNN-k3, Gaussian, Kalofolias)

## Resultados Estadísticos

| Métrica | TV/Tiempo | Instant |
|---------|-----------|---------|
| MAE mediana | 1.672307e-07 | 2.539366e-07 |
| Mejora TV (%) | 34.1% | — |
| p-valor (Mann-Whitney) | 1.79e-25 | — |
| U-estadístico | 229 | — |

## Decisión

**✓ GO**
- TV median MAE < Instant median MAE: True
- p < 0.05: True
- Mejor método: `trss` (MAE=1.605002e-07)

## Configuración

- Datasets: ['mne_sample_proxy']
- Grafos: ['knn__k3', 'gaussian__sigma1', 'kalofolias']
- Missing ratios: [0.1, 0.2, 0.3]
- Sujetos: [0]
- Métodos TV: 7
- Métodos Instant: 13
- Total filas: 180
