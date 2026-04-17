# Tesis de Magister - Estructura de trabajo

Este directorio contiene la base de redaccion de la tesis completa en LaTeX.

## Objetivo editorial

- Idioma: espanol academico (consistente y formal).
- Enfoque: documento extenso que describe el proceso completo, desde diseno experimental hasta resultados y discusion.
- Formato: plantilla base en LaTeX, preparada para adaptarse al formato institucional USM.

## Estructura propuesta

- `usm/main.tex`: archivo principal de tesis.
- `usm/config/metadata.tex`: metadatos institucionales, autores y comision.
- `usm/config/packages.tex`: paquetes y configuracion de estilo base.
- `usm/frontmatter/`: cover page, title page, approval page, resumenes, agradecimientos.
- `usm/chapters/`: capitulos principales del manuscrito.
- `usm/figures/`: figuras de tesis.
- `usm/tables/`: tablas de tesis.
- `usm/bibliography/references.bib`: referencias bibtex de tesis.
- `usm/assets/logo_usm/`: carpeta para logo institucional.

## Compilacion local

Comando sugerido:

```bash
latexmk -pdf -interaction=nonstopmode usm/main.tex
```

## Nota sobre formato institucional

Se incluye una base `book` funcional para iniciar redaccion inmediatamente.
Cuando se extraiga la tesis de referencia en `Referencias/Tesis_Borrador_Tomas_Bernal.zip`, se debe ajustar la portada y estilos al formato exacto USM.

## Estado actual de adaptacion USM

- Plantilla migrada a esquema tipo `book` con frontmatter institucional.
- Se agregaron paginas de cover/title/approval en `usm/frontmatter/`.
- La portada intenta usar primero `usm/assets/logo_usm/logo_usm.pdf` o `logo_usm.png`.
- Si el logo local no existe, usa como respaldo el logo de la tesis extraida en `Referencias/Tesis_Borrador_Tomas_Bernal/Figures/UTFSM.pdf`.

## Nota sobre normalización de resultados

Al integrar resultados en la tesis, asegúrese de no mezclar ejecuciones normalizadas y no-normalizadas. Consulte `../docs/normalization_and_dataset_policy.md` para la convención de nombres y los campos de metadatos obligatorios (`normalization`, `missing_mode`).
