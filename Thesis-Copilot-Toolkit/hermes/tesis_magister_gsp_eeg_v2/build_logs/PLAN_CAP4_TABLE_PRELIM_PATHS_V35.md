# Plan Capítulo 4 V3.5 — Tabla 4.3, figura exploratoria, rutas y exclusiones

Fecha: 2026-06-24  
Backup: `backups/cap1_4_table_prelim_paths_20260624_222305/`

## Diagnóstico solicitado

1. **Tabla 4.3**: la columna “Medianas MNE → TRSS” comprimía dos valores científicos en una sola celda y mezclaba coma decimal en medianas con punto decimal en porcentajes. Se debía separar MNE y TRSS y normalizar presentación.
2. **Fase experimental preliminar**: el capítulo mostraba ranking por conjunto, pero faltaba una figura general de la campaña exploratoria. Se identificó `results/tablas_resumen/phase2_iteration_metrics_pivot.csv` como resumen consolidado de la campaña con 736 iteraciones válidas, además de archivos hasta `itX0800`.
3. **Rutas locales**: en Capítulo 3 se mencionaba explícitamente el archivo local de MNE Sample; debe eliminarse cualquier mención a rutas o nombres de archivo internos.
4. **Guiones largos**: varios capítulos usaban rayas largas para incisos que podían resolverse con comas, paréntesis o dos puntos.
5. **Visibility NNK**: se detectó un error de implementación. Sus resultados no deben usarse para ordenar métodos, justificar decisiones ni sostener conclusiones.
6. **Métodos implementados**: se debe mantener explícita la presencia de Tikhonov, ICA/FastICA/Picard y otros métodos no finales para que no parezca que solo se evaluaron TRSS/MNE.

## Cambios planificados

1. Reformatear `tables/ch4_descriptive_trss_mne.tex`:
   - separar `Med. MNE` y `Med. TRSS`;
   - usar coma decimal en porcentajes e intervalos;
   - mantener solo métricas de calidad, dejando el costo para la sección de costo computacional.
2. Generar `figures/ch4_preliminary_iteration_summary.pdf` desde `phase2_iteration_metrics_pivot.csv`:
   - graficar MAE mediano por método;
   - excluir Visibility NNK;
   - dejar manifiesto reproducible.
3. Insertar la figura en la sección 4.2 con explicación de la campaña exploratoria y de la exclusión de Visibility NNK.
4. Quitar Visibility NNK de la tabla de microbenchmark de reducción de candidatos.
5. Limpiar Capítulo 3:
   - reemplazar nombre de archivo MNE Sample por “registro público”;
   - reemplazar “screening” por “selección preliminar”;
   - añadir nota explícita de exclusión de Visibility NNK.
6. Reducir rayas largas innecesarias en capítulos 1--3.
7. Recompilar `tesis_caps_1_4.tex` y validar visualmente.

## Criterio de aceptación

- Tabla 4.3 legible y sin columna combinada MNE→TRSS.
- Figura preliminar nueva basada en artefactos reales.
- Sin rutas locales o nombres de archivo internos en capítulos 1--4.
- Visibility NNK explícitamente excluido.
- Tikhonov, ICA y otros métodos aparecen como parte de la fase exploratoria.
- PDF 1--4 compila con 0 errores, 0 referencias indefinidas, 0 citas indefinidas y 0 overfull.
