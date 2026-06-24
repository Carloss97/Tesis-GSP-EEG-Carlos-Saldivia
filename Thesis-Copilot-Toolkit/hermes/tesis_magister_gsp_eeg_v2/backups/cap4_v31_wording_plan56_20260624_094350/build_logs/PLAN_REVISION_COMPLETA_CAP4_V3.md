# Plan ejecutable de revisión completa — Capítulo 4 V3

Fecha: 2026-06-24  
Documento objetivo: `tesis_completa.tex`  
Capítulo objetivo: `chapters/04_resultados.tex`  
Alcance extendido: ajustar después `chapters/05_discusion.tex` y `chapters/06_conclusiones.tex` para mantener coherencia.

## Actualización V3.1: Capítulo 4 como “Experimentos y Resultados”

La revisión posterior a V3 identificó que el capítulo corregido resolvía el encuadre sin pruebas de hipótesis, pero todavía se leía principalmente como capítulo de resultados finales. La versión V3.1 agrega explícitamente la trayectoria experimental completa: cribado preliminar de métodos y grafos, reducción de candidatos, optimización intermedia, comparación final TRSS--MNE e inspección cualitativa. El plan detallado queda registrado en `build_logs/PLAN_REVISION_CAP4_V31_EXPERIMENTOS_RESULTADOS.md`.

## 1. Estado inicial verificado

### 1.1 Comentarios activos por capítulo

- `01_introduccion.tex`: 0 comentarios activos.
- `02_marco_teorico.tex`: 0 comentarios activos.
- `03_metodologia.tex`: 0 comentarios activos.
- `04_resultados.tex`: 14 comentarios activos.
- `05_discusion.tex`: 0 comentarios activos.
- `06_conclusiones.tex`: 0 comentarios activos.

### 1.2 Respaldo creado

Antes de cualquier reescritura se creó:

- `backups/cap4_v3_rewrite_20260624_021454/`

Incluye:

- capítulos 4--6;
- tablas `ch6_*.tex`;
- scripts locales de generación;
- figuras actualmente referenciadas por el capítulo 4;
- plan V3 previo si existía.

Puntero:

- `build_logs/latest_cap4_v3_backup.txt`

### 1.3 Comentarios del profesor que guían la revisión

1. El capítulo es difícil de entender y el análisis estadístico dificulta seguir los resultados.
2. Faltan resultados representativos de señales interpoladas con distintas estrategias.
3. Solo hay dos casos cualitativos y una figura no es informativa.
4. Hay que explicar o reemplazar el término “ablación”.
5. No aplica usar tests de hipótesis como eje en este setup.
6. Hay etiquetas poco claras: “tasa de victoria”.
7. Hay celdas de mapas/figuras cuya primera línea no se entiende.
8. Un caso TRSS se ve malo y debe explicarse si es representativo o excepcional.
9. El PSD actual no muestra lo esperado: original versus interpolado.
10. La complejidad usa variables no explicadas, especialmente `H`.
11. El capítulo debe replantearse en general y no parecer texto dependiente de IA.

## 2. Principio rector V3

El capítulo 4 no debe argumentar mediante tests de hipótesis. Debe responder preguntas prácticas de evaluación:

1. ¿Qué método reconstruye mejor bajo cada régimen de pérdida?
2. ¿Cuándo TRSS aporta valor adicional frente a MNE?
3. ¿Cuándo MNE es preferible?
4. ¿Qué costo computacional se paga por la mejora de TRSS?
5. ¿Las señales reconstruidas son plausibles en tiempo y frecuencia?

Los tests estadísticos se eliminan del cuerpo principal como eje narrativo. Si se conserva algún resultado tipo Wilcoxon/q-BH, debe moverse a apéndice o quedar como control secundario, no como argumento central.

## 3. Inventario actual del capítulo 4

### 3.1 Secciones actuales

1. Relación entre Fases Experimentales.
2. Inventario de Evidencia Experimental.
3. Comparación Pareada TRSS--MNE.
4. Estratificación por Conjunto de Datos.
5. Efecto del Patrón y Severidad de Pérdida.
6. Componente Temporal de TRSS.
7. Preservación Morfológica y Espectral.
8. Tiempo de Cómputo y Complejidad.
9. Síntesis de Resultados.

### 3.2 Tablas actualmente incluidas

