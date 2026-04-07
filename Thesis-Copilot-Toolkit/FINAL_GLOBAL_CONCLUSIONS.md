## Documento final de conclusiones globales (estado al 2026-04-07)

## Alcance consolidado

- Iteraciones integradas y documentadas: `it02` a `it120`.
- Estado de `it120`: cierre operativo completado con perfil controlado de destrabe y artefactos completos emitidos.
- Cobertura metodológica consolidada:
  - comparación TV/tiempo vs instantáneos,
  - múltiples topologías de grafo,
  - robustez por missing ratio y ruido,
  - transferencia EEG y no-EEG (Iris/MovieLens),
  - análisis de eficiencia (runtime) y sensibilidad topológica.

## Conclusiones globales

1. El pipeline experimental está técnicamente maduro y reproducible, con artefactos estandarizados por iteración (`raw`, `stats`, `significance`, `qa`, `metadata`, `integration_log`, figuras).
2. En fases históricas de EEG/proxy (especialmente Fase 5 y bloques it71–it100), la familia TV/tiempo mostró ventaja robusta en escenarios relevantes de reconstrucción.
3. En la expansión multidominio reciente (it105–it119), el gate global TV vs Instant no mostró superioridad estadística consolidada (`NO-GO` en todas las corridas de ese bloque), lo que sugiere alta sensibilidad al dominio y al protocolo agregado.
4. Aun con `NO-GO` global en ese bloque, `trss` aparece repetidamente como mejor método puntual en varios escenarios, y `tv` destaca en subconjuntos específicos (p. ej., MovieLens).
5. La evidencia acumulada respalda un mensaje científico más matizado: no existe una dominancia universal por familia en todos los dominios; el rendimiento depende fuertemente de dataset, topología y configuración experimental.
6. El proyecto queda listo para cierre editorial técnico en su versión operativa actual; el faltante explícito es repetir `it120` en perfil exhaustivo original para comparabilidad estricta con el diseño inicial.

## Estado de riesgo y recomendaciones inmediatas

- Riesgo principal actual: brecha entre cierre operativo (controlado) y cierre exhaustivo equivalente al diseño completo original de `it120`.
- Recomendación operativa: ejecutar rerun exhaustivo de `it120` en ventana dedicada (sin tareas concurrentes) y monitoreo por hitos de artefactos para evitar ciclos largos sin visibilidad.
- Recomendación de reporte: mantener explícita la distinción entre:
  - evidencia fuerte en bloques EEG/proxy previos,
  - evidencia mixta/no concluyente en expansión multidominio reciente.

## Propuesta de 10 iteraciones finales adicionales (it121–it130)

Estas iteraciones están enfocadas en extraer información nueva útil y no redundante respecto a lo ya obtenido:

1. **it121_domain_stratified_gate**  
   Evaluar gate GO/NO-GO por dominio separado (EEG real, EEG proxy, no-EEG) para evitar cancelación estadística por agregación heterogénea.
2. **it122_subjectwise_bci_holdout**  
   Validación leave-one-subject-out en BCI IV 2a para medir generalización real entre sujetos.
3. **it123_graph_density_calibration**  
   Barrido controlado de densidad de grafo (k y sigma) con objetivo de estabilizar desempeño TV en dominios donde cae.
4. **it124_missing_pattern_realistic_v2**  
   Patrones de pérdida no aleatorios por regiones fisiológicas y clústeres funcionales para contrastar con missing uniforme.
5. **it125_temporal_window_sensitivity**  
   Sensibilidad a tamaño de ventana temporal (n_times) y submuestreo para detectar sesgo por longitud de segmento.
6. **it126_metric_robustness_multiobjective**  
   Ranking multiobjetivo (MAE/RMSE/DTW/SNR + runtime) con fronte de Pareto por dominio.
7. **it127_noise_profile_non_gaussian**  
   Robustez con ruido impulsivo y mezcla no gaussiana (además de SNR gaussiano).
8. **it128_calibration_by_dataset_family**  
   Calibración ligera de hiperparámetros TV por familia de dataset y evaluación de transferencia cruzada.
9. **it129_confidence_interval_stability**  
   Estabilidad de conclusiones bajo bootstrap de seeds para cuantificar fragilidad de decisiones GO/NO-GO.
10. **it130_final_decision_matrix**  
    Matriz final de decisión por caso de uso (EEG clínico, BCI, no-EEG) con recomendación de método/grafo/configuración.

## Criterio de cierre sugerido para ciclo final

- Completar rerun exhaustivo de `it120`.
- Ejecutar al menos 3 de las iteraciones propuestas más informativas (`it121`, `it122`, `it126`).
- Emitir un cierre con recomendación condicional por dominio en lugar de una recomendación única global.
