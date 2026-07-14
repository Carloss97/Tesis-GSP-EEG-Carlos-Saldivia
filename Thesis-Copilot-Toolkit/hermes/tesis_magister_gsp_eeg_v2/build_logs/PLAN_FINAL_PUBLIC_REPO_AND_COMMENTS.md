# Plan final: comentarios de profesor y preparación de repositorio público

Fecha: 2026-07-13  
Backup: `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/backups/final_repo_publication_pass_20260713_212342/`

## Objetivo

Dejar la versión final completa lista para corrección del profesor y preparar una versión pública entendible del repositorio. No se hará `git push` ni se cambiará la visibilidad del remoto en esta pasada.

## Comentarios finales a resolver

1. **Portada:** quitar co-director/co-guía de portada y metadata visible.
2. **Capítulo 1, sección 1.3:** añadir citas al párrafo que menciona enfoques de aprendizaje profundo.
3. **Capítulo 2, sección 2.2.3:** añadir salto/separación antes de “Grafos data-driven” y eliminar comentario `%` pendiente.
4. **Capítulo 3, sección 3.7.1:** reemplazar URL provisoria por el remoto real: `https://github.com/Carloss97/Tesis-GSP-EEG-Carlos-Saldivia`.

## Limpieza/preparación del repositorio público

1. Mantener como contenido público curado:
   - fuentes LaTeX y PDF final bajo `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/`;
   - código fuente necesario bajo `Thesis-Copilot-Toolkit/src/` y scripts reproducibles relevantes;
   - documentación de reproducción y manifiesto público.
2. Excluir/retirar ruido del índice público mediante `.gitignore` y manifiesto:
   - datasets crudos;
   - resultados pesados o intermedios;
   - cachés, entornos, logs temporales y archivos auxiliares de LaTeX;
   - directorios personales o de trabajo no necesarios para reproducir la investigación.
3. Crear documentación mínima de publicación:
   - `README.md` en la raíz con propósito, estructura, cómo compilar la tesis y qué no se versiona;
   - `PUBLICATION_MANIFEST.md` con qué incluir/excluir antes de cambiar el repo a público.
4. Verificar que no queden menciones a rutas locales, comentarios pendientes ni términos descartados en fuentes/PDF activos.

## Verificación

1. Compilar `tesis_caps_1_4.tex` y `tesis_completa.tex`.
2. Ejecutar `scripts/validate_thesis.py`.
3. Revisar logs: 0 errores, 0 citas indefinidas, 0 refs indefinidas, 0 overfull hbox.
4. Revisar texto fuente/PDF para comentarios `%`, `Visibility`, `NNK`, `TV dirigida`, `cribado`, `Wilcoxon`, `q_{BH}`, `significancia`, URL provisoria y co-director visible.
5. Reportar que la verificación es ad-hoc, no suite canónica.
