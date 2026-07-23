# Plan de nueva iteración IEEE TBME desde la tesis

Fecha: 2026-07-23  
Estado: aprobado por instrucción del autor; en ejecución.  
Destino editorial de trabajo: **IEEE Transactions on Biomedical Engineering (TBME)**.  
Título de trabajo: **Missing EEG Channel Reconstruction Using Graph Signal Processing With Temporal Regularization**.

## 1. Propósito

Crear un manuscrito nuevo, sin reutilizar la estructura narrativa de los borradores `paper/ieee` ni `paper/bspc`, cuyo documento fuente principal sea la tesis final. El artículo se redactará en inglés, en formato IEEE de dos columnas, y se orientará como regular paper de TBME.

## 2. Decisiones editoriales

1. Se adopta TBME como interpretación operativa de “revista IEEE, biomedical signal processing”.
2. Se usa `IEEEtran` y se mantienen figuras y tablas embebidas en doble columna.
3. Se apunta a ocho páginas; doce es un máximo editorial con cargos por exceso.
4. El resumen será estructurado con Objective, Methods, Results, Conclusion y Significance, y tendrá menos de 250 palabras.
5. La conclusión no excederá 300 palabras.
6. El manuscrito no contendrá biografías.
7. El título se deriva fielmente del título de la tesis y reemplaza los títulos de los borradores anteriores.

## 3. Jerarquía de fuentes

1. Tesis final en `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/`.
2. Tablas y figuras finales incluidas en esa tesis.
3. Bibliografía de la tesis, verificando que cada cita respalde exactamente la afirmación asociada.
4. Código y artefactos existentes solo para comprobar trazabilidad; no se ejecutarán experimentos nuevos.

Los resultados de `paper_core_v1` y cualquier borrador BSPC quedan fuera de esta iteración salvo como material histórico de auditoría. No se combinarán denominadores, protocolos ni cifras entre iteraciones.

## 4. Evidencia que puede reutilizarse

- Diseño pareado descrito en la tesis.
- Comparación final de TRSS fijo frente a MNE-Python.
- Métricas calculadas únicamente en canales artificialmente ocultos.
- Resúmenes descriptivos, intervalos de incertidumbre y tasas de victoria ya incluidos en la tesis.
- Figuras y tablas finales de la tesis que superen revisión de legibilidad y consistencia.

No se ejecutarán nuevas corridas, optimizaciones, ablaciones ni análisis estadísticos. Adaptar idioma, tamaño, rótulos o disposición de una figura o tabla no crea evidencia nueva y debe preservar sus números.

## 5. Selección inicial de material visual

### Figuras candidatas

1. `ch3_methodology_flow.pdf`: diseño pareado y flujo experimental.
2. `ch2_trss_operator.pdf`: formulación espacio-temporal.
3. `ch6_robust_improvement_ci.pdf`: mejora e incertidumbre frente a MNE.
4. `ch6_scenario_heatmap_mae.pdf`: heterogeneidad por patrón y severidad.
5. `ch4_representative_timeseries.pdf`: ejemplo temporal verificable.
6. `ch6_runtime_mae_tradeoff.pdf`: compromiso precisión–costo.

### Tablas candidatas

1. Características de datasets, adaptada de la Tabla `tab:datasets`.
2. `ch6_robust_main.tex`, restringida a TRSS fijo frente a MNE.
3. `ch6_selected_scenarios_mae.tex`, si cabe sin sacrificar legibilidad.
4. `ch6_runtime_complexity.tex`.

La selección final se decidirá por aporte científico por página, legibilidad a tamaño de columna y consistencia con los claims permitidos.

## 6. Estructura del artículo

1. Introduction.
2. Related Work and Contribution.
3. Materials and Methods.
4. Experimental Design.
5. Results.
6. Discussion.
7. Limitations.
8. Conclusion.
9. References.

## 7. Secuencia de trabajo

1. Respaldar documentos Markdown y borradores que puedan verse afectados.
2. Marcar como históricos los documentos BSPC y `paper_core_v1`.
3. Crear protocolo y matriz claim–evidence activos para IEEE TBME.
4. Inventariar figuras, tablas y cifras de la tesis.
5. Crear `paper/ieee_tbme/` desde cero con `IEEEtran`.
6. Copiar solo los recursos visuales seleccionados y adaptar tablas a ancho IEEE.
7. Redactar desde la tesis, sin copiar pasajes extensos ni inventar evidencia.
8. Compilar y resolver errores, referencias, cajas desbordadas y floats.
9. Renderizar el PDF y revisar todas las páginas, figuras y tablas.
10. Auditar título, resumen estructurado, páginas, citas, claims y consistencia numérica.

## 8. Criterios de aceptación

- [ ] Formato IEEE real de dos columnas.
- [ ] Título correcto y consistente en todos los archivos.
- [ ] Ocho páginas objetivo; cualquier exceso queda documentado.
- [ ] Resumen estructurado menor de 250 palabras.
- [ ] Conclusión menor de 300 palabras.
- [ ] Sin experimentos nuevos ni mezcla con `paper_core_v1`.
- [ ] Cada cifra cuantitativa aparece en la tesis o en una tabla/figura final de la tesis.
- [ ] Las métricas se describen como evaluadas sobre canales ocultos.
- [ ] No se presenta Visibility/NNK como método activo.
- [ ] No se afirma superioridad clínica, universal ni fuera del benchmark.
- [ ] Figuras y tablas legibles en doble columna, sin texto superpuesto.
- [ ] Compilación limpia y revisión visual completa.

## 9. Respaldo

Los documentos de referencia previos se respaldaron en:

`docs/backups/20260723-104101-ieee-restart/`

El archivo `SHA256SUMS.txt` permite verificar los originales antes de esta iteración.
