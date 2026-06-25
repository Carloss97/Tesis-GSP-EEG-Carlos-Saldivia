# Plan Capítulo 4 V3.4 — Reducir tablas textuales y mejorar lectura

Fecha: 2026-06-24  
Backup: `backups/cap4_reader_table_reduction_20260624_200509/`

## Lectura crítica como lector

El Capítulo 4 ya contiene la información correcta y está bien orientado como “Experimentos y Resultados”, pero todavía se siente cargado de tablas. El problema no es la cantidad de evidencia, sino la forma: varias tablas no contienen datos comparativos sino decisiones, roles o explicaciones narrativas. Como lector, esas tablas interrumpen la lectura y obligan a leer párrafos fragmentados en columnas estrechas.

### Observaciones principales

1. **Tablas que son básicamente prosa**
   - La tabla de fases experimentales cumple una función introductoria, pero como tabla fuerza frases en columnas y no mejora la comprensión.
   - La tabla de reducción de candidatos presenta decisiones metodológicas; se entiende mejor como lista argumentada.
   - La tabla de optimización intermedia explica roles de variantes; se lee mejor como párrafo con viñetas.
   - El inventario de evidencia mezcla datos, métodos, escenarios y métricas; puede integrarse en prosa sin perder trazabilidad.
   - La frontera práctica TRSS--MNE es más útil como regla de decisión narrada que como tabla.

2. **Tablas que sí deben mantenerse**
   - Ranking preliminar método--grafo: contiene resultados experimentales concretos.
   - Microbenchmark de latencia: contiene mediciones numéricas.
   - Resumen TRSS--MNE: contiene métricas cuantitativas.
   - Resumen por escenario: contiene resultados por estrato.
   - Casos representativos: documenta selección reproducible.
   - Contribución temporal: contiene resultados de comparación interna.
   - Complejidad/tiempo observado: combina fórmulas y medición útil.

3. **Problema de ritmo**
   El inicio del capítulo acumula muchas tablas seguidas antes de llegar a resultados finales. La solución no es eliminar información, sino convertir decisiones de diseño en prosa para que el lector entienda el razonamiento antes de ver datos numéricos.

4. **Justificación de resultados**
   Cada cálculo debe quedar justificado por su función: preliminar para diseñar, intermedio para congelar variantes, final para responder preguntas. El texto debe decir explícitamente qué hace cada bloque.

## Plan de corrección

1. Reemplazar tabla de fases experimentales por una lista narrativa de cinco fases.
2. Mantener la tabla de selección preliminar porque contiene ranking experimental.
3. Mantener microbenchmark de latencia, pero convertir la tabla de reducción de candidatos en prosa argumentada.
4. Convertir tabla de optimización intermedia en una explicación por roles: búsqueda por familia, configuración global, TRSS fijo, TRSS calibrado y oráculo.
5. Convertir inventario de evidencia en párrafos que explican datos, métodos, escenarios, métricas y casos cualitativos.
6. Mantener tablas cuantitativas de resultados finales.
7. Convertir la tabla de símbolos de complejidad en una frase explicativa y conservar solo la tabla con complejidad/tiempo observado.
8. Convertir frontera práctica en lista de reglas de uso en prosa.
9. Recompilar `tesis_caps_1_4.tex`.
10. Verificar refs, figuras, overfull y QA visual.

## Criterio de aceptación

- Menos tablas textuales.
- Capítulo más fluido para un lector.
- Mismo contenido conceptual preservado.
- Tablas restantes justificadas por datos, métricas o comparaciones.
- `tesis_caps_1_4.pdf` compila limpio.