- `tables/ch6_phase_map.tex`
- `tables/ch6_global_summary.tex`
- `tables/ch6_robust_main.tex`
- `tables/ch6_metric_portfolio.tex`
- `tables/ch6_by_dataset_mae.tex`
- `tables/ch6_selected_scenarios_mae.tex`
- `tables/ch6_runtime_complexity.tex`

### 3.3 Figuras actualmente incluidas

- `figures/ch6_runtime_mae_tradeoff.pdf`
- `figures/ch6_metric_portfolio_improvement.pdf`
- `figures/ch6_boxplot_nrmse_balanced.pdf`
- `figures/ch6_robust_improvement_ci.pdf`
- `figures/ch6_dataset_mae_improvement.pdf`
- `figures/ch6_scenario_heatmap_mae.pdf`
- `figures/ch6_ablation_temporal_component.pdf`
- `figures/res_opt_final__erp_comparison_static_mne_trss_filtered.pdf`
- `figures/res_opt_final__best_psd_comparison_clean.pdf`
- `figures/ch6_boxplot_runtime_balanced.pdf`

### 3.4 Script generador identificado

- `scripts/generate_ch6_artifacts.py`

Este script copia CSV fuente desde `results/`, genera tablas `ch6_*` y produce varias figuras `ch6_*`.

### 3.5 CSV fuente identificados

Principales fuentes usadas o disponibles:

- `results/trss_vs_mne_bads_extensive/summary_overall_balanced.csv`
- `results/trss_vs_mne_bads_extensive/pairwise_comparisons_balanced.csv`
- `results/trss_vs_mne_bads_extensive/derived_balanced.csv`
- `results/trss_vs_mne_bads_extensive/raw_balanced.csv`
- `results/trss_vs_mne_bads_extensive/mae_winrate_by_scenario_balanced.csv`
- `results/trss_vs_mne_bads_extensive/robust_stats/robust_pairwise_summary.csv`
- `results/trss_vs_mne_bads_extensive/robust_stats/robust_by_dataset.csv`
- `results/trss_vs_mne_bads_extensive/robust_stats/robust_by_missing_scenario.csv`
- `results/ablation_real_data_extended_results.csv`
- `results/tablas_resumen/phase2_microbench_latency.csv`

No se detectaron `.npz` directamente bajo `results/` con búsqueda simple. La siguiente fase debe localizar señales reconstruidas en otros subdirectorios o, si no existen, regenerarlas desde scripts/código base.

## 4. Nueva estructura propuesta del capítulo 4

### 4.1 Propósito de la evaluación comparativa

Objetivo: reemplazar la apertura actual por una guía de lectura clara.

Debe explicar:

- comparación pareada descriptiva;
- mismos datos, máscara y semilla para todos los métodos;
- métricas de amplitud, forma, espectro y costo;
- criterio práctico de interpretación.

Debe eliminar:

- “hipótesis respaldada”;
- “prueba confirmatoria” como eje;
- Wilcoxon/q-BH en el texto principal.

### 4.2 Inventario de escenarios, métodos y métricas

Reorganizar el inventario como tabla/verificación trazable:

| Elemento | Contenido | Fuente |
|---|---|---|
| Datos | MNE Sample, PhysioNet, BCI IV 2a, sintéticos | Cap. 3 / CSV |
| Métodos | MNE, TRSS fijo, TRSS calibrado, oráculo solo como cota | CSV |
| Escenarios | patrón, severidad, semilla | `derived_balanced.csv` |
| Métricas | MAE, RMSE, NRMSE, DTW, SNR, LSD, coherencia, correlación, tiempo | tablas/CSV |
| Artefactos | tablas, figuras, CSV, scripts | `generate_ch6_artifacts.py` |

### 4.3 Resumen global descriptivo TRSS--MNE

Reemplazar la sección “Comparación Pareada TRSS--MNE”.

Contenido principal:

- mediana MNE;
- mediana TRSS;
- diferencia o mejora mediana;
- tasa de victoria;
- intervalo bootstrap como incertidumbre descriptiva.

No usar:

- p-values;
- q-BH;
- lenguaje de rechazo/aceptación de hipótesis.

Tablas afectadas:

- `ch6_robust_main.tex`
- `ch6_metric_portfolio.tex`

Acción sobre tablas:

- crear versiones descriptivas sin columnas `q_BH` ni “Efecto” como columnas centrales;
- si se desea conservar pruebas, crear tabla suplementaria para apéndice.

### 4.4 Resultados por dataset y escenario de pérdida

