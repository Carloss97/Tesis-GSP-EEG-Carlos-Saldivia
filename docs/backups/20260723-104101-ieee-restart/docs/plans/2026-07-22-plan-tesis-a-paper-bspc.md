# Plan de trabajo: de tesis aprobada a paper publicable en Biomedical Signal Processing and Control

> **Para Hermes:** ejecutar este plan por fases, con evidencia verificable en cada gate. No reutilizar automáticamente el paper IEEE actual como versión de envío.

**Objetivo:** convertir la tesis aprobada sobre reconstrucción de canales EEG faltantes mediante procesamiento de señales en grafos y regularización temporal en un artículo original, coherente, reproducible y editorialmente compatible con Biomedical Signal Processing and Control (BSPC), manteniendo una ruta de contingencia para otra revista indexada.

**Arquitectura editorial:** artículo de investigación completo, centrado en una contribución metodológica/experimental de benchmarking justo y no en una afirmación de superioridad universal de TRSS. La tesis será la fuente científica aprobada; los resultados y artefactos congelados serán la fuente numérica; el manuscrito se escribirá de nuevo con estructura IMRaD y límites explícitos.

**Tecnologías y artefactos:** LaTeX/Elsevier, BibTeX, Python, Optuna, MNE-Python, CSV/JSON/NPZ, validadores del repositorio, `Thesis-Copilot-Toolkit/paper/` y `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/`.

---

## 0. Diagnóstico de partida

### Evidencia ya disponible

- Tesis completa aprobada: `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/tesis_completa.tex` y `tesis_completa.pdf`.
- Línea argumental final validada por el supervisor en `build_logs/REVISION_PROFESOR_GUIA_FINAL.md`:
  - comparación TRSS--MNE condicional;
  - MNE como referencia fuerte y rápida;
  - TRSS como alternativa para pérdidas espaciales difíciles y procesamiento fuera de línea;
  - limitaciones explícitas: canales ocultos artificialmente, ausencia de evaluación experta y ausencia de tareas posteriores.
- QA final de la tesis en `build_logs/FINAL_VISUAL_QA_REPORT.md`: compilación exitosa, 0 errores LaTeX, 0 citas/referencias indefinidas y revisión visual aprobada.
- Sistema de paper existente en `Thesis-Copilot-Toolkit/paper/ieee/`, con versiones inglesa y española, figuras, tablas y bibliografía.
- Handoffs históricos recuperados de Git (`.agent_work/PUBLICATION_STRATEGY_GUIDE.md`, `SESSION_COMPREHENSIVE_STATUS.md` y `FINAL_SESSION_REPORT.md` del commit anterior): ya recomendaban tratar el trabajo como benchmark/validación metodológica, añadir limitaciones, y no presentarlo como algoritmo fundamentalmente nuevo.

### Problemas que bloquean reutilizar el paper actual sin una auditoría

1. El paper IEEE contiene afirmaciones más fuertes que la tesis aprobada: por ejemplo, “statistically significant margins”, “theoretical ceiling”, “clinical interpretation”, “sub-millisecond precision” y superioridad generalizada. Deben eliminarse o demostrarse de nuevo.
2. El paper actual contiene referencias a resultados y métodos históricos que no deben entrar en el manuscrito final si no pertenecen al protocolo final. En particular, cualquier mención a Visibility/NNK queda excluida del texto activo y de los artefactos visibles.
3. Hay dos escalas experimentales que deben reconciliarse antes de redactar: la tesis describe 3 datasets, 120 escenarios y una comparación final de 100 estratos/300 casos; el paper heredado mezcla además conteos de iteraciones, ratios, conteos de canales y resultados de ablación. No se puede publicar ningún número hasta construir una tabla maestra de procedencia.
4. El paper IEEE no es todavía una plantilla BSPC: el objetivo editorial exige fuente editable, abstract de menos de 250 palabras, highlights separados, keywords en inglés, referencias numeradas consistentes, declaración de disponibilidad de datos y declaraciones éticas/CRediT/IA cuando correspondan.
5. El término “ATS” no debe tratarse como una prueba científica única ni como algo que pueda burlarse. El riesgo real es el desk screening editorial: alcance, novedad, claridad, duplicación, integridad, formato, idioma, referencias y coherencia de archivos. El plan optimiza esos criterios de forma honesta; no promete evitar automáticamente un rechazo.

---

## Fase A — Congelamiento científico y control de versiones

**Estado:** [ ] Por implementar  
**Prioridad:** P0 — bloqueo de todas las fases de escritura

