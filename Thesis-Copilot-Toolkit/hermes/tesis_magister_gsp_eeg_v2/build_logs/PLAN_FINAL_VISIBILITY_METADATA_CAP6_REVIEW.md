# Plan final — metadata, eliminación Visibility/NNK, Capítulo 6 y revisión de profesor guía

Fecha: 2026-07-07  
Backup: `backups/final_visibility_cap6_metadata_20260707_175155/`

## 1. Comentario de portada/metadata

Comentario detectado en `config/metadata.tex`:

- `Borrar palabra Ingeniería.` sobre `\ThesisDepartment`.

Acción:

1. Cambiar `Departamento de Ingeniería Electrónica` por `Departamento de Electrónica`.
2. Actualizar también `frontmatter/cover_page.tex`, porque la portada tenía `DEPARTAMENTO DE INGENIERÍA ELECTRÓNICA` hardcodeado y no usaba `\ThesisDepartment`.
3. Eliminar comentarios auxiliares no usados en metadata.

## 2. Eliminación de Visibility/NNK

Instrucción del usuario:

- No hacer referencia en ningún momento a Visibility NNK.
- El método no se usó finalmente, por lo que no vale la pena mencionarlo.

Acción:

1. Eliminar menciones explícitas a `Visibility NNK` de capítulos, anexos y captions.
2. Eliminar `NNK` visible del documento si aparece como método data-driven, reemplazándolo por formulaciones generales de regresión local no negativa o retirándolo de tablas activas.
3. Mantener la exclusión en scripts solo si es necesaria para filtrar artefactos, pero sin texto visible en el documento.
4. Verificar con PyMuPDF que `tesis_completa.pdf` no contenga `Visibility`, `visibility`, `NNK` ni `nnk`.

## 3. Tablas del Capítulo 6

Problema:

- Las tablas del Capítulo 6 son densas y estrechas.

Acción:

1. Quitar tablas densas del cuerpo de Capítulo 6.
2. Reemplazar la tabla de fases por una lista narrativa de fases.
3. Reemplazar la matriz de cumplimiento por una lista de cierre por objetivos/preguntas.
4. Mantener tablas de síntesis en anexos cuando sean útiles, pero no sobrecargar el cierre.

## 4. Revisión crítica tipo profesor guía

Acción:

1. Leer Capítulo 4, 5 y 6 como corrector.
2. Revisar coherencia entre Capítulo 4 y cierre.
3. Verificar que el Capítulo 4 no prometa evidencia que 5--6 no usen.
4. Verificar que 5--6 no reintroduzcan conclusiones absolutas ni métodos no usados.
5. Dejar informe en `build_logs/REVISION_PROFESOR_GUIA_FINAL.md`.
6. Aplicar correcciones menores derivadas de esa revisión.

## 5. Validación

1. Compilar `tesis_caps_1_4.tex` y `tesis_completa.tex`.
2. Ejecutar `scripts/validate_thesis.py`.
3. Verificar términos prohibidos y comentarios `%` activos.
4. QA visual de portada, Capítulo 4, Capítulo 6 y anexos.
5. Ejecutar verificación ad-hoc temporal `/tmp/hermes-verify-*.py` y eliminarla.
