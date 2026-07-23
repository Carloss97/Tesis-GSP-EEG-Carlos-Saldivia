# Plan de trabajo: presentación y narrativa para defensa de título

Fecha: 2026-07-23  
Proyecto: `Tesis-GSP-EEG-Carlos-Saldivia`  
Estado: plan previo a ejecución; no se modifica aún la tesis, el paper ni sus figuras fuente.

## 1. Objetivo

Preparar dos entregables coordinados para una defensa formal de aproximadamente 30 minutos:

1. Una presentación Beamer en LaTeX (`.tex` y PDF), visualmente legible, basada en la tesis final, el manuscrito derivado y los artefactos realmente producidos en el proyecto.
2. Un documento de narrativa en LaTeX (`.tex` y PDF) que indique qué decir en cada diapositiva, transiciones, tiempos, motivación de decisiones, límites de interpretación y un banco de preguntas y respuestas para el comité.

La defensa no se construirá como un resumen capítulo por capítulo. Se organizará como un argumento científico:

**problema → brecha → decisión metodológica → diseño controlado → evidencia → frontera práctica → aportes y límites**.

## 2. Fuentes auditadas y jerarquía de evidencia

### 2.1 Fuente canónica

La fuente primaria será la tesis final:

- `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/tesis_completa.tex`
- `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/tesis_completa.pdf`
- capítulos en `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/chapters/`
- tablas finales en `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/tables/`
- figuras finales en `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/figures/`

### 2.2 Fuente secundaria

El paper se utilizará para condensar el argumento, afinar la formulación de contribuciones y anticipar preguntas editoriales, pero no para sustituir ni mezclar protocolos:

- `Thesis-Copilot-Toolkit/paper/ieee_tbme/`
- `docs/paper/ieee_tbme_thesis_protocol.md`
- `docs/paper/ieee_tbme_claim_evidence_matrix.md`

### 2.3 Artefactos de apoyo

- scripts de generación y validación de la tesis;
- protocolos y matrices claim–evidence;
- figuras finales y tablas trazables;
- documentación de fases experimentales, reducción de candidatos y reproducibilidad.

### 2.4 Regla de consistencia

Antes de escribir las diapositivas se construirá una matriz específica para la defensa con estas columnas:

- afirmación;
- cifra o conclusión;
- protocolo al que pertenece;
- unidad estadística;
- tabla/figura fuente;
- frase autorizada para exposición;
- limitación asociada;
- posible pregunta del comité.

No se mezclarán como si fueran una sola evaluación:

- el diseño amplio de tres datasets, dos patrones, cuatro severidades y cinco semillas (120 combinaciones exploratorias);
- la trayectoria de 18 métodos y nueve grafos;
- la comparación final pareada de TRSS fijo frente a MNE;
- campañas o manuscritos históricos que no pertenezcan a la evidencia final de la tesis.

El punto deberá quedar explícito en la defensa: **la amplitud del trabajo corresponde a la fase exploratoria y de selección; las cifras principales corresponden a la comparación final congelada**.

Visibility/NNK no aparecerá en texto, tablas, figuras, notas ni diapositivas de respaldo.

## 3. Entregables propuestos

Se creará una carpeta nueva y separada:

`Thesis-Copilot-Toolkit/defensa/`

Estructura prevista:

```text
Thesis-Copilot-Toolkit/defensa/
├── presentacion_defensa.tex
├── presentacion_defensa.pdf
├── narrativa_defensa.tex
├── narrativa_defensa.pdf
├── config/
│   ├── metadata.tex
│   ├── theme.tex
│   └── sources.tex
├── figures/
│   ├── source/        # referencias o enlaces a figuras canónicas
│   └── adapted/       # copias editoriales para formato 16:9
├── tables/
│   └── defense_claims.tex
├── qa/
│   ├── claim_evidence_defensa.md
│   ├── control_tiempos.md
│   ├── preguntas_comite.md
│   └── revision_visual.md
├── previews/
└── README.md
```

Si `defensa/` ya existe al comenzar la ejecución, se hará primero un respaldo fechado bajo `docs/backups/`. Los originales de tesis, paper y figuras no se editarán en sitio.

## 4. Formato de la presentación

