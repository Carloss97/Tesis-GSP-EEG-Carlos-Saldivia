<!-- markdownlint-disable-file -->

# Task Research Notes: Cierre de validacion publicable para experimento EEG-GSP

## Research Executed

### File Analysis

- Thesis-Copilot-Toolkit/README.md
  - Declara pendientes explicitos: reproducibilidad numerica completa, DTW extendido, tabla consolidada final.
- Thesis-Copilot-Toolkit/backlog.md
  - PRT-01 esta parcial y faltan escenarios realistas, bateria multi-nivel y protocolo congelado por dataset.
- Thesis-Copilot-Toolkit/VALIDATION_REPORT.md
  - Confirma tres brechas mayores: BGSRP 1:1 con MATLAB/GSPBox, DTW final extendido, cierre PRT-01.
- Thesis-Copilot-Toolkit/REFERENCES.md
  - Matriz de estado por metodo confirma INS-13 (bgsrp) y GRA-07 como validacion parcial.
- Thesis-Copilot-Toolkit/tests/test_paper_faithful.py
  - Cobertura centrada en sanidad numerica/alias funcional, sin validacion estadistica final multi-dataset para claims.
- Thesis-Copilot-Toolkit/tests/test_graph_methods_paper_faithful.py
  - Verifica propiedades de adyacencia para nnk/aew, pero no cierra equivalencia experimental paper-level.
- Thesis-Copilot-Toolkit/experiments/reproduce_puy_2018_frozen.py
  - Tiene seeds y resumen mean/std, evidencia buena para reproducibilidad interna de esa familia.
- Thesis-Copilot-Toolkit/experiments/replicate_bgsrp_exfig4_frozen.py
  - Replica Python aproximada con config congelada; no certifica equivalencia estricta 1:1 con MATLAB original.
- Thesis-Copilot-Toolkit/experiments/optimize_and_benchmark.py
  - No incluye DTW en la salida principal; usa MAE/RMSE/SNR.
- Thesis-Copilot-Toolkit/src/evaluation.py
  - DTW esta implementado, pero no se usa de forma sistematica en corrida final de benchmark.

### Code Search Results

- PRT-01|protocolo realista|missing_ratio|simulate_missing_channels_systematic
  - Coincidencias en backlog y VALIDATION_REPORT con subtareas pendientes PRT-01.D/E/F.
- dtw|DTW|evaluate_signals
  - Implementacion disponible en src/evaluation.py, pero ausente en optimize_and_benchmark.py (solo mae/rmse/snr).
- bgsrp|exfig4|MATLAB|GSPBox
  - Evidencia de replica frozen Python y nota explicita de pendiente 1:1 en README/VALIDATION_REPORT.
- paper_faithful|closure|validacion final
  - Se reporta avance fuerte en trss/sobolev y nnk, con cierre global todavia abierto.

### External Research

- #githubRepo:"mne-tools/mne-python interpolation tests bad channels reproducibility"
  - Patrones robustos observados: validacion por correlacion antes/despues, comprobacion de canales excluidos, manejo de condiciones invalidas, y pruebas multi-modalidad de interpolacion.
- #fetch:https://mne.tools/stable/auto_tutorials/preprocessing/15_handling_bad_channels.html
  - Recomendacion fuerte de marcar bad channels temprano, preservar trazabilidad de bads, y documentar estrategia de interpolacion para analisis comparables entre sujetos.
- #fetch:https://mne.tools/stable/auto_examples/preprocessing/interpolate_bad_channels.html
  - Ejemplifica reporte reproducible con metodo, configuracion, y visualizacion antes/despues en pipeline EEG/MEG.
- #fetch:https://neurips.cc/public/guides/PaperChecklist
  - Checklist exigente para resultados publicables: detalles experimentales completos, significancia/variabilidad (error bars/CI), recursos de computo, instrucciones de reproduccion exactas, y declaracion de limitaciones.

### Project Conventions

- Standards referenced: EARS en requirements, trazabilidad por tickets GRA/INS/TVT/PRT, artefactos frozen en results.
- Instructions followed: .github/instructions/spec-driven-workflow-v1.instructions.md, security-and-owasp.instructions.md, markdown-content-creation.instructions.md, markdown-gfm.instructions.md, taming-copilot.instructions.md.

