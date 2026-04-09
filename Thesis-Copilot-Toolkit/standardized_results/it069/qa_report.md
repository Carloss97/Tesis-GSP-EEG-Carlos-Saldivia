# QA Report: it69_mne_bci_high_mr

**Status**: ✓ GO
**Fecha**: 2026-04-05 16:07
**Descripción**: MNE Sample + BCI Competition proxy, alta pérdida (30-40%)

## Resultados Estadísticos

| Métrica | TV/Tiempo | Instant |
|---------|-----------|---------|
| MAE mediana | 3.534849e-07 | 4.933928e-07 |
| Mejora TV (%) | 28.4% | — |
| p-valor (Mann-Whitney) | 1.23e-04 | — |
| U-estadístico | 364 | — |

## Decisión

**✓ GO**
- TV median MAE < Instant median MAE: True
- p < 0.05: True
- Mejor método: `tv` (MAE=3.535717e-07)

## Configuración

- Datasets: ['mne_sample_proxy', 'bci_competition_iv_2a_proxy']
- Grafos: ['knn__k3']
- Missing ratios: [0.3, 0.4]
- Sujetos: [0]
- Métodos TV: 7
- Métodos Instant: 13
- Total filas: 80