- Clase: `beamer`.
- Relación de aspecto: 16:9 (`aspectratio=169`).
- Idioma: español.
- Estilo: formal, sobrio, alto contraste y con identidad UTFSM discreta.
- Portada: título oficial, Carlos Saldivia Heinz, Magíster en Ciencias de la Ingeniería, Departamento de Electrónica, Universidad Técnica Federico Santa María, profesor guía y fecha.
- Tipografía mínima efectiva: títulos 26–32 pt; cuerpo 18–22 pt; evitar tablas con texto menor a 15–16 pt.
- Máximo normal: 3–5 ideas por diapositiva.
- Una afirmación central por slide.
- Figuras sin texto o leyendas sobre datos/dibujos; se reservará espacio lateral o inferior para explicación.
- Citas breves al pie solo cuando sostengan una decisión conceptual; bibliografía completa en respaldo.
- Numeración visible de diapositivas para facilitar preguntas.
- Diapositivas de respaldo fuera del conteo de 30 minutos.

## 5. Guion visual y distribución de tiempo

Meta: 24–25 diapositivas principales, 28–30 minutos reales, dejando un margen de 30–90 segundos. La velocidad objetivo será de 115–130 palabras/minuto, con pausas al mostrar resultados.

| N.º | Diapositiva | Propósito | Recurso principal | Tiempo |
|---:|---|---|---|---:|
| 1 | Portada | Identificar trabajo y abrir con la pregunta práctica | Portada limpia | 0:30 |
| 2 | El problema real | Mostrar por qué un canal EEG faltante afecta análisis posteriores | Esquema EEG/canales | 1:20 |
| 3 | Por qué interpolar no es trivial | Contrastar continuidad espacial y temporal | Ejemplo conceptual | 1:10 |
| 4 | Brecha y motivación | Explicar límites de líneas base débiles, métricas únicas y escenarios simples | Tres brechas | 1:20 |
| 5 | Preguntas y objetivo | Delimitar exactamente qué se busca responder | P1, P2 y objetivo general | 1:00 |
| 6 | EEG como señal sobre un grafo | Introducir nodos, aristas, pesos y Laplaciano sin sobrecargar matemática | `ch2_gsp_concepts_clean.pdf` | 1:20 |
| 7 | MNE frente a TRSS | Explicar qué información utiliza cada método | `ch2_trss_operator.pdf` + esquema MNE | 1:50 |
| 8 | Decisiones de alcance | Justificar MNE como referencia, exclusión de DL y uso de grafos geométricos | Cuadro decisión–razón | 1:20 |
| 9 | Estrategia experimental completa | Mostrar selección, reducción, congelamiento y comparación | `ch3_methodology_flow.pdf` | 1:30 |
| 10 | Datos y diversidad experimental | Presentar datasets y aclarar unidad/alcance | Tabla simplificada | 1:00 |
| 11 | Cómo se simula la pérdida | Explicar verdad de terreno, patrones y severidades | Montaje con máscaras | 1:10 |
| 12 | Evaluación multi-métrica | Explicar por qué MAE no basta | Amplitud, forma, espectro, costo | 1:10 |
| 13 | Sistema y reproducibilidad | Mostrar arquitectura, semillas y trazabilidad | `ch3_architecture_blocks.pdf` o `ch4_traceability_pipeline.pdf` | 1:10 |
| 14 | De 18 métodos a la comparación final | Defender la reducción de candidatos y separar exploración de evidencia final | Flujo de reducción | 1:20 |
| 15 | Protocolo pareado final | Explicar misma señal, máscara y semilla; unidad estadística e intervalos | Diagrama pareado | 1:30 |
| 16 | Resultado principal | Presentar +12,4% MAE, intervalo y 72,0% de victorias | `ch6_robust_improvement_ci.pdf` | 1:30 |
| 17 | No hay un ganador universal | Mostrar portafolio de métricas y tensión con LSD | `ch6_metric_portfolio_improvement.pdf` | 1:20 |
| 18 | ¿Cuándo ayuda TRSS? | Mostrar heterogeneidad por patrón y severidad | `ch6_scenario_heatmap_mae.pdf` | 1:30 |
| 19 | Qué ocurre en la señal | Mostrar casos TRSS, MNE y empate sin usar ejemplos como prueba global | `ch4_representative_timeseries.pdf` | 1:15 |
| 20 | Tensión espectral | Explicar por qué menor MAE no implica menor LSD | `ch4_psd_original_vs_interpolated.pdf` | 1:10 |
| 21 | El costo computacional | Mostrar 0,1214 frente a 0,0090 s/caso y su dependencia de implementación | `ch6_runtime_mae_tradeoff.pdf` | 1:10 |
| 22 | Frontera práctica de decisión | Sintetizar cuándo preferir MNE, considerar TRSS o evaluar ambos | `ch7_decision_map.pdf` adaptada | 1:30 |
| 23 | Aportes | Separar aporte científico, metodológico, experimental y reproducible | Cuatro bloques breves | 1:10 |
| 24 | Limitaciones y validez | Reconocer ocultamiento artificial, tamaño efectivo, falta de validación clínica/downstream y costo | Matriz alcance/no alcance | 1:30 |
| 25 | Conclusión y trabajo futuro | Responder P1/P2 y cerrar con una frase defendible | Mensaje final + 3 prioridades | 1:30 |

