# Revisión visual y refuerzo de figuras — tesis completa

## Alcance

Se revisó `tesis_completa.tex` con foco en la calidad visual de la tesis completa, no solo en `tesis_caps_1_5.tex`. La pasada priorizó figuras que aportan información conceptual o comparativa adicional y evitó agregar gráficos decorativos.

## Brechas detectadas

1. Los capítulos teóricos y metodológicos tenían muy pocas figuras explicativas frente a la densidad conceptual del texto.
2. La figura GSP original del Capítulo 2 tenía un panel de espectro del Laplaciano con riesgo de superposición de etiquetas en el eje $\lambda_k$.
3. La relación entre problema, métodos, evaluación y decisión práctica quedaba principalmente textual en la introducción.
4. La metodología y el diseño experimental no tenían una visualización compacta de flujo, estratificación e inferencia pareada.
5. La arquitectura de trazabilidad estaba descrita en texto y tablas, pero no como cadena visual verificable.
6. En resultados faltaba una visualización integrada del portafolio completo de métricas TRSS--MNE.
7. La discusión tenía una tabla de decisión, pero no una figura que mostrara la frontera práctica entre MNE y TRSS.

## Figuras añadidas o reemplazadas

- `figures/ch1_thesis_roadmap.pdf`: mapa lógico de la tesis.
- `figures/ch2_gsp_concepts_clean.pdf`: reemplazo de la figura GSP con panel del espectro del Laplaciano corregido.
- `figures/ch2_trss_operator.pdf`: descomposición conceptual del operador TRSS.
- `figures/ch3_methodology_flow.pdf`: flujo metodológico de evaluación.
- `figures/ch4_traceability_pipeline.pdf`: cadena de trazabilidad experimental.
- `figures/ch5_experimental_design_matrix.pdf`: matriz conceptual del diseño experimental e inferencia pareada.
- `figures/ch6_metric_portfolio_improvement.pdf`: visualización integrada de métricas confirmatorias TRSS vs MNE.
- `figures/ch7_decision_map.pdf`: mapa de decisión práctica MNE--TRSS.

El script reproducible correspondiente es:

- `scripts/generate_additional_figures.py`

También se mantuvo y actualizó:

- `scripts/generate_ch6_artifacts.py`

## Correcciones adicionales de texto y tablas

- Se moderó la descripción de resultados ERP en la estructura de la tesis: ahora se habla de visualizaciones temporales representativas y PSD, no de prueba cuantitativa formal de componentes ERP.
- Se reformuló la explicación de TRSS para indicar que la interacción espacio--temporal se evalúa empíricamente mediante ablación, evitando afirmar sinergia como hecho teórico previo.
- Se cambió la limitación de MNE en la tabla de familias desde “colapso” a “pierde precisión”, más académico y defendible.
- Se corrigieron tablas/fragmentos que producían overfull hboxes >10pt.

## Validación

Comandos ejecutados:

```bash
python3 scripts/validate_thesis.py
latexmk -pdf -interaction=nonstopmode tesis_completa.tex
```

Resultado final de `tesis_completa.tex`:

- PDF generado: `tesis_completa.pdf`
- Páginas: 80
- Tamaño: 1,607,440 bytes
- Errores LaTeX: 0
- Citas indefinidas: 0
- Referencias indefinidas: 0
- Overfull hboxes totales: 3
- Overfull hboxes >10pt: 0
- Figuras usadas por validación estática: 18
- Labels: 54

## Revisión simulada

### Revisor 1 — Técnico/estadístico

Fortalezas:
- Mejor separación entre fase exploratoria y fase confirmatoria.
- Mayor trazabilidad visual entre diseño, datos, métricas y evidencia.
- La visualización del portafolio de métricas evita seleccionar solo resultados favorables.
- La corrección del lenguaje alrededor de TRSS/MNE reduce riesgo de sobreafirmación.

Observaciones menores:
- Sigue siendo recomendable, como trabajo futuro, una prueba formal de equivalencia si se desea sostener equivalencia estadística; el texto actual evita esa afirmación.
- La preservación ERP queda tratada como evidencia morfológica cualitativa, no como análisis clínico formal de componentes.

Calificación estimada: 94--96/100.

### Revisor 2 — Redacción, estructura e impacto

Fortalezas:
- La tesis ahora es más visual y legible: cada capítulo central tiene una figura que cumple una función específica.
- La introducción gana una figura de ruta lógica que ayuda a orientar al lector.
- El Capítulo 2 mejora sustancialmente al reemplazar la figura superpuesta y añadir el operador TRSS.
- La discusión termina con una frontera práctica entre MNE y TRSS, más útil que una afirmación de dominancia.

Observaciones menores:
- Conviene una revisión visual humana del PDF final para confirmar ubicación de flotantes y saltos de página.
- El documento pasó de 73 a 80 páginas por el refuerzo visual; esto es aceptable para una tesis, pero debe revisarse según normas internas de extensión si existieran.

Calificación estimada: 95/100.
