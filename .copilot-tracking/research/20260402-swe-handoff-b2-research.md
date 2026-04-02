<!-- markdownlint-disable-file -->

# Task Research Notes: Handoff SWE para ejecutar B2 (incorporando feedback)

## Research Executed

### File Analysis

- .copilot-tracking/research/20260402-swe-handoff-b1-research.md
  - Sirve de baseline de formato y criterios de handoff.
- .copilot-tracking/research/20260402-one-month-execution-table-research.md
  - Define B2 como bloque de corridas finales + equivalencia principal.
- .copilot-tracking/research/20260402-publication-validation-gaps-research.md
  - Contiene IDs, dependencias y criterios de cierre global.

### Code Search Results

- MET-02|INS-13.A|INS-13.B|STAT-01
  - IDs de B2 confirmados para ejecución full-scale y consolidación estadística.
- warnings|interpolacion|DTW|ranking final
  - Riesgos y pendientes reportados por SWE alinean con objetivos B2.

### External Research

- #fetch:https://neurips.cc/public/guides/PaperChecklist
  - Relevante para exigir reporte de variabilidad, detalle experimental y reproducibilidad al cerrar B2.

### Project Conventions

- Standards referenced: trazabilidad por IDs, artifacts en results (raw/summary/config), consistencia documental en archivos canónicos.
- Instructions followed: esta nota se mantiene dentro de .copilot-tracking/research para handoff operativo.

## Key Discoveries

### Project Structure

El feedback de SWE confirma que B1 habilita B2, pero B2 debe ampliar escala experimental, robustecer estabilidad y preparar directamente insumos de manuscrito.

### Implementation Patterns

- Patrón de riesgo técnico: warnings no fatales en interpolación pueden sesgar confianza en corridas masivas.
- Patrón de riesgo científico: sin corrida full-scale no se puede consolidar ranking publicable final.
- Patrón de riesgo editorial: sin tabla final top-k y narrativa actualizada, paper y thesis quedan desalineados con resultados nuevos.

### Complete Examples

```text
B2 reforzado = MET-02 + INS-13.A + INS-13.B + STAT-01 + hardening de warnings + tabla narrativa pre-final
```

### API and Schema Documentation

- Entradas esperadas:
  - matriz completa de datasets/grafos/metodos
  - configuraciones B1 congeladas
  - pipeline con DTW habilitado
- Salidas obligatorias:
  - resultados full-scale raw/summary/config
  - ranking consolidado de publicación
  - evidencia de warnings tratados (o documentados con criterio)

### Configuration Examples

```text
Full-scale matrix -> run artifacts -> ranking consolidation -> manuscript-ready tables
```

### Technical Requirements

- B2 no se considera completo si no hay corrida full-scale con trazabilidad.
- Warnings no fatales deben ser reducidos o clasificados formalmente por impacto.
- Debe existir puente directo entre artefactos B1+B2 y tabla narrativa de paper/thesis.

## Recommended Approach

Ejecutar B2 con foco en robustez y publicación, usando el siguiente prompt operativo para SWE.

## SWE Handoff Prompt (B2, ready to paste)

Usa este texto con el agente SWE:

1. Objetivo
   - Ejecutar B2 full-scale y preparar salida lista para consolidación de publicación, incorporando feedback posterior a B1.

2. Riesgos remanentes a cubrir (reportados por SWE)
   - Falta corrida extendida full-scale (más datasets/grafos/métodos) para consolidar ranking final de publicación.
   - Persisten warnings no fatales en algunos caminos de interpolación; no bloquean B1 pero conviene endurecerlos para B2.
   - Falta consolidación final de tablas y narrativa de manuscrito con los nuevos resultados DTW.

3. Alcance de implementación B2
   - Ejecutar MET-02 en matriz completa de datasets/grafos/métodos activos para ranking final.
   - Ejecutar INS-13.A e INS-13.B con comparativa controlada BGSRP (Python vs MATLAB/GSPBox) y cuantificación de gap residual.
   - Ejecutar STAT-01 consolidando variabilidad (media-desviación o CI) en resultados clave.
   - Endurecer warnings no fatales en interpolación: resolver causa o dejar clasificación explícita por severidad/impacto.
   - Preparar tabla pre-final de paper (top-k por familia y escenario) a partir de artefactos B1+B2.

4. Archivos y zonas objetivo
   - Scripts de benchmark/experimentos full-scale.
   - Módulos de interpolación con warnings no fatales.
   - Artefactos en results para ranking y resumen estadístico.
   - Documentación de estado en backlog/README/VALIDATION_REPORT.

5. Artefactos obligatorios de salida
   - Full-scale raw/summary/config en results.
   - Ranking consolidado final (publicación).
   - Reporte BGSRP equivalencia + tabla de gap residual.
   - Tabla pre-final top-k por familia y escenario (paper-ready input).
   - Registro de warnings remanentes con decisión (fixed/accepted/deferred).

6. Criterios de aceptación B2
   - MET-02, INS-13.A, INS-13.B, STAT-01 en Done con evidencia verificable.
   - Warnings críticos en interpolación mitigados o formalmente clasificados.
   - Existe insumo directo para narrativa final de paper/thesis basado en DTW y ranking consolidado.

7. Siguientes pasos naturales (alineados a SWE)
   - Ejecutar B2 full-scale ahora con matriz completa.
   - Preparar tabla final de paper (top-k por familia y escenario) usando los artefactos B1+B2.
   - Dejar listo un commit atómico solo con archivos B1 y evidencia.

8. Requisito de entrega del SWE
   - Resumen de cambios por archivo.
   - Comandos ejecutados para reproducir resultados.
   - Lista de artefactos generados.
   - Riesgos remanentes para B3/B4.

## Implementation Guidance

- **Objectives**: convertir salida B1 en evidencia full-scale consolidada para publicación.
- **Key Tasks**: corrida completa, robustez de warnings, equivalencia BGSRP y pre-tablas de manuscrito.
- **Dependencies**: configs B1, entorno reproducible, acceso a stack MATLAB/GSPBox para comparativa.
- **Success Criteria**: B2 cerrado con ranking final trazable, gap BGSRP cuantificado y entrada editorial lista para paper/thesis.