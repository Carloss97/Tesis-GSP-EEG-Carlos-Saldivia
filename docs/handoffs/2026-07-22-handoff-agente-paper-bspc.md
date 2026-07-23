# Handoff para agente de redacción académica — Paper BSPC

Fecha: 2026-07-22

## Propósito

Este documento permite iniciar una sesión nueva con un agente que tenga skills de redacción académica y continuar el trabajo de conversión de la tesis aprobada en un artículo publicable para *Biomedical Signal Processing and Control* (BSPC), reduciendo el riesgo de rechazo editorial inicial (*desk screening*).

No es un encargo para resumir la tesis ni para copiar el paper IEEE actual. Es un encargo de auditoría científica, reconciliación de resultados y redacción de un manuscrito nuevo, trazable y compatible con BSPC.

---

# Prompt para copiar en una sesión nueva

Carga obligatoriamente el skill `academic-writing` antes de trabajar. Si necesitas configurar o diagnosticar Hermes, carga también `hermes-agent`. Trabaja en español al comunicarte conmigo, pero el manuscrito destinado a BSPC debe escribirse en inglés académico.

## Contexto del proyecto

Estoy convirtiendo una tesis de magíster aprobada por mi supervisor en un artículo para una revista indexada. La primera opción editorial es *Biomedical Signal Processing and Control* (BSPC), de Elsevier.

Repositorio:

`/mnt/c/Users/sarlo/OneDrive/Escritorio/Proyectos/Tesis-GSP-EEG-Carlos-Saldivia`

Documento estratégico principal:

`docs/plans/2026-07-22-plan-tesis-a-paper-bspc.md`

Handoff actual:

`docs/handoffs/2026-07-22-handoff-agente-paper-bspc.md`

Tesis aprobada:

`Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/tesis_completa.tex`

PDF aprobado:

`Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/tesis_completa.pdf`

Paper IEEE histórico, que no debe reutilizarse automáticamente:

`Thesis-Copilot-Toolkit/paper/ieee/`

Reporte final del supervisor:

`Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/build_logs/REVISION_PROFESOR_GUIA_FINAL.md`

QA visual y de compilación de la tesis:

`Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/build_logs/FINAL_VISUAL_QA_REPORT.md`

Plan completo de trabajo:

`docs/plans/2026-07-22-plan-tesis-a-paper-bspc.md`

## Qué debes hacer primero

No redactes todavía el paper completo. Ejecuta primero una auditoría de contexto en este orden:

1. Lee el plan completo.
2. Lee este handoff.
3. Lee la tesis completa o, como mínimo, la introducción, metodología, resultados, discusión, conclusiones, tablas de resultados y `config/results_data.tex`.
4. Lee el reporte final del supervisor y el QA final.
5. Inspecciona `Thesis-Copilot-Toolkit/paper/ieee/` para identificar qué contenido puede rescatarse y qué debe descartarse.
6. Recupera, si es necesario, los handoffs históricos eliminados del árbol activo usando Git:
   - `.agent_work/PUBLICATION_STRATEGY_GUIDE.md`
   - `.agent_work/SESSION_COMPREHENSIVE_STATUS.md`
   - `.agent_work/FINAL_SESSION_REPORT.md`
   Estos archivos existen en el historial previo a la limpieza del repositorio; no asumas que están actualmente presentes.
7. Inspecciona los resultados y scripts reales antes de aceptar cualquier cifra del paper histórico.
8. Produce un informe de auditoría antes de modificar o crear el manuscrito.

## Objetivo científico del artículo

El artículo debe presentar una contribución metodológica/experimental, no afirmar que TRSS es un algoritmo completamente nuevo ni que existe superioridad universal.

Tesis editorial de trabajo:

> A rigorously controlled, multi-metric benchmark of missing-channel EEG reconstruction that compares graph/temporal regularization with a mature MNE-Python reference under reproducible random and spatially contiguous masking, with explicit reporting of the accuracy–spectral-fidelity–runtime trade-off.

