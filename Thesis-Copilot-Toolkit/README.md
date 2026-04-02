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

## Estructura documental de investigacion (abril 2026)

### Paper (objetivo: revista indexada, formato IEEE)

- `paper/README.md`: guia editorial para el manuscrito.
- `paper/ieee/main.tex`: archivo principal de compilacion.
- `paper/ieee/sections/`: secciones modulares (`abstract`, `introduction`, `methods`, `experiments`, `results`, `discussion`, `conclusion`).
- `paper/ieee/figures/` y `paper/ieee/tables/`: recursos visuales para envio.
- `paper/ieee/bibliography/references.bib`: base BibTeX del paper.

Idioma esperado para paper: ingles academico.

### Tesis de magister (objetivo: documento extendido institucional)

- `thesis/README.md`: guia de redaccion y compilacion.
- `thesis/usm/main.tex`: archivo principal de tesis.
- `thesis/usm/config/metadata.tex`: metadatos institucionales.
- `thesis/usm/frontmatter/`: portada, resumen en espanol, abstract en ingles y agradecimientos.
- `thesis/usm/chapters/`: capitulos 01-06 de la tesis.
- `thesis/usm/figures/` y `thesis/usm/tables/`: recursos visuales de tesis.
- `thesis/usm/bibliography/references.bib`: referencias bibtex de tesis.
- `thesis/usm/assets/logo_usm/`: carpeta para logo oficial USM.

Idioma esperado para tesis: espanol academico.

### Referencia externa para formato institucional

- Referencia disponible: `Referencias/Tesis_Borrador_Tomas_Bernal.zip`.
- Uso previsto: tomar estructura de capitulos, formato de portada y convenciones de estilo.
- Nota: el logo USM debe incorporarse en `thesis/usm/assets/logo_usm/` cuando se confirme el archivo oficial autorizado.

## Nuevos avances (abril 2026)

- `experiments/reproduce_narang_2013_frozen.py`
- `experiments/reproduce_puy_2018_frozen.py`
- `experiments/replicate_bgsrp_exfig4_frozen.py`
- Protocolo realista de canales faltantes iniciado (Ticket `PRT-01`) con estado ⚠ parcial.

## Estado de validacion paper-faithful
- [ ] PRT-01: protocolo realista final de canales faltantes (actual: ⚠ parcial, random+sistematico ya implementados)
Resumen rapido:
- `trss` / `sobolev_temporal`: ✓✓
- `nnk`: ✓✓
- `spherical_spline`: ✓✓
- `bgsrp`: ⚠ (alineado a RKHS, con replica exfig4-like en Python; pendiente equivalencia estricta 1:1 MATLAB/GSPBox)
- Baselines geometricos/classicos: ✓ o ⚠ segun metodo (ver backlog y REFERENCES)

Detalle completo en `VALIDATION_REPORT.md` y trazabilidad por metodo en `REFERENCES.md`.

### Tickets clave por familia

- Grafos: `nnk` (✓✓), `fully_connected_inverse_distance` (⚠), resto principales (✓)
- Instantaneo: `spherical_spline` (✓✓), `bgsrp` (⚠), resto principales (✓)
- TV/Tiempo: `trss` y `sobolev_temporal` (✓✓), resto principales (✓)

### Nomenclatura de tickets

- GRA-xx: metodos de construccion de grafos
- INS-xx: metodos de interpolacion por instante
- TVT-xx: metodos de interpolacion TV/tiempo
- PRT-xx: tareas de protocolo experimental (reporte tesis/paper)

Mapa canonico rapido:
- GRA-01..GRA-10
- INS-01..INS-15
- TVT-01..TVT-10
- PRT-01..PRT-99

Ejemplos de trazabilidad:
- GRA-08: `nnk`
- INS-06: `spherical_spline`
- INS-13: `bgsrp`
- TVT-02: `trss`
- TVT-03: `sobolev_temporal`
- PRT-01: protocolo realista de canales faltantes (estado actual: ⚠ parcial)

La lista completa de tickets por metodo esta en `backlog.md` y se replica en `REFERENCES.md` y `VALIDATION_REPORT.md`.

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
- `results/bgsrp_exfig4_like_raw.csv`
- `results/bgsrp_exfig4_like_summary.csv`
- `results/bgsrp_exfig4_like_config.json`
- `results/graphtrss_main_figure_raw.csv`
- `results/graphtrss_main_figure_summary.csv`
- `results/graphtrss_main_figure.png`
- `results/narang_2013_frozen_raw.csv`
- `results/narang_2013_frozen_summary.csv`
- `results/narang_2013_frozen_config.json`
- `results/puy_2018_frozen_raw.csv`
- `results/puy_2018_frozen_summary.csv`
- `results/puy_2018_frozen_config.json`
- `results/paper_faithful_closure_active_methods_2026-04-01.md`

## Checklist minimo

- [x] Referencias bibliograficas por metodo
- [x] Estado paper-faithful documentado
- [x] Tests paper-faithful ampliados (incluye TV/tiempo activos y `nnk`/`aew`)
- [ ] Reproducibilidad numerica completa para todos los metodos paper-faithful (pendiente cierre total)
- [ ] Corrida final extendida con DTW completo
- [ ] Tabla final consolidada baseline vs GSP vs TV/tiempo

Nota de alcance:
- La equivalencia estricta 1:1 con stack MATLAB/GSPBox del paper BGSRP sigue marcada como pendiente de cierre final, aunque ya existe replica exfig4-like congelada y reproducible en Python.
- Existen replicas frozen para Narang y Puy en entorno Python, pero el cierre total requiere completar la matriz de replicacion numerica de todos los metodos paper-faithful definidos en `REFERENCES.md` y validar equivalencia/criterios por metodo.
