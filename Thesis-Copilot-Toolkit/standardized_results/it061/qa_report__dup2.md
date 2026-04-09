# QA Report: it61_mne_sample_knn

**Status**: ✓ GO
**Fecha**: 2026-04-05 16:07
**Descripción**: MNE Sample Dataset proxy (60ch auditory/visual), kNN-k3 graph, todos los MR

## Resultados Estadísticos

| Métrica | TV/Tiempo | Instant |
|---------|-----------|---------|
| MAE mediana | 1.542489e-07 | 2.400192e-07 |
| Mejora TV (%) | 35.7% | — |
| p-valor (Mann-Whitney) | 9.45e-11 | — |
| U-estadístico | 96 | — |

## Decisión

**✓ GO**
- TV median MAE < Instant median MAE: True
- p < 0.05: True
- Mejor método: `temporal_laplacian` (MAE=1.490819e-07)

## Configuración

- Datasets: ['mne_sample_proxy']
- Grafos: ['knn__k3']
- Missing ratios: [0.1, 0.2, 0.3, 0.4]
- Sujetos: [0]
- Métodos TV: 7
- Métodos Instant: 13
- Total filas: 80
