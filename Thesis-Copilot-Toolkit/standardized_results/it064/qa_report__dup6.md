# QA Report: it64_bci_competition_single_subj

**Status**: ✓ GO
**Fecha**: 2026-04-05 16:07
**Descripción**: BCI Competition IV 2a proxy (22ch motor imagery), sujeto 1, kNN-k3

## Resultados Estadísticos

| Métrica | TV/Tiempo | Instant |
|---------|-----------|---------|
| MAE mediana | 5.211109e-07 | 7.473256e-07 |
| Mejora TV (%) | 30.3% | — |
| p-valor (Mann-Whitney) | 5.95e-11 | — |
| U-estadístico | 89 | — |

## Decisión

**✓ GO**
- TV median MAE < Instant median MAE: True
- p < 0.05: True
- Mejor método: `temporal_laplacian` (MAE=4.848798e-07)

## Configuración

- Datasets: ['bci_competition_iv_2a_proxy']
- Grafos: ['knn__k3']
- Missing ratios: [0.1, 0.2, 0.3, 0.4]
- Sujetos: [1]
- Métodos TV: 7
- Métodos Instant: 13
- Total filas: 80