## Key Discoveries

### Project Structure

El proyecto ya tiene estructura util para cierre publicable: scripts frozen por referencia, reporte de validacion consolidado, archivos de ranking y tests paper-faithful. Las brechas no son de implementacion base sino de cierre metodologico y evidencia estadistica final.

### Implementation Patterns

- Patrón fuerte: replicas frozen con config JSON + CSV raw + CSV summary.
- Patrón incompleto: benchmark principal no integra DTW aunque el modulo de evaluacion lo soporta.
- Patrón parcial: protocolo de faltantes cubre random+sistematico, pero no escenarios fisiologicamente realistas por regiones/electrodos y severidad.
- Patrón de riesgo para publicacion: algunas afirmaciones paper-faithful dependen de aproximacion Python sin equivalencia 1:1 con stack original MATLAB/GSPBox.

### Complete Examples

```python
def evaluate_signals(original: np.ndarray, reconstructed: np.ndarray, metrics: list = None) -> Dict[str, Any]:
    if metrics is None:
        metrics = ['mae', 'rmse', 'dtw', 'snr']
    results = {}
    for metric in metrics:
        if metric == 'mae':
            results['mae'] = mean_absolute_error(original, reconstructed)
        elif metric == 'rmse':
            results['rmse'] = root_mean_squared_error(original, reconstructed)
        elif metric == 'dtw':
            results['dtw'] = dtw_distance(original, reconstructed)
        elif metric == 'snr':
            results['snr'] = snr(original, reconstructed)
    return results
```

### API and Schema Documentation

- Artefacto frozen esperado por experimento:
  - `*_raw.csv`: corrida por seed/condicion.
  - `*_summary.csv`: agregados (media/desviacion).
  - `*_config.json`: parametros congelados.
- Requisito faltante para paper-ready:
  - metadatos de split, semilla global, version de dependencias, y comando exacto de reproduccion por figura/tabla.

### Configuration Examples

```json
{
  "reference": "Puy et al. 2018",
  "graph_method": "knng",
  "graph_params": {"k": 6, "sigma": 1.0},
  "bandwidth": 12,
  "missing_ratios": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
  "seeds": [1, 7, 13, 21, 42, 77, 101],
  "methods": ["puy", "gsp"]
}
```

### Technical Requirements

Para resultados validados y publicables aun falta:

1. Cerrar PRT-01 completo:
   - escenarios realistas por region/tipo de electrodo
   - bateria multi-nivel por dataset (10/20/30/40% o equivalente justificado)
   - protocolo congelado final por dataset/documento.
2. Integrar DTW completo en corrida final de candidatas y reportar media/desviacion o CI por escenario.
3. Cerrar equivalencia BGSRP:
   - comparacion controlada 1:1 contra referencia MATLAB/GSPBox (misma topologia, parametros y barrido N).
   - cuantificar gap residual y justificarlo si no es cero.
4. Completar validacion estadistica para claims:
   - multiples seeds y/o folds por dataset
   - barras de error/IC + test de significancia para comparaciones clave.
5. Cerrar tabla publicable final:
   - baseline vs GSP vs TV/tiempo con media +- desviacion
   - seccion de limitaciones alineada a lo pendiente no replicado 1:1.
6. Cerrar paquete de reproducibilidad:
   - comandos exactos, versionado de entorno, tiempo de computo y activos usados.

## Recommended Approach

Adoptar un **"Publication Closure Protocol v1"** con un unico objetivo: convertir el estado paper-faithful parcial en evidencia publicable trazable y auditada.

Secuencia optima (sin alternativas paralelas):
- Paso 1: Cierre PRT-01 (definicion y congelado de escenarios).
- Paso 2: Corrida extendida final con DTW+MAE+RMSE+SNR para shortlist de metodos.
- Paso 3: Auditoria BGSRP 1:1 MATLAB/GSPBox y reporte de divergencia.
- Paso 4: Consolidacion estadistica y tabla final de paper.
- Paso 5: Paquete de reproducibilidad y checklist de envio (detalle experimental, limitaciones, compute, licencias).