**Objetivo:** establecer una única versión científica defendible y evitar mezclar resultados históricos, proxies, ejecuciones normalizadas y resultados finales.

**Archivos:**
- Crear: `docs/paper/` con inventario y decisiones editoriales.
- Crear: `docs/paper/resultados_fuente_maestra.csv` o equivalente documentado.
- Revisar: `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/config/results_data.tex`.
- Revisar: `Thesis-Copilot-Toolkit/results/` y sus reportes canónicos.
- Revisar: scripts y configuraciones que generaron los resultados finales.

**Tareas:**
- [ ] Crear una tabla afirmación → número → CSV/JSON/figura → script → configuración → commit.
- [ ] Separar resultados finales, exploratorios, proxies y ablaciones auxiliares.
- [ ] Fijar la unidad estadística: caso pareado, estrato, sujeto, ensayo o ventana; no usar “iteración” ambiguamente.
- [ ] Registrar dataset, versión, sujetos/ensayos, canales, frecuencia, segmento, máscara, severidad, semilla, método, hiperparámetros y normalización.
- [ ] Verificar que no se agreguen ejecuciones normalizadas y no normalizadas.
- [ ] Congelar un tag/commit de resultados del paper, sin modificar la tesis aprobada.
- [ ] Crear una lista de números que no pueden aparecer hasta tener respaldo.

**Criterio de éxito:** ningún número del futuro manuscrito puede existir sin una ruta de trazabilidad completa y reproducible.

---

## Fase B — Auditoría de elegibilidad y encaje con BSPC

**Estado:** [ ] Por implementar  
**Prioridad:** P0

**Objetivo:** comprobar que el artículo es un full paper original dentro del alcance de BSPC y que los requisitos de envío se satisfacen antes de invertir en edición fina.

**Fuente editorial vigente consultada:** Guide for Authors oficial de BSPC/Elsevier: https://www.sciencedirect.com/journal/biomedical-signal-processing-and-control/publish/guide-for-authors

**Requisitos que deben incorporarse al checklist:**
- [ ] Full paper de aproximadamente 5.000 palabras.
- [ ] Abstract factual de menos de 250 palabras.
- [ ] Entre 1 y 7 keywords en inglés.
- [ ] Highlights separados: 3–5 bullets, máximo 85 caracteres cada uno.
- [ ] Graphical abstract opcional, recomendable, con archivo separado y dimensiones/formato indicados por BSPC.
- [ ] Fuente editable `.tex` y archivos editables; el PDF no sustituye los fuentes.
- [ ] Secciones numeradas y referencias cruzadas coherentes.
- [ ] Tablas editables, figuras separadas, captions autoexplicativos y resoluciones requeridas.
- [ ] Referencias numeradas y datos bibliográficos/DOI completos.
- [ ] Data availability statement; BSPC indica depósito de datos en repositorio o explicación si no es posible.
- [ ] Declaración de conflictos, financiamiento, contribuciones CRediT y uso de IA generativa, según corresponda.
- [ ] Confirmación de autoría, autor corresponsal y aprobación de todos los autores.
- [ ] Declaración de que la tesis previa no impide la publicación y que el manuscrito no está simultáneamente bajo revisión en otra revista.

**Criterio de éxito:** checklist editorial BSPC completo y una matriz de encaje que conecte cada requisito del journal con un archivo o sección del paquete de envío.

---

## Fase C — Reposicionamiento de la contribución

**Estado:** [ ] Por implementar  
**Prioridad:** P0

**Objetivo:** presentar una contribución que sea novedosa por su diseño de evaluación, control de referencias y caracterización condicional, sin vender TRSS como algoritmo nuevo ni realizar claims clínicos no sustentados.

**Tesis editorial propuesta:**

> A rigorously controlled, multi-metric benchmark of missing-channel EEG reconstruction that compares graph/temporal regularization with a mature MNE-Python reference under reproducible random and spatially contiguous masking, with explicit reporting of the accuracy–spectral-fidelity–runtime trade-off.

**Tareas:**
- [ ] Elegir un título informativo sin prometer “clinical improvement”, “real-time” o “state-of-the-art” salvo evidencia directa.
- [ ] Formular 2–3 contribuciones verificables:
  1. protocolo pareado y reproducible;
  2. comparación justa contra MNE-Python y baselines optimizados;
  3. frontera práctica dependiente de patrón/severidad/métrica/costo.
- [ ] Separar novedad metodológica del origen de TRSS: citar correctamente el método original y declarar que la contribución de este paper es su evaluación controlada.
- [ ] Reescribir la motivación para BSPC: robustez de señales biomédicas, no una aplicación clínica no realizada.
- [ ] Eliminar lenguaje de marketing, causalidad clínica, “fisiológicamente probado”, “clinical-grade” y “automáticamente generalizable”.
- [ ] Incluir un párrafo claro de limitaciones y otro de qué no se evaluó.

**Criterio de éxito:** introducción, abstract, discusión y conclusión podrían leerse de forma independiente y producir exactamente la misma interpretación prudente.

---

## Fase D — Auditoría metodológica y estadística antes de escribir resultados

**Estado:** [ ] Por implementar  
**Prioridad:** P0

**Objetivo:** cerrar las inconsistencias técnicas que un editor o revisor detectaría inmediatamente.

**Tareas:**
- [ ] Auditar datasets: PhysioNet EEGBCI, BCI Competition IV 2a y MNE Sample; confirmar sujetos, ensayos, canales, frecuencia, preprocesamiento y disponibilidad.
- [ ] Auditar la definición de pérdida aleatoria y contigua/cercana; usar una terminología única.
- [ ] Confirmar si se reportan ratios 10–40%, escenarios de 1–3 canales o ambos; si ambos son necesarios, separarlos como experimentos distintos.
- [ ] Confirmar si los resultados principales son los 120 escenarios de la tesis o los 300 casos de la validación comparativa; no combinarlos en una misma tabla sin explicar la relación.
- [ ] Auditar la partición exploratoria versus comparativa y demostrar que los hiperparámetros quedaron congelados antes de la evaluación principal.
- [ ] Revisar el estado de validación de implementaciones externas: cualquier equivalencia Python–MATLAB/GSPBox parcial debe declararse como parcial/proxy, nunca como equivalencia estricta.
- [ ] Definir agregación por sujeto/ensayo antes de agregar por ventanas o iteraciones, para evitar pseudorreplicación.
- [ ] Preferir medianas, IQR, diferencias pareadas, tasa de victoria e intervalos bootstrap jerárquicos cuando sea compatible con el protocolo aprobado.
- [ ] Tratar pruebas de hipótesis como auxiliares; no construir la conclusión alrededor de p-values.
- [ ] Verificar la ablación temporal con los artefactos finales: las narrativas históricas reportan tanto beneficio pequeño/no significativo como mejoras espectrales significativas. Solo una versión puede quedar en el paper, y debe concordar con el CSV fuente.
- [ ] Recalcular desde datos congelados los números que el paper va a mostrar; no copiar tablas de la tesis manualmente.

**Criterio de éxito:** auditoría independiente sin contradicciones en n, unidades, denominadores, dirección de métricas, particiones ni significancia.

---

## Fase E — Reanálisis mínimo de alto valor

**Estado:** [ ] Por implementar  
**Prioridad:** P1 — ejecutar solo si la Fase D identifica una brecha

**Objetivo:** reforzar el artículo sin abrir una campaña experimental ilimitada.

**Paquete mínimo recomendado:**
- [ ] Reproducir la comparación principal TRSS fijo vs MNE con hiperparámetros congelados.
- [ ] Reportar resultados por patrón de pérdida y severidad, no solo una media global.
- [ ] Incluir una ablación TRSS completo vs sin término temporal, con su interpretación exacta.
- [ ] Incluir runtime por caso y costo de calibración por separado.
- [ ] Incluir una tabla de sensibilidad o estabilidad de los hiperparámetros principales.
- [ ] Reportar señales/PSD representativas seleccionadas con una regla predefinida, incluyendo al menos un caso favorable a cada método y un empate práctico.
- [ ] Añadir, si los datos lo permiten, una validación externa o un análisis por sujeto/registro; no llamarlo validación clínica.

**No hacer en esta fase:**
- No añadir deep learning solo para “parecer más actual” sin protocolo de entrenamiento, validación externa y control de fuga.
- No abrir nuevos datasets si no se puede documentar su versión y reproducibilidad.
- No usar resultados exploratorios como confirmatorios.
- No perseguir significancia después de mirar resultados.

**Criterio de éxito:** cada experimento adicional responde una objeción editorial concreta y tiene configuración, semilla, script y artefacto reproducible.

---

## Fase F — Redacción del manuscrito BSPC desde la evidencia

**Estado:** [ ] Por implementar  
**Prioridad:** P1

**Objetivo:** escribir un manuscrito de aproximadamente 5.000 palabras, no una tesis comprimida.

**Estructura propuesta:**