Unificar y hacer más legibles:

- `ch6_by_dataset_mae.tex`
- `ch6_selected_scenarios_mae.tex`
- `ch6_dataset_mae_improvement.pdf`
- `ch6_scenario_heatmap_mae.pdf`

Cambios requeridos:

- definir “tasa de victoria” antes de usarla;
- explicar cada celda de mapas o tablas;
- preferir tabla limpia si el mapa de calor sigue siendo confuso.

Formato recomendado para celdas de escenario:

```text
ΔMAE mediana
WR = tasa de victoria
n = pares
```

### 4.5 Reconstrucciones temporales representativas

Nueva sección central, necesaria por comentario del profesor.

Debe mostrar señales temporales original/MNE/TRSS para casos seleccionados por regla reproducible:

1. caso favorable a TRSS;
2. caso favorable a MNE;
3. caso donde TRSS se ve malo;
4. empate práctico o caso intermedio.

Cada caso debe documentar:

- dataset;
- patrón de pérdida;
- severidad;
- semilla;
- canal(es) ocultos;
- métrica usada para selección;
- razón de inclusión.

Figura nueva recomendada:

- `figures/ch4_representative_timeseries.pdf`

Tabla nueva recomendada:

- `tables/ch4_representative_cases.tex`

### 4.6 Preservación espectral: PSD original vs interpolado

Reemplazar la figura PSD actual si no muestra claramente original vs reconstruido.

Figura nueva recomendada:

- `figures/ch4_psd_original_vs_interpolated.pdf`

Contenido mínimo:

- PSD original;
- PSD MNE;
- PSD TRSS;
- caso(s) representativos;
- método Welch explícito;
- ventana, solapamiento y frecuencia de muestreo;
- misma escala entre métodos.

El texto debe responder:

- por qué una curva puede ser rugosa;
- qué se espera preservar;
- por qué MAE y LSD pueden discrepar.

### 4.7 Contribución del término temporal de TRSS

Renombrar “ablación” o definirla antes.

Título sugerido:

- `Contribución del término temporal de TRSS`

Definición necesaria:

> En esta sección, ablación significa repetir la evaluación retirando el término temporal del modelo para estimar su contribución específica.

Figura actual afectada:

- `ch6_ablation_temporal_component.pdf`

Tabla/CSV fuente:

- `results/ablation_real_data_extended_results.csv`

### 4.8 Costo computacional y complejidad

Revisar:

- `ch6_runtime_complexity.tex`
- `ch6_boxplot_runtime_balanced.pdf`
- `ch6_runtime_mae_tradeoff.pdf`

Acciones:

1. Definir variables antes de la tabla:
   - `N`: canales;
   - `T`: muestras temporales;
   - `E`: aristas;
   - `K`: iteraciones del resolvedor;
   - `H`: número de configuraciones/hiperparámetros evaluados, solo si realmente se usa.
2. Justificar de dónde viene cada complejidad.
3. Vincular complejidad con tiempos medidos.
4. Evitar que el tiempo sea “otra prueba estadística”; debe leerse como criterio práctico.

### 4.9 Síntesis: frontera práctica TRSS vs MNE

Reemplazar la síntesis actual que todavía dice:

- “hipótesis se respaldan”;
- H1/H2.

Nueva síntesis:

| Condición | Método preferible | Justificación |
|---|---|---|
| pérdida cercana severa | TRSS | aprovecha regularidad temporal |
| pérdida periférica alta | TRSS | estabiliza cuando falta vecindario local |
| señal suave / baja pérdida | MNE | prior espacial suficiente |
| análisis offline | TRSS posible | costo aceptable |
| procesamiento masivo/interactivo | MNE | menor latencia |

## 5. Cambios concretos sobre artefactos

### 5.1 Tablas a regenerar

1. `ch6_robust_main.tex` → versión descriptiva sin Wilcoxon como eje.
2. `ch6_metric_portfolio.tex` → agrupar por categoría y retirar q-BH del cuerpo principal.
3. `ch6_selected_scenarios_mae.tex` → aclarar WR/n/mejora.
4. `ch6_runtime_complexity.tex` → definir símbolos y justificar expresiones.
5. Crear `ch4_representative_cases.tex`.

### 5.2 Figuras a conservar con cambios menores

