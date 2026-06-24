# Plan de trabajo y mejora continua — tesis GSP-EEG V3

Fecha de preparación: 2026-06-23.

## 1. Alcance confirmado

1. Corregir primero los capítulos 1--3, resolviendo comentarios del profesor marcados con `%` y eliminando cada comentario una vez corregido.
2. No ejecutar todavía una reestructuración destructiva del capítulo 4 ni mover capítulos/archivos.
3. Empezar el replanteamiento del capítulo 4 como plan V3, con énfasis en una exposición sin tests de hipótesis como mecanismo principal de evaluación.
4. Mantener la versión principal `tesis_completa.tex` como documento objetivo.

## 2. Estado de entrada levantado

1. La versión principal es `tesis_completa.tex`, con estructura de 6 capítulos.
2. La ruta de trabajo es `hermes/tesis_magister_gsp_eeg_v2/`.
3. El historial relevante del directorio muestra:
   - `2026-06-23`: commit `8209f1b15`, `comentarios 19-06`, con cambios en capítulos 1--4.
   - `2026-06-08`: commits `d2dcb3659`, `089cd47fd`, `398e54558`, asociados a revisiones y comentarios del profesor.
   - `2026-06-04`: portada y revisión de tesis.
4. La sesión previa recuperada indica que el 08-06 se corrigieron capítulos 1--3, se separó construcción de grafos de interpolación, se regeneraron figuras de capítulo 3, y se alcanzó compilación sin errores en esa ronda.
5. La validación estructural actual de `tesis_completa.tex` pasó: 27 archivos TeX cargados, 24 citas usadas, 19 figuras usadas, 59 labels, sin figuras/citas/referencias faltantes.
6. `tesis_caps_1_5.tex` falla por includes obsoletos (`04_arquitectura_y_trazabilidad.tex`, `05_diseno_experimental.tex`); no es el objetivo principal, pero queda marcado como limpieza secundaria.

## 3. Correcciones aplicadas en capítulos 1--3

1. Capítulo 1:
   - Se eliminó la figura `ch1_thesis_roadmap` del texto porque el comentario cuestionaba su propósito.
   - Se eliminó la cronología completa del proyecto, marcada explícitamente como `Sacar`.
   - Se reemplazó la sección de hipótesis por preguntas de investigación y criterios comparativos.
   - Se eliminó la sección duplicada de tesis/contribución.
   - Se retiró la afirmación con referencias de deep learning que no correspondían directamente a interpolación EEG.
2. Capítulo 2:
   - Se movió la figura de conceptos GSP después de introducir Laplaciano/GFT.
   - Se aclaró que el panel espectral muestra autovalores, no energía de la señal.
   - Se definió mejor reconstrucción regularizada.
   - Se corrigió el tratamiento de grafos de correlación para reconocer el riesgo de circularidad.
   - Se incorporó el trabajo de Jäger et al. (2016), DOI `10.1016/j.clinph.2016.01.003`, a la discusión de RBF.
   - Se explicitó dónde entra `lambda` en splines esféricos y qué representan `p`, `G` y `epsilon` en MNE.
   - Se eliminó la afirmación fuerte de que MNE es bayesiano; quedó como estimador penalizado con preferencia de suavidad.
3. Capítulo 3:
   - Se aclaró que MNE Sample es un registro de un sujeto del cual se usan 60 canales EEG, no un único canal.
   - Se añadió la fuente de posiciones físicas de electrodos desde MNE/montajes estándar.
   - Se reemplazó la matriz de hipótesis por preguntas de investigación y evidencia esperada.
   - Se cambió el protocolo de “validación confirmatoria” a “validación comparativa”, sin Wilcoxon como eje narrativo.
   - Se eliminaron comentarios sobre espacios, cajas grises y figures una vez abordados.

## 4. Replanteamiento V3 del capítulo 4

### 4.1 Diagnóstico de los comentarios del profesor

Los comentarios del capítulo 4 apuntan a cuatro problemas centrales:

1. La narrativa depende demasiado de tests estadísticos y dificulta seguir los resultados.
2. Faltan señales interpoladas representativas con distintas estrategias.
3. Las figuras cualitativas actuales no convencen: un caso TRSS se ve malo y el PSD no muestra claramente original vs interpolado.
4. Hay elementos visuales que requieren explicación directa: etiquetas de tasa de victoria, celdas de mapas de calor, complejidad y significado de la descomposición temporal.

