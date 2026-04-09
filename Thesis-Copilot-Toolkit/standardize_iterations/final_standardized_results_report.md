# Informe final: Compactación de standardized_results

**Fecha:** 2026-04-09

## Resumen ejecutivo

- **Archivos escaneados:** 38,314
- **Movimientos planificados:** 38,313
- **Movimientos aplicados:** 38,313
- **Iteraciones canonizadas:** 130 (it001..it130)
- **Respaldo creado:** Thesis-Copilot-Toolkit/standardize_iterations/standardized_results_backup.tar.gz
- **Reportes técnicos:**
  - Dry-run (JSON): Thesis-Copilot-Toolkit/standardize_iterations/compact_standardized_results_report.json
  - Apply (JSON): Thesis-Copilot-Toolkit/standardize_iterations/compact_standardized_results_apply_report.json
- **Índice regenerado:** Thesis-Copilot-Toolkit/standardized_results/index.json

## Política de colisiones

Las colisiones (múltiples orígenes apuntando a un mismo archivo destino) se resolvieron de forma no destructiva renombrando con el sufijo `__dupN` cuando fue necesario. Revisa los archivos que contienen `__dup` si necesitas versiones separadas.

## Ejemplos representativos (muestras)

- **Destino:** standardized_results/it001/figures/metadata.json
  - Orígenes (muestra):
    - standardized_results/it001_it001_it001_it001_it001_it001_it001_it01_figures/metadata.json
    - standardized_results/it001_it001_it001_it001_it001_it001_it001_it01_retry_figures/metadata.json
    - standardized_results/it001_it001_it001_it001_it001_it001_it001_it01_figures/metadata.json
    - standardized_results/it001_it001_it001_it001_it001_it001_it01_figures/metadata.json
    - standardized_results/it001_it001_it001_it001_it001_it01_figures/metadata.json

- **Destino:** standardized_results/it001/metadata.json
  - Orígenes (muestra):
    - standardized_results/it001_it001_it001_it001_it001_it001_it001_it01_nogo_report/metadata.json
    - standardized_results/it001_it001_it001_it001_it001_it001_it001_it01_qa_report/metadata.json
    - standardized_results/it001_it001_it001_it001_it001_it001_it001_it01_raw/metadata.json
    - standardized_results/it001_it001_it001_it001_it001_it001_it01_run_metadata/metadata.json
    - standardized_results/it001_it001_it001_it001_it001_it001_it01_significance/metadata.json

## Hotspots (sugerencia de revisión manual)

- `it001`, `it002`, `it003` muestran un alto número de orígenes distintos que fueron consolidados. Recomiendo una revisión manual de esas carpetas si esperas conservar variantes históricas.

## Archivos generados / ubicaciones

- Informe dry-run (JSON): Thesis-Copilot-Toolkit/standardize_iterations/compact_standardized_results_report.json
- Informe apply (JSON): Thesis-Copilot-Toolkit/standardize_iterations/compact_standardized_results_apply_report.json
- Backup (tar.gz): Thesis-Copilot-Toolkit/standardize_iterations/standardized_results_backup.tar.gz
- Índice regenerado: Thesis-Copilot-Toolkit/standardized_results/index.json
- Informe final (este archivo): Thesis-Copilot-Toolkit/standardize_iterations/final_standardized_results_report.md

## Recomendaciones siguientes

- Hacer que el estandarizador sea idempotente: escribir siempre a la ruta canónica `it{NNN}/{figures,tables,raw,...}` y no concatenar el nombre de la carpeta origen en la nueva salida.
- Ejecutar una validación manual rápida sobre `it001..it005` para confirmar que las versiones consolidadas contienen los archivos esperados.
- Si necesitas revertir la compactación, puedo generar un script que restaure desde `standardized_results_backup.tar.gz`.

---

## Eliminación de carpetas vacías

