# Plan Capítulo 4 Focus V3.2 — Documento capítulos 1–4

Fecha: 2026-06-24  
Backup: `backups/cap4_focus_1_4_20260624_183831/`

## Objetivo

Revisar exclusivamente el Capítulo 4 y producir un documento parcial con capítulos 1--4. La prioridad es que el Capítulo 4 funcione como capítulo autónomo de **Experimentos y Resultados**, mostrando la trayectoria completa:

1. resultados preliminares de exploración;
2. reducción de métodos y grafos;
3. optimización intermedia;
4. comparación final TRSS--MNE;
5. inspección temporal, espectral y práctica.

## Auditoría sección por sección

### 4.1 Mapa de fases experimentales

Estado: correcto.  
Función: introduce la secuencia experimental y distingue preliminar/intermedio/final.  
Acción: mantener, verificando que use “exploración preliminar” y no terminología poco natural.

### 4.2 Selección preliminar de métodos y grafos

Estado: correcto.  
Función: muestra resultados preliminares por combinación método--grafo.  
Acción: mantener tabla `ch4_preliminary_screening_top_candidates`, asegurar que se lea como evidencia exploratoria y no conclusión final.

### 4.3 Reducción de candidatos

Estado: correcto.  
Función: explica descarte por circularidad, costo y reproducibilidad.  
Acción: mantener tablas de microbenchmark y decisiones.

### 4.4 Optimización intermedia y congelamiento

Estado: necesita refuerzo.  
Problema: actualmente es principalmente narrativa, sin tabla propia.  
Acción: crear `tables/ch4_intermediate_optimization_summary.tex` para mostrar variantes, rol experimental y decisión de uso.

### 4.5 Inventario final

Estado: correcto.  
Función: separa artefactos cuantitativos y figuras cualitativas.  
Acción: mantener.

### 4.6 Resumen TRSS--MNE

Estado: correcto.  
Función: reporta resultados finales descriptivos.  
Acción: mantener, cuidando que costo no comprima figura de calidad.

### 4.7 Dependencia por escenario

Estado: correcto.  
Función: muestra dónde TRSS gana más.  
Acción: mantener mapa de calor secuencial positivo.

### 4.8 Reconstrucciones temporales

Estado: correcto.  
Función: muestra casos favorables, desfavorables, empate y pérdida severa.  
Acción: mantener.

### 4.9 Preservación espectral

Estado: correcto.  
Función: muestra que MAE y PSD/LSD no son equivalentes.  
Acción: mantener.

### 4.10 Contribución temporal

Estado: correcto, pero puede mejorar terminología.  
Acción: reemplazar “ablación” por “análisis de contribución” para evitar tecnicismo innecesario.

### 4.11 Costo computacional y complejidad

Estado: funcional, pero usa tabla con nombre/label `ch6`.  
Acción: crear copia `tables/ch4_runtime_complexity.tex` con label `tab:ch4_runtime_complexity` y actualizar referencias.

### 4.12 Síntesis práctica

Estado: correcto.  
Función: frontera práctica TRSS--MNE.  
Acción: mantener.

## Acciones ejecutables

1. Crear tabla de optimización intermedia.
2. Crear tabla de complejidad específica de Cap. 4.
3. Actualizar `chapters/04_resultados.tex` para usar ambas tablas.
4. Reemplazar “ablación” por “análisis de contribución”.
5. Crear `tesis_caps_1_4.tex` con solo capítulos 1--4.
6. Compilar `tesis_caps_1_4.tex`.
7. Verificar errores, referencias indefinidas, figuras faltantes y overfull hbox.
8. QA visual del documento 1--4, especialmente páginas de Cap. 4.

## Criterios de aceptación

- El documento parcial `tesis_caps_1_4.pdf` compila.
- Cap. 4 incluye evidencia preliminar, intermedia y final.
- Todas las tablas y figuras de Cap. 4 están referenciadas.
- No quedan referencias a capítulos 5--6 en el driver parcial.
- No hay texto superpuesto, figuras recortadas, captions cortadas ni páginas casi vacías graves.
- Compilación con 0 errores, 0 referencias/citas indefinidas y 0 overfull hbox.