### 4.2 Criterio V3 sin tests de hipótesis como eje

El capítulo 4 debe reorganizarse para responder preguntas prácticas, no para aceptar/rechazar hipótesis:

1. **Pregunta A:** ¿Qué método reconstruye mejor bajo cada régimen de pérdida?
2. **Pregunta B:** ¿Cuándo TRSS aporta valor adicional frente a MNE?
3. **Pregunta C:** ¿Qué costo computacional se paga por esa mejora?
4. **Pregunta D:** ¿Las señales reconstruidas se ven fisiológicamente plausibles en tiempo y frecuencia?

Los tests de hipótesis no deben ser la columna vertebral. Si se mantienen, deben quedar como material auxiliar o apéndice. La narrativa principal debe usar:

1. diferencias pareadas por caso;
2. medianas y rangos intercuartílicos;
3. tasas de victoria como frecuencia empírica;
4. intervalos bootstrap como incertidumbre descriptiva;
5. ejemplos cualitativos seleccionados con criterio explícito, no cherry-picking.

### 4.3 Figuras nuevas o rediseñadas necesarias

1. **Figura de señales temporales representativas:** original, MNE, TRSS y al menos una referencia geométrica/GSP, en 3--4 escenarios: pérdida baja, pérdida severa cercana, pérdida periférica y control sintético suave/rugoso.
2. **Figura PSD corregida:** espectro de señal original vs señal interpolada, con suavizado Welch o promediado por banda, evitando curvas excesivamente rugosas.
3. **Figura de resumen por escenario:** mapa o tabla gráfica donde cada celda indique claramente `mejora mediana` y `tasa de victoria`, con leyenda explícita.
4. **Figura de costo vs precisión compacta:** evitar espacio vacío; usar escala log solo si realmente mejora la lectura.
5. **Tabla de casos cualitativos:** dataset, patrón, severidad, canales ocultos, razón de selección y conclusión visual.
6. **Tabla de complejidad:** definir `N`, `T`, `E`, `K` y `H` antes de mostrar expresiones asintóticas.

### 4.4 Experimentos o artefactos a generar antes de reescribir capítulo 4

1. Extraer de los CSV existentes pares representativos con criterios reproducibles:
   - mejor caso TRSS;
   - peor caso TRSS;
   - empate práctico;
   - caso favorable a MNE;
   - caso de pérdida severa agrupada.
2. Revisar si los archivos crudos permiten reconstruir y graficar señal original, MNE y TRSS para esos casos.
3. Regenerar PSD con método explícito: ventana, solapamiento, frecuencia de muestreo, escala y unidades.
4. Generar una tabla de trazabilidad para cada figura: CSV/NPZ fuente, script generador, parámetros y commit.
5. Hacer QA visual de cada figura antes de incorporarla.

## 5. Ciclo de mejora continua

1. **Preparar:** revisar comentarios `%`, crear backup, levantar fuente/cita/artefacto.
2. **Corregir:** aplicar cambios en lotes pequeños por capítulo.
3. **Eliminar comentario:** borrar cada comentario del `.tex` solo cuando la corrección esté aplicada.
4. **Regenerar artefactos:** figuras y tablas desde scripts, no manualmente.
5. **Validar:** ejecutar validador estructural, compilar LaTeX y revisar warnings de referencias/citas.
6. **QA visual:** revisar figuras/tablas renderizadas en PDF, especialmente tamaño de letra, espacios, leyendas y propósito.
7. **Registrar:** dejar plan, backups y logs en `build_logs/`.

## 6. Criterios de aceptación para esta ronda

1. Capítulos 1--3 sin comentarios del profesor marcados con `%`.
2. Figuras de capítulos 2--3 regeneradas o ajustadas según comentarios de legibilidad.
3. `tesis_completa.tex` compila sin errores LaTeX, sin citas indefinidas y sin referencias indefinidas.
4. Validador estructural pasa para `tesis_completa.tex`.
5. Capítulo 4 queda diagnosticado y con ruta V3 documentada, pero sin reestructuración destructiva todavía.
