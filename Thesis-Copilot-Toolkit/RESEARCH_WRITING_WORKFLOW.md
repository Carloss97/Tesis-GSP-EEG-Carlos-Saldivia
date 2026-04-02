# Workflow de redaccion cientifica (paper + tesis)

## 1. Entregables

- Paper: manuscrito en ingles con formato IEEE para envio a revista indexada.
- Tesis: manuscrito extendido en espanol con formato institucional USM.

## 2. Fuente de referencias

- Fuente principal de bibtex existente: `../Referencias/Mi biblioteca.bib`.
- Copia de trabajo local:
  - `paper/ieee/bibliography/references.bib`
  - `thesis/usm/bibliography/references.bib`

Regla practica:
- Mantener claves BibTeX estables entre paper y tesis.
- Evitar duplicados de la misma referencia con claves distintas.

## 3. Politica de lenguaje

- Paper:
  - Ingles tecnico y conciso.
  - Tiempo verbal predominante en pasado para metodologia/experimentos.
  - Evitar afirmaciones sin respaldo cuantitativo.

- Tesis:
  - Espanol academico formal y consistente.
  - Definir acronimos en su primera aparicion.
  - Incluir contexto metodologico detallado y justificacion de decisiones.

## 4. Politica de formato

- Paper IEEE:
  - Secciones minimas: Abstract, Introduction, Methods, Experimental Setup, Results, Discussion, Conclusion.
  - Figuras y tablas con captions autoexplicativos.
  - Referencias en estilo IEEE.

- Tesis USM:
  - Frontmatter: portada, resumen, abstract, agradecimientos, indices.
  - Cuerpo: introduccion, marco teorico, metodologia, resultados, discusion, conclusiones.
  - Ajustar portada/logos al formato institucional definitivo.

## 5. Trazabilidad con resultados

Todo resultado declarado en paper o tesis debe apuntar a un artefacto concreto en `results/`.

Plantilla de trazabilidad recomendada:
- Resultado reportado -> archivo CSV/figura -> script de experimento -> commit/tag.

## 6. Integracion de referencia USM (.zip)

Archivo de referencia detectado:
- `../Referencias/Tesis_Borrador_Tomas_Bernal.zip`

Acciones sugeridas:
1. Extraer estructura de carpetas y macros de formato.
2. Identificar clase/paquetes institucionales usados.
3. Migrar portada y convenciones de estilo a `thesis/usm/`.
4. Incorporar logo oficial en `thesis/usm/assets/logo_usm/`.

Estado aplicado en esta iteracion:
- Se detecto como referencia principal `Main_Tesis.tex` con clase `book`.
- Se incorporo esquema de portada, title page y approval page en `thesis/usm/frontmatter/`.
- Se agrego fallback de logo hacia `Referencias/Tesis_Borrador_Tomas_Bernal/Figures/UTFSM.pdf` si no existe un logo local.

## 7. Criterios de cierre documental

- Paper listo para pre-submission:
  - Texto completo en ingles revisado.
  - Figuras/tablas finales incorporadas.
  - Bibliografia sin claves faltantes.

- Tesis lista para entrega interna:
  - Capitulos completos con narrativa coherente.
  - Metodologia y experimentos totalmente reproducibles.
  - Formato institucional validado con plantilla USM final.
