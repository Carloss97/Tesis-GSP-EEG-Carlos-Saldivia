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

## Dual-Language Support (English & Spanish)

As of this session, the paper infrastructure supports **full dual-language compilation** with complete translations:

### Structure

- **`ieee/`** - English version (primary, source of truth for shared content)
  - English-specific sections: `abstract.tex`, `introduction.tex`, `conclusion.tex`
  - Shared sections: `related_work.tex`, `methods.tex`, `experiments.tex`, `results.tex`, `discussion.tex`, `reproducibility.tex`
  - Shared resources: `figures/`, `tables/`, `bibliography/`

- **`ieee_es/`** - Spanish version (COMPLETE with full translations)
  - Spanish-translated sections: `abstract_es.tex`, `introduction_es.tex`, `related_work_es.tex`, `methods_es.tex`, `experiments_es.tex`, `results_es.tex`, `discussion_es.tex`, `reproducibility_es.tex`, `conclusion_es.tex`
  - All sections now in Spanish for comprehensive professor reviews
  - Shares: `figures/`, `tables/`, `bibliography/` with English version

### Building Dual Versions

```bash
# Build both versions
make

# Build only English
make pdf-en

# Build only Spanish
make pdf-es

# Clean intermediate files
make clean

# See all options
make help
```

### Synchronizing Changes

When you modify shared sections (methods, results, figures, bibliography) in English, sync to Spanish:

```bash
# Preview changes (dry-run)
python sync_structure.py --dry-run

# Apply sync (English → Spanish)
python sync_structure.py

# Specify direction
python sync_structure.py --direction EN_TO_ES

# See all options
python sync_structure.py --help
```

### What Gets Synced

With full translation complete, sync is primarily for visual/reference content:

**Synced items** (shared resources):
- `figures/` directory
- `tables/` directory
- `bibliography/` directory

**NOT synced** (language-specific — independently maintained):
- All **English** sections: `abstract.tex`, `introduction.tex`, `related_work.tex`, `methods.tex`, `experiments.tex`, `results.tex`, `discussion.tex`, `reproducibility.tex`, `conclusion.tex`
- All **Spanish** sections: `abstract_es.tex`, `introduction_es.tex`, `related_work_es.tex`, `methods_es.tex`, `experiments_es.tex`, `results_es.tex`, `discussion_es.tex`, `reproducibility_es.tex`, `conclusion_es.tex`

**Note**: With complete translations, you typically only sync if you update figures, bibliography, or other visual/reference resources.

### Workflow for Updates

**For content/text updates** (now fully translated):
1. **Edit English version** text in `ieee/sections/` (e.g., `methods.tex`)
2. **Manually translate and update Spanish version** in `ieee_es/sections/` (e.g., `methods_es.tex`)
3. **Compile both**: `make` or `make pdf-both`
4. **Both PDFs ready**: `ieee/main.pdf` and `ieee_es/main.pdf`

**For visual/reference updates** (figures, bibliography):
1. **Edit shared resource** in `ieee/figures/` or `ieee/bibliography/`
2. **Sync to Spanish**: `python sync_structure.py`
3. **Compile both**: `make pdf-both`

**For translations of new sections**:
1. Create new English section in `ieee/sections/newsection.tex`
2. Create Spanish translation in `ieee_es/sections/newsection_es.tex`
3. Include both in their respective `main.tex` files
4. Compile and verify both versions

For detailed instructions, see the dual-language workflow section in this README or run:

```bash
python sync_structure.py --help
make help
```

## Checklist minimo de pre-envio

- Titulo y contribuciones claramente delimitadas.
- Metodologia reproducible y trazable a scripts.
- Resultados con comparativas y pruebas de robustez.
- ✅ English and Spanish versions compilable and in sync.
- Referencias completas y consistentes con BibTeX.
- Revision gramatical en ingles tecnico.

## Nota sobre normalización de resultados

Cuando integre resultados en el manuscrito, verifique que no se mezclen ejecuciones normalizadas y no-normalizadas. Consulte `../docs/normalization_and_dataset_policy.md` para la convención de nombres y metadatos (`normalization`, `missing_mode`).
