# Desk screening BSPC y auditoría tesis→manuscrito

Fecha: 2026-07-23  
Manuscrito activo: `Thesis-Copilot-Toolkit/paper/ieee_tbme/`  
Revista objetivo: *Biomedical Signal Processing and Control* (BSPC)  
Dictamen antes de revisión: **NO-GO para envío; GO para revisión interna controlada por evidencia**.

## 1. Alcance y jerarquía documental

La evaluación contrasta el manuscrito con:

1. la tesis final en `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/`;
2. `docs/paper/ieee_tbme_thesis_protocol.md`, que declara en su línea 5 que reemplaza el protocolo `paper_core_v1` para esta iteración;
3. `docs/paper/ieee_tbme_claim_evidence_matrix.md`;
4. tablas finales de la tesis, especialmente `ch6_robust_main.tex`, `ch6_metric_portfolio.tex`, `ch6_selected_scenarios_mae.tex` y `ch6_runtime_complexity.tex`;
5. los CSV congelados que reproducen esas tablas, utilizados solo como control de consistencia;
6. los requisitos oficiales vigentes de BSPC consultados el 2026-07-23.

`docs/paper/result_protocol_audit.md` se conserva como antecedente. Su gate abierto no gobierna esta iteración porque el protocolo activo posterior autoriza expresamente la reutilización de los valores que quedaron incorporados en las tablas finales de la tesis. No se incorporarán resultados exclusivos de `paper_core_v1`, experimentos nuevos ni cifras que no aparezcan en la tesis final.

## 2. Dictamen editorial

El núcleo científico es compatible con el alcance de BSPC: reconstrucción de señales biomédicas, procesamiento espacio-temporal y evaluación comparativa de un método determinista. El artículo no está listo para envío por cuatro causas bloqueantes:

1. **Formato editorial incorrecto.** `main.tex:1` usa `IEEEtran`, con dos columnas, secciones romanas, `Index Terms` y bibliografía IEEE. BSPC es una revista Elsevier y requiere una entrega editable compatible con su flujo.
2. **Extensión insuficiente.** El cuerpo sustantivo contiene aproximadamente 1.920 palabras, lejos de la referencia de unas 5.000 palabras para un full paper de BSPC. Métodos, material de evaluación, análisis de incertidumbre, literatura y discusión están demasiado comprimidos para una evaluación reproducible.
3. **Envoltura editorial incompleta.** Faltan highlights, declaración de conflictos, financiación, disponibilidad de datos/código, contribuciones CRediT y una declaración de uso de IA aplicable. La afiliación está resuelta como nota al pie IEEE.
4. **Trazabilidad editorial no expuesta.** Las cifras sí coinciden con las tablas finales de la tesis, pero el manuscrito no explica de forma suficiente la unidad pareada, el remuestreo por escenario, la composición exacta del benchmark y los límites de generalización.

Estos defectos son corregibles sin ejecutar nuevos experimentos.

## 3. Auditoría de evidencia

### 3.1. Consistencia numérica confirmada

La comprobación automatizada de `derived_balanced.csv` y `robust_pairwise_summary.csv` confirmó:

- 300 casos para `trss_default`;
- 300 claves pareadas únicas;
- 100 clústeres definidos por etiqueta de datos × patrón de pérdida × nivel de pérdida;
- MAE: +12,4% de mejora mediana, intervalo descriptivo [7,8; 17,4]%, 72,0% de victorias;
- NRMSE: +13,9%, intervalo [6,4; 19,3]%, 70,3% de victorias;
- DTW: +9,8%, intervalo [5,5; 12,7]%, 71,0% de victorias;
- LSD: −2,3%, intervalo [−4,0; −0,2]%, 40,7% de victorias;
- tiempo: −1004,1%, intervalo [−1072,8; −934,0]%, 0,3% de victorias.

Los valores coinciden con `ch6_robust_main.tex` y `ch6_metric_portfolio.tex`. Las medianas de tiempo de `ch6_runtime_complexity.tex` son 0,1214 s/caso para TRSS fijo y 0,0090 s/caso para MNE.

### 3.2. Límites obligatorios

- Las cinco etiquetas no son cinco cohortes independientes: son dos controles sintéticos, dos registros PhysioNet y un segmento MNE Sample.
- Las 300 máscaras no son 300 participantes.
- Los intervalos describen los casos observados y respetan clústeres de escenario; no demuestran generalización poblacional.
- El ocultamiento artificial ofrece verdad de referencia, pero no equivale a electrodos naturalmente dañados.
- El benchmark no valida diagnóstico, BCI, ERP, conectividad, localización de fuentes ni uso clínico.
- LSD favorece a MNE en el resumen agregado; una mejora de MAE no implica preservación universal de propiedades espectrales.
- Los tiempos dependen de hardware, implementación y longitud de segmento; no autorizan afirmar tiempo real.
- El script estadístico contiene pruebas de Wilcoxon y corrección BH, pero el protocolo activo prohíbe presentar significación no reportada en la tesis. El paper conservará un marco descriptivo y no importará esos valores p.
- Visibility/NNK no forma parte del método final y no debe aparecer en texto, tablas, captions ni figuras visibles.

### 3.3. Riesgo de reproducibilidad

Los artefactos principales bajo `Thesis-Copilot-Toolkit/results/` están ignorados por Git. Para esta primera revisión se mantendrá una declaración conservadora de disponibilidad y se añadirá un manifiesto versionable con rutas, roles y SHA-256 de las fuentes numéricas exactas, sin afirmar que existe todavía un repositorio público o un paquete de replicación completo.