1. **Introduction** — problema, brecha, objetivo, contribuciones y límites.
2. **Related work** — interpolación EEG, spherical splines/MNE, GSP, regularización temporal, evaluación de canales faltantes.
3. **Materials and methods** — datasets, preprocesamiento, máscaras, métodos, grafos, métricas, optimización, separación de fases y unidad estadística.
4. **Experimental design** — protocolo congelado, escenarios, comparación pareada y reproducibilidad.
5. **Results** — resultados principales primero; ablación, runtime, sensibilidad y ejemplos cualitativos después.
6. **Discussion** — interpretación condicional, comparación con literatura, limitaciones y relevancia para pipelines biomédicos.
7. **Conclusion** — 3–5 conclusiones estrictamente respaldadas.
8. **Data availability, code availability, funding, competing interests, CRediT y AI declaration**, según proceda.

**Regla de redacción:** escribir primero Methods y Results desde la tabla maestra; luego Introduction/Related Work; cerrar Abstract, Highlights, Discussion y Conclusion al final.

**Archivos de trabajo:**
- Crear: `Thesis-Copilot-Toolkit/paper/bspc/`.
- Crear: `bspc/main.tex`, `bspc/sections/*.tex`, `bspc/bibliography/references.bib`.
- Crear: `bspc/highlights.txt`.
- Crear: `bspc/graphical_abstract.*` si se decide incluirlo.
- Mantener: `paper/ieee/` como versión histórica, no como fuente automática de copia.

**Criterio de éxito:** el manuscrito puede leerse sin conocer la tesis, no contiene capítulos de revisión institucional, y todos los resultados principales están respaldados por una figura/tabla y una referencia de datos.

---

## Fase G — Conversión editorial, accesibilidad y control de desk screening

**Estado:** [ ] Por implementar  
**Prioridad:** P1

**Objetivo:** reducir rechazos administrativos o de primera lectura por forma, claridad, duplicación o inconsistencias.

**Checklist:**
- [ ] Abstract <250 palabras; keywords 1–7 y en inglés.
- [ ] Highlights 3–5 bullets, ≤85 caracteres por bullet.
- [ ] Título conciso y sin acrónimos innecesarios.
- [ ] Una sola variante de inglés: americano o británico.
- [ ] Todas las abreviaturas se definen en la primera aparición.
- [ ] No hay afirmaciones clínicas sin estudio clínico.
- [ ] No hay referencias a Visibility/NNK ni métodos descartados que no formen parte del relato final.
- [ ] No hay rutas locales, nombres internos de archivos ni identificadores de ejecución en el texto principal.
- [ ] Figuras separadas, legibles en 5–13 cm cuando corresponda, con texto no superpuesto, paleta accesible y captions completos.
- [ ] Tablas editables, sin duplicar innecesariamente las figuras.
- [ ] Todas las citas aparecen en la bibliografía y viceversa; DOI y metadatos revisados.
- [ ] Similaridad textual tesis–paper revisada: reutilizar ideas y resultados con redacción nueva, declarar la tesis previa cuando el sistema lo solicite y evitar publicación redundante.
- [ ] Declarar honestamente el uso de herramientas generativas en la preparación si se usaron, conforme a la política vigente de Elsevier; nunca atribuirles autoría ni delegar la verificación científica.
- [ ] Revisar que el PDF de revisión y los fuentes editables produzcan el mismo contenido.

**Criterio de éxito:** checklist firmado por autor y supervisor, sin defectos administrativos conocidos y con un paquete que un editor pueda procesar sin pedir reconstrucciones básicas.

---

## Fase H — Revisión humana, decisión de revista y envío

**Estado:** [ ] Por implementar  
**Prioridad:** P1

**Objetivo:** obtener una evaluación experta antes del envío y presentar una candidatura editorial coherente.

**Tareas:**
- [ ] Hacer revisión ciega interna por una persona con experiencia en EEG/GSP y otra con experiencia en publicación biomédica.
- [ ] Pedir que respondan únicamente: ¿cuál es la contribución?, ¿qué evidencia la respalda?, ¿qué claim parece exagerado?, ¿qué falta para reproducirlo?, ¿lo enviaría a BSPC?
- [ ] Preparar carta de presentación: problema BSPC, contribución metodológica, resultados principales, límites y declaración de originalidad.
- [ ] Confirmar autoría, orden, afiliaciones institucionales, autor corresponsal, financiación y conflictos con el supervisor antes de subir archivos.
- [ ] Enviar primero a BSPC si el encaje y la tabla maestra están cerrados.
- [ ] Si hay rechazo editorial por alcance o nivel de novedad, usar la transferencia de Elsevier solo tras revisar el diagnóstico; no reenviar sin cambiar el problema identificado.