Tiempo objetivo total: aproximadamente 29 minutos.

### Diapositivas de respaldo previstas

1. Ecuación completa de TRSS y significado de cada término.
2. Construcción del grafo k-NN gaussiano.
3. Diferencias entre spline propio y MNE-Python.
4. Lista de los 18 métodos y nueve estrategias de grafo.
5. Espacios de hiperparámetros y Optuna.
6. Tabla completa de datasets y preprocesamiento.
7. Definición y dirección de cada métrica.
8. Detalle de bootstrap jerárquico y unidad estadística.
9. Tabla numérica completa TRSS–MNE.
10. Resultados por escenario y casos frontera.
11. Complejidad asintótica y costo de calibración frente a aplicación.
12. Trazabilidad y estructura de artefactos.
13. Limitaciones de validez interna, externa y de constructo.
14. Referencias principales.

## 6. Estructura del documento narrativo

`narrativa_defensa.tex` se organizará por diapositiva. Cada bloque contendrá:

1. **Objetivo de la diapositiva**: qué debe comprender el comité.
2. **Narrativa oral**: texto natural para decir, no prosa de tesis.
3. **Idea que debe quedar**: una frase de retención.
4. **Transición**: enlace explícito a la siguiente diapositiva.
5. **Tiempo acumulado y tiempo de la slide**.
6. **Evidencia fuente**: capítulo, tabla, figura o artefacto.
7. **Qué no afirmar**: límites para evitar sobreinterpretaciones.
8. **Pregunta probable**: pregunta que puede surgir en ese punto.
9. **Respuesta breve**: 20–30 segundos.
10. **Respuesta ampliada**: 60–90 segundos, con respaldo técnico.

La narrativa completa se calibrará inicialmente en 3.400–3.700 palabras y luego se ajustará mediante dos ensayos cronometrados. No se escribirá para ser leída literalmente: se redactará en tono oral, con frases cortas y puntos de respiración.

## 7. Banco de preguntas del comité

Se prepararán aproximadamente 30–40 preguntas, agrupadas por tipo:

### 7.1 Motivación y originalidad

- ¿Cuál es el problema científico y cuál es el problema de ingeniería?
- ¿Dónde está la novedad si TRSS ya existía?
- ¿Por qué este trabajo es más que aplicar varios algoritmos?
- ¿Por qué MNE-Python es una referencia exigente y no una línea base débil?

### 7.2 Decisiones metodológicas

- ¿Por qué ocultar canales artificialmente?
- ¿Por qué patrones aleatorios y contiguos/periféricos?
- ¿Por qué 10–40% de severidad?
- ¿Por qué grafos geométricos y no aprendidos/correlacionales?
- ¿Por qué no incluir aprendizaje profundo?
- ¿Por qué congelar hiperparámetros?
- ¿Qué diferencia hay entre TRSS fijo, calibrado y oráculo?

### 7.3 Diseño, datos y estadística

- ¿Cuál es la unidad estadística real?
- ¿Por qué las máscaras o semillas no equivalen a sujetos?
- ¿Qué significa que el diseño sea pareado?
- ¿Cómo se construyeron los intervalos descriptivos?
- ¿Por qué no usar pruebas de hipótesis como marco principal?
- ¿Cómo evitar contaminación entre selección y evaluación?
- ¿Qué se puede generalizar desde los datasets usados?