## 4. Evaluación por sección

### Título y resumen

Fortalezas:

- el título identifica problema, dominio y enfoque;
- el resumen contiene el comparador, el diseño pareado, el resultado principal y el compromiso de costo;
- evita claims clínicos.

Deficiencias:

- la redacción está optimizada para IEEE y debe adaptarse a Elsevier;
- la composición del benchmark necesita diferenciar explícitamente controles sintéticos de registros EEG;
- la frase de 13,5 veces más rápido debe anclarse a las dos medianas y declararse dependiente de implementación;
- debe mantenerse por debajo de 250 palabras.

### Introducción

Deficiencias:

- revisión de antecedentes demasiado breve;
- hueco de conocimiento poco desarrollado frente a RBF, métodos de aprendizaje profundo, superresolución espacial y reconstrucción dinámica sobre grafos;
- la frase “new synthesis of the frozen thesis evidence” es documentación de procedencia, no una contribución científica para el lector de BSPC;
- la contribución debe formularse como método, benchmark pareado y regla de decisión condicionada, sin vender la tesis como novedad editorial.

### Trabajos relacionados

Deficiencias:

- 235 palabras y un repertorio bibliográfico muy reducido;
- no sitúa suficientemente los enfoques aprendidos ya presentes en la bibliografía;
- no separa interpolación geométrica, modelos aprendidos y métodos GSP dinámicos;
- debe distinguir reconstrucción de canales de detección de canales malos y de generación EEG.

### Materiales y métodos

Deficiencias críticas:

- no explica suficientemente la procedencia y selección de los dos registros PhysioNet y el segmento MNE Sample;
- no presenta una tabla compacta de los cinco estratos;
- la construcción del grafo, normalización, operador temporal, resolvedor y criterios de parada requieren mayor detalle trazable a la tesis/código;
- el diseño 5 × 4 × 5 × 3 = 300 y los 100 clústeres deben quedar explícitos;
- debe explicar por qué las métricas se calculan solo en canales ocultos;
- debe distinguir métricas “menor es mejor” y “mayor es mejor” y definir la mejora relativa;
- el bootstrap debe describirse como descriptivo y agrupado por escenario;
- deben declararse hardware/software únicamente si están registrados en la tesis.

### Resultados

Fortalezas:

- cifras centrales consistentes con la tesis;
- incluye heterogeneidad, excepción espectral y costo.

Deficiencias:

- exceso de cifras en una única tabla estrecha;
- escasa interpretación de los intervalos y de la variabilidad por estrato;
- deben separarse resultado principal, portafolio de métricas, heterogeneidad y costo;
- los controles sintéticos deben llamarse controles y no “datasets” independientes;
- no usar valores p generados fuera del marco final de la tesis.

### Discusión y conclusión

Fortalezas:

- reconoce no dominancia, costo, tamaño reducido de la muestra real y diferencia entre ocultamiento artificial y fallas naturales.

Deficiencias:

- falta contrastar con métodos alternativos y aclarar por qué no se compararon modelos aprendidos;
- la regla de decisión práctica es la contribución editorial más defendible y debe ocupar un lugar central;
- debe distinguir aplicabilidad offline de despliegue en tiempo real;
- la conclusión debe responder la pregunta principal sin repetir todos los números.

## 5. Compilación y QA visual base

Comandos ejecutados:

- `latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex`: código de salida 0;
- inspección de `main.pdf` con PyMuPDF 1.26.7 en modo de solo lectura.

Estado base:

- 5 páginas Letter, 612 × 792 pt;
- sin errores LaTeX, citas indefinidas, referencias indefinidas ni cajas `Overfull`;
- avisos `Underfull` menores;
- sin bloques detectados fuera de la caja de página;
- sin cortes ni solapamientos visibles.

Problemas visuales observados:

- identidad IEEE impropia para BSPC;
- resumen denso y afiliación muy pequeña;
- tablas legibles pero con tipografía reducida;
- flujo interrumpido por flotantes en las páginas 3–4;
- una línea huérfana bajo la figura de costo;
- conclusión partida con solo tres líneas en la página 5;
- aproximadamente dos tercios de la última página vacíos.

## 6. Plan de corrección aprobado por evidencia

1. Migrar `main.tex` a `elsarticle` en modo preprint y bibliografía numérica Elsevier.
2. Conservar el directorio activo `paper/ieee_tbme`, documentando que BSPC es el destino.
3. Reescribir y ampliar Introducción/Related Work con literatura verificada y claims acotados.
4. Ampliar Materials and Methods: datos, diseño 300/100, formulación, comparador, métricas e incertidumbre descriptiva.
5. Reorganizar Results para separar resultado primario, portafolio, heterogeneidad y costo.
6. Fortalecer Discussion alrededor de una regla de decisión metodológica y limitaciones explícitas.
7. Añadir highlights y declaraciones editoriales conservadoras.
8. Crear un manifiesto SHA-256 versionable de las fuentes de evidencia utilizadas.
9. Recompilar, auditar log, comprobar referencias y revisar visualmente todas las páginas.

## 7. Criterio de liberación de este borrador

El borrador podrá remitirse al profesor, pero no considerarse listo para envío, cuando:

- compile sin errores ni referencias indefinidas;
- abstract, keywords y highlights cumplan los límites BSPC;
- cada cifra cuantitativa tenga fuente en la tesis final;
- no incluya resultados de `paper_core_v1` ni valores p no autorizados;
- las declaraciones editoriales no prometan disponibilidad inexistente;
- todas las páginas y recursos visuales sean legibles en el PDF final.
