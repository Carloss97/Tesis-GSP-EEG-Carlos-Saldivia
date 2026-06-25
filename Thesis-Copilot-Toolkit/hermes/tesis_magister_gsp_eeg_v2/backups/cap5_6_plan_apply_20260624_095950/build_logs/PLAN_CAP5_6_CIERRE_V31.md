# Plan V3.1 — Revisión de capítulos 5 y 6: discusión, conclusiones y trabajo futuro

Fecha: 2026-06-24  
Estado: plan propuesto; no aplicado todavía a `chapters/05_discusion.tex` ni `chapters/06_conclusiones.tex`.

## 1. Punto de partida verificado

La revisión V3.1 del Capítulo 4 ya deja el capítulo como **Experimentos y Resultados**. La estructura actual cubre:

1. mapa de fases experimentales;
2. selección preliminar de métodos y grafos;
3. reducción de candidatos;
4. optimización intermedia;
5. inventario de la comparación final;
6. comparación descriptiva TRSS--MNE;
7. dependencia por escenario de pérdida;
8. señales temporales representativas;
9. PSD original--interpolado;
10. contribución del término temporal;
11. costo computacional;
12. frontera práctica TRSS--MNE.

Auditoría realizada:

- No quedan ocurrencias activas del término reemplazado en capítulos, tablas, scripts activos ni planes actuales.
- Todas las tablas insertadas en Capítulo 4 están mencionadas en el texto.
- Todas las figuras insertadas en Capítulo 4 están mencionadas en el texto.
- No hay `Wilcoxon`, `q_{BH}`, `significancia`, `H1/H2` ni “hipótesis respaldada” como eje narrativo en capítulos.
- Compilación actual: 0 errores, 0 citas indefinidas, 0 referencias indefinidas, 0 overfull hbox.
- Validador estructural: `PASS` en `tesis_completa.tex` y `tesis_caps_1_5.tex`.
- QA visual final: sin problemas graves en páginas revisadas ni figuras individuales.

## 2. Problema pendiente después de mejorar Capítulo 4

Los capítulos 5 y 6 fueron corregidos en V3 para evitar el marco de hipótesis, pero todavía pueden fortalecerse para cerrar mejor la nueva estructura experimental. Ahora que el Capítulo 4 incluye selección preliminar, reducción de candidatos, optimización intermedia y comparación final, la discusión y las conclusiones deben reflejar esa trayectoria completa, no solo la comparación final TRSS--MNE.

El cierre debe responder explícitamente:

- qué se hizo realmente;
- qué decisiones se tomaron y por qué;
- qué resultados son finales y cuáles son preliminares/intermedios;
- qué carencias quedan;
- qué se omitió por tiempo, costo, datos o alcance;
- qué líneas de trabajo futuro se desprenden naturalmente de esas limitaciones.

## 3. Objetivo del plan para Capítulo 5

Convertir el Capítulo 5 en una discusión crítica de tres niveles:

1. **Nivel experimental:** qué se aprendió de la selección preliminar, reducción de candidatos y optimización intermedia.
2. **Nivel comparativo:** cómo interpretar TRSS frente a MNE bajo escenarios de pérdida, métricas y costo.
3. **Nivel de alcance:** qué no se puede concluir todavía y por qué.

## 4. Nueva estructura propuesta para Capítulo 5 — Discusión

### 5.1 Lectura integrada de la trayectoria experimental

Propósito: explicar que el resultado principal no es solo una tabla TRSS--MNE, sino una secuencia de decisiones experimentales.

Debe discutir:

- la exploración inicial de múltiples métodos/grafos;
- por qué no todos los métodos implementados pasan a la comparación final;
- la reducción como resultado experimental legítimo;
- diferencia entre evidencia preliminar e inferencia final.

Mensaje central:

> La tesis no selecciona TRSS arbitrariamente: llega a TRSS mediante una trayectoria experimental trazable.

### 5.2 Qué aportó la selección preliminar de métodos y grafos

Propósito: discutir el valor de los resultados intermedios.

Debe incluir:

- métodos temporales aparecen competitivos en varios conjuntos;
- grafos geométricos reproducibles son preferibles para conclusiones finales;
- grafos data-driven son prometedores pero más costosos o menos deterministas;
- grafos de correlación son informativos pero arriesgan circularidad.

