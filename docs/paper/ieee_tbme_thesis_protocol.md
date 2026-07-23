# Protocolo activo del manuscrito IEEE TBME basado en la tesis

Fecha: 2026-07-23  
Estado: manuscrito compilado y auditado visualmente.  
Reemplaza para esta iteración a `paper_core_v1_protocol.md`.

## 1. Identidad editorial

- Revista objetivo de trabajo: IEEE Transactions on Biomedical Engineering (TBME).
- Tipo: regular paper.
- Plantilla: `IEEEtran`, dos columnas, texto a espacio simple, figuras y tablas embebidas.
- Título: **Missing EEG Channel Reconstruction Using Graph Signal Processing With Temporal Regularization**.
- Idioma: inglés.
- Extensión objetivo: ocho páginas.

La elección de TBME es la interpretación operativa de la instrucción “revista IEEE, biomedical signal processing”. Si el autor selecciona otra revista IEEE, se revisarán alcance y límites antes de preparar la entrega.

## 2. Fuente principal y congelamiento de evidencia

La fuente narrativa, metodológica y cuantitativa principal es la tesis final ubicada en:

`Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/`

Esta iteración no ejecuta experimentos nuevos. Solo puede reutilizar:

- texto conceptual y metodológico de la tesis, reescrito como artículo;
- valores ya incluidos en la tesis final;
- tablas finales de la tesis;
- figuras finales de la tesis;
- referencias bibliográficas de la tesis después de comprobar su correspondencia con cada afirmación.

Queda prohibido combinar cifras de la tesis con `paper_core_v1`, resultados históricos archivados o nuevos cálculos. Los artefactos antiguos se conservan únicamente para auditoría.

## 3. Pregunta y alcance

Pregunta principal: ¿en qué regímenes de pérdida simulada de canales EEG una regularización espacio-temporal sobre grafos (TRSS) mejora la reconstrucción frente a la interpolación por splines esféricos de MNE-Python, y qué compromiso existe entre fidelidad de reconstrucción, preservación espectral y costo computacional?

El estudio se limita a:

- canales artificialmente ocultos con señal verdadera disponible;
- conjuntos públicos y escenarios descritos en la tesis;
- comparación pareada sobre la misma señal, máscara y semilla;
- interpretación descriptiva y condicional.

No constituye validación clínica ni evaluación sobre canales realmente dañados.

## 4. Métodos activos

- TRSS fijo como propuesta principal.
- MNE-Python spherical splines como referencia comunitaria.

Otros métodos y grafos pueden resumirse como etapa exploratoria de la tesis, pero no deben presentarse como comparadores confirmatorios si no aparecen en la evidencia final. Visibility/NNK no es un método activo y no debe aparecer en texto, tablas, captions ni figuras visibles.

## 5. Resultados autorizados

Los siguientes valores pueden usarse porque aparecen en las tablas finales de la tesis:

- mejora mediana de MAE de TRSS fijo frente a MNE: +12.4%, intervalo descriptivo al 95% [+7.8, +17.4], tasa de victoria 72.0%;
- mejora mediana de NRMSE: +13.9%, intervalo [+6.4, +19.3], tasa de victoria 70.3%;
- mejora mediana de DTW: +9.8%, intervalo [+5.5, +12.7], tasa de victoria 71.0%;
- LSD: -2.3%, intervalo [-4.0, -0.2], tasa de victoria 40.7%, favoreciendo a MNE en preservación espectral global;
- tiempo: -1004.1%, intervalo [-1072.8, -934.0], tasa de victoria 0.3%, indicando mayor costo de TRSS;
- medianas por caso: 0.1214 s para TRSS fijo y 0.0090 s para MNE.

Todo valor adicional debe rastrearse a una tabla o figura final de la tesis antes de incorporarse.

## 6. Incertidumbre y rigor

- Las máscaras no se interpretan como sujetos independientes.
- Se reportan medianas, IQR cuando estén disponibles, diferencias pareadas, tasas de victoria e intervalos descriptivos.
- La tesis no organiza sus conclusiones en torno a pruebas de hipótesis; el artículo debe describir honestamente esta decisión.
- TBME recomienda pruebas de hipótesis y valores p en comparaciones de métodos. Como no se harán nuevos análisis, esta ausencia se declarará como decisión/limitación y no se inventarán valores p.

## 7. Figuras y tablas

Se priorizan recursos ya incluidos en la tesis que:

1. sostienen un claim central;
2. conservan trazabilidad;
3. son legibles a una o dos columnas;
4. no duplican una tabla;
5. no contienen resultados incompatibles o Visibility/NNK.

Se permiten cambios editoriales no analíticos: traducción de rótulos, recorte de márgenes, redimensionamiento, remaquetación de tablas y exportación vectorial. Los datos subyacentes no pueden cambiar.

## 8. Claims prohibidos

- superioridad universal de TRSS;
- beneficio clínico demostrado;
- generalización a otros datasets, montajes, patologías o tareas posteriores;
- desempeño sobre canales realmente dañados;
- causalidad fisiológica;
- significación estadística no calculada;
- despliegue en tiempo real;
- resultados derivados de `paper_core_v1` presentados como parte de esta iteración.

## 9. Requisitos TBME verificados

Según las instrucciones oficiales consultadas el 2026-07-23:

- formato IEEE de doble columna;
- resumen estructurado menor de 250 palabras;
- figuras y tablas embebidas y legibles;
- conclusión menor de 300 palabras;
- ocho páginas esperadas para regular papers, con máximo de doce sin permiso especial;
- referencias numéricas IEEE;
- sin biografías.

Fuente: https://www.embs.org/tbme/prepare-a-manuscript/

## 10. Criterios de liberación

El PDF solo se considera candidato editorial cuando compila sin errores, no tiene referencias indefinidas ni desbordes visibles, todas sus páginas fueron revisadas visualmente y cada cifra cuantitativa fue contrastada con la tesis.

## 11. Registro de compilación y revisión

- Fuente: `Thesis-Copilot-Toolkit/paper/ieee_tbme/main.tex`.
- PDF: `Thesis-Copilot-Toolkit/paper/ieee_tbme/main.pdf`.
- Compilación final: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`, completada sin errores.
- Extensión compilada: cinco páginas IEEEtran a doble columna.
- Auditoría de log: sin `Overfull`, citas indefinidas, referencias indefinidas ni errores LaTeX.
- Revisión visual: cinco páginas renderizadas e inspeccionadas; no se observaron recortes, superposiciones ni elementos ilegibles.
- Ajustes visuales finales: margen adicional para el valor LSD negativo, rótulos abreviados en la figura por dataset y balance bibliográfico mediante `\IEEEtriggeratref{6}`.
- Verificación cuantitativa automática: 300 pares, 100 clústeres, mejora MAE de 12.4%, tasa de victoria de 72.0% e intervalo descriptivo [7.8, 17.4]% contrastados con `robust_pairwise_summary.csv`.
