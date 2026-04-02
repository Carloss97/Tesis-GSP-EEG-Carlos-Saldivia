# Paper IEEE - Estructura de trabajo

Este directorio contiene la base de redaccion para un manuscrito orientado a revista indexada de perfil IEEE.

## Objetivo editorial

- Idioma: ingles academico.
- Formato: IEEE (doble columna en version de envio).
- Enfoque: evidencia reproducible desde los experimentos de `results/`.

## Estructura propuesta

- `ieee/main.tex`: archivo principal del paper.
- `ieee/sections/`: secciones separadas para escritura modular.
- `ieee/figures/`: figuras listas para envio (PDF/PNG, 300 dpi o mas).
- `ieee/tables/`: tablas en formato LaTeX.
- `ieee/bibliography/references.bib`: base BibTeX del paper.

Secciones actuales del manuscrito:

- `abstract`
- `introduction`
- `related_work`
- `methods`
- `experiments`
- `results`
- `discussion`
- `reproducibility`
- `conclusion`

## Flujo de redaccion recomendado

1. Congelar resultados finales en `results/`.
2. Escribir primero `sections/results.tex` y `sections/experiments.tex`.
3. Derivar `sections/introduction.tex` y `sections/discussion.tex` con base en evidencia.
4. Cerrar `sections/abstract.tex` y `sections/conclusion.tex` al final.

## Compilacion local

Comando sugerido:

```bash
latexmk -pdf -interaction=nonstopmode ieee/main.tex
```

## Checklist minimo de pre-envio

- Titulo y contribuciones claramente delimitadas.
- Metodologia reproducible y trazable a scripts.
- Resultados con comparativas y pruebas de robustez.
- Referencias completas y consistentes con BibTeX.
- Revision gramatical en ingles tecnico.
