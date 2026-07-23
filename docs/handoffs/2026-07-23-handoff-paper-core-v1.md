# HISTÓRICO — Handoff de continuación — Paper BSPC / paper_core_v1

> **Iteración cerrada como antecedente.** Desde el 2026-07-23 se trabaja en un manuscrito nuevo para IEEE TBME, en doble columna, con la tesis como referencia primaria y sin nuevos experimentos. No reanudar las tareas de este handoff para el artículo activo. Véase `docs/plans/2026-07-23-plan-ieee-tbme-from-thesis.md`.

Fecha: 2026-07-23

## Instrucción de inicio

Carga obligatoriamente el skill `academic-writing`. Comunícate con el usuario en español; el manuscrito BSPC debe escribirse en inglés académico. No cargues ni resumas sesiones anteriores: este archivo contiene el estado necesario.

Repositorio:

`/mnt/c/Users/sarlo/OneDrive/Escritorio/Proyectos/Tesis-GSP-EEG-Carlos-Saldivia`

## Objetivo inmediato

Continuar desde el protocolo congelado hasta una primera versión compilable del draft BSPC:

1. probar el procesamiento común completo;
2. implementar el benchmark `paper_core_v1`;
3. ejecutar 760 casos pareados TRSS fijo–MNE;
4. generar resultados, checksums, tablas y figuras;
5. actualizar la matriz de evidencia;
6. crear y compilar `Thesis-Copilot-Toolkit/paper/bspc/main.tex` y sus secciones;
7. ejecutar QA científico/editorial/visual.

No redactar cifras no verificadas. No modificar la tesis aprobada ni el paper IEEE histórico.

## Skills ya aplicados

- `academic-writing`;
- `software-development/software-delivery-workflows`.

## Auditoría completada

Entregables validados:

- `docs/paper/claim_evidence_matrix.csv` (machine-readable, ignorado por `*.csv`);
- `docs/paper/claim_evidence_matrix.md` (representación versionable);
- `docs/paper/result_protocol_audit.md`;
- `docs/paper/editorial_fit_bspc.md`;
- `docs/paper/paper_core_v1_protocol.md`.

Hallazgos bloqueantes ya resueltos en el diseño nuevo:

- el benchmark antiguo de 300 pares no incluía BCI IV 2a;
- mezclaba dos controles sintéticos con dos sujetos PhysioNet y MNE Sample;
- 2700 filas crudas no equivalían a 3300 filas derivadas;
- las figuras cualitativas no usaban exactamente las señales del CSV;
- la evaluación temporal antigua era solo exploratoria.

## Protocolo `paper_core_v1`

Configuración:

`Thesis-Copilot-Toolkit/paper/bspc/evidence/paper_core_v1/config.json`

Diseño:

- PhysioNet EEGBCI: sujetos 1–9, run 4;
- BCI Competition IV 2a: sujetos 1–9, sesión T, 22 EEG;
- MNE Sample: un registro;
- 19 unidades de registro;
- máscaras random y nearby;
- severidades 10%, 20%, 30%, 40%;
- semillas 0–4;
- 760 casos pareados;
- 1520 aplicaciones de método;
- TRSS fijo: knng, k=4, sigma=1.0, alpha=0.8, beta=0.15, n_iter=120, lr=0.05;
- MNE: `interpolate_bads(method='spline', origin='auto')`;
- métricas exclusivamente sobre canales ocultos;
- bootstrap descriptivo jerárquico por dataset y registro.

Preprocesamiento congelado:

- EEG únicamente;
- coordenadas reales verificables;
- crop inicial de 20 s;
- referencia promedio;
- filtro 0.5–45 Hz;
- remuestreo a 160 Hz;
- ventana central 8–12 s (640 muestras).

## Datos verificados

Smoke test ejecutado con MNE 1.12.1:

- PhysioNet S001R04: 64 canales, 160 Hz, 64 posiciones;
- BCI A01T: 25 canales en el GDF, 22 EEG + 3 EOG por nombre, 250 Hz;
- MNE Sample: 60 EEG, 600.615 Hz, 60 posiciones.

Disponibilidad local:

- BCI IV 2a: A01–A09, sesiones T y E (18 GDF);
- PhysioNet: sujetos 1–9, runs 4/8/12, más S001R01;
- MNE Sample: `sample_audvis_raw.fif`.

## Entorno Python preparado

Ubicación:

`Thesis-Copilot-Toolkit/.venv-paper`

Creado con Python 3.11.15 mediante `uv` e instalado desde `requirements.txt`.

Versiones principales observadas:

- numpy 2.4.6;
- scipy 1.17.1;
- pandas 3.0.5;
- matplotlib 3.11.1;
- mne 1.12.1;
- scikit-learn 1.9.0;
- optuna 4.9.0.

Smoke script temporal:

`/tmp/paper_core_loader_smoke.py`

## Código existente relevante

- `Thesis-Copilot-Toolkit/src/interpolation_methods.py`;
  - `interpolate_signals` en torno a línea 187;
  - `interpolate_trss` en torno a línea 992;
  - TRSS conserva observaciones duras y usa el término temporal Sobolev.
- `Thesis-Copilot-Toolkit/src/graph_construction/graph_constructors.py`;
  - `build_graph('knng', positions, k, sigma)`.
- `Thesis-Copilot-Toolkit/src/evaluation/evaluation.py`;
  - `evaluate_signals`;
  - debe recibir exclusivamente `clean[:, bad_idx]` y `reconstruction[:, bad_idx]`.
- benchmark histórico de referencia estructural:
  - `Thesis-Copilot-Toolkit/experiments/trss_vs_mne_bads_extensive.py`.

## Próximo cambio a implementar

Crear un script nuevo, sin modificar el benchmark histórico:

`Thesis-Copilot-Toolkit/experiments/run_paper_core_v1.py`

Debe incluir:

1. loaders reales y deterministas;
2. exclusión explícita de los 3 EOG de BCI;
3. mapping de los primeros 22 canales BCI al montaje estándar;
4. preprocesamiento común;
5. generación compartida de máscaras;
6. ejecución MNE y TRSS;
7. métricas hidden-only y extras NRMSE/correlación/R²;
8. escritura incremental/reanudable;
9. análisis pareado jerárquico;
10. selección y NPZ de casos representativos;
11. tablas/figuras/manifiesto.

Crear pruebas focalizadas para:

- conteo esperado de casos;
- máscara determinista y compartida;
- exclusión EOG;
- métricas hidden-only;
- conservación de canales observados;
- ausencia de duplicados.

## Estado del plan

- [x] Definir `paper_core_v1`.
- [x] Crear entorno Python.
- [x] Verificar loaders básicos.
- [ ] Implementar benchmark.
- [ ] Ejecutar reanálisis.
- [ ] Crear paquete LaTeX BSPC.
- [ ] Redactar primera versión.
- [ ] Compilar y ejecutar QA.

## Configuración Hermes aplicada

La sesión antigua fallaba por enviar aproximadamente 370k tokens con configuración cargada de un solo intento. Se cambió la configuración persistente a:

- `agent.api_max_retries: 3`;
- `compression.threshold_tokens: 120000`;
- `auxiliary.compression.provider: auto`;
- fallback principal: Nous `tencent/hy3:free`;
- timeout Azure solicitado: 900 s;
- stale timeout Azure: 600 s.

El fallback Nous y una consulta mínima Azure fueron probados con éxito.

No reanudar la sesión saturada. Iniciar una sesión nueva desde el root y pedir que lea este handoff.
