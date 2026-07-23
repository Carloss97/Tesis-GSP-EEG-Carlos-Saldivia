# Informe de corrector independiente — defensa de tesis

Fecha de revisión: 2026-07-23  
Alcance: presentación completa, narrativa oral, banco de preguntas y respuestas, compilación, renderizado y trazabilidad.

## Dictamen ejecutivo

**Aprobada para ensayo final y defensa, con observaciones menores no bloqueantes.**

La defensa presenta una tesis clara y científicamente prudente: no intenta convertir una ventaja descriptiva condicionada de TRSS en superioridad universal. La separación entre exploración y evaluación final, la comparación pareada y el reconocimiento explícito de las ventajas de MNE en LSD y tiempo son fortalezas centrales.

No se detectaron defectos P0 ni P1 después de aplicar las correcciones. Los riesgos residuales son de exposición oral y densidad de algunas láminas técnicas, no de integridad documental.

## Puntuación independiente

| Dimensión | Nota | Juicio |
|---|---:|---|
| Estructura y narrativa científica | 9,3/10 | Problema → método → evidencia → decisión; cierre responde P1 y P2. |
| Material visual | 9,1/10 | Consistente, sobrio y sin superposición; algunas gráficas requieren guía oral. |
| Rigor metodológico y alcance | 9,5/10 | Diferencia claramente exploración, congelamiento, unidad observacional y agrupación. |
| Narrativa oral y control de tiempo | 9,2/10 | Guion trazable de 29:00, con rutas de 25:00 y 20:00. |
| Preguntas y respuestas | 9,4/10 | 38 preguntas, con respuesta breve y desarrollada; buena cobertura adversarial. |
| Reproducibilidad y QA | 9,6/10 | 16/16 gates, checksums, fuentes, conteos y renders auditados. |
| **Evaluación global** | **9,4/10** | **Material defendible y listo para ensayo final.** |

## Fortalezas observadas

1. **Tesis central comprensible.** La defensa responde cuándo aporta la temporalidad y cuándo MNE sigue siendo preferible.
2. **Comparador fuerte.** MNE-Python no se presenta como una línea base débil ni se confunde con el spline propio.
3. **Separación experimental honesta.** Los 18 métodos, 9 grafos y 120 escenarios pertenecen a exploración; las cifras centrales pertenecen al protocolo final congelado.
4. **Resultado no sobrevendido.** Se muestran conjuntamente MAE, intervalo descriptivo, tasa de victoria, LSD y costo.
5. **Heterogeneidad visible.** La presentación incluye tanto el máximo cercano a +41 % como la frontera práctica cercana a 0 %.
6. **Limitaciones bien formuladas.** Se distingue validez interna de generalización a daño real, nuevas poblaciones y tareas posteriores.
7. **Banco útil para defensa.** La respuesta breve permite contestar primero; la desarrollada permite ampliar sin improvisar.
8. **Material visual consistente.** Las figuras canónicas permanecen sin texto superpuesto; la interpretación se mantiene en columnas o cajas separadas.

## Hallazgos y mejoras ejecutadas

### P1 — corregidos

1. **Fuentes de diapositivas con caracteres UTF-8 corruptos.**
   - Causa: `\detokenize` aplicado a la línea completa de fuente bajo pdfLaTeX.
   - Corrección: las fuentes se procesan como texto UTF-8 normal y solo se escapan los guiones bajos de nombres de archivo.
   - Verificación: el texto extraído contiene cero marcadores `Ã`, `Â`, `�` o `âĂ`; la inspección visual confirma acentos y comillas correctos.

2. **Ambigüedad visual de la comparación pareada.**
   - Antes: la relación TRSS–MNE podía partirse en dos líneas y no distinguía observación de agrupación.
   - Corrección: se incorporó `TRSS → Δᵢ ← MNE`, la definición de Δ, `n=300` diferencias observacionales y `n=100` estratos de agrupación.
   - Verificación: página 15 aprobada sin recortes, solapamientos ni ambigüedad estadística.

### P2 — corregidos

3. **Dirección de mejora poco explícita en el portafolio.**
   - Se añadió que los valores positivos favorecen a TRSS y se reformularon las cajas como decisiones “Priorizar TRSS/MNE”.

4. **Mapa de heterogeneidad dependía demasiado de celdas pequeñas.**
   - Se añadieron, fuera de la figura, dos anclas legibles: máximo `+41 % / 80–87 %` y frontera `≈0 % / 47 %`.

5. **Tabla de limitaciones demasiado genérica.**
   - Se precisaron los límites de generalización, evaluación experta y despliegue; las columnas quedaron alineadas a la izquierda y sin warnings tipográficos.

6. **Cobertura adversarial incompleta del banco.**
   - Se agregaron preguntas sobre: diferencia entre 120 escenarios y 100 estratos; inclusión de calibración en los tiempos; y carácter no automático del mapa de decisión.
   - El banco aumentó de 35 a 38 preguntas, dentro del rango previsto.

7. **Etiqueta de novedad impropia para el grado.**
   - “Contribución doctoral o novedosa” se corrigió a “contribución novedosa”.

8. **Error sintáctico en el guion oral.**
   - Se corrigió “La segunda pregunta el compromiso” por “La segunda pregunta examina el compromiso”.

9. **Narrativa estadística menos precisa que la diapositiva.**
   - El guion ahora distingue oralmente la unidad observacional (`Δ`, n=300) de la unidad de agrupación (estrato, n=100).

## Riesgos residuales no bloqueantes

1. **Densidad de gráficas.** Las láminas del portafolio, heterogeneidad y respaldos numéricos no deben leerse celda por celda; el expositor debe señalar solo el contraste preparado.
2. **Margen temporal.** La ruta principal dura exactamente 29:00. Conviene ensayar con meta real de 28:15–28:30 para absorber pausas, cambios de diapositiva y una interrupción breve.
3. **Tipografía secundaria.** Las fuentes documentales y algunas tablas de respaldo son deliberadamente pequeñas. Son legibles en PDF, pero no deben constituir el contenido oral principal.
4. **Alcance científico.** Persisten —correctamente declaradas— la ausencia de daño real, validación externa, evaluación ciega y tareas posteriores. No son defectos de la defensa; son límites del estudio.
5. **Decisión no automatizada.** El mapa práctico es una síntesis del benchmark, no un clasificador validado.

## Resultado técnico final

- Presentación: 39 páginas = 25 principales + 14 respaldos.
- Narrativa: 16 páginas y 25 entradas de guion.
- Banco: 38 preguntas con respuestas breves y desarrolladas.
- Tiempo principal: 29:00; rutas alternativas: 25:00 y 20:00.
- Compilación: código 0 en ambos documentos y cero diagnósticos auditados.
- Auditor determinista: 16/16 gates aprobados.
- Render final: 39/39 páginas de presentación y 16/16 de narrativa, sin páginas sospechosas.
- Figuras: 12/12 checksums aprobados.
- Términos prohibidos: cero coincidencias en fuentes y PDF.
- Inspección visual final: cero P0 y cero P1.

## Recomendación al tesista

No añadir más contenido antes de la defensa. El trabajo pendiente debe concentrarse en ensayo oral: memorizar la apertura y el cierre, practicar la explicación de la unidad estadística, y responder primero en una frase antes de desarrollar. Las rutas de 25 y 20 minutos deben ensayarse al menos una vez como contingencia.
