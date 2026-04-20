# Resumen de la conversación (pilotos A vs B)

Generado por GitHub Copilot (GPT-5 mini).

Fecha: (automático al crear el archivo)

---

1. Conversation Overview:
- Primary Objectives:
  - Canonicalizar experimentos para usar datos reales y finalizar cambios de código.
  - Estandarizar métodos baseline (`linear`, `ica`, `spherical_spline`, `rbfi_tps`).
  - Remover `mean` y `nearest` de listas activas (mantener implementaciones).
  - Centralizar deprecaciones/exclusiones en `deprecation_manifest.json`.
  - Forzar uso de datos reales; documentar y manejar `OverflowError` de MNE GDF.
  - Ejecutar pilotos (light, representative), recolectar artefactos y generar informe comparativo.
- Session Context: reproducibilidad usando datos reales; diagnóstico de parser MNE GDF; provisión de MNE sample; normalización de schedules; ejecución de pilotos; generación de artefactos QA.
- User Intent Evolution: canonicalización → diagnóstico MNE → provisión datos reales → normalizar schedule → mapear synthetic→real (opciones) → ejecutar fases A (variada) y B (control) → generar informe comparativo.

2. Technical Foundation:
- Tecnologías: Python, MNE para I/O EEG, scikit-learn, numpy, pandas, matplotlib, SciPy.
- Runner: schedules JSON → runner (`run_schedule_pilot.py`) → engine (`run_future_work_it121_it130.py`) que valida `load_data_availability()` y aplica gate "no available datasets".
- Entorno: Windows con entorno conda `eegrasp`; MNE sample provisionado en `datasets/`.

3. Codebase Status:
- `Thesis-Copilot-Toolkit/src/data/data_loader.py`: loaders modificados para preferir datos reales y exponer diagnósticos de `OverflowError`.
- `Thesis-Copilot-Toolkit/experiments/run_future_work_it121_it130.py`: engine con `load_data_availability`, `_run_iteration`, `_write_artifacts()`.
- `Thesis-Copilot-Toolkit/experiments/run_schedule_pilot.py`: ejecutor de schedules; escribe `pilot_skipped_iterations.json` en skips.
- `Thesis-Copilot-Toolkit/experiments/normalize_schedule_to_real.py`: nuevo script para mapear tokens `synthetic_*` → datasets reales (soporta mapping y `--inplace` con `.bak.json`).
- Schedules: `it01-it50_schedule.json` (backup `it01-it50_schedule.json.bak.json`) — se aplicaron 30 reemplazos en total.
- Artifacts: `Thesis-Copilot-Toolkit/results/` contiene CSVs, QA reports y `*_run_metadata.json` por iteración completada.

4. Problem Resolution:
- Problemas:
  - Muchos `skipped` por tokens `synthetic_*` no presentes en el mapa de disponibilidad.
  - `OverflowError` del parser MNE GDF (diagnosticado y documentado en loaders).
  - Warnings: FastICA ConvergenceWarning y advertencia de joblib/loky en Windows (no fatales).
- Soluciones implementadas:
  - `normalize_schedule_to_real.py` para mapear tokens sintéticos a datasets reales.
  - Restauración del backup y aplicación de mapping variado (A).
  - Ejecución de pilotos representativo (A) y control (`mne_sample`) (B).
  - Provisión del dataset MNE sample en `datasets/`.

5. Progress Tracking:
- Completado:
  - Provisión de MNE sample.
  - Cambios en loaders para diagnósticos GDF.
  - Script de normalización aplicado (30 reemplazos).
  - Piloto fase A (mapeo variado) para tags seleccionados — éxitos reportados.
  - Piloto fase B (control `mne_sample`) para tags seleccionados — éxitos reportados.
- Parcial / Pendiente:
  - Generar informe comparativo QA agregando metadata de fases A vs B (solicitado por usuario).
  - (Opcional) ejecutar schedule completo con mapping variado.
  - Consolidar listas de métodos y `deprecation_manifest.json` si se desea.

6. Active Work State:
- Foco actual: agregar metadata QA de iteraciones completadas y producir un informe comparativo (A vs B).
- Últimas acciones: crear `normalize_schedule_to_real.py`, restaurar backup, aplicar mapping variado, ejecutar sets de pilotos A y B, comenzar recolección de metadatos.
- Artefactos relevantes: schedule normalizado en `Thesis-Copilot-Toolkit/experiments/schedules/it01-it50_schedule.json`, reports y `*_run_metadata.json` en `Thesis-Copilot-Toolkit/results/`.

7. Recent Operations (resumen rápido):
- Lectura y análisis de schedules para detectar tokens `synthetic_*`.
- Creación de `normalize_schedule_to_real.py` y ejecución con mapping por token.
- Pilotos fase A: tags `it01 it02 it03 it05 it06 it09 it10` — reportaron éxito.
- Pilotos fase B: tags `it01 it04 it07 it11 it14 it17` — reportaron éxito.
- Light-profile pilot: intentó `it17` (skipped) y `it48` (success).

8. Continuation Plan (próximos pasos concretos):
- Generar informe comparativo QA (solicitado ahora):
  1. Recolectar `*_run_metadata.json`, `{tag}_stats.csv` y `{tag}_qa_report.md` para las iteraciones ejecutadas en A y B.
  2. Agregar métricas clave (MAE mediana por método/dataset), realizar comparaciones estadísticas (Mann–Whitney U) entre A y B.
  3. Escribir `Thesis-Copilot-Toolkit/results/pilot_comparative_report_A_vs_B.md` con resumen ejecutivo, tablas y decisiones.
- Prioridad: completar el informe comparativo ahora, luego correr schedule completo si el usuario lo autoriza.

---

Acciones disponibles ahora:
- Generar y escribir `pilot_comparative_report_A_vs_B.md` (agregar archivos relevantes desde `results/`).
- Ejecutar el schedule completo con el mapping variado (si autorizas).

Indica qué prefieres y procedo.
