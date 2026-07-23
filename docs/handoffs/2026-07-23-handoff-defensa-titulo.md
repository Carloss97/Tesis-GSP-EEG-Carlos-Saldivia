# Handoff — Presentación y narrativa para defensa de título

Fecha: 2026-07-23  
Repositorio: `/mnt/c/Users/sarlo/OneDrive/Escritorio/Proyectos/Tesis-GSP-EEG-Carlos-Saldivia`  
Rama observada: `main`

## Instrucción de inicio para la sesión nueva

Trabajar en español. Cargar antes de actuar:

- `academic-writing`;
- `document-productivity-workflows`.

Leer este handoff y el plan canónico:

- `.hermes/plans/2026-07-23_164629-presentacion-defensa-tesis-gsp-eeg.md`

No buscar ni resumir sesiones anteriores salvo que aparezca una contradicción que no pueda resolverse desde los archivos. Este handoff y el plan contienen el contexto operativo necesario.

No comenzar a editar hasta que el usuario indique explícitamente que se comience. Cuando lo haga, ejecutar el plan completo y verificar los entregables reales; no detenerse en un storyboard o borrador incompleto.

## Solicitud del usuario

Preparar dos entregables coordinados para su defensa de título:

1. Presentación formal en LaTeX Beamer, con figuras, títulos, secciones y punteo apropiado, para aproximadamente 30 minutos.
2. Documento paralelo con la narrativa oral por diapositiva, distribución de tiempos, motivaciones, razonamiento, justificación de decisiones y posibles preguntas/respuestas del comité.

La exposición debe presentar únicamente lo realmente alcanzado y permitir defender metodología, decisiones, resultados, validez, limitaciones y contribuciones.

## Estado actual

- El plan formal está terminado y aprobado por el usuario.
- No se ha creado `Thesis-Copilot-Toolkit/defensa/`.
- No existen aún `presentacion_defensa.tex` ni `narrativa_defensa.tex`.
- No se ha modificado la tesis, el paper ni sus figuras.
- No se ha compilado ningún material de defensa.
- El único archivo nuevo observado antes de este handoff era el plan en `.hermes/plans/`.
- No hacer commit ni push salvo solicitud expresa.

## Configuración Hermes preparada

La configuración persistente ya tenía:

- `model.context_length: 1050000`;
- `compression.enabled: true`;
- `compression.threshold: 0.70`;
- `compression.target_ratio: 0.15`.

Se aumentó solo:

- `compression.threshold: 0.75`.

La nueva sesión debe tomar esta configuración automáticamente. Respaldo:

`/home/sarlo/.hermes/backups/config-before-defense-context-20260723_170601.yaml`

Objetivo de costo: usar búsquedas y lecturas dirigidas, agrupar llamadas independientes, conservar una matriz de evidencia central y evitar releer documentos completos después de extraer claims canónicos.

## Fuente canónica y jerarquía

### 1. Tesis final — autoridad primaria

- `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/tesis_completa.tex`
- `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/tesis_completa.pdf`
- `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/chapters/`
- `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/tables/`
- `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/figures/`

Capítulos ya auditados en la sesión anterior:

- `frontmatter/abstract_es.tex`;
- `chapters/01_introduccion.tex`;
- `chapters/03_metodologia.tex`;
- `chapters/04_resultados.tex`;
- `chapters/05_discusion.tex`;
- `chapters/06_conclusiones.tex`.

### 2. Paper y documentación — fuentes secundarias

- `docs/paper/ieee_tbme_thesis_protocol.md`;
- `docs/paper/ieee_tbme_claim_evidence_matrix.md`;
- `Thesis-Copilot-Toolkit/paper/ieee_tbme/`;
- `Thesis-Copilot-Toolkit/paper/bspc/`;
- `docs/paper/claim_evidence_matrix.md`;
- `docs/paper/paper_core_v1_protocol.md`.

Precaución crítica: se detectó que `Thesis-Copilot-Toolkit/paper/ieee_tbme/main.tex` usa actualmente `elsarticle` y contenido asociado al benchmark nuevo, mientras que `docs/paper/ieee_tbme_*` describe un manuscrito derivado estrictamente de la tesis. No asumir que el nombre de carpeta identifica el protocolo. Auditar y etiquetar cada claim antes de usarlo. Ante cualquier conflicto, prevalece la tesis final.

## Regla científica principal

No mezclar como si fueran un solo protocolo:

1. exploración amplia de tres datasets, patrones, severidades y semillas;
2. trayectoria de 18 métodos y nueve estrategias de grafo;
3. reducción de candidatos;
4. comparación final pareada y congelada TRSS fijo–MNE;
5. campañas posteriores o históricas del paper.

La defensa debe declarar que la amplitud corresponde a exploración/selección y que las cifras principales provienen de la comparación final congelada.

Crear al inicio:

`Thesis-Copilot-Toolkit/defensa/qa/claim_evidence_defensa.md`

Campos mínimos:

- afirmación;
- cifra;
- protocolo;
- unidad estadística;
- fuente exacta;
- frase oral autorizada;
- limitación;
- pregunta probable.

## Cifras finales ya verificadas en tablas de tesis

Fuentes:

- `tables/ch6_robust_main.tex`;
- `tables/ch6_metric_portfolio.tex`;
- `tables/ch6_runtime_complexity.tex`;
- `tables/ch6_selected_scenarios_mae.tex`.

TRSS fijo frente a MNE:

- MAE: mejora mediana `+12,4%`, IC descriptivo `[+7,8; +17,4]`, victoria `72,0%`;
- NRMSE: `+13,9%`, IC `[+6,4; +19,3]`, victoria `70,3%`;
- DTW: `+9,8%`, victoria `71,0%`;
- SNR: `+3,7%`, victoria `61,0%`;
- LSD: `-2,3%`, IC `[-4,0; -0,2]`, victoria `40,7%`, favorece a MNE;
- correlación: `+0,8%`, victoria `68,7%`;
- tiempo: `-1004,1%`, victoria `0,3%`, favorece claramente a MNE.

Medianas observadas por caso:

- MNE spline: `0,0090 s`;
- TRSS fijo: `0,1214 s`;
- TRSS calibrado: `0,0845 s`.

Lectura defendible: TRSS presenta una ventaja condicionada en amplitud y forma temporal, especialmente en pérdidas agrupadas o periféricas severas; MNE conserva ventajas espectrales globales y de costo. No existe un ganador universal.

## Claims prohibidos o que requieren calificación

No afirmar:

- superioridad universal de TRSS;
- validación clínica;
- preservación fisiológica demostrada;
- mejora demostrada en clasificación BCI, ERP, conectividad o localización de fuentes;
- operación en tiempo real;
- generalización poblacional fuerte;
- significación estadística si no se calculó;
- que semillas o máscaras equivalen a sujetos independientes.

Usar “intervalos descriptivos”, “comparación pareada”, “evidencia condicionada” y “alcance de los datos evaluados”.

No mencionar Visibility/NNK en texto, slides, figuras, notas ni respaldo.

La portada debe usar: `Departamento de Electrónica`.

## Arquitectura aprobada

Argumento científico:

`problema → brecha → decisión metodológica → diseño controlado → evidencia → frontera práctica → aportes y límites`

Plan aprobado:

- 25 diapositivas principales;
- aproximadamente 29 minutos;
- 14 diapositivas de respaldo;
- narrativa inicial de 3.400–3.700 palabras;
- 30–40 preguntas del comité;
- respuestas breves de 20–30 s y ampliadas de 60–90 s.

El detalle slide por slide y los tiempos están en el plan canónico. No rediseñar la estructura sin una razón comprobable.

## Entregables y ubicación

Crear:

```text
Thesis-Copilot-Toolkit/defensa/
├── presentacion_defensa.tex
├── presentacion_defensa.pdf
├── narrativa_defensa.tex
├── narrativa_defensa.pdf
├── config/
├── figures/source/
├── figures/adapted/
├── tables/
├── qa/
├── previews/
└── README.md
```

Si la carpeta ya existe al iniciar, respaldarla primero bajo `docs/backups/` con timestamp. No editar figuras canónicas en sitio; copiar o redibujar únicamente en `defensa/figures/adapted/`.

## Figuras candidatas ya localizadas

En `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/figures/`:

- `ch2_gsp_concepts_clean.pdf`;
- `ch2_trss_operator.pdf`;
- `ch3_methodology_flow.pdf`;
- `ch3_architecture_blocks.pdf`;
- `ch4_traceability_pipeline.pdf`;
- `ch4_representative_timeseries.pdf`;
- `ch4_psd_original_vs_interpolated.pdf`;
- `ch6_robust_improvement_ci.pdf`;
- `ch6_metric_portfolio_improvement.pdf`;
- `ch6_scenario_heatmap_mae.pdf`;
- `ch6_runtime_mae_tradeoff.pdf`;
- `ch7_decision_map.pdf`.

Regla visual del usuario: nunca poner texto o leyendas sobre dibujos o datos; reservar espacio lateral/inferior y verificar cada figura de forma aislada y dentro de la página compilada.

## Primera secuencia de ejecución, cuando el usuario autorice

1. Verificar rama y estado Git actuales con alcance acotado.
2. Confirmar si `defensa/` existe; respaldar si corresponde.
3. Crear la matriz claim–evidence de defensa antes de redactar slides.
4. Auditar únicamente los fragmentos exactos necesarios de tesis/paper mediante búsquedas dirigidas.
5. Congelar storyboard de 25 slides y procedencia de cada visual.
6. Crear presentación y narrativa completas, no stubs.
7. Compilar con `latexmk`.
8. Auditar errores, referencias, citas y overfull boxes.
9. Renderizar todas las páginas; crear hojas de contacto e inspeccionar slide por slide.
10. Verificar texto extraído, cifras clave y ausencia de Visibility/NNK.
11. Ajustar tiempos y producir rutas abreviadas de 25 y 20 minutos.

## Gates de finalización

No declarar terminado hasta comprobar:

- ambos `.tex` compilan;
- existen ambos PDF;
- todas las cifras tienen fuente;
- exploración y comparación final están claramente separadas;
- se explica diseño pareado y unidad estadística;
- la conclusión responde P1/P2;
- las limitaciones aparecen explícitamente;
- todas las páginas fueron revisadas visualmente;
- no hay Visibility/NNK;
- la exposición cabe en 28:30–29:30;
- existe respaldo para preguntas técnicas.

## Prompt sugerido para la sesión nueva

`Lee docs/handoffs/2026-07-23-handoff-defensa-titulo.md y el plan canónico que referencia. Luego comienza la ejecución completa de la presentación y narrativa de defensa, siguiendo la jerarquía de evidencia, los respaldos y todos los gates de validación. Trabaja en español y no te detengas hasta compilar y verificar ambos entregables.`
