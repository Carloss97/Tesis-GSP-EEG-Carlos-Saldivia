# Diagnóstico de encaje editorial con Biomedical Signal Processing and Control

Fecha de consulta: 2026-07-23

Fuentes oficiales:

- Guide for Authors: https://www.sciencedirect.com/journal/biomedical-signal-processing-and-control/publish/guide-for-authors
- Página oficial de la revista: https://www.sciencedirect.com/journal/biomedical-signal-processing-and-control

## 1. Dictamen editorial

Decisión: `encaje condicional favorable`, pero `no listo para envío`.

El tema encaja de forma directa con el procesamiento y análisis de señales biomédicas, EEG, reconstrucción de sensores faltantes, preprocesamiento y evaluación de métodos computacionales. El riesgo editorial principal no es el área temática, sino que BSPC solicita contribuciones metodológicas claras y el journal no declara explícitamente que todo benchmark sea suficiente por sí solo.

La contribución debe presentarse como un estudio metodológico y experimental controlado que produce una regla de decisión reproducible, no como una mera comparación de implementaciones ni como un algoritmo completamente nuevo.

Tesis editorial recomendada, sujeta al reanálisis congelado:

> A rigorously controlled, multi-metric evaluation of missing-channel EEG reconstruction that compares fixed graph–temporal regularization with MNE-Python spherical splines under paired random and spatially clustered masking, while explicitly quantifying reconstruction quality, spectral fidelity, and computational cost.

## 2. Encaje con el alcance de BSPC

### Encaje fuerte

- procesamiento y análisis de señales biomédicas;
- EEG como señal fisiológica;
- métodos de adquisición, procesamiento, análisis e interpretación;
- preprocesamiento y robustez frente a sensores faltantes;
- análisis temporal, espectral y computacional;
- evaluación reproducible de algoritmos.

### Encaje que debe justificarse

- El procesamiento de señales en grafos no aparece nombrado literalmente en el alcance, pero es una metodología de procesamiento de señal compatible con él.
- El benchmarking no aparece nombrado como categoría editorial autónoma. Debe vincularse con una pregunta metodológica: cuándo una regularización espacio-temporal aporta valor frente a una referencia operativa madura.
- La novedad no puede depender solo del uso de Optuna. Debe surgir del protocolo pareado, la separación entre selección y evaluación, la evaluación multimétrica y la caracterización del compromiso calidad–espectro–costo.

### Fuera del alcance demostrable del estudio

- validación clínica;
- mejora de diagnóstico o pronóstico;
- evaluación por expertos EEG;
- impacto en clasificación BCI, ERP, conectividad o localización de fuentes;
- generalización a pacientes o hardware clínico real;
- reconstrucción de canales realmente dañados con ruido no binario.

## 3. Requisitos formales vigentes

| Requisito BSPC | Estado actual | Acción necesaria |
|---|---|---|
| Full paper de aproximadamente 5000 palabras | Pendiente | Redactar un artículo nuevo, no comprimir la tesis ni reutilizar automáticamente el IEEE histórico. |
| Abstract factual de menos de 250 palabras | Pendiente | Escribir al final, después de congelar Results. |
| 1–7 keywords en inglés | Pendiente | Seleccionar después del título y abstract. |
| 3–5 highlights, máximo 85 caracteres cada uno | Pendiente | Crear `highlights.txt` y validar caracteres automáticamente. |
| Graphical abstract | Opcional/recomendado | Decidir después de cerrar el protocolo; debe ser reproducible y no promocional. |
| Fuentes editables `.tex` | Pendiente | Crear paquete independiente `paper/bspc/`. |
| Figuras como archivos separados y citados | Parcial | Reutilizar solo figuras cuya procedencia coincida con los resultados congelados. |
| Captions autoexplicativos | Pendiente | Escribir desde la matriz de evidencia. |
| Tablas como texto editable, no imágenes | Viable | Generarlas desde CSV congelados. |
| Referencias coherentes | Parcial | Verificar metadatos y DOI antes de migrarlas a la bibliografía BSPC. |
| Data availability statement | Obligatorio | Declarar datasets públicos y disponibilidad de resultados derivados; justificar cualquier restricción. |
| Funding statement | Obligatorio según corresponda | Confirmar con autores y supervisor. |
| Competing interests | Obligatorio | Declarar conflictos o “nothing to declare”. |
| CRediT author contributions | Obligatorio | Aprobar roles con todos los autores. |
| Autor corresponsal | Obligatorio | Decisión humana pendiente. |
| Declaración de IA generativa | Obligatoria si se usó | Incluir declaración transparente conforme a la política vigente. |
| Originalidad y ausencia de envío simultáneo | Obligatorio | Confirmar antes de enviar. |
| Trabajo previo como tesis | Permitido por la guía | Declarar la relación cuando el sistema o editor lo solicite y evitar reutilización textual extensa. |
| Code availability | Recomendado | Añadir statement y enlace persistente cuando el paquete reproducible esté publicado. |

La guía indica que el trabajo previo en forma de tesis académica no impide automáticamente la publicación. Esto no elimina la obligación de originalidad del manuscrito ni la necesidad de explicar la relación con la tesis.

## 4. Contribución admisible

Contribuciones potencialmente publicables, si el reanálisis las confirma:

1. Un protocolo pareado y trazable para comparar reconstrucción de canales EEG faltantes bajo máscaras aleatorias y espacialmente agrupadas.
2. Una comparación contra MNE-Python como referencia comunitaria madura, usando hiperparámetros TRSS fijados antes de la evaluación.
3. Una caracterización condicional del compromiso entre error de reconstrucción, fidelidad temporal/espectral y tiempo de aplicación.
4. Un análisis transparente de regímenes favorables, desfavorables y empates prácticos, sin lenguaje de dominancia universal.

No es admisible presentar como contribución:

- la invención de TRSS;
- una validación clínica;
- una superioridad general de GSP sobre métodos clásicos;
- un “límite teórico” derivado de búsqueda de hiperparámetros;
- una equivalencia estricta entre implementaciones externas no cerrada;
- la mera existencia de una gran cantidad de iteraciones exploratorias.

## 5. Pregunta central recomendada

> Under which missing-channel regimes does fixed graph–temporal regularization provide a practically relevant reconstruction advantage over MNE-Python spherical-spline interpolation, and what computational and spectral trade-offs accompany that advantage?

Esta pregunta es compatible con BSPC porque:

- se centra en procesamiento de una señal biomédica;
- exige una comparación controlada;
- produce una decisión metodológica;
- integra precisión, espectro y costo;
- no presupone superioridad ni relevancia clínica.

## 6. Riesgos de desk screening

| Riesgo | Severidad | Evidencia | Mitigación |
|---|---:|---|---|
| Contradicción entre datasets declarados y resultados fuente | Bloqueante | BCI IV 2a no está en los 300 pares actuales | Regenerar cohorte del paper o reducir explícitamente el alcance. |
| Resultados no congelados en control de versiones | Bloqueante | CSV principales ignorados por Git | Publicar paquete versionado con checksums y manifiesto. |
| Contribución percibida como benchmark incremental | Alta | Benchmarking no aparece explícitamente como categoría de alcance | Formular una pregunta metodológica única y una frontera práctica. |
| Claims heredados demasiado fuertes | Alta | Paper IEEE histórico | Redacción nueva y auditoría de términos prohibidos. |
| Figuras cualitativas sin identidad exacta con el benchmark | Alta | Generador usa un flujo de señal distinto | Regenerar desde arrays congelados. |
| Unidad estadística/pseudorreplicación | Alta | Máscaras y semillas anidadas en pocos sujetos | Agregar por sujeto/registro y usar bootstrap jerárquico. |
| Ablación temporal débil | Media/alta | Un sujeto por dataset y métricas sobre matriz completa | Recalcular sobre canales ocultos con coordenadas reales y análisis pareado. |
| Falta de comparación entrenable moderna | Media | Deep learning fuera del alcance | Justificar el alcance sin afirmar que el benchmark cubre todo el estado del arte. |
| Similaridad textual con tesis o paper IEEE | Media | Dos manuscritos previos en el repositorio | Escribir desde evidencia y estructura BSPC, no copiar párrafos. |
| Declaraciones editoriales incompletas | Media | Autoría, funding y CRediT pendientes | Crear checklist humano antes del envío. |
| Inglés o formato inconsistente | Baja durante auditoría | Manuscrito BSPC aún no creado | QA final con una sola variante de inglés y validadores automáticos. |

