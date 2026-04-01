# Validation Report (Paper-Faithful)

Fecha: 2026-04-01  
Proyecto: Thesis-Copilot-Toolkit

## 1) Objetivo de esta iteracion

Actualizar el estado paper-faithful en base a avances recientes y dejar consistentes:
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

### 2.3 Test paper-faithful inicial

Archivo disponible:
- `tests/test_paper_faithful.py`

Cobertura actual del archivo de tests:
- ejecucion finita de `bgsrp`
- sensibilidad de `bgsrp` ante cambio de `gamma`
- preservacion de observados en `trss`
- equivalencia `trss` vs `sobolev_temporal`

## 3) Estado de confianza por metodo clave

Leyenda:
- `HIGH`: paper + formulacion + implementacion alineadas
- `MEDIUM`: alineado, pendiente reproduccion numerica completa
- `N/A`: baseline/derivado sin claim paper-faithful estricto

| Metodo | Estado | Comentario |
|---|---|---|
| `trss` / `sobolev_temporal` | HIGH | Alias consistente y evidencia de reproduccion de figura |
| `bgsrp` | MEDIUM | Alineado a RKHS, pendiente benchmark 1:1 con referencia MATLAB |
| `nnk` | HIGH | Implementacion NNLS local alineada al enfoque NNK |
| `spherical_spline` | HIGH | Implementacion basada en formulacion de Perrin |
| Baselines clasicos/geometricos | N/A | Utiles para comparacion, no paper-faithful estricto |

## 4) Archivos y artefactos relevantes verificados

- `results/paper_faithful_results.csv`
- `results/paper_faithful_rank_mae.csv`
- `results/bgsrp_vs_narang_check.csv`
- `results/bgsrp_vs_narang_check_summary.csv`
- `results/graphtrss_main_figure_raw.csv`
- `results/graphtrss_main_figure_summary.csv`
- `results/graphtrss_main_figure.png`
- `tests/test_paper_faithful.py`
- `experiments/verify_bgsrp_vs_narang.py`
- `experiments/reproduce_graphtrss_figure.py`

## 5) Riesgos y brechas actuales

1. BGSRP aun requiere cierre de reproducibilidad numerica equivalente a script MATLAB de referencia.
2. No todos los metodos activos tienen test dedicado paper-faithful.
3. Falta corrida final larga con DTW completo para cierre de reporte final.

## 6) Siguiente bloque de cierre recomendado

1. Ejecutar comparacion 1:1 BGSRP vs referencia MATLAB en escenario controlado.
2. Extender `tests/test_paper_faithful.py` para `nnk`, `spherical_spline` y `temporal_laplacian`.
3. Cerrar corrida final de robustez (DTW extendido) y congelar configuraciones por dataset.

## 7) Nota de consistencia documental

Este reporte se alinea con:
- `backlog.md`
- `README.md`
- `REFERENCES.md`

Cualquier cambio futuro en metodos o estado de validacion debe reflejarse en los 4 archivos anteriores en la misma iteracion.