Contribuciones admisibles, si los datos las respaldan:

1. Un protocolo pareado, reproducible y trazable para evaluar reconstrucción de canales EEG faltantes.
2. Una comparación justa entre métodos GSP/espacio-temporales, baselines geométricos y una referencia madura de MNE-Python.
3. Una caracterización condicional del compromiso entre error de reconstrucción, fidelidad temporal/espectral y costo computacional.

Conclusión esperada, siempre condicionada a la evidencia congelada:

- MNE-Python permanece como referencia operativa fuerte, rápida y robusta.
- TRSS puede ser útil en regímenes de pérdida espacial difícil, especialmente cuando la vecindad local es insuficiente y se acepta procesamiento fuera de línea.
- No debe recomendarse TRSS como sustituto universal ni presentarse como validación clínica.

## Reglas científicas no negociables

- No inventes cifras, resultados, datasets, sujetos, referencias, DOI ni claims.
- No copies automáticamente el paper IEEE actual.
- No mezcles resultados históricos, exploratorios, proxies, normalizados y no normalizados.
- No uses una cifra hasta poder vincularla a CSV/JSON/figura, script, configuración y commit.
- No confundas iteraciones, ventanas, ensayos, sujetos, estratos ni casos pareados.
- No copies una tabla de la tesis manualmente: recalcula o verifica contra la fuente.
- No conviertas resultados exploratorios en evidencia confirmatoria.
- Mantén la tesis aprobada como límite de lo que puede afirmarse.
- Todo reanálisis posterior debe declararse como reanálisis y quedar separado de los resultados finales de la tesis.
- Las pruebas de hipótesis son auxiliares; prioriza diferencias pareadas, medianas/IQR, tasas de victoria e intervalos de incertidumbre cuando corresponda.
- No uses “clinical validation”, “clinical-grade”, “physiologically proven”, “state of the art”, “theoretical ceiling”, “statistically significant margins” o expresiones equivalentes salvo que exista evidencia directa y verificable.
- No uses lenguaje de superioridad universal.
- Visibility/NNK no pertenece al relato final activo y no debe aparecer en el manuscrito, captions, tablas, anexos ni artefactos visibles.
- No menciones rutas locales, nombres internos de archivos, iteraciones de desarrollo ni detalles de handoff en el paper.
- Si existe una contradicción entre la tesis, el paper histórico y los resultados fuente, detente y reporta la contradicción; no la resuelvas inventando.

## Inconsistencias conocidas que debes resolver

Antes de escribir Results, audita especialmente:

1. La tesis describe tres datasets: PhysioNet, BCI Competition IV 2a y MNE Sample.
2. La tesis describe 120 escenarios en un protocolo: 3 datasets × 2 modos × 4 severidades × 5 semillas.
3. La metodología también describe una validación comparativa independiente con 100 estratos y 300 casos pareados.
4. El paper IEEE histórico mezcla ratios 10–40%, conteos de canales 1–3, iteraciones, resultados de ablación y afirmaciones estadísticas de distintas campañas.
5. Existen handoffs históricos con conclusiones divergentes sobre la contribución temporal de TRSS. La ablación debe verificarse desde sus CSV/JSON finales; no elijas la narrativa más favorable.
6. Las comparaciones Python–MATLAB/GSPBox que tengan estado `proxy_or_partial` o `strict_close=False` deben reportarse como parciales, nunca como equivalencia estricta.

Tu primer entregable debe ser una matriz con estas columnas:

`claim | value | unit | dataset | protocol | statistical unit | source artifact | generating script | config | commit | status | allowed wording`

Clasifica cada afirmación como:

- `verified`: puede entrar en el manuscrito;
- `needs_recalculation`: requiere regeneración o comprobación;
- `exploratory_only`: solo puede aparecer como contexto metodológico;
- `unsupported`: no debe aparecer.

