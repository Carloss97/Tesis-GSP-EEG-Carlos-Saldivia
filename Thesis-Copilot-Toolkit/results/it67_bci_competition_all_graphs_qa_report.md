# QA Report: it67_bci_competition_all_graphs

**Status**: ✓ GO
**Fecha**: 2026-04-05 16:07
**Descripción**: BCI Competition IV 2a proxy, sujeto 1, 3 grafos

## Resultados Estadísticos

| Métrica | TV/Tiempo | Instant |
|---------|-----------|---------|
| MAE mediana | 4.282252e-07 | 6.475890e-07 |
| Mejora TV (%) | 33.9% | — |
| p-valor (Mann-Whitney) | 2.32e-25 | — |
| U-estadístico | 1247 | — |

## Decisión

**✓ GO**
- TV median MAE < Instant median MAE: True
- p < 0.05: True
- Mejor método: `trss` (MAE=4.207202e-07)

## Configuración

- Datasets: ['bci_competition_iv_2a_proxy']
- Grafos: ['knn__k3', 'gaussian__sigma1', 'kalofolias']
- Missing ratios: [0.1, 0.2, 0.3, 0.4]
- Sujetos: [1]
- Métodos TV: 7
- Métodos Instant: 13
- Total filas: 240
