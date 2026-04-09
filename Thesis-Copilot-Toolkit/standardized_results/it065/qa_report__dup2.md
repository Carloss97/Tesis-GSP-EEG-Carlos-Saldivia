# QA Report: it65_bci_competition_multisubj

**Status**: ✓ GO
**Fecha**: 2026-04-05 16:07
**Descripción**: BCI Competition IV 2a proxy, 9 sujetos, kNN-k3

## Resultados Estadísticos

| Métrica | TV/Tiempo | Instant |
|---------|-----------|---------|
| MAE mediana | 4.569340e-07 | 6.631168e-07 |
| Mejora TV (%) | 31.1% | — |
| p-valor (Mann-Whitney) | 4.49e-77 | — |
| U-estadístico | 9602 | — |

## Decisión

**✓ GO**
- TV median MAE < Instant median MAE: True
- p < 0.05: True
- Mejor método: `tv` (MAE=4.499216e-07)

## Configuración

- Datasets: ['bci_competition_iv_2a_proxy']
- Grafos: ['knn__k3']
- Missing ratios: [0.1, 0.2, 0.3, 0.4]
- Sujetos: [1, 2, 3, 4, 5, 6, 7, 8, 9]
- Métodos TV: 7
- Métodos Instant: 13
- Total filas: 720
