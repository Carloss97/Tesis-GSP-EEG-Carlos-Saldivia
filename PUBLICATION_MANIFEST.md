# Manifiesto de publicación pública

Este manifiesto define qué debe quedar visible en la versión pública del repositorio de tesis y qué debe mantenerse fuera de Git.

## Incluido

### Código reproducible

- `Thesis-Copilot-Toolkit/src/`
- `Thesis-Copilot-Toolkit/scripts/*.py`
- `Thesis-Copilot-Toolkit/experiments/*.py`
- `Thesis-Copilot-Toolkit/experiments/schedules/**/*.json`
- `Thesis-Copilot-Toolkit/tests/`

### Documentación

- `README.md`
- `PUBLICATION_MANIFEST.md`
- `Thesis-Copilot-Toolkit/README.md`
- `Thesis-Copilot-Toolkit/docs/`
- documentación metodológica no generada.

### Tesis final

- `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/tesis_completa.tex`
- `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/tesis_caps_1_4.tex`
- `config/`, `frontmatter/`, `chapters/`, `appendices/`, `tables/`, `bibliography/`, `figures/`, `scripts/`
- `tesis_completa.pdf`
- `tesis_caps_1_4.pdf`

## Excluido

### Datos crudos

- `datasets/`
- `Thesis-Copilot-Toolkit/datasets/`
- archivos `.edf`, `.gdf`, `.fif`, `.mat`, `.dat`, `.raw`, `.npz`, `.npy`, `.pkl`, `.h5`, `.sqlite`, etc.

### Resultados y artefactos generados

- `results/`
- `Thesis-Copilot-Toolkit/results*/`
- `Thesis-Copilot-Toolkit/standardized_results/`
- logs de ejecución, caches y salidas masivas.

### Material personal o de trabajo no publicable

- `Code1201/`
- `Papers/`
- `Referencias/`
- `Tesis/`
- `informes/`
- `Escritos-gamma4/`
- `.agent_work/`, `.copilot-tracking/`, `.tools/`

### Auxiliares de compilación

- `.aux`, `.log`, `.fls`, `.fdb_latexmk`, `.toc`, `.lof`, `.lot`, `.out`, `.blg`, `.bbl`, `build_logs/`, `backups/`.

## Criterio

El repositorio público debe permitir entender:

1. qué problema aborda la tesis;
2. qué métodos se implementaron;
3. cómo se organizó la evaluación;
4. cómo se compila el documento;
5. qué artefactos finales respaldan la narrativa.

No debe redistribuir datasets externos, resultados exploratorios masivos, PDFs de literatura descargados ni carpetas de trabajo personales.

## Seguridad local

La limpieza de publicación se realiza con `git rm --cached`, por lo que los archivos excluidos dejan de versionarse pero permanecen en el disco local.