### Ruta de contingencia editorial

- **Opción primaria:** Biomedical Signal Processing and Control — encaja por EEG, robustez, GSP, análisis temporal y benchmarking; acepta full papers y benchmark/dataset papers.
- **Opción secundaria a evaluar con datos actualizados:** Computers in Biology and Medicine — si el manuscrito enfatiza pipeline biomédico reproducible y evaluación computacional.
- **Opción de menor riesgo editorial, sujeto a requisitos e indexación vigentes:** IEEE Access u otra revista compatible con estudios metodológicos reproducibles.
- **No seleccionar TBME/JBHI/TNSRE automáticamente:** exigir una revisión de alcance y nivel de contribución; el artículo actual es más naturalmente benchmark/validación que innovación clínica o algorítmica de alto impacto.

**Criterio de éxito:** envío realizado con número de manuscrito y copia íntegra del paquete; cualquier decisión posterior se gestiona con respuesta punto por punto, no con reescrituras improvisadas.

---

## Gates obligatorios antes de enviar

### Gate 1 — Integridad científica
- [ ] Tabla maestra completa.
- [ ] Resultados reproducidos desde fuentes congeladas.
- [ ] Sin mezcla de versiones, normalizaciones o denominadores.
- [ ] Claims ajustados a limitaciones.

### Gate 2 — Coherencia tesis–paper
- [ ] No se contradice la tesis aprobada.
- [ ] El paper no afirma resultados que la tesis no respalda.
- [ ] Las diferencias de protocolo están documentadas como reanálisis posterior, si las hubiera.
- [ ] No se incluye Visibility/NNK en el texto activo.

### Gate 3 — Encaje BSPC
- [ ] Full paper ~5.000 palabras.
- [ ] Abstract, keywords, highlights y graphical abstract según guía.
- [ ] Secciones numeradas, fuentes editables y figuras separadas.
- [ ] Datos/código/declaraciones preparados.

### Gate 4 — Calidad lingüística y visual
- [ ] Inglés científico revisado por humano competente.
- [ ] Figuras legibles aisladas y en el PDF completo.
- [ ] Referencias verificadas con DOI cuando exista.
- [ ] No hay lenguaje genérico, promocional o evidentemente ensamblado.

### Gate 5 — Aprobación de autores
- [ ] Supervisor aprueba tesis narrativa, resultados y contribución.
- [ ] Todos los autores aprueban versión, orden y declaraciones.
- [ ] Carta de presentación revisada.

---

## Secuencia temporal realista

- **Semana 1:** Fases A–B, congelamiento y auditoría editorial.
- **Semana 2:** Fases C–D, contribución y reconciliación estadística.
- **Semanas 3–4:** Fase E solo si hay brechas; regeneración de tablas/figuras.
- **Semanas 5–6:** Fase F, redacción completa del manuscrito BSPC.
- **Semana 7:** Fase G, edición, idioma, figuras, referencias y checklist.
- **Semana 8:** Fase H, revisión humana, aprobación del supervisor y envío.

La fecha se ajusta al tiempo de cómputo y a la disponibilidad del supervisor; no se debe acortar eliminando los Gates 1–3.

---

## Entregables finales

1. Manuscrito BSPC editable y PDF de revisión.
2. `highlights.txt` válido.
3. Graphical abstract, si se incluye.
4. Tabla maestra de trazabilidad.
5. Repositorio/archivo de código y resultados congelados, con README reproducible.
6. Data availability statement y enlaces persistentes cuando sea posible.
7. Carta de presentación.
8. Checklist de autoría, CRediT, financiación, conflictos y declaración de IA.
9. Informe final de QA: compilación, referencias, figuras, tablas, similaridad y coherencia numérica.

## Decisión recomendada ahora

No enviar el `paper/ieee/main.pdf` actual directamente. El siguiente trabajo correcto es ejecutar las Fases A y D en conjunto: congelar la evidencia y reconciliar las cifras. Después se puede aprovechar estructura, figuras y bibliografía, pero la redacción debe rehacerse con BSPC como objetivo y con la tesis aprobada como límite de lo que se afirma.

## Fuentes editoriales

- Guide for Authors oficial de BSPC/Elsevier: https://www.sciencedirect.com/journal/biomedical-signal-processing-and-control/publish/guide-for-authors
- Página oficial de la revista: https://www.sciencedirect.com/journal/biomedical-signal-processing-and-control
- Sistema oficial de envío: https://submit.elsevier.com/BSPC
