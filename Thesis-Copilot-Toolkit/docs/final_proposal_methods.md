**Propuesta Final: Métodos Incluidos y Exclusiones**

- **Resumen rápido:** eliminamos de la familia TV/temporal `heat_diffusion_temporal` y `wavelet_temporal`; no se designa un método "primario" — en su lugar se utilizará un conjunto de candidatos experimentales. Ver también: [Resumen rápido y comandos](quick_run_summary.md).

- **Familia TV/temporal (candidatos):** `trss`, `sobolev_temporal`, `graph_time_tikhonov`, `temporal_laplacian`, `tv`.
  - Nota: `temporal_laplacian` se mantiene como candidato, pero no como método primario.

- **Interpoladores espaciales / baselines:** `linear`, `spherical_spline`, `rbfi_tps`.

- **Baseline de separación de fuentes:** `ica` (implementado en `src/interpolation_methods.py`).

- **Constructores de grafos (a usar en pilotos):** preferir `nnk` y `knn`. Catálogo válido: `knn`, `knng`, `vknng`, `gaussian`, `epsilon_ball`, `mst`, `nnk`, `aew`, `kalofolias`.

- **Exclusiones explícitas:**
  - `directed_tv` (no usar en esta fase).
  - `iv100hz_mat` / 100Hz dataset (excluido de las ejecuciones actuales).

- **Pilot mínimo (implementado):**
  - Archivo: `Thesis-Copilot-Toolkit/experiments/pilot_minimal.py`.
  - Datasets preferidos: `mne_sample`, `synthetic_16ch` (fallback), `iris_graph_signal`.
  - Métodos piloto: `linear`, `ica`, `spherical_spline`, `rbfi_tps`, `trss`.
  - Grafos: `nnk` (k=4) y `knn` (k=3).
  - Configuración rápida recomendada:
    - `NORMALIZE_DATASETS=1`
    - `NORM_METHOD=rms`
    - `seeds=[0,1,2]`
    - `missing_list=[0.2]` (20% missing)

- **Implementaciones realizadas:**
  - `interpolate_ica()` añadido y soportado por `interpolate_signals()` en `Thesis-Copilot-Toolkit/src/interpolation_methods.py`.
  - `Thesis-Copilot-Toolkit/experiments/pilot_minimal.py` creado para ejecuciones rápidas.

- **Cómo ejecutar el piloto mínimo (ejemplo Windows PowerShell):**
```
$env:NORMALIZE_DATASETS='1'
$env:NORM_METHOD='rms'
& .venv\Scripts\python.exe Thesis-Copilot-Toolkit/experiments/pilot_minimal.py --stop-on-error
```

- **Qué verificar tras la ejecución:**
  - Revisar `results_pilot_minimal/` para `pilot_minimal_*_qa_report.md` y `*_run_metadata.json`.
  - Asegurarse de que cada `*_run_metadata.json` contiene las claves `normalization` y `missing_mode` (se rellenaron por defecto si faltaban).

- **Siguientes pasos recomendados:**
  - Ejecutar el piloto mínimo y validar QA. Si los resultados son prometedores, ejecutar un piloto confirmatorio con `seeds=8` y `NORM_METHOD=rms`.
  - Ejecutar el script backfill semántico (pendiente) para normalización histórica.

Fecha: 2026-04-18

  ## TODOs (plan derivado)

  - **Implementar y versionar este documento**: Asegurar `docs/final_proposal_methods.md` en rama `experiment/final-proposal` y abrir PR. (status: completed)
  - **Alinear `iteration_plan_50.md`**: Revisar y confirmar que `docs/iteration_plan_50.md` refleja las iteraciones definitivas y las dependencias de datasets. (status: not-started)
  - **Generar `it01-it50` schedules**: crear y validar `experiments/schedules/it01-it50_schedule.json` conforme al plan maestro. (status: not-started)
  - **Preparar entorno y datasets**: `conda activate eegrasp`, verificar `datasets/` y proxies; añadir README de setup. (status: in-progress)
  - **Ejecutar supervisor confirmatorio**: lanzar `pilot_minimal.py` con perfil confirmatorio y recoger `*_run_metadata.json`. (status: not-started)
  - **Ejecutar confirmatorios seleccionados**: ejecutar iteraciones seleccionadas en `it01-it50` para completar `method_count > 1`. (status: not-started)
  - **Postprocesar y agregar QA**: ejecutar `inspect_all_stats.py`, generar QA reports y traza de mapeo. (status: not-started)
  - **Analizar resultados y validar**: pruebas estadísticas, correcciones por comparaciones múltiples y estimar tamaños del efecto. (status: not-started)
  - **Commit y push resultados**: versionar sidecar metadata y abrir PR con artefactos esenciales. (status: not-started)
  - **Planificar scheduling y presupuesto**: estimar tiempo de cómputo, paralelismo y costes. (status: not-started)
  - **Implementar backfill semántico**: script para crear `*_run_metadata_deprecation_map.json` para artefactos históricos. (status: not-started)
  - **Documentar decisiones y handoff**: compilar Decision Records y handoff README. (status: not-started)
  - **Preparar PR final**: PR que incluya `final_proposal_methods.md` y `iteration_plan_50.md` con resumen ejecutivo. (status: not-started)

  ---
  Estas TODOs reflejan la integración del `final_proposal_methods.md` con `iteration_plan_50.md` y el piloto previo (Phase A y B). Ejecuta la tarea que prefieras a continuación: generar schedules, preparar el entorno, o crear el PR con estos documentos.
