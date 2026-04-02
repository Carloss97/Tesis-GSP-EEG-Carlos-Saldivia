# Validation Report (Paper-Faithful)

Fecha: 2026-04-02  
Proyecto: Thesis-Copilot-Toolkit

## 1) Objetivo de esta iteracion

Actualizar el estado paper-faithful en base a avances recientes, cerrar B1 (PRT-01.D/E/F + MET-01) y dejar consistentes:
- `backlog.md`
- `README.md`
- `REFERENCES.md`
- este reporte

## 2) Avances incorporados

### 2.1 BGSRP normalizado a fuente primaria

Se consolida `bgsrp` con referencia primaria:
- Zhang et al. (2024), enfoque RKHS para reconstruccion bandlimited en grafo.

Evidencia en repo:
- `results/bgsrp_vs_narang_check.csv`
- `results/bgsrp_vs_narang_check_summary.csv`

Interpretacion actual:
- BGSRP se trata como metodo distinto a Narang/Tikhonov.
- Alineacion conceptual: alta.
- Pendiente: comparacion numerica 1:1 contra experimento MATLAB equivalente.

### 2.2 TRSS / sobolev_temporal consolidados

`trss` y `sobolev_temporal` comparten nucleo de implementacion (alias funcional).

Evidencia en repo:
- `results/graphtrss_main_figure_raw.csv`
- `results/graphtrss_main_figure_summary.csv`
- `results/graphtrss_main_figure.png`
- `results/paper_faithful_closure_active_methods_2026-04-01.md`

### 2.3 Test paper-faithful inicial

Archivo disponible:
- `tests/test_paper_faithful.py`

Cobertura actual del archivo de tests:
- ejecucion finita de `bgsrp`
- sensibilidad de `bgsrp` ante cambio de `gamma`
- preservacion de observados en `trss`
- equivalencia `trss` vs `sobolev_temporal`

### 2.4 Replicaciones frozen agregadas (paper-specific)

- Narang 2013-like (config congelada):
	- `experiments/reproduce_narang_2013_frozen.py`
	- artefactos: `results/narang_2013_frozen_raw.csv`, `results/narang_2013_frozen_summary.csv`, `results/narang_2013_frozen_config.json`

- Puy 2018-like (config congelada):
	- `experiments/reproduce_puy_2018_frozen.py`
	- artefactos: `results/puy_2018_frozen_raw.csv`, `results/puy_2018_frozen_summary.csv`, `results/puy_2018_frozen_config.json`

- BGSRP exfig4-like (config congelada, aproximacion Python):
	- `experiments/replicate_bgsrp_exfig4_frozen.py`
	- artefactos: `results/bgsrp_exfig4_like_raw.csv`, `results/bgsrp_exfig4_like_summary.csv`, `results/bgsrp_exfig4_like_config.json`

### 2.5 Cobertura de tests ampliada

- `tests/test_paper_faithful.py` ampliado para metodos TV/tiempo activos y control de warnings en `spline_surface`.
- Nuevo archivo `tests/test_graph_methods_paper_faithful.py` para `nnk` y `aew`.
- Ejecucion consolidada: `python -m unittest tests.test_paper_faithful tests.test_graph_methods_paper_faithful` -> 11/11 OK.

### 2.6 Correccion spline_surface

- Se implemento estabilizacion numerica con suavizado adaptativo y fallback controlado.
- Verificacion post-fix: 0 warnings FITPACK (`nxest/nyest`), sin NaN y salidas finitas.

### 2.7 Protocolo realista de canales faltantes (PRT-01)

Estado actual: ✓ done.

Cubierto en cierre B1:
- enmascaramiento aleatorio reproducible (`simulate_missing_channels`, `missing_ratio`, `random_state`)
- enmascaramiento sistematico por indices (`simulate_missing_channels_systematic`, `missing_indices`)
- integracion en benchmark final (`optimize_and_benchmark.py`) con:
	- escenarios realistas por region/tipo de electrodo (`frontal_band`, `occipital_band`, `left_lateral_temporal`, `right_lateral_temporal`)
	- bateria multi-nivel de perdida por dataset (10/20/30/40)
	- protocolo congelado por dataset en config versionada

Evidencia de artefactos:
- `results/opt_benchmark_b1_protocol_raw.csv`
- `results/opt_benchmark_b1_protocol_summary.csv`
- `results/opt_benchmark_b1_protocol_config.json`

### 2.8 Cierre de metrica final DTW (MET-01)

Estado actual: ✓ done.

Se integra DTW en benchmark final junto con MAE, RMSE y SNR en salidas consolidadas.

