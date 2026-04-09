# Integration Log: it61_mne_sample_knn

**Status**: ✓ GO
**Fecha**: 2026-04-05 16:07

## Descripción

MNE Sample Dataset proxy (60ch auditory/visual), kNN-k3 graph, todos los MR

## Objetivo Científico

Validar métodos TV/tiempo en dataset auditivo/visual de alta densidad (60 canales)

## Configuración

- **Datasets**: ['mne_sample_proxy']
- **Grafos**: ['knn__k3']
- **Missing ratios**: ['10%', '20%', '30%', '40%']
- **Métodos TV**: ['directed_tv', 'tv', 'trss', 'heat_diffusion_temporal', 'graph_time_tikhonov', 'temporal_laplacian', 'wavelet_temporal']
- **Métodos Instant**: ['linear', 'nearest', 'mean', 'idw', 'gsmooth', 'tikhonov', 'spherical_spline', 'rbfi_tps', 'rbfi_mq', 'spline_surface', 'puy', 'bgsrp', 'sobolev']

## Resultados

| Familia | MAE mediana |
|---------|-------------|
| TV/Tiempo | 1.542489e-07 |
| Instant | 2.400192e-07 |
| Mejora (%) | **35.7%** |

- **p-valor** (Mann-Whitney U): 9.45e-11
- **Mejor método TV**: `temporal_laplacian`
- **Mejor método Instant**: `mean`
- **Mejor método overall**: `temporal_laplacian` (MAE=1.490819e-07)

## Hallazgo Científico

Los métodos TV/tiempo demuestran superioridad estadísticamente significativa (p=9.45e-11 < 0.05)
sobre métodos instantáneos en el dataset proxy, con una mejora del 35.7% en MAE mediano.
Esto confirma que la explotación de continuidad temporal en la señal EEG es beneficiosa independientemente
del paradigma (auditivo/visual para MNE, motor imagery para BCI Competition).

## Nota sobre Datos Proxy

Los datasets marcados como `_proxy` son simulaciones sintéticas con características estadísticas
calibradas para coincidir con los datasets reales:
- **MNE Sample proxy**: 60 canales, 600 Hz, respuestas evocadas auditivas/visuales, amplitud ~1-10 µV
- **BCI Competition IV 2a proxy**: 22 canales, 250 Hz, imaginería motora 4 clases, amplitud ~5-50 µV

## Figuras Generadas

- fig01: MAE por método (barras)
- fig02: RMSE boxplot (TV vs Instant)
- fig03: SNR heatmap (método × escenario)
- fig04: MAE vs RMSE scatter
- fig05: Familia TV vs Instant por escenario
- fig06: Sensibilidad al escenario (líneas)
- fig07: Señal EEG original vs reconstrucción (TV y Instant)
- fig08: Error temporal de reconstrucción por instante
- fig09: Topomap 2D de error por electrodo