## Encaje editorial BSPC

Usa como fuente oficial vigente:

https://www.sciencedirect.com/journal/biomedical-signal-processing-and-control/publish/guide-for-authors

El manuscrito debe prepararse como full paper original, aproximadamente 5.000 palabras, sujeto a la guía vigente.

Requisitos editoriales que deben verificarse:

- abstract factual de menos de 250 palabras;
- 1–7 keywords en inglés;
- 3–5 highlights en archivo separado, cada uno de máximo 85 caracteres incluyendo espacios;
- graphical abstract opcional, preferible si se puede hacer de manera reproducible y no engañosa;
- fuentes editables LaTeX y archivos de figuras/tablas;
- secciones numeradas y referencias cruzadas consistentes;
- figuras separadas, legibles y con captions autoexplicativos;
- tablas editables, sin duplicación innecesaria de figuras;
- referencias numeradas, consistentes y con metadatos/DOI comprobados;
- data availability statement;
- code availability statement cuando corresponda;
- funding, competing interests, CRediT y declaración de uso de IA generativa cuando corresponda;
- autoría, orden, afiliaciones y autor corresponsal aprobados por todos los autores;
- declaración correcta sobre la relación con la tesis previa y ausencia de envío simultáneo.

## Qué significa ATS en este proyecto

Cuando digo “ATS”, me refiero a *desk screening* o evaluación editorial inicial, no a un sistema de selección laboral.

El objetivo es reducir el riesgo de rechazo editorial inicial por:

- falta de encaje con BSPC;
- contribución poco clara o exagerada;
- contradicciones numéricas;
- claims clínicos no sustentados;
- baja reproducibilidad;
- formato incorrecto;
- abstract/keywords/highlights defectuosos;
- idioma deficiente;
- referencias incompletas;
- figuras ilegibles;
- similitud textual o publicación redundante con la tesis;
- archivos incompletos o declaraciones ausentes.

No intentes evadir verificadores. Redacta de forma original, transparente, científicamente trazable y conforme a las políticas editoriales.

## Secuencia de ejecución requerida

### Fase 1 — Auditoría y tabla maestra

No escribir Results hasta terminar la reconciliación de cifras.

Entregables:

- `docs/paper/claim_evidence_matrix.*`
- `docs/paper/result_protocol_audit.md`
- `docs/paper/editorial_fit_bspc.md`
- decisión explícita sobre cuál protocolo será principal;
- lista de resultados no utilizables.

### Fase 2 — Reanálisis mínimo, solo si se detectan brechas

Reproducir desde resultados congelados:

- TRSS fijo vs MNE-Python;
- resultados por patrón y severidad;
- runtime de aplicación y costo de calibración por separado;
- ablación TRSS completo vs sin término temporal;
- sensibilidad de hiperparámetros;
- ejemplos temporales y PSD con regla de selección predefinida.

No añadir deep learning únicamente para parecer más actual. No abrir una campaña ilimitada.

### Fase 3 — Crear manuscrito BSPC separado

Crear:

`Thesis-Copilot-Toolkit/paper/bspc/`

Estructura inicial sugerida:

- `main.tex`
- `sections/01_introduction.tex`
- `sections/02_related_work.tex`
- `sections/03_materials_methods.tex`
- `sections/04_experimental_design.tex`
- `sections/05_results.tex`
- `sections/06_discussion.tex`
- `sections/07_conclusion.tex`
- `sections/08_declarations.tex`
- `bibliography/references.bib`
- `highlights.txt`
- `figures/`
- `tables/`
- `README.md`

El paper IEEE debe conservarse como histórico. Puede servir para localizar recursos, pero no como fuente automática de texto o cifras.

### Fase 4 — Redacción

Escribe en este orden:

1. Materials and Methods.
2. Experimental Design.
3. Results.
4. Related Work.
5. Introduction.
6. Discussion.
7. Conclusion.
8. Abstract y Highlights al final.

