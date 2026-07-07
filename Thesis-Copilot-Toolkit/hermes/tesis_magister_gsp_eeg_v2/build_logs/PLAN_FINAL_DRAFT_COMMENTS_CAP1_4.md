# Plan de cierre final — comentarios hasta Capítulo 4, Capítulos 5--6 y anexos

Fecha: 2026-07-07  
Backup: `backups/final_draft_comments_cap1_4_20260707_171307/`

## 1. Inventario de comentarios `%` sustantivos hasta Capítulo 4

Se detectaron ocho comentarios reales del profesor/usuario y separadores técnicos `%====` en Capítulo 3. Los separadores se eliminarán o normalizarán porque no aportan al documento final.

### Capítulo 1

1. Línea 26: `enfoques de aprendizaje profundo como cuales?`  
   **Acción:** nombrar ejemplos concretos de familias entrenables relevantes para imputación/reconstrucción temporal (autoencoders, redes convolucionales/TCN, modelos recurrentes/transformers, difusión) y justificar por qué quedan fuera del alcance.

2. Línea 61: `A que te refieres con referencias geometricas?`  
   **Acción:** reemplazar o definir “referencias geométricas” como métodos espaciales basados en distancia/splines/RBF/vecino más cercano y MNE-Python, evitando ambigüedad.

### Capítulo 2

3. Línea 20: `Borrar de figura 2.1 imagen (a) y (b)...`  
   **Acción:** regenerar Figura 2.1 sin los paneles de generación/propagación/dipolo. La figura debe centrarse en manifestaciones relevantes para interpolación: ERP y topografía de electrodos/canales fallados. Actualizar referencias en texto y caption.

4. Línea 75: `Error de formato con salto de linea...`  
   **Acción:** corregir el salto y separación antes de “Grafos data-driven”, para que el bloque de grafos no quede visualmente pegado ni con error de formato.

### Capítulo 3

5. Línea 79: `standard_1005, revisar esa referencia en cuanto al guion`  
   **Acción:** evitar código/localismo en prosa; escribir “montaje estándar 1005 de MNE-Python” y dejar el identificador técnico solo si es necesario en anexo o reproducibilidad.

### Capítulo 4

6. Línea 16: `columna método: indicar relación con los nombres... sección 3`  
   **Acción:** ajustar Tabla 4.1 para que el método visible sea legible y se relacione explícitamente con la nomenclatura de la Tabla 3.3. Añadir nota aclaratoria en caption/prosa.

7. Línea 35: `columna método e identificador son iguales...`  
   **Acción:** rediseñar Tabla 4.2 con columnas no redundantes: método/familia, rol experimental y mediana de latencia; eliminar columna duplicada “Identificador”.

8. Separadores `%====` en Capítulo 3.  
   **Acción:** eliminar separadores internos del fuente final si no son necesarios.

## 2. Correcciones transversales para el draft final

1. Mantener el marco sin pruebas de hipótesis como eje narrativo.
2. Buscar y eliminar de capítulos/tablas activas términos residuales: `cribado`, `Wilcoxon`, `q_{BH}`, `significancia`, `H1`, `H2`, `benchmark final`, `ablación`, rutas locales y nombres de archivo internos.
3. Mantener explícita la exclusión de Visibility NNK por error de implementación, sin usar sus resultados para ordenar métodos ni sostener conclusiones.
4. Asegurar que métodos como Tikhonov, ICA/FastICA/Picard, BGSRP, TV, GTT, RBF, IDW y splines aparezcan como parte de la fase exploratoria, aunque la comparación final sea TRSS--MNE.

## 3. Capítulos 5--6

Después de resolver comentarios hasta Capítulo 4:

1. Regenerar Capítulo 5 como discusión final, no solo comentario de resultados: trayectoria experimental, selección preliminar, reducción, fortaleza de MNE, lectura condicional de TRSS, tensión forma/espectro/costo, limitaciones, alcance y lecciones metodológicas.
2. Regenerar Capítulo 6 como cierre final: respuestas directas a P1/P2, aportes, deficiencias, trabajo futuro priorizado y cierre condicional TRSS--MNE.
3. Actualizar `tables/ch8_objective_evidence_matrix.tex` para que refleje la matriz final sin hipótesis H1/H2.

## 4. Anexos necesarios para draft completo final

1. Revisar apéndices A--E para consistencia con el marco final.
2. Sustituir anexos/tablas antiguas que usen `q_{BH}` o lenguaje de significancia por tablas descriptivas, inventarios, reproducibilidad y trazabilidad.
3. Mantener anexos útiles: derivaciones, protocolo reproducible, inventario de artefactos y tabla de trazabilidad de evidencia.
4. Evitar anexos históricos que contradigan la narrativa final si no están claramente rotulados como material histórico.

## 5. Verificación

1. Regenerar figuras/tablas modificadas desde scripts.
2. Compilar `tesis_caps_1_4.tex` y `tesis_completa.tex`.
3. Validar: 0 errores, 0 citas indefinidas, 0 referencias indefinidas, 0 overfull hbox.
4. Ejecutar QA visual en páginas de Capítulos 1--4 corregidos y cierre Capítulos 5--6/anexos.
5. Reportar archivos modificados, comentarios resueltos, compilación y problemas restantes si los hubiera.