## 7. Recomendación de estructura BSPC

Estructura propuesta, después de cerrar el Gate 1 científico:

1. Introduction
2. Related work
3. Materials and methods
4. Experimental design
5. Results
6. Discussion
7. Conclusion
8. Declarations

Orden de redacción:

1. Materials and methods
2. Experimental design
3. Results
4. Related work
5. Introduction
6. Discussion
7. Conclusion
8. Abstract, keywords y highlights

Distribución orientativa para un manuscrito cercano a 5000 palabras:

- Introduction: 650–800;
- Related work: 450–600;
- Materials and methods: 1200–1400;
- Experimental design: 600–750;
- Results: 900–1100;
- Discussion: 800–1000;
- Conclusion: 200–300;
- declaraciones fuera o parcialmente fuera del conteo editorial, según plantilla.

Estos rangos son una guía de trabajo, no un requisito oficial por sección.

## 8. Paquete de envío previsto

Después de aprobar la auditoría científica se crearán:

- `Thesis-Copilot-Toolkit/paper/bspc/main.tex`;
- `paper/bspc/sections/01_introduction.tex`;
- `paper/bspc/sections/02_related_work.tex`;
- `paper/bspc/sections/03_materials_methods.tex`;
- `paper/bspc/sections/04_experimental_design.tex`;
- `paper/bspc/sections/05_results.tex`;
- `paper/bspc/sections/06_discussion.tex`;
- `paper/bspc/sections/07_conclusion.tex`;
- `paper/bspc/sections/08_declarations.tex`;
- `paper/bspc/bibliography/references.bib`;
- `paper/bspc/highlights.txt`;
- `paper/bspc/figures/`;
- `paper/bspc/tables/`;
- `paper/bspc/evidence/`;
- `paper/bspc/README.md`.

El paper IEEE se conservará sin modificaciones como artefacto histórico.

## 9. Checklist previo a autorizar la redacción de Results

- [ ] Cohorte del paper definida por dataset, sujeto, run y ventana.
- [ ] BCI IV 2a incluido realmente o retirado del alcance principal.
- [ ] Patrones y severidades fijados antes de ejecutar.
- [ ] TRSS fijo congelado antes de la evaluación.
- [ ] MNE ejecutado sobre las mismas señales y máscaras.
- [ ] Métricas calculadas solo en canales ocultos.
- [ ] Tiempo de aplicación separado del costo de calibración.
- [ ] Unidad estadística sujeto/registro definida.
- [ ] Bootstrap jerárquico y resúmenes pareados regenerados.
- [ ] Ablación temporal recalculada o retirada del paper.
- [ ] Casos temporales/PSD generados desde los arrays exactos.
- [ ] Resultados y configuración versionados con checksums.
- [ ] Matriz de claims actualizada a `verified`.

## 10. Decisión final de esta fase

BSPC sigue siendo la primera opción editorial razonable.

La recomendación es `GO condicional` para continuar con el reanálisis mínimo y la preparación del manuscrito, pero `NO-GO` para redactar Results o afirmar que el paper está listo.

El bloqueo inmediato es científico y de trazabilidad, no de formato editorial: reconciliar la cohorte y congelar el benchmark real-EEG principal.