El artículo no debe parecer una tesis reducida. Debe tener una única pregunta central, pocas figuras de alta información y una conclusión condicional.

### Fase 5 — QA de desk screening

Antes de decir que está listo:

- compila LaTeX;
- revisa citas, labels y referencias cruzadas;
- comprueba que no existan cifras sin fuente;
- compara texto y tablas con los artefactos fuente;
- inspecciona cada figura individualmente y el PDF completo;
- cuenta palabras, abstract, keywords y caracteres de highlights;
- comprueba que las figuras sean legibles y accesibles;
- busca términos prohibidos o claims no respaldados;
- busca Visibility/NNK en fuentes y PDF extraído;
- busca rutas locales y nombres de archivos internos;
- verifica consistencia de inglés americano o británico;
- verifica la matriz de declaraciones editoriales;
- redacta una evaluación simulada de desk screening con riesgos restantes.

## Entregables de la primera sesión nueva

No afirmes que el paper está listo después de una sola lectura. La primera sesión debe producir:

1. Informe de auditoría del repositorio.
2. Matriz de evidencia y claims.
3. Lista de contradicciones y decisiones pendientes.
4. Diagnóstico de encaje BSPC.
5. Recomendación del protocolo principal.
6. Plan de archivos a crear/modificar.
7. Solo después de aprobar esa auditoría: esquema detallado y comienzo de Methods/Results.

## Cómo reportar incertidumbre

Usa explícitamente estas etiquetas:

- `Confirmado por fuente`;
- `Requiere recalculo`;
- `Solo exploratorio`;
- `No publicable sin nueva evidencia`;
- `Decisión editorial pendiente`.

Nunca conviertas una inferencia en un hecho.

---

# Estado de Hermes y error observado

En una sesión previa apareció:

```text
Invalid API response (attempt 1/1): response.status=failed: Responses API returned status 'failed'
Provider: model=gpt-5.6-luna
Provider message: Unknown
Max retries (1) exceeded for invalid responses
```

Esto debe tratarse como un fallo de transporte/proveedor o de compatibilidad de la Responses API, no como un fallo científico del proyecto.

Si vuelve a ocurrir:

1. Ejecuta `hermes doctor`.
2. Comprueba configuración con `hermes config check`.
3. Revisa proveedor/modelo/base URL sin exponer secretos.
4. Ejecuta una consulta mínima con el mismo proveedor para distinguir fallo general de fallo del prompt.
5. Reduce el tamaño inicial del prompt: carga el handoff como archivo y referencia las rutas, en lugar de pegar tesis completas en el mensaje.
6. Inicia la sesión nueva con el skill académico explícito:

```bash
hermes -s academic-writing
```

7. Si el modelo `gpt-5.6-luna` sigue fallando, cambia temporalmente a un modelo/proveedor compatible con la Responses API configurada y conserva el mismo handoff.
8. Reinicia Hermes después de cambios de proveedor/configuración; las herramientas y skills se aplican correctamente en una sesión nueva.
9. No reintentes indefinidamente la misma solicitud grande: el error indica que el proveedor devolvió `failed` y Hermes agotó el único reintento configurado.

No incluy API keys, tokens, contenido de `.env` ni datos personales en informes o handoffs.

---

# Criterio de finalización del proyecto

El proyecto no se considera listo porque el PDF compile. Está listo para envío solo cuando:

- los resultados principales estén congelados y trazados;
- las contradicciones estén resueltas;
- el manuscrito no contradiga la tesis aprobada;
- BSPC sea un encaje explícito;
- el abstract, highlights, keywords, figuras, tablas y referencias cumplan la guía;
- las limitaciones estén claramente expresadas;
- el paper no contenga claims clínicos no evaluados;
- supervisor y autores hayan aprobado contenido, orden y declaraciones;
- exista un paquete editable completo y una carta de presentación;
- la evaluación simulada de desk screening no detecte un bloqueo conocido.
