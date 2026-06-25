# Plan Capítulo 4 Focus V3.3 — Pasada de forma, tablas y figuras

Fecha: 2026-06-24  
Backup: `backups/cap4_format_pass_20260624_193111/`

## Diagnóstico visual confirmado

Se revisó `tesis_caps_1_4.pdf` y las capturas enviadas por el usuario. Problemas principales:

1. **Títulos de sección partidos de forma antiestética**
   - 4.3: “Reducción de candidatos para la fase comparati- / va”.
   - 4.4: “Optimización intermedia y congelamiento de va- / riantes”.
   - 4.9: “Preservación espectral de las señales reconstrui- / das”.
   - Acción: acortar títulos visibles manteniendo explicación en el párrafo inicial.

2. **Tablas textuales con exceso de partición silábica**
   - Tabla 4.1: fases experimentales.
   - Tabla 4.4: reducción de candidatos.
   - Tabla 4.5: optimización intermedia.
   - Tabla 4.6: inventario de evidencia.
   - Tablas 4.11--4.13: complejidad/frontera práctica.
   - Acción: convertir tablas de tres columnas estrechas a dos columnas cuando sea posible; usar columnas `p{}` más anchas y `\raggedright` para evitar justificación agresiva.

3. **Figura 4.2 ocupa una página completa**
   - La figura es correcta como contenido, pero interrumpe el flujo.
   - Acción: reducir ancho de inclusión y permitir que comparta página con texto si LaTeX puede hacerlo.

4. **Justificación de resultados/cálculos**
   - La narrativa ya explica preliminar/intermedio/final, pero se reforzará que cada tabla responde a una función experimental.
   - Acción: mejorar frases de introducción y captions donde haga falta, sin añadir resultados no respaldados.

## Cambios a ejecutar

1. Renombrar títulos visibles:
   - 4.3 `Reducción de candidatos`.
   - 4.4 `Optimización intermedia`.
   - 4.5 `Inventario de la comparación final`.
   - 4.7 `Efecto del escenario de pérdida`.
   - 4.8 `Señales temporales representativas`.
   - 4.9 `Preservación espectral`.
   - 4.10 `Contribución temporal de TRSS`.
   - 4.11 `Costo computacional`.
   - 4.12 `Frontera práctica TRSS--MNE`.

2. Rediseñar tablas textuales:
   - `ch4_experimental_phase_overview.tex` a dos columnas.
   - `ch4_candidate_reduction_decisions.tex` a dos columnas.
   - `ch4_intermediate_optimization_summary.tex` a dos columnas.
   - `ch4_evidence_inventory.tex` a dos columnas.
   - `ch4_complexity_symbols.tex`, `ch4_runtime_complexity.tex`, `ch4_decision_boundary_trss_mne.tex` con columnas ragged y textos abreviados.

3. Reducir Figura 4.2:
   - `\includegraphics[width=0.78\textwidth]{ch4_scenario_summary_descriptive}` inicialmente.
   - Recompilar y decidir si el flujo mejora sin perder legibilidad.

4. Compilar `tesis_caps_1_4.tex`.

5. Validar:
   - 0 errores.
   - 0 citas indefinidas.
   - 0 referencias indefinidas.
   - 0 overfull hbox.
   - Todas las figuras/tablas de Cap. 4 referenciadas.

6. QA visual:
   - revisar páginas del Cap. 4;
   - revisar figura 4.2 aislada si el contact sheet acusa espacio;
   - confirmar que títulos ya no se parten de forma antiestética.