- `ch6_runtime_mae_tradeoff.pdf`: conservar solo si el propósito queda claro.
- `ch6_metric_portfolio_improvement.pdf`: puede conservarse si se adapta a lectura descriptiva.
- `ch6_boxplot_nrmse_balanced.pdf`: útil como distribución, pero no debe ser argumento principal.
- `ch6_boxplot_runtime_balanced.pdf`: útil para costo.

### 5.3 Figuras a reemplazar o rediseñar

- `res_opt_final__erp_comparison_static_mne_trss_filtered.pdf`: reemplazar por una figura multi-caso original/MNE/TRSS trazable.
- `res_opt_final__best_psd_comparison_clean.pdf`: reemplazar por PSD original vs MNE vs TRSS.
- `ch6_scenario_heatmap_mae.pdf`: rediseñar o sustituir por tabla si sigue confusa.
- `ch6_ablation_temporal_component.pdf`: renombrar conceptualmente y explicar “ablación”.

## 6. Orden de ejecución

### Fase A — Preparación ya iniciada

- Respaldo creado.
- Comentarios extraídos.
- Figuras/tablas actuales inventariadas.
- Script `generate_ch6_artifacts.py` identificado.

### Fase B — Inspección de datos para figuras cualitativas

1. Revisar columnas de:
   - `raw_balanced.csv`;
   - `derived_balanced.csv`;
   - `pairwise_comparisons_balanced.csv`.
2. Verificar si contienen rutas a señales reconstruidas o identificadores suficientes.
3. Buscar señales reconstruidas fuera de `results/` si no aparecen `.npz` con búsqueda simple.
4. Si no existen señales guardadas, regenerar desde métodos y máscaras usando código fuente del toolkit.

### Fase C — Selección reproducible de casos

Crear un script o notebook reproducible que seleccione:

1. mejor caso TRSS;
2. peor caso TRSS;
3. mejor caso MNE;
4. empate práctico;
5. caso severo cercano;
6. control sintético suave/rugoso si aplica.

Salida esperada:

- `tables/ch4_representative_cases.tex`
- `tables/ch4_representative_cases.csv`

### Fase D — Regeneración de figuras prioritarias

1. `ch4_representative_timeseries.pdf`
2. `ch4_psd_original_vs_interpolated.pdf`
3. `ch4_scenario_summary_descriptive.pdf` o tabla reemplazo.
4. `ch4_decision_boundary_trss_mne.pdf` si aporta claridad.

### Fase E — Reescritura del capítulo 4

Reescribir `04_resultados.tex` en bloques:

1. introducción y propósito;
2. inventario;
3. resumen global descriptivo;
4. escenarios;
5. señales temporales;
6. PSD;
7. término temporal;
8. costo;
9. síntesis práctica.

Después de cada bloque:

- eliminar comentarios resueltos;
- compilar;
- revisar referencias/figuras.

### Fase F — Ajuste de capítulos 5 y 6

Después del capítulo 4:

- Cap. 5: discutir frontera TRSS/MNE, no dominancia universal, costo y limitaciones.
- Cap. 6: responder preguntas de investigación, no hipótesis.

## 7. Criterios de aceptación

La revisión del capítulo 4 se considera completa cuando:

1. `04_resultados.tex` no contiene comentarios `%` del profesor.
2. No hay narrativa basada en tests de hipótesis.
3. Wilcoxon/q-BH no son eje del capítulo.
4. Hay evidencia temporal original/MNE/TRSS.
5. Hay PSD original/MNE/TRSS.
6. Tasa de victoria está definida claramente.
7. Celdas de escenarios se entienden sin adivinar.
8. “Ablación” está definida o reemplazada.
9. Complejidad define `N`, `T`, `E`, `K`, `H` o elimina variables innecesarias.
10. Cap. 5 y 6 quedan consistentes con el nuevo encuadre.
11. `tesis_completa.tex` y `tesis_caps_1_5.tex` compilan sin errores, citas indefinidas, referencias indefinidas ni overfull hbox.
12. QA visual aprueba figuras nuevas o rediseñadas.

## 8. Próximo paso inmediato

Ejecutar Fase B:

1. leer estructura/columnas de `raw_balanced.csv`, `derived_balanced.csv` y `pairwise_comparisons_balanced.csv`;
2. ubicar señales reconstruidas o sus identificadores;
3. decidir si las figuras temporales/PSD pueden regenerarse desde artefactos existentes o requieren re-ejecutar métodos;
4. producir el primer script de selección de casos representativos.