Evidencia:
- columnas `mae`, `rmse`, `dtw`, `snr` en `results/opt_benchmark_b1_protocol_raw.csv`
- agregacion de metricas en `results/opt_benchmark_b1_protocol_summary.csv`
- configuracion reproducible en `results/opt_benchmark_b1_protocol_config.json`

Comando reproducible ejecutado para esta validacion:

```powershell
Push-Location Thesis-Copilot-Toolkit
$env:PYTHONPATH='.'
$env:INCLUDE_MNE='0'
$env:MAX_TIME_SAMPLES='60'
$env:B1_GRAPH_NAMES='knn'
$env:B1_METHOD_NAMES='linear,idw,tikhonov,trss'
$env:B1_MAX_SCENARIOS='4'
$env:B1_MISSING_LEVELS='0.10,0.20,0.30,0.40'
$env:B1_RANDOM_SEED='42'
& .\.venv\Scripts\python.exe -m experiments.optimize_and_benchmark
Pop-Location
```

## 3) Estado de confianza por metodo clave

Leyenda:
- ✓: Implementado y validado en corridas internas
- ✓✓: Implementado, validado y con evidencia paper-faithful fuerte
- ⚠: Implementado, pero con validacion paper-faithful parcial o pendiente

| Metodo | Estado Validacion | Comentario |
|---|---|---|
| TVT-02 / TVT-03 (`trss` / `sobolev_temporal`) | ✓✓ | Alias consistente y evidencia de reproduccion de figura |
| INS-13 (`bgsrp`) | ⚠ | Alineado a RKHS, pendiente benchmark 1:1 con referencia MATLAB |
| INS-10/11/12 (`gsp`/`tikhonov`/`gsmooth`) | ✓ | Replica frozen Narang-style disponible |
| INS-14 (`puy`) | ✓ | Replica frozen Puy-style disponible |
| GRA-08 (`nnk`) | ✓✓ | Implementacion NNLS local alineada al enfoque NNK |
| GRA-09 (`aew`) | ✓ | Test dedicado de propiedades y sensibilidad de estructura agregado |
| INS-06 (`spherical_spline`) | ✓✓ | Implementacion basada en formulacion de Perrin |
| Baselines clasicos/geometricos | ✓ o ⚠ | Utiles para comparacion, no paper-faithful estricto |

## 4) Archivos y artefactos relevantes verificados

- `results/paper_faithful_results.csv`
- `results/paper_faithful_rank_mae.csv`
- `results/bgsrp_vs_narang_check.csv`
- `results/bgsrp_vs_narang_check_summary.csv`
- `results/graphtrss_main_figure_raw.csv`
- `results/graphtrss_main_figure_summary.csv`
- `results/graphtrss_main_figure.png`
- `results/narang_2013_frozen_raw.csv`
- `results/narang_2013_frozen_summary.csv`
- `results/puy_2018_frozen_raw.csv`
- `results/puy_2018_frozen_summary.csv`
- `results/bgsrp_exfig4_like_raw.csv`
- `results/bgsrp_exfig4_like_summary.csv`
- `tests/test_paper_faithful.py`
- `tests/test_graph_methods_paper_faithful.py`
- `experiments/verify_bgsrp_vs_narang.py`
- `experiments/reproduce_graphtrss_figure.py`
- `experiments/reproduce_narang_2013_frozen.py`
- `experiments/reproduce_puy_2018_frozen.py`
- `experiments/replicate_bgsrp_exfig4_frozen.py`

## 5) Riesgos y brechas actuales

1. BGSRP aun requiere cierre mas cercano a 1:1 MATLAB/GSPBox (entorno y generador de grafo original).
2. La corrida B1 ejecutada usa configuracion reproducible acotada (INCLUDE_MNE=0 y subconjunto de metodos/grafos); falta corrida extendida full para tablas finales de publicacion.
3. Falta consolidar resultados finales baseline vs GSP vs TV/tiempo con matriz final para manuscrito.

## 6) Siguiente bloque de cierre recomendado

1. Ejecutar comparacion 1:1 BGSRP vs referencia MATLAB en escenario controlado (incluyendo barrido N completo de exfig4).
2. Ejecutar corrida full de robustez con todos los metodos/grafos objetivo para cierre B2 y tabla final de paper.

## 7) Nota de consistencia documental

Este reporte se alinea con:
- `backlog.md`
- `README.md`
- `REFERENCES.md`

Cualquier cambio futuro en metodos o estado de validacion debe reflejarse en los 4 archivos anteriores en la misma iteracion.

Nomenclatura canonica de tickets:
- GRA-01..GRA-10
- INS-01..INS-15
- TVT-01..TVT-10