Cuidado: no convertir la selección preliminar en conclusión principal.

### 5.3 Por qué MNE-Python sigue siendo una referencia fuerte

Mantener y reforzar la sección ya existente.

Debe conectar con Cap. 2:

- MNE no es una spline ingenua;
- normalización, regularización, pseudoinversa y uso global de canales explican su solidez;
- por eso la comparación final contra MNE es más exigente que comparar contra implementaciones propias simples.

### 5.4 Interpretación condicional de TRSS

Debe discutir:

- TRSS mejora varias métricas de reconstrucción, pero no domina todo;
- mejora más en pérdida cercana/periférica/severa;
- puede no ser preferible en señales suaves, baja pérdida o restricciones de velocidad;
- la contribución debe formularse como frontera de uso.

### 5.5 Tensión entre tiempo, forma temporal y espectro

Debe discutir explícitamente:

- MAE/NRMSE/DTW no son equivalentes a LSD/PSD;
- TRSS puede mejorar amplitud/forma y no mejorar distancia espectral global;
- MNE puede ser preferible para análisis espectral;
- PSD representativa ayuda, pero no reemplaza validación espectral más amplia.

### 5.6 Costo computacional y escalabilidad

Debe discutir:

- TRSS es más lento que MNE;
- sigue siendo viable offline, pero no necesariamente en preprocesamiento interactivo;
- costo aumenta con ventanas, sujetos, búsqueda de hiperparámetros y variantes de grafo;
- implementación dispersa/paralela queda como trabajo futuro.

### 5.7 Deficiencias y carencias del estudio

Esta sección debe ser más explícita que la actual. Debe listar limitaciones reales:

1. **Canales ocultos artificialmente.** Permite verdad de terreno, pero no equivale a canales realmente dañados.
2. **Ausencia de evaluación clínica experta.** No hay inspección ciega por especialistas EEG.
3. **Sin tareas downstream.** No se prueba impacto en clasificación BCI, ERP, conectividad, PSD por bandas o localización de fuentes.
4. **Reducción del espacio experimental.** Métodos/grafos descartados no fueron evaluados con igual profundidad en la comparación final.
5. **Grafos data-driven no cerrados.** Son prometedores, pero quedaron fuera por costo/reproducibilidad/circularidad.
6. **Limitación de datasets/montajes.** La evaluación cubre bases públicas relevantes, pero no todos los equipos, referencias, montajes ni poblaciones.
7. **Hiperparámetros.** El oráculo no es desplegable; la calibración automática sigue abierta.
8. **Costo de TRSS.** Falta optimización para tiempo real o procesamiento masivo.
9. **Modelos entrenables excluidos.** Deep learning y modelos supervisados quedan fuera del alcance metodológico.
10. **Validación externa.** Falta repetir el protocolo en nuevos registros y canales dañados reales.

### 5.8 Qué se obvió por alcance, tiempo o recursos

Nueva sección sugerida o subsección dentro de limitaciones.

Debe decir claramente:

- no se incorporaron modelos deep learning por requerir diseño de entrenamiento/validación externa;
- no se hizo validación clínica con expertos;
- no se hizo clasificación BCI downstream;
- no se hizo optimización de ingeniería de TRSS para tiempo real;
- no se agotaron grafos aprendidos ni adaptativos;
- no se evaluaron todas las combinaciones posibles en fase final para evitar sobreajuste y saturación del documento.

### 5.9 Lecciones metodológicas

Reformular como cierre de discusión:

- comparar contra referencias comunitarias maduras es obligatorio;
- resultados negativos o descartes también son resultados;
- una tesis experimental debe mostrar la ruta de reducción, no solo el resultado final;
- multi-métrica evita conclusiones simplistas;
- trazabilidad de artefactos es parte de la contribución.

## 5. Objetivo del plan para Capítulo 6

Convertir el Capítulo 6 en un cierre que responda directamente a objetivos y preguntas de investigación, incorporando lo aprendido de la fase experimental completa.

Debe evitar:

- lenguaje de hipótesis;
- afirmaciones de dominancia universal;
- conclusiones que parezcan más fuertes que la evidencia.

Debe reforzar:

- contribución metodológica;
- contribución experimental;
- frontera de uso;
- limitaciones honestas;
- trabajo futuro accionable.

## 6. Nueva estructura propuesta para Capítulo 6

### 6.1 Conclusiones por pregunta de investigación

En vez de conclusiones genéricas, responder P1 y P2.

#### P1 — ¿Cuándo mejora TRSS?

Respuesta esperada:

- mejora en varios escenarios difíciles;
- especialmente pérdida cercana/periférica/severa;
- no domina universalmente;
- evidencia basada en comparación pareada, señales representativas y métricas descriptivas.

#### P2 — ¿Qué compromiso existe entre precisión, espectro y costo?

Respuesta esperada:

- TRSS mejora amplitud/forma en muchos casos;
- MNE conserva ventajas en costo y LSD;
- elección depende del objetivo posterior;
- frontera práctica es la conclusión central.

### 6.2 Conclusiones sobre la fase experimental completa

Nueva sección o bloque:

- selección preliminar mostró heterogeneidad de familias/grafos;
- reducción de candidatos fue necesaria para evitar comparación saturada;
- optimización intermedia demostró sensibilidad de hiperparámetros;
- comparación final permitió una lectura más limpia y trazable.

### 6.3 Aportes de la tesis

Reordenar aportes:

1. marco experimental reproducible;
2. evaluación multi-fase de métodos/grafos;
3. comparación justa contra MNE-Python;
4. caracterización condicional de TRSS;
5. paquete de artefactos trazables.

### 6.4 Deficiencias reconocidas como cierre

No repetir toda la discusión, pero sí resumir carencias:

- canales artificialmente ocultos;
- ausencia de validación con expertos;
- no downstream;
- no real-time;
- grafos aprendidos no cerrados;
- modelos entrenables fuera de scope.

### 6.5 Trabajo futuro priorizado

Organizar por prioridad, no como lista plana.

#### Prioridad técnica inmediata

- acelerar TRSS con matrices dispersas, factorización reutilizable, paralelización y ventanas por lote;
- regla automática de hiperparámetros sin oráculo;
- implementación reproducible empaquetada.

#### Prioridad experimental

- validar con canales realmente dañados;
- evaluación ciega por expertos;
- datasets externos y más sujetos/montajes;
- validación por tarea downstream: BCI, ERP, PSD, conectividad, fuente.

#### Prioridad metodológica

- grafos adaptativos no circulares;
- grafos data-driven con separación entrenamiento/evaluación;
- estimación de incertidumbre por caso;
- reglas de decisión automatizadas TRSS vs MNE.

#### Prioridad de extensión

- MEG, ECoG, arreglos de microelectrodos;
- modelos temporales más ricos;
- comparación futura contra modelos entrenables si existe diseño de validación independiente.

### 6.6 Cierre final

Debe terminar con una frase condicional y precisa:

> MNE debe mantenerse como referencia robusta y rápida; TRSS es una alternativa justificable cuando la pérdida espacial vuelve insuficiente el prior puramente espacial y el análisis permite asumir costo computacional adicional.

## 7. Cambios concretos que se harían si el usuario aprueba

1. Reescribir `chapters/05_discusion.tex` con la estructura anterior.
2. Reescribir `chapters/06_conclusiones.tex` con respuestas explícitas a P1/P2.
3. Actualizar `tables/ch8_objective_evidence_matrix.tex` si hace falta para reflejar selección preliminar, reducción y limitaciones.
4. Compilar `tesis_completa.tex` y `tesis_caps_1_5.tex`.
5. Ejecutar `scripts/validate_thesis.py`.
6. Ejecutar QA visual de páginas de discusión/conclusiones.
7. Verificar de nuevo ausencia de lenguaje de hipótesis/test como eje.

## 8. Criterios de aceptación

Los capítulos 5 y 6 estarán listos cuando:

- discutan no solo los resultados finales, sino también la ruta experimental completa;
- separen claramente evidencia preliminar, evidencia comparativa final y trabajo futuro;
- reconozcan explícitamente limitaciones y omisiones;
- no prometan validaciones no realizadas;
- respondan P1 y P2 de forma directa;
- dejen clara la frontera práctica MNE--TRSS;
- compilen sin errores, citas indefinidas, referencias indefinidas ni overfull;
- pasen QA visual final.
