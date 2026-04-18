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