Razon de seleccion: es el camino minimo que cierra exactamente las tres brechas abiertas declaradas por el propio repositorio y agrega los requisitos de significancia/reproducibilidad que piden estandares de publicacion.

## Implementation Guidance

- **Objectives**: cerrar brechas de validacion declaradas, sostener claims con estadistica y lograr trazabilidad reproducible de figuras/tablas.
- **Key Tasks**: completar PRT-01, ejecutar benchmark final con DTW, certificar BGSRP contra MATLAB, consolidar tabla final y checklist de publicacion.
- **Dependencies**: `dtaidistance`, entorno MATLAB/GSPBox para comparativa 1:1, datasets y seeds congeladas, scripts frozen existentes.
- **Success Criteria**:
  - PRT-01 marcado completo en backlog/reportes.
  - Existe corrida final con DTW reportada en `results/` y resumida con variabilidad.
  - Existe informe BGSRP 1:1 con desviacion cuantificada y conclusion.
  - Tabla final baseline vs GSP vs TV/tiempo lista para manuscrito.
  - Checklist de reproducibilidad/publicacion contestable en modo "yes" o "no justificado" con evidencia.

## Operational Closure Board

### Estado Legend

- `Not started`: no ejecutado.
- `In progress`: en ejecucion parcial.
- `Blocked`: con dependencia externa no resuelta.
- `Done`: cerrado con evidencia.

### Publication-Ready Checklist Board

| ID | Work Item | Estado | Responsable | Evidencia esperada | Fecha objetivo | Riesgo |
|---|---|---|---|---|---|---|
| PRT-01.D | Escenarios realistas por region/tipo de electrodo | Not started | Tesis team | Documento de escenarios + config por dataset | 2026-04-07 | Alto |
| PRT-01.E | Bateria multi-nivel de perdida (10/20/30/40%) por dataset | Not started | Tesis team | CSV raw/summary por nivel y dataset | 2026-04-09 | Alto |
| PRT-01.F | Protocolo final congelado por dataset | Not started | Tesis team | `*_config.json` versionados + seccion metodologica | 2026-04-10 | Alto |
| MET-01 | Integrar DTW en corrida final de benchmark | In progress | Tesis team | Resultados con columnas DTW en salidas finales | 2026-04-11 | Alto |
| MET-02 | Corrida final extendida de candidatas (MAE/RMSE/DTW/SNR) | Not started | Tesis team | `results/*final*_raw.csv` y `results/*final*_summary.csv` | 2026-04-13 | Alto |
| INS-13.A | Comparacion BGSRP 1:1 Python vs MATLAB/GSPBox en escenario controlado | In progress | Tesis team | Reporte de equivalencia con mismo setup y barrido N | 2026-04-15 | Alto |
| INS-13.B | Cuantificar y justificar gap residual de BGSRP | In progress | Tesis team | Tabla de desviaciones + justificacion tecnica | 2026-04-16 | Alto |
| STAT-01 | Variabilidad: media+-std o IC por metodo/escenario | In progress | Tesis team | Tablas y figuras con barras de error trazables | 2026-04-17 | Medio |
| STAT-02 | Significancia estadistica de comparaciones clave | Not started | Tesis team | Test estadistico y seccion de interpretacion | 2026-04-18 | Medio |
| REP-01 | Tabla final baseline vs GSP vs TV/tiempo | Not started | Tesis team | Tabla final lista para paper y tesis | 2026-04-19 | Alto |
| REP-02 | Seccion de limitaciones alineada a evidencia | In progress | Tesis team | Texto de limitaciones sincronizado en paper/tesis | 2026-04-19 | Medio |
| DOC-01 | Sincronizacion README/backlog/REFERENCES/VALIDATION_REPORT | In progress | Tesis team | Consistencia de estado y tickets en 4 archivos | 2026-04-20 | Medio |
| RPL-01 | Comandos exactos y entorno reproducible por figura/tabla | In progress | Tesis team | Guia de reproduccion + versiones dependencias | 2026-04-21 | Alto |
| RPL-02 | Reporte de recursos computacionales (tiempo/memoria) | Not started | Tesis team | Seccion de compute para envio/publicacion | 2026-04-21 | Medio |
| REL-01 | Verificacion final de checklist de envio | Not started | Tesis team | Checklist respondible con evidencia adjunta | 2026-04-22 | Alto |

