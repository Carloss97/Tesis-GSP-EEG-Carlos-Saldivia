# Segunda revisión editorial y desk screening BSPC

Fecha: 2026-07-23  
Manuscrito: `Thesis-Copilot-Toolkit/paper/ieee_tbme/`  
Revista objetivo: *Biomedical Signal Processing and Control* (BSPC)

## 1. Dictamen ejecutivo

- **Para revisión del profesor supervisor:** **GO**.
- **Mérito científico para superar desk screening:** **PASS CONDICIONADO, con riesgo moderado**.
- **Envío del PDF en su estado actual:** **NO-GO FORMAL**.

El artículo ya satisface alcance, formato, extensión aproximada, estructura científica, trazabilidad numérica y presentación visual. Los dos bloqueos formales actuales son:

1. la declaración de financiación conserva una instrucción roja visible en `sections/07_declarations.tex:9-11`;
2. el bloque de autores no identifica autor de correspondencia ni correo electrónico (`main.tex:36-40`).

Una vez resueltos esos metadatos, el manuscrito tiene una base razonable para pasar a revisión externa. El riesgo científico de rechazo editorial no desaparece: la validación real comprende solo dos registros EEGMMIDB y una ventana MNE Sample, y la comparación experimental ejecutada incluye un único baseline, spherical splines.

## 2. Resultado por criterio

| Criterio | Estado | Evaluación |
|---|---|---|
| Alcance BSPC | **PASS** | Reconstrucción de canales EEG, procesamiento espacio-temporal y evaluación de señales biomédicas encajan en la revista. |
| Título | **PASS** | El título ya no usa “benchmark”; “controlled paired evaluation” describe mejor una comparación de dos métodos (`main.tex:34`). |
| Abstract/keywords/highlights | **PASS** | Abstract de 216 palabras, 5 keywords y 5 highlights de 67–73 caracteres. |
| Extensión | **PASS** | Recuento aproximado de 4.932 palabras incluyendo abstract y declaraciones, cercano a la referencia de unas 5.000 palabras. |
| Pregunta y contribución | **PASS** | Las tres preguntas y el aporte orientado a decisión están explícitos (`01_introduction.tex:10-20`). |
| Novedad/impacto | **CONDITIONAL** | La contribución principal es una evaluación emparejada y una regla de selección, no un algoritmo completamente nuevo. Puede considerarse incremental por un editor estricto. |
| Material de evaluación | **CONDITIONAL** | El diseño 5 × 5 × 4 × 3 = 300 y los 100 clústeres están claros (`03_methods.tex:68-79`), pero solo hay tres estratos reales y no equivalen a una cohorte. |
| Comparador | **CONDITIONAL** | Spherical splines es un baseline práctico y pertinente (`03_methods.tex:40-42`), pero RBF, matrix completion, modelos aprendidos y source-informed no fueron ejecutados (`05_discussion.tex:62`). |
| Estadística/estimandos | **PASS** | Endpoint primario, mejora pareada, win rate y bootstrap por 100 clústeres están definidos; no se presentan p-values (`03_methods.tex:81-100`). |
| Trazabilidad/reproducibilidad | **PASS** | Las tablas y figuras derivan de artefactos congelados; el manifiesto SHA-256 valida 14/14 archivos (`03_methods.tex:102-104`). |
| Generalización y claims | **PASS** | El artículo niega explícitamente generalización clínica, demográfica y poblacional (`05_discussion.tex:56-66`; `06_conclusion.tex:4-6`). |
| Literatura | **PASS CONDICIONADO** | Se distinguen interpolación geométrica, GSP temporal y alternativas aprendidas/source-informed (`02_related_work.tex:4-24`). La cobertura es suficiente para desk screening, aunque modesta para peer review. |
| Autoría | **PASS PARCIAL** | Alejandro Weinstein figura como segundo autor y afiliado a USM (`main.tex:36-40`). Falta correspondencia/email. |
| Conflictos | **PASS** | Declaración estándar de ausencia de intereses (`07_declarations.tex:13-15`). |
| CRediT | **PASS CON CONFIRMACIÓN** | Roles asignados a Carlos Saldivia y Alejandro Weinstein (`07_declarations.tex:17-19`); deben ser aprobados por ambos autores antes del envío. |
| Financiación | **BLOCKER** | Permanece pendiente por indicación del autor (`07_declarations.tex:9-11`). |
| Declaración de IA | **PASS** | Declara herramienta, alcance, revisión humana y responsabilidad autoral (`07_declarations.tex:21-23`). |
| Compilación/maquetación | **PASS** | PDF de 22 páginas; 0 errores, advertencias, referencias/citas indefinidas y cajas over/underfull; QA visual final aprobado. |

