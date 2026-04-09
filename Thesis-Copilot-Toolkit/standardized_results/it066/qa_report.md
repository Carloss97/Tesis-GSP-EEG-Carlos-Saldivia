# QA Report: it66_bci_competition_gaussian

**Status**: ✓ GO
**Fecha**: 2026-04-05 16:07
**Descripción**: BCI Competition IV 2a proxy, 9 sujetos, grafo Gaussiano

## Resultados Estadísticos

| Métrica | TV/Tiempo | Instant |
|---------|-----------|---------|
| MAE mediana | 4.676258e-07 | 6.609199e-07 |
| Mejora TV (%) | 29.2% | — |
| p-valor (Mann-Whitney) | 6.10e-69 | — |
| U-estadístico | 12359 | — |

## Decisión

**✓ GO**
- TV median MAE < Instant median MAE: True
- p < 0.05: True
- Mejor método: `directed_tv` (MAE=4.505689e-07)

## Configuración

- Datasets: ['bci_competition_iv_2a_proxy']
- Grafos: ['gaussian__sigma1']
- Missing ratios: [0.1, 0.2, 0.3, 0.4]
- Sujetos: [1, 2, 3, 4, 5, 6, 7, 8, 9]
- Métodos TV: 7
- Métodos Instant: 13
- Total filas: 720
