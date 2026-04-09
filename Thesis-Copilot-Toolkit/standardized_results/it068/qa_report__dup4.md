# QA Report: it68_three_real_datasets

**Status**: ✓ GO
**Fecha**: 2026-04-05 16:07
**Descripción**: Tres datasets reales/proxy (PhysioNet+MNE+BCI), kNN-k3

## Resultados Estadísticos

| Métrica | TV/Tiempo | Instant |
|---------|-----------|---------|
| MAE mediana | 4.387629e-07 | 6.632211e-07 |
| Mejora TV (%) | 33.8% | — |
| p-valor (Mann-Whitney) | 1.62e-04 | — |
| U-estadístico | 4707 | — |

## Decisión

**✓ GO**
- TV median MAE < Instant median MAE: True
- p < 0.05: True
- Mejor método: `directed_tv` (MAE=1.730541e-03)

## Configuración

- Datasets: ['synthetic_broad', 'mne_sample_proxy', 'bci_competition_iv_2a_proxy']
- Grafos: ['knn__k3']
- Missing ratios: [0.1, 0.2, 0.3, 0.4]
- Sujetos: [0]
- Métodos TV: 7
- Métodos Instant: 13
- Total filas: 240