## 3. Evaluación de la sección 3.4

La objeción de formato quedó resuelta.

- La sección se denomina “Spherical-spline comparator” (`03_methods.tex:40`).
- Describe el procedimiento, coordenadas, montaje, canales ocultos y restauración de muestras observadas (`03_methods.tex:42`).
- MNE-Python se identifica como implementación y se cita; no se usa una llamada de API como explicación metodológica principal.
- El PDF y las fuentes contienen 0 apariciones de `Raw.interpolate_bads` y 0 de `method=spline`.

## 4. Riesgos reales de desk rejection

### 4.1. Validación real reducida — riesgo alto

El principal riesgo es la externalidad: dos registros EEGMMIDB y una ventana MNE Sample (`03_methods.tex:48`; `05_discussion.tex:58`). Las 300 máscaras aumentan cobertura de condiciones, no el número de sujetos. Un editor puede decidir que la evidencia biomédica es insuficiente para una revista aplicada, aunque el manuscrito lo declare correctamente.

### 4.2. Un solo baseline ejecutado — riesgo medio/alto

La comparación directa está limitada a MNE spherical splines. Es defendible por relevancia práctica y por el objetivo training-free, pero no demuestra superioridad frente al conjunto de métodos modernos. El texto evita esa sobreafirmación (`02_related_work.tex:16-24`; `05_discussion.tex:62`).

### 4.3. Novedad principalmente evaluativa — riesgo medio

TRSS adopta una estructura Sobolev espacio-temporal previa y el aporte más fuerte es la evaluación emparejada, la identificación de regímenes adversos y la regla condicional. Este encuadre es honesto, pero un editor que exija novedad algorítmica podría rechazarlo sin revisión.

### 4.4. Datos derivados no archivados públicamente — riesgo medio/bajo

El manuscrito no promete un repositorio inexistente y ofrece los archivos derivados bajo solicitud (`07_declarations.tex:5-7`). Esto es editorialmente conservador, aunque un paquete de replicación público fortalecería el envío.

## 5. Aspectos que previsiblemente pasarían a peer review

No son bloqueos corregibles con edición del manuscrito congelado; requerirían experimentos futuros:

1. evaluación con sujetos, montajes y sitios independientes;
2. canales naturalmente defectuosos y detección de canales malos;
3. comparación con al menos un método aprendido o source-informed;
4. endpoints downstream como ERP, espectro, conectividad o clasificación;
5. benchmark de tiempo con hardware/software registrado;
6. sensibilidad de parámetros y alternativas de construcción del grafo.

El manuscrito ya presenta estos puntos como limitaciones y próximos pasos (`05_discussion.tex:58-70`), sin fingir que fueron evaluados.

## 6. Verificación final del artefacto

- `latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex`: código 0.
- PDF: 22 páginas, 414.268 bytes.
- SHA-256 de `main.pdf`: `c7f5d67a5b613ab573097212ce8ecdaf19d22fc83f4ab10c9ba3db4e19537bbd`.
- Log: 0 errores, 0 advertencias, 0 citas/referencias indefinidas y 0 cajas over/underfull.
- PyMuPDF: 0 bloques fuera de página.
- Evidencia: 14/14 checksums válidos.
- QA visual: portada, keywords, tablas, figuras, §3.4, reflujo de páginas 13–16, declaraciones y bibliografía aprobados.
- Alejandro Weinstein aparece correctamente en portada.
- El placeholder rojo de financiación aparece en la página 20 y es el único marcador editorial visible.

## 7. Gate mínimo antes de enviar

1. Confirmar financiación y reemplazar el placeholder por la declaración definitiva.
2. Definir autor de correspondencia, correo y, si BSPC lo solicita en el archivo, dirección postal completa.
3. Obtener aprobación de ambos autores sobre orden, afiliación y roles CRediT.
4. Recompilar y repetir auditoría de log y página 20.
5. Preparar archivos separados exigidos por el portal: manuscript, highlights, figuras y declaraciones si corresponde.

## 8. Conclusión editorial

**Respuesta corta a “¿pasa el desk screening?”:** científicamente, **probablemente sí, pero no de manera segura**. El encaje temático y la calidad de presentación justifican enviarlo a revisión; la validación real limitada y el único comparator son las razones más plausibles para un rechazo editorial. Administrativamente, el archivo actual **no debe enviarse** hasta resolver financiación y correspondencia.