### Current Snapshot (2026-04-02)

- `In progress` justificado por evidencia existente:
  - MET-01: DTW implementado en `src/evaluation.py`, pero aun no integrado al benchmark final.
  - INS-13.A/INS-13.B: existe replica BGSRP exfig4-like y chequeo vs familia Narang, pendiente 1:1 MATLAB/GSPBox.
  - STAT-01: varias replicas frozen reportan media/desviacion (ej. Puy), pero no consolidado para toda la matriz final.
  - REP-02 y DOC-01: existe sincronizacion documental parcial reportada en backlog/reporte.
  - RPL-01: existen scripts frozen y configuraciones, faltan comandos finales unificados y pin de entorno completo.
- `Not started` mantenido cuando no hay evidencia verificable de ejecucion/cierre en los artefactos actuales.

### Weekly Review Cadence

| Fecha revision | Objetivo de control | Salida esperada |
|---|---|---|
| 2026-04-08 | Revisar cierre parcial PRT-01.D/E | Estado actualizado + riesgos activos |
| 2026-04-12 | Revisar corrida final con DTW | Evidencia MET-01/MET-02 validada |
| 2026-04-16 | Revisar cierre BGSRP 1:1 | Decision sobre INS-13 (cerrado o limitacion) |
| 2026-04-20 | Revisar tabla final y sincronizacion documental | REP-01, REP-02 y DOC-01 en estado Done |
| 2026-04-22 | Go/No-Go publicable | REL-01 completado con evidencia |

## Sprint Plan (Execution Breakdown)

### Sprint 1: Protocolo y metrica completa

- Ventana: 2026-04-03 a 2026-04-08
- Objetivo: cerrar definicion experimental base para corrida final.
- Alcance (IDs): PRT-01.D, PRT-01.E, PRT-01.F, MET-01.
- Entregables:
  - Protocolo realista por regiones/tipos de electrodo.
  - Bateria multi-nivel por dataset.
  - Configuraciones congeladas por dataset.
  - Integracion de DTW en benchmark final.
- Evidencia minima:
  - Configs versionadas en results.
  - Salidas de benchmark con columna DTW.
  - Actualizacion sincronizada en README/backlog/VALIDATION_REPORT.
- Criterio de cierre:
  - PRT-01.D/E/F en Done.
  - MET-01 en Done.

### Sprint 2: Corridas finales y equivalencia BGSRP

- Ventana: 2026-04-09 a 2026-04-16
- Objetivo: generar evidencia numerica final y cerrar brecha de equivalencia principal.
- Alcance (IDs): MET-02, INS-13.A, INS-13.B, STAT-01.
- Entregables:
  - Corrida final extendida MAE/RMSE/DTW/SNR en candidatas.
  - Reporte comparativo BGSRP Python vs MATLAB/GSPBox en setup controlado.
  - Tabla de gap residual con justificacion tecnica.
  - Resumen estadistico de variabilidad por metodo/escenario.
- Evidencia minima:
  - CSV raw/summary finales en results.
  - Informe de equivalencia BGSRP y conclusion documentada.
  - Figuras o tablas con variabilidad (media-desviacion o IC).
- Criterio de cierre:
  - MET-02, INS-13.A, INS-13.B, STAT-01 en Done.

### Sprint 3: Significancia, narrativa final y reproducibilidad de envio

- Ventana: 2026-04-17 a 2026-04-22
- Objetivo: dejar el paquete final listo para submission.
- Alcance (IDs): STAT-02, REP-01, REP-02, DOC-01, RPL-01, RPL-02, REL-01.
- Entregables:
  - Significancia estadistica de comparaciones clave.
  - Tabla final baseline vs GSP vs TV/tiempo.
  - Seccion de limitaciones alineada a evidencia real.
  - Documentacion sincronizada entre archivos canonicos.
  - Guia de reproduccion completa y reporte de recursos computacionales.
  - Checklist final de envio completado con trazabilidad.
- Evidencia minima:
  - Secciones finalizadas en paper y tesis.
  - Guia de comandos y entorno reproducible.
  - Checklist respondible con referencias cruzadas a artefactos.