### 7.4 Interpretación de resultados

- ¿Cómo puede TRSS mejorar MAE y empeorar LSD?
- ¿Por qué TRSS ayuda más con pérdida agrupada severa?
- ¿En qué casos falla o no vale la pena?
- ¿La mejora de 12,4% es práctica o solo numérica?
- ¿Por qué una tasa de victoria de 72% no implica superioridad universal?
- ¿Qué explica la fortaleza de MNE-Python?
- ¿Puede afirmarse preservación fisiológica?

### 7.5 Implementación y reproducibilidad

- ¿Cuál es la complejidad de ambos métodos?
- ¿Por qué TRSS es más lento y cómo podría acelerarse?
- ¿Cómo se garantiza que ambos métodos usan la misma máscara?
- ¿Cómo se rastrea una cifra hasta el artefacto original?
- ¿Puede un tercero reproducir el flujo completo?

### 7.6 Limitaciones y trabajo futuro

- ¿Qué cambia con canales realmente dañados?
- ¿Qué validación clínica faltaría?
- ¿Cómo evaluar impacto en BCI, ERP, conectividad o fuentes?
- ¿Cómo diseñar una regla automática MNE/TRSS?
- ¿Qué experimento realizaría primero con más tiempo o recursos?

Cada respuesta incluirá una versión directa y una ampliada, evitando respuestas defensivas. Cuando la evidencia no permita una conclusión, la respuesta correcta será delimitar el alcance y proponer la validación necesaria.

## 8. Fases de ejecución

### Fase 0 — Protección y congelamiento

1. Verificar `git status` y rama actuales.
2. Crear respaldo fechado si ya existe material de defensa.
3. No modificar la tesis final, el paper ni figuras fuente.
4. Registrar checksums o rutas de las figuras y tablas seleccionadas.

### Fase 1 — Auditoría de evidencia para defensa

1. Extraer claims principales de introducción, metodología, resultados, discusión y conclusión.
2. Reconciliar denominadores y protocolos.
3. Separar evidencia exploratoria de evidencia final.
4. Crear `qa/claim_evidence_defensa.md`.
5. Bloquear claims no autorizados: superioridad universal, validación clínica, tiempo real, generalización a tareas posteriores o significación no calculada.

### Fase 2 — Storyboard y control de tiempo

1. Confirmar la secuencia de 25 slides.
2. Asignar una idea central, figura y tiempo a cada slide.
3. Eliminar repeticiones entre motivación, discusión y conclusión.
4. Diseñar respaldo técnico para preguntas sin sobrecargar el cuerpo principal.

### Fase 3 — Construcción de la presentación Beamer

1. Crear preámbulo, tema, portada, pie, numeración y paleta.
2. Implementar las 25 diapositivas principales.
3. Incorporar figuras vectoriales canónicas o adaptaciones editoriales sin cambiar datos.
4. Redibujar solo esquemas cuando la versión de tesis no sea legible en 16:9.
5. Añadir diapositivas de respaldo y bibliografía.

### Fase 4 — Preparación de figuras y tablas

1. Inspeccionar cada figura en forma aislada.
2. Recortar márgenes sin cortar etiquetas.
3. Reubicar leyendas fuera de datos/dibujos cuando sea necesario.
4. Convertir tablas densas en gráficos o resúmenes de 3–5 filas.
5. Mantener una tabla de procedencia de cada visual.
6. Verificar legibilidad en la escala real de proyección.

### Fase 5 — Redacción de narrativa

1. Escribir el guion oral slide por slide.
2. Explicar explícitamente motivación, razonamiento y motivo de cada decisión crítica.
3. Incluir transiciones y frases de cierre.
4. Marcar pausas para explicar figuras.
5. Ajustar a 3.400–3.700 palabras antes del ensayo.

### Fase 6 — Preguntas y respuestas

1. Construir el banco de 30–40 preguntas.
2. Vincular cada respuesta con evidencia o limitación.
3. Preparar respuestas de 30 y 90 segundos.
4. Asociar cada pregunta técnica con una slide de respaldo.
5. Preparar preguntas adversariales: novedad, unidad estadística, validez externa, hiperparámetros, LSD y costo.

### Fase 7 — Compilación y validación técnica

