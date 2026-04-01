# Tesis: Reconstruccion de EEG usando GSP e Interpolacion

## Hipotesis
El uso de tecnicas de interpolacion basadas en grafos (GSP) permite reconstruir senales de EEG de manera mas precisa que metodos clasicos.

## Objetivos
1. Implementar y comparar metodos de construccion de grafos para EEG.
2. Implementar y comparar metodos de interpolacion (GSP, baselines clasicos y metodos temporales).
3. Evaluar desempeno con MAE, RMSE, DTW y SNR.
4. Consolidar resultados para paper cientifico y tesis.

## Pipeline general
1. Carga de senal EEG y posiciones de electrodos
2. Construccion de grafo
3. Simulacion de canales faltantes
4. Reconstruccion/interpolacion
5. Evaluacion cuantitativa y ranking
6. Analisis y reporte

## Estructura
- `experiments/`: scripts de experimentacion
- `src/`: implementacion modular
- `results/`: salidas (csv, rankings, figuras)
- `paper/`: borrador de paper
- `thesis/`: borrador de tesis
- `backlog.md`: estado de tareas y metodos
- `REFERENCES.md`: referencias por metodo
- `VALIDATION_REPORT.md`: estado paper-faithful

## Nuevos avances (abril 2026)

- BGSRP actualizado a referencia primaria RKHS (Zhang et al., 2024).
- Figura principal tipo GraphTRSS reproducida y guardada en `results/graphtrss_main_figure.png`.
- Benchmark de chequeo BGSRP vs familia Narang generado en `results/bgsrp_vs_narang_check_summary.csv`.
- Tests paper-faithful agregados en `tests/test_paper_faithful.py`.

## Estado de validacion paper-faithful

Se usa una matriz de estado por metodo:
- `HIGH`: paper + formulacion + implementacion alineadas
- `MEDIUM`: alineado, pendiente de reproducibilidad numerica completa
- `N/A`: baseline sin claim paper-faithful

Resumen rapido:
- `trss` / `sobolev_temporal`: HIGH
- `bgsrp`: MEDIUM (alineado a RKHS, pendiente comparacion numerica 1:1 con MATLAB)
- Baselines geometricos/classicos: N/A

Detalle completo en `VALIDATION_REPORT.md` y trazabilidad por metodo en `REFERENCES.md`.

## Metodos activos

### Construccion de grafos
`knn`, `knng`, `vknng`, `gaussian`, `epsilon_ball`, `mst`, `fully_connected_inverse_distance`, `nnk`, `aew`, `kalofolias`

### Interpolacion por instante
`linear`, `nearest`, `mean`, `random`, `idw`, `spherical_spline`, `rbfi_tps`, `rbfi_mq`, `spline_surface`, `gsp`, `tikhonov`, `gsmooth`, `bgsrp`, `puy`, `sobolev`

### Interpolacion TV/tiempo
`graph_time_tikhonov`, `trss`, `sobolev_temporal`, `tv`, `temporal_laplacian`, `heat_diffusion_temporal`, `spline_temporal`, `wavelet_temporal`, `directed_tv`, `adaptive_temporal`

## Artefactos de validacion disponibles

- `results/paper_faithful_results.csv`
- `results/paper_faithful_rank_mae.csv`
- `results/bgsrp_vs_narang_check.csv`
- `results/bgsrp_vs_narang_check_summary.csv`
- `results/graphtrss_main_figure_raw.csv`
- `results/graphtrss_main_figure_summary.csv`
- `results/graphtrss_main_figure.png`

## Checklist minimo

- [x] Referencias bibliograficas por metodo
- [x] Estado paper-faithful documentado
- [x] Tests paper-faithful iniciales
- [ ] Reproducibilidad numerica completa para todos los metodos paper-faithful
- [ ] Corrida final extendida con DTW completo
- [ ] Tabla final consolidada baseline vs GSP vs TV/tiempo
