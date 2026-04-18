**Resumen rápido — Pilot mínimo**

Objetivo breve
- Ejecutar un piloto rápido para validar las decisiones de diseño actuales (exclusiones, candidatos TV, ICA como baseline) y recoger artefactos mínimos para QA.

Decisiones clave (estado actual)
- Se han eliminado de la familia TV: `heat_diffusion_temporal`, `wavelet_temporal`.
- No hay "método primario"; la familia TV incluye candidatos: `trss`, `sobolev_temporal`, `graph_time_tikhonov`, `temporal_laplacian`, `tv`.
- Exclusiones explícitas: `directed_tv`, dataset `iv100hz_mat` (100Hz).

Pilot mínimo — configuración (rápida)
- Archivo: `Thesis-Copilot-Toolkit/experiments/pilot_minimal.py`.
- Datasets preferidos: `mne_sample`, `synthetic_16ch`, `iris_graph_signal`.
- Métodos: `linear`, `ica`, `spherical_spline`, `rbfi_tps`, `trss`.
- Grafos: `nnk` (k=4), `knn` (k=3).
- Parámetros rápidos: `seeds=[0,1,2]`, `missing_list=[0.2]`, `NORMALIZE_DATASETS=1`, `NORM_METHOD=rms`.

Comandos de ejecución (PowerShell)
```
$env:NORMALIZE_DATASETS='1'
$env:NORM_METHOD='rms'
& .venv\Scripts\python.exe Thesis-Copilot-Toolkit/experiments/pilot_minimal.py --stop-on-error
```

Qué revisar en los artefactos
- Carpeta de salida: `results_pilot_minimal/`.
- Archivos clave: `pilot_minimal_*_qa_report.md`, `*_run_metadata.json`, `*_integration_log.md`.
- Verificar que cada `*_run_metadata.json` contiene las claves `normalization` y `missing_mode`.
- Revisar `*_qa_report.md` para la decisión de QA (GO / NO-GO) y el resumen estadístico básico.

Próximos pasos sugeridos
- Si QA muestra prometedor: ejecutar piloto confirmatorio con `seeds=8` y `NORM_METHOD=rms` y ampliar `graph_specs`.
- Si QA es NO-GO: revisar parámetros `trss`/`temporal_laplacian` y repetir piloto con ajustes.

Contacto rápido
- Para dudas o cambios en exclusiones, modificar `Thesis-Copilot-Toolkit/docs/final_proposal_methods.md` o los scripts en `Thesis-Copilot-Toolkit/experiments/`.

Fecha: 2026-04-18
