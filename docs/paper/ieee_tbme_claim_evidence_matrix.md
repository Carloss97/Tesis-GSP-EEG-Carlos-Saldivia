# Matriz activa claim–evidence: IEEE TBME desde la tesis

Fecha: 2026-07-23  
Estado: aplicada al manuscrito compilado.  
Título: **Missing EEG Channel Reconstruction Using Graph Signal Processing With Temporal Regularization**.

## Regla de uso

La tesis final es la referencia primaria. No se agregan experimentos ni se mezclan cifras con `paper_core_v1`. Cada claim cuantitativo del artículo debe apuntar a una tabla, figura o pasaje de la tesis.

| ID | Claim permitido | Evidencia primaria en la tesis | Recurso candidato en el artículo | Límite obligatorio |
|---|---|---|---|---|
| C1 | La evaluación oculta artificialmente canales conocidos y calcula error solo en esos canales. | `chapters/03_metodologia.tex`, protocolos y métricas | Fig. de flujo metodológico; Methods | No equivale a daño real ni a validación clínica. |
| C2 | El diseño es pareado: ambos métodos usan la misma señal, máscara y semilla. | `chapters/03_metodologia.tex` | Fig. `ch3_methodology_flow.pdf` | No tratar máscaras repetidas como sujetos independientes. |
| C3 | TRSS añade regularización temporal a una formulación espacial sobre grafos. | Cap. 2 y 3; `ch2_trss_operator.pdf` | Ecuación y figura del operador | No atribuir causalidad fisiológica. |
| C4 | Frente a MNE, TRSS fijo obtuvo +12.4% de mejora mediana en MAE, IC descriptivo [+7.8, +17.4] y 72.0% de victorias. | `tables/ch6_robust_main.tex`; `tables/ch6_metric_portfolio.tex` | Tabla principal; figura de intervalos | Resultado condicionado al benchmark de la tesis. |
| C5 | TRSS fijo obtuvo +13.9% de mejora mediana en NRMSE y 70.3% de victorias. | `tables/ch6_robust_main.tex` | Tabla principal | No llamarlo mejora clínica. |
| C6 | La ventaja de TRSS es mayor en pérdidas agrupadas/periféricas severas y no es homogénea. | `tables/ch6_selected_scenarios_mae.tex`; `figures/ch6_scenario_heatmap_mae.pdf` | Heatmap o tabla de escenarios | Presentar como heterogeneidad descriptiva. |
| C7 | MNE preserva mejor la LSD global en el resumen agregado. | `tables/ch6_metric_portfolio.tex` | Tabla principal | No generalizar a todas las medidas espectrales. |
| C8 | TRSS es aproximadamente un orden de magnitud más lento en las medianas reportadas (0.1214 frente a 0.0090 s/caso). | `tables/ch6_runtime_complexity.tex`; `tables/ch6_global_summary.tex` | Tabla de costo o figura trade-off | Los tiempos dependen del hardware e implementación. |
| C9 | Las reconstrucciones representativas ilustran diferencias temporales, pero no sustituyen el resumen cuantitativo. | `figures/ch4_representative_timeseries.pdf`; capítulo de resultados | Figura cualitativa | No seleccionar el caso como prueba de desempeño global. |
| C10 | El beneficio observado no es universal; MNE puede ser preferible bajo baja pérdida, suavidad espacial, prioridad espectral o restricciones de tiempo. | `chapters/05_discusion.tex`; `chapters/06_conclusiones.tex` | Discussion y Conclusion | Evitar lenguaje de dominancia. |

## Claims no autorizados

1. TRSS es superior para todo EEG o todo patrón de pérdida.
2. TRSS mejora diagnóstico, clasificación BCI, ERP, conectividad o localización de fuentes.
3. El estudio demuestra desempeño sobre canales realmente dañados.
4. Existe significación estadística si no se reporta una prueba en la tesis.
5. El método está listo para tiempo real o uso clínico.
6. Visibility/NNK forma parte del método final.
7. Cualquier número proveniente solo de `paper_core_v1`.

## Material visual incluido

- Resultado multimetric: `paper/ieee_tbme/figures/metric_portfolio.pdf` (Fig. 1).
- Heterogeneidad por dataset: `paper/ieee_tbme/figures/dataset_summary.pdf` (Fig. 2).
- Costo frente a error: `paper/ieee_tbme/figures/runtime_tradeoff.pdf` (Fig. 3).

Las tres figuras se regeneran mediante `paper/ieee_tbme/scripts/prepare_figures.py` a partir de CSV congelados de la tesis; el script no repite reconstrucciones ni modifica valores. Las cinco páginas del PDF fueron inspeccionadas visualmente en tamaño IEEE y no presentan texto o leyendas superpuestos sobre los datos.
