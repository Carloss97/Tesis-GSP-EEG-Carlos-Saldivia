# Plan final de pulido evidente: tablas, figuras y resúmenes

Fecha: 2026-07-07  
Backup: `backups/final_polish_tables_figures_abstracts_20260707_182931/`

## Diagnóstico

1. **Resumen/Abstract**: el resumen español tiene un comentario `%` pendiente sobre conectividad funcional y ambos resúmenes son suficientemente largos como para generar páginas de continuación con poco contenido.
2. **Apéndice B**: las tablas B.1--B.3 son funcionales, pero visualmente densas para una versión que se enviará a corrección. Conviene mantener la información principal como síntesis extendida legible y dejar los CSV/tablas completas como artefactos reproducibles.
3. **Figuras**:
   - Figura 2.2 está aceptable; no requiere intervención.
   - Figura 2.3 está clara, pero puede mejorar con margen inferior y flechas menos convergentes.
   - Figura temporal multipanel de Cap. 4 tiene leyenda dentro del primer eje; conviene usar leyenda global superior.
   - Figura PSD usa “1 canal(es)”; conviene cambiar a singular/plural editorialmente limpio.

## Acciones

1. Compactar `frontmatter/abstract_es.tex` y `frontmatter/abstract_en.tex`, eliminando la mención a conectividad funcional y cualquier comentario `%`.
2. Reescribir `appendices/B_tablas_extensas.tex` como síntesis extendida en prosa/listas y una tabla compacta no densa, sin insertar las tablas anchas B.1--B.3 en el cuerpo del anexo.
3. Retocar `scripts/generate_additional_figures.py` para mejorar Figura 2.3 y regenerarla.
4. Retocar `scripts/generate_ch4_v3_artifacts.py` para mover leyenda temporal a leyenda global y limpiar “1 canal(es)” en títulos, luego regenerar figuras de Cap. 4.
5. Compilar, validar y ejecutar QA visual antes de entregar.
