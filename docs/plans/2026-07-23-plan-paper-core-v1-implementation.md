# Plan numerado de implementación — primera versión compilable BSPC

Fecha: 2026-07-23

## Objetivo

Implementar y ejecutar el protocolo congelado `paper_core_v1`, congelar sus artefactos verificables y producir una primera versión compilable e independiente del manuscrito BSPC, sin modificar la tesis aprobada ni el paper IEEE histórico.

## Plan de ejecución

1. **Verificar prerrequisitos y datos.** Confirmar el entorno Python 3.11, las versiones científicas, los 9 registros PhysioNet, los 9 registros BCI IV 2a, MNE Sample y la cadena LaTeX.
2. **Respaldar artefactos preexistentes.** Copiar la configuración congelada antes de modificar el árbol BSPC y registrar checksum del respaldo.
3. **Implementar el benchmark con TDD focalizado.** Crear `experiments/run_paper_core_v1.py` y pruebas para conteos, máscaras compartidas/deterministas, exclusión EOG, métricas hidden-only, conservación de observados y ausencia de duplicados.
4. **Probar primero el flujo mínimo.** Ejecutar pruebas unitarias y un smoke run real de una unidad/caso antes de lanzar el protocolo completo.
5. **Ejecutar los 760 casos pareados.** Procesar 19 unidades reales, dos modos, cuatro severidades y cinco semillas; escribir resultados incrementales y reanudables.
6. **Analizar y congelar.** Generar tabla pareada, resúmenes globales/por dataset/escenario, bootstrap jerárquico descriptivo, casos representativos, NPZ, tablas LaTeX, figuras y manifiesto SHA-256.
7. **Actualizar trazabilidad.** Añadir a la matriz claim–evidence solo cifras obtenidas del paquete ejecutado y dejar explícito cualquier desvío o fallo.
8. **Crear el paquete BSPC.** Escribir un manuscrito nuevo en inglés académico con Methods, Experimental Design y Results derivados de los artefactos congelados; completar Introduction, Related Work, Discussion, Conclusion, Declarations, highlights y README.
9. **Compilar y corregir.** Ejecutar `latexmk`, eliminar errores, citas/referencias indefinidas y rutas internas visibles.
10. **QA científico, editorial y visual.** Comprobar denominadores, términos prohibidos, abstract/highlights, consistencia entre tablas/figuras/CSV, extracción de texto y páginas renderizadas del PDF.

## Criterios de cierre

- 19 unidades documentadas y 760 pares completos, o exclusiones explícitas que obliguen a versionar otro protocolo.
- 1520 evaluaciones exitosas, sin duplicados y con métricas finitas salvo excepciones justificadas.
- Configuración, código, resultados, casos cualitativos y manifiesto trazables.
- `paper/bspc/main.pdf` compilado sin errores ni referencias indefinidas.
- Primera versión marcada como draft científico/editorial, no como manuscrito listo para envío.

## Respaldo inicial

- Directorio: `backups/paper_core_v1_20260723-024312/`
- Configuración original y respaldo: SHA-256 `ab0e23da33140321b0dceecc2fa8bef0fcbb63483ac6d9d223bcf8d13b024b67`.