- **Directorios escaneados:** 4,398
- **Candidatos para eliminación (dry-run):** 3,641
- **Directorios eliminados (apply):** 3,641
- **Informe dry-run:** Thesis-Copilot-Toolkit/standardize_iterations/cleanup_empty_dirs_dryrun_report.json
- **Informe apply:** Thesis-Copilot-Toolkit/standardize_iterations/cleanup_empty_dirs_apply_report.json

**Muestra de directorios eliminados (primeras 10):**

- Thesis-Copilot-Toolkit/standardized_results/it001_it001_it001_it001_it001_it001_it001_it001_it01_nogo_report
- Thesis-Copilot-Toolkit/standardized_results/it001_it001_it001_it001_it001_it001_it001_it001_it01_qa_report
- Thesis-Copilot-Toolkit/standardized_results/it001_it001_it001_it001_it001_it001_it001_it001_it01_raw
- Thesis-Copilot-Toolkit/standardized_results/it001_it001_it001_it001_it001_it001_it001_it001_it01_retry_nogo_report
- Thesis-Copilot-Toolkit/standardized_results/it001_it001_it001_it001_it001_it001_it001_it001_it01_retry_qa_report
- Thesis-Copilot-Toolkit/standardized_results/it001_it001_it001_it001_it001_it001_it001_it001_it01_retry_raw
- Thesis-Copilot-Toolkit/standardized_results/it001_it001_it001_it001_it001_it001_it001_it001_it01_retry_run_metadata
- Thesis-Copilot-Toolkit/standardized_results/it001_it001_it001_it001_it001_it001_it001_it001_it01_retry_significance
- Thesis-Copilot-Toolkit/standardized_results/it001_it001_it001_it001_it001_it001_it001_it001_it01_retry_stats
- Thesis-Copilot-Toolkit/standardized_results/it001_it001_it001_it001_it001_it001_it001_it001_it01_run_metadata

---

## Condensación de archivos `__dup` (archivado)

- **Archivos candidatos detectados:** 34,060
- **Iteraciones afectadas:** 130 (it001..it130)
- **ZIPs creados:** 130 (`archived_dup_files_20260409_180004.zip` dentro de cada `itNNN`)
- **Archivos eliminados tras archivado:** 34,060
- **Informe apply (JSON):** Thesis-Copilot-Toolkit/standardize_iterations/condense_standardized_results_apply_report_20260409_180004.json
- **Ejemplo de ZIP generado:** Thesis-Copilot-Toolkit/standardized_results/it001/archived_dup_files_20260409_180004.zip
- **Ejemplo de manifiesto:** Thesis-Copilot-Toolkit/standardized_results/it001/archived_dup_files_20260409_180004_manifest.json

Notas:

- Los archivos que contenían `__dup` se agruparon por `itNNN` en un ZIP por iteración y se generó un manifiesto JSON con sumas SHA256 y tamaños. Esto reduce el número de ficheros en los árboles `itNNN` preservando la trazabilidad.
- Hay un respaldo completo en: Thesis-Copilot-Toolkit/standardize_iterations/standardized_results_backup.tar.gz (útil para restauración si es necesario).

---

Informe generado automáticamente por la herramienta de compactación. Ver los JSONs de reporte para listados completos y el historial de movimientos.

## Verificación de archivos archivados (comprobación completa)

- **Archivos verificados:** 34,060
- **Iteraciones verificadas:** 130 (it001..it130)
- **ZIPs verificados:** 130 (`archived_dup_files_20260409_180004.zip` por iteración)
- **Coincidencias (SHA256/tamaños):** 34,060 (0 mismatches)
- **Errores durante verificación:** 0
- **Informe de verificación:** Thesis-Copilot-Toolkit/standardize_iterations/verify_archives_report_20260409_180004.json

Notas:

- La verificación valida que cada archivo dentro de los ZIP coincide con el manifiesto correspondiente (SHA256 y tamaño). El informe JSON contiene el detalle por `itNNN`.