1. Compilar ambos documentos con `latexmk`.
2. Resolver errores, referencias y archivos faltantes.
3. Auditar logs: errores, referencias/citas indefinidas y desbordes.
4. Verificar que todas las figuras y tablas existan.
5. Confirmar que no haya menciones visibles a Visibility/NNK.
6. Extraer texto de ambos PDF y comprobar cifras clave.

### Fase 8 — QA visual página por página

1. Renderizar todas las páginas a PNG.
2. Crear hojas de contacto para visión global.
3. Abrir cada slide individualmente.
4. Revisar contraste, tamaño, recortes, superposición, densidad y coherencia.
5. Revisar con especial cuidado gráficos con intervalos, heatmaps, señales y PSD.
6. Recompilar y repetir revisión después de cada cambio visual.

### Fase 9 — Ensayo cronometrado y ajuste final

1. Ensayo 1: lectura controlada del guion; registrar tiempo por slide.
2. Reducir texto donde el tiempo acumulado supere 30 minutos.
3. Ensayo 2: exposición natural sin leer literalmente.
4. Ajustar narrativa para quedar entre 28:30 y 29:30.
5. Preparar rutas abreviadas de 25 y 20 minutos por si el comité cambia el tiempo.
6. Congelar una versión final y registrar checksums.

## 9. Validación de contenido

La entrega se considerará completa solo si:

- las dos fuentes `.tex` compilan;
- existen los dos PDF;
- la presentación principal cabe en 30 minutos;
- cada cifra tiene fuente trazable;
- la diferencia entre fase exploratoria y comparación final es inequívoca;
- el diseño pareado y la unidad estadística se explican con claridad;
- las conclusiones responden directamente P1 y P2;
- las limitaciones se exponen antes de que el comité deba señalarlas;
- no se afirma validación clínica, generalización poblacional ni superioridad universal;
- no aparece Visibility/NNK;
- todas las diapositivas fueron inspeccionadas visualmente en tamaño real;
- existe respaldo técnico para las preguntas previsibles.

## 10. Riesgos y mitigaciones

### Riesgo 1: exceso de contenido para 30 minutos

Mitigación: limitar el cuerpo a 25 slides, mover derivaciones, tablas completas y detalles de implementación al respaldo.

### Riesgo 2: confusión entre protocolos

Mitigación: matriz claim–evidence de la defensa y una slide explícita que separe exploración amplia de comparación final.

### Riesgo 3: cifras incompatibles entre tesis y versiones del paper

Mitigación: tesis final como autoridad; el paper solo aporta síntesis. Toda cifra se verifica contra tablas finales antes de incorporarla.

### Riesgo 4: figuras ilegibles al proyectar

Mitigación: adaptación 16:9, leyendas externas, inspección aislada y dentro del PDF, mínimo tipográfico y sustitución de tablas densas.

### Riesgo 5: defensa de una “superioridad” que la evidencia no sostiene

Mitigación: lenguaje condicional y slide de frontera práctica MNE–TRSS.

### Riesgo 6: preguntas sobre estadística y generalización

Mitigación: explicar diseño pareado, clústeres, repetición de máscaras, intervalos descriptivos y alcance de la inferencia; disponer de una slide de respaldo específica.

### Riesgo 7: narrativa demasiado escrita

Mitigación: frases orales, transiciones, puntos de pausa y dos ensayos cronometrados.

## 11. Decisiones que no bloquean el inicio

Se usarán placeholders editables para:

- fecha exacta de defensa;
- nombres definitivos de examinadores;
- logotipo institucional oficial si existe una plantilla exigida;
- duración oficial si finalmente difiere de 30 minutos.

Si la universidad entrega una plantilla Beamer obligatoria o un límite distinto, se adaptará el tema y el cronograma sin cambiar la arquitectura argumental.

## 12. Resultado esperado

Una defensa que no solo muestre “qué se hizo”, sino que permita explicar con claridad:

- por qué el problema importa;
- por qué se eligió GSP/TRSS;
- por qué MNE es una comparación exigente;
- por qué se redujo el espacio de métodos;
- por qué el diseño pareado es necesario;
- qué significan realmente las mejoras observadas;
- por qué MAE, espectro y costo entregan respuestas distintas;
- cuándo usar TRSS, cuándo conservar MNE y cuándo evaluar ambos;
- qué no demuestra la tesis;
- cuál es el aporte científico y reproducible del trabajo.
