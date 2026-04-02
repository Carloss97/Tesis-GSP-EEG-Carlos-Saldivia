<!-- markdownlint-disable-file -->

# Task Research Notes: Handoff SWE para ejecutar B3/B4

## Research Executed

### File Analysis

- .copilot-tracking/research/20260402-swe-handoff-b2-research.md
  - Define el cierre de B2 y sus riesgos remanentes.
- .copilot-tracking/research/20260402-one-month-execution-table-research.md
  - Situa B3/B4 como bloque final de significancia, narrativa y reproducibilidad.
- .copilot-tracking/research/20260402-publication-validation-gaps-research.md
  - Contiene IDs y criterios de cierre para STAT-02, REP-01, REP-02, DOC-01, RPL-01, RPL-02 y REL-01.

### Code Search Results

- STAT-02|REP-01|REP-02|DOC-01|RPL-01|RPL-02|REL-01
  - IDs de cierre final de publicacion confirmados.
- hardening|warnings|narrative|paper|thesis
  - Riesgos remanentes alineados a la fase editorial final.

### External Research

- #fetch:https://neurips.cc/public/guides/PaperChecklist
  - Soporta el cierre de B3/B4 con exigencias de reproducibilidad, significancia, limitaciones y recursos.

### Project Conventions

- Standards referenced: trazabilidad por tickets, artefactos raw/summary/config, sincronizacion documental canonica.
- Instructions followed: nota mantenida dentro de .copilot-tracking/research para handoff operativo.

## Key Discoveries

### Project Structure

B3/B4 corresponde a la fase de cierre editorial y de submission, donde los resultados B2 deben integrarse en paper y thesis sin introducir nuevas ambiguedades tecnicas.

### Implementation Patterns

- Patrón científico: primero consolidar evidencia, luego traducirla a narrativa.
- Patrón operativo: no reabrir B1/B2 salvo bloqueo real; B3/B4 debe consumir artefactos ya congelados.
- Patrón de control: hardening continuo de warnings, pero sin expandir alcance experimental.

### Complete Examples

```text
B3/B4 = cerrar estadistica + tabla final + narrativa paper/thesis + reproducibilidad + checklist final
```

### API and Schema Documentation

- Entradas esperadas:
  - resultados consolidados de B2
  - ranking final y tablas de variabilidad
  - estado clasificado de warnings no fatales
- Salidas obligatorias:
  - tablas finales para paper y thesis
  - secciones narrativas alineadas con resultados
  - guia reproducible y checklist final de submission

### Configuration Examples

```text
B2 artifacts -> statistical closure -> manuscript narrative -> reproducibility package -> final checklist
```

### Technical Requirements

- No cerrar B3/B4 sin narrativa editorial final sincronizada con resultados B2.
- Mantener clasificacion formal de warnings no fatales.
- Preparar salida final apta para paper y thesis con trazabilidad completa.

## Recommended Approach

Delegar a SWE con un prompt operativo cerrado para cerrar B3/B4 usando resultados B2 ya consolidados.

## SWE Handoff Prompt (B3/B4, ready to paste)

Usa este texto con el agente SWE:

1. Objetivo
   - Ejecutar B3/B4 como fase final de cierre publicable, consumiendo los artefactos consolidados de B1+B2.

2. Riesgos remanentes a cubrir (reportados al final de B2)
   - Cierre estricto INS-13 contra stack MATLAB/GSPBox sigue pendiente (actualmente se cierra en proxy Python controlado).
   - Integración editorial final de resultados B2 en narrativa paper/tesis aún pendiente.
   - Warnings no fatales quedaron formalmente clasificados; conviene mantener hardening continuo en futuras corridas.

3. Alcance de implementación B3/B4
   - Cerrar STAT-02 con pruebas de significancia sobre resultados finales y documentar el criterio.
   - Generar REP-01 con la tabla final baseline vs GSP vs TV/tiempo usando artefactos B1+B2.
   - Redactar REP-02 con limitaciones alineadas a evidencia real, incluyendo el estado proxy de INS-13 si aplica.
   - Sincronizar DOC-01 entre README, backlog, REFERENCES y VALIDATION_REPORT.
   - Preparar RPL-01 y RPL-02: comandos exactos, entorno reproducible y recursos computacionales.
   - Cerrar REL-01 con checklist final de envio y decision Go/No-Go.

4. Archivos y zonas objetivo
   - Documentacion canonica del toolkit.
   - Artefactos de results que soportan la tabla final.
   - Secciones de paper y thesis donde se integran resultados, limitaciones y reproducibilidad.

5. Artefactos obligatorios de salida
   - Tabla final lista para paper/thesis.
   - Seccion de resultados/narrativa actualizada.
   - Seccion de limitaciones y reproducibilidad.
   - Checklist final de submission.
   - Registro de warnings clasificados y decision de hardening.

6. Criterios de aceptacion B3/B4
   - STAT-02, REP-01, REP-02, DOC-01, RPL-01, RPL-02 y REL-01 en Done con evidencia verificable.
   - Paper y thesis integran los resultados B2 sin contradicciones.
   - INS-13 queda explicitamente descrito como proxy/controlado si no hay equivalencia 1:1 completa.
   - Existe paquete reproducible de submission listo para revision.

7. Siguientes pasos naturales
   - Consolidar la narrativa final del paper con top-k por familia y escenario.
   - Sincronizar la tesis con la misma tabla final y las mismas limitaciones.
   - Emitir un commit atomico final cuando los artefactos B3/B4 esten listos.

8. Requisito de entrega del SWE
   - Resumen de cambios por archivo.
   - Comandos ejecutados para reproducir la version final.
   - Lista de artefactos generados y su ubicacion.
   - Riesgos residuales explicitados en el reporte final.

## Implementation Guidance

- **Objectives**: cerrar la fase de publicacion y documentacion final sin reabrir el nucleo tecnico.
- **Key Tasks**: significancia, tabla final, narrativa, reproducibilidad, checklist y sincronizacion documental.
- **Dependencies**: artefactos consolidados B1+B2, estado formal de warnings y resultados full-scale.
- **Success Criteria**: B3/B4 cerrados con paper/thesis consistentes, reproducibles y listos para revision.