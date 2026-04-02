<!-- markdownlint-disable-file -->

# Task Research Notes: Tabla mensual de ejecucion (bajo microcontrol)

## Research Executed

### File Analysis

- .copilot-tracking/research/20260402-publication-validation-gaps-research.md
  - Contiene el plan maestro a 30 dias y el desglose por sprints/objetivos.

### Code Search Results

- publication-ready checklist board
  - Se identificaron IDs y dependencias para agrupar trabajo por bloques semanales.
- one-month master plan
  - Se identificaron ventanas temporales base para una tabla separada y mas ligera.

### External Research

- #fetch:https://neurips.cc/public/guides/PaperChecklist
  - Se usa como marco de cierre para reproducibilidad, detalles experimentales y significancia.

### Project Conventions

- Standards referenced: planificacion por tickets (PRT/MET/INS/STAT/REP/DOC/RPL/REL), trazabilidad de artefactos en results.
- Instructions followed: spec-driven workflow y reglas de documentacion de investigacion en .copilot-tracking/research.

## Key Discoveries

### Project Structure

La mejor forma de evitar microcontrol diario y mantener foco es usar una tabla separada por bloques semanales con objetivos, entregables y criterio de aceptacion, sin asignar tareas dia por dia.

### Implementation Patterns

- Patron recomendado: plan operacional en un archivo dedicado.
- Granularidad recomendada: semanal (no diaria), con 3-5 entregables maximos por bloque.
- Regla de control: un unico checkpoint de avance al final de cada semana.

### Complete Examples

```markdown
| Bloque | Fechas | Foco | Entregables clave | Criterio de cierre |
|---|---|---|---|---|
| B1 | 2026-04-03 a 2026-04-09 | Protocolo y DTW | Protocolo congelado + benchmark con DTW | PRT y MET listos |
```

### API and Schema Documentation

- Artefactos de control por bloque:
  - evidencia tecnica en `results/`
  - estado en reportes canonicos
  - actualizacion de tablero (Done/In progress/Blocked)

### Configuration Examples

```text
Bloque semanal -> IDs asociados -> evidencias minimas -> decision de cierre
```

### Technical Requirements

- Mantener trazabilidad por IDs del tablero.
- No subdividir en tareas diarias salvo bloqueo.
- Confirmar cierre semanal con evidencia objetiva.

## Recommended Approach

Usar la siguiente tabla mensual separada como vista de ejecucion principal, manteniendo el archivo original como fuente detallada y este nuevo archivo como panel operativo ligero.

### Tabla mensual (bajo microcontrol)

| Bloque | Fechas | Foco | IDs | Entregables clave | Criterio de cierre |
|---|---|---|---|---|---|
| B1 | 2026-04-03 a 2026-04-09 | Cerrar protocolo y metrica completa | PRT-01.D, PRT-01.E, PRT-01.F, MET-01 | Escenarios realistas, bateria multi-nivel, protocolo congelado, benchmark con DTW | IDs B1 en Done y evidencia en results/reportes |
| B2 | 2026-04-10 a 2026-04-16 | Corridas finales y equivalencia BGSRP | MET-02, INS-13.A, INS-13.B, STAT-01 | Corrida final MAE/RMSE/DTW/SNR, comparativa BGSRP 1:1, tabla de gap residual, variabilidad consolidada | IDs B2 en Done y reporte de equivalencia publicado |
| B3 | 2026-04-17 a 2026-04-23 | Significancia y tabla final | STAT-02, REP-01, REP-02, DOC-01 | Tests de significancia, tabla final baseline vs GSP vs TV/tiempo, limitaciones alineadas, consistencia documental | IDs B3 en Done y documentos canonicos sincronizados |
| B4 | 2026-04-24 a 2026-05-02 | Paquete final paper + thesis + reproducibilidad | RPL-01, RPL-02, REL-01 | Guia de reproduccion, reporte de recursos, revision final de paper y thesis, checklist final | Go/No-Go publicable con evidencia completa |

### Cadencia recomendada (sin microcontrol)

- Lunes: definir objetivo semanal y riesgo principal.
- Miercoles: checkpoint unico de avance (sin replanificaciones menores).
- Viernes/Sabado: cierre semanal con evidencia y decision Done/In progress/Blocked.

## Implementation Guidance

- **Objectives**: ejecutar cierre completo en 1 mes sin sobrecarga de seguimiento diario.
- **Key Tasks**: trabajar por bloques semanales con salida verificable.
- **Dependencies**: entorno reproducible, MATLAB/GSPBox para comparativa BGSRP, scripts frozen y artefactos en results.
- **Success Criteria**: cada bloque semanal cerrado con evidencias y estado actualizado; paper y thesis listos al finalizar B4.