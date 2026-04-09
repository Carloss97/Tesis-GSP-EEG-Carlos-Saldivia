# QA Report: it63_mne_sample_high_mr

**Status**: ✓ GO
**Fecha**: 2026-04-05 16:07
**Descripción**: MNE Sample proxy, escenario de alta tasa de pérdida (30-40%)

## Resultados Estadísticos

| Métrica | TV/Tiempo | Instant |
|---------|-----------|---------|
| MAE mediana | 2.122063e-07 | 3.038537e-07 |
| Mejora TV (%) | 30.2% | — |
| p-valor (Mann-Whitney) | 1.33e-07 | — |
| U-estadístico | 0 | — |

## Decisión

**✓ GO**
- TV median MAE < Instant median MAE: True
- p < 0.05: True
- Mejor método: `trss` (MAE=2.005584e-07)

## Configuración

- Datasets: ['mne_sample_proxy']
- Grafos: ['knn__k3']
- Missing ratios: [0.3, 0.4]
- Sujetos: [0]
- Métodos TV: 7
- Métodos Instant: 13
- Total filas: 40