- Criterio de cierre:
  - Todos los IDs restantes en Done.
  - Decision final Go para publicacion.

### Dependencias entre sprints

- Sprint 2 depende de cierre de Sprint 1 (sin protocolo congelado no hay corrida final valida).
- Sprint 3 depende de resultados finales de Sprint 2 (sin evidencia final no hay significancia ni tabla definitiva).

### Riesgos de calendario

- Riesgo alto: equivalencia BGSRP 1:1 puede requerir iteraciones extra por diferencias de stack.
- Mitigacion: reservar buffer de 1 a 2 dias entre Sprint 2 y Sprint 3 para ajustes de equivalencia.

## One-Month Master Plan (Daily Execution)

This section supersedes the short sprint windows and assumes 30 days of constant daily work, including experiment closure, paper, and thesis.

### Global Horizon

- Start: 2026-04-03
- End: 2026-05-02
- Mode: daily execution, 6 days active + 1 day light-review each week.

### Monthly Sprint Layout

| Sprint | Window | Main objective | Primary IDs |
|---|---|---|---|
| Sprint A | 2026-04-03 to 2026-04-10 | Close protocol and metric completeness | PRT-01.D, PRT-01.E, PRT-01.F, MET-01 |
| Sprint B | 2026-04-11 to 2026-04-18 | Final runs and BGSRP equivalence closure | MET-02, INS-13.A, INS-13.B, STAT-01 |
| Sprint C | 2026-04-19 to 2026-04-26 | Statistical claims and final result packaging | STAT-02, REP-01, REP-02, DOC-01 |
| Sprint D | 2026-04-27 to 2026-05-02 | Paper + thesis finalization and submission package | RPL-01, RPL-02, REL-01 + manuscript closure |

### Daily Work Template (recommended)

- Block 1 (Experiments): run or validate one core task with artifact output.
- Block 2 (Analysis): update summaries/tables/figures from that day output.
- Block 3 (Writing): update paper and thesis sections linked to the new evidence.
- End of day (15-20 min): sync status in README/backlog/REFERENCES/VALIDATION_REPORT and this board.

### 30-Day Operational Sequence

| Day range | Daily focus | Expected output |
|---|---|---|
| Days 1-3 | Define realistic missing-channel scenarios by region/type | Scenario document + draft dataset configs |
| Days 4-5 | Multi-level loss battery (10/20/30/40) across datasets | Initial raw/summary CSVs per dataset |
| Days 6-8 | Freeze final protocol and integrate DTW in final benchmark | Versioned configs + DTW-enabled benchmark output |
| Days 9-12 | Run full candidate benchmark with MAE/RMSE/DTW/SNR | Final run raw files in results |
| Days 13-16 | BGSRP 1:1 controlled comparison vs MATLAB/GSPBox | Equivalence report + residual gap table |
| Days 17-19 | Variability consolidation (mean/std or CI) | Statistical summary tables/plots |
| Days 20-22 | Significance testing for key claims | Significance section and decision notes |
| Days 23-24 | Final baseline vs GSP vs TV/time table | Final consolidated table for paper/thesis |
| Days 25-26 | Limitations and consistency synchronization | Updated README/backlog/REFERENCES/VALIDATION_REPORT |
| Days 27-28 | Reproducibility package (commands, env, compute report) | Repro guide + compute section |
| Days 29-30 | Final editorial pass paper + thesis and go/no-go review | Submission-ready package and final checklist |

### Writing Plan Embedded in the Month

| Week | Paper target | Thesis target |
|---|---|---|
| Week 1 | Methods and experimental protocol draft updated | Chapter methodology aligned with PRT-01 closure |
| Week 2 | Results section with final-run placeholders | Results chapter with per-method evidence blocks |
| Week 3 | Statistical claims + limitations fully drafted | Discussion and limitations chapter synchronized |
| Week 4 | Final manuscript polish, references, consistency pass | Final thesis coherence pass and bibliography check |

### Monthly Exit Criteria

- All board IDs in `Done`.
- Final experimental artifacts exist and are traceable.
- Paper has complete methods/results/discussion/limitations with evidence links.
- Thesis has synchronized methodology/results/discussion aligned to final artifacts.
- Final go/no-go review completed with explicit publication decision.