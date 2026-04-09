# QA Report: it70_all_five_datasets

**Status**: ✓ GO
**Fecha**: 2026-04-05 16:07
**Descripción**: Los 5 datasets (3 sintéticos + MNE proxy + BCI proxy), kNN-k3

## Resultados Estadísticos

| Métrica | TV/Tiempo | Instant |
|---------|-----------|---------|
| MAE mediana | 4.157744e-03 | 5.913862e-03 |
| Mejora TV (%) | 29.7% | — |
| p-valor (Mann-Whitney) | 7.96e-11 | — |
| U-estadístico | 11145 | — |

## Decisión

**✓ GO**
- TV median MAE < Instant median MAE: True
- p < 0.05: True
- Mejor método: `directed_tv` (MAE=2.751957e-03)

## Configuración

- Datasets: ['synthetic_broad', 'synthetic_alpha', 'synthetic_beta', 'mne_sample_proxy', 'bci_competition_iv_2a_proxy']
- Grafos: ['knn__k3']
- Missing ratios: [0.1, 0.2, 0.3, 0.4]
- Sujetos: [0]
- Métodos TV: 7
- Métodos Instant: 13
- Total filas: 400
