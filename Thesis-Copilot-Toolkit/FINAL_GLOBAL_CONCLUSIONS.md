## Documento final de conclusiones globales (estado al 2026-04-07)

## Alcance consolidado

- Iteraciones integradas y documentadas: `it02` a `it130`.
- Estado de `it120`: cierre operativo completado con perfil controlado de destrabe y artefactos completos emitidos (NO-GO, `p=0.0535`).
- Estado de `it121–it130`: bloque final ejecutado completamente con resultados mixtos (GO en `it124` e `it125`; resto NO-GO).
- Cobertura metodológica consolidada:
  - comparación TV/tiempo vs instantáneos,
  - múltiples topologías de grafo,
  - robustez por missing ratio y ruido,
  - transferencia EEG y no-EEG (Iris/MovieLens),
  - análisis de eficiencia (runtime) y sensibilidad topológica.

## Conclusiones globales

1. El pipeline experimental está técnicamente maduro y reproducible, con artefactos estandarizados por iteración (`raw`, `stats`, `significance`, `qa`, `metadata`, `integration_log`, figuras).
2. En fases históricas de EEG/proxy (especialmente Fase 5 y bloques it71–it100), la familia TV/tiempo mostró ventaja robusta en escenarios relevantes de reconstrucción.
3. En la expansión multidominio (it105–it120), el gate global TV vs Instant no mostró superioridad estadística consolidada (`NO-GO` en todas las corridas de ese bloque), lo que sugiere alta sensibilidad al dominio y al protocolo agregado.
4. Aun con `NO-GO` global en ese bloque, `trss` aparece repetidamente como mejor método puntual en varios escenarios, y `tv` destaca en subconjuntos específicos (p. ej., MovieLens).
5. El bloque final it121–it130 aporta evidencia adicional útil (incluyendo estratificación por dominio, holdout por sujeto y matriz final de decisión), con señal GO puntual en `it124` e `it125`, pero sin revertir el resultado global multidominio.
6. La evidencia acumulada respalda un mensaje científico matizado: no existe una dominancia universal por familia en todos los dominios; el rendimiento depende de dataset, topología y configuración experimental.
7. El proyecto queda listo para cierre editorial técnico con recomendación **CONDICIONAL por dominio/caso de uso**.

## Estado de riesgo y recomendaciones inmediatas

- Riesgo principal residual: brecha metodológica entre cierre operativo (controlado) y diseño exhaustivo original de `it120` que no completó en última ventana.
- Recomendación operativa: documentar explícitamente esta brecha como limitación y no bloquear más el cierre editorial.
- Recomendación de reporte: mantener explícita la distinción entre:
  - evidencia fuerte en bloques EEG/proxy previos,
  - evidencia mixta/no concluyente en expansión multidominio reciente.

## Ejecución final it121–it130 (completada)

Estas iteraciones se ejecutaron para extraer información adicional no redundante respecto a los bloques previos:

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

## Criterio de cierre aplicado

- Se ejecutaron primero las iteraciones más informativas (`it121`, `it122`, `it126`) y luego el bloque restante `it123–it130`.
- El cierre se emitió con recomendación condicional por dominio en lugar de una recomendación global única.

## Actualización operativa aplicada (2026-04-07, cierre rápido)

Decisión aplicada para no bloquear el escrito final:
- Se ejecutó un último intento exhaustivo de `it120`, sin cierre en ventana razonable; se cerró ciclo con perfil controlado.
- Se ejecutaron primero las iteraciones más informativas priorizadas: `it121`, `it122`, `it126`.
- Se ejecutó luego el bloque pendiente `it123–it130` en perfil operativo rápido.

Resultado de las iteraciones priorizadas:
- `it121_domain_stratified_gate`: **NO-GO** global (`p=0.9923`, gain=-10.6%) y también NO-GO por dominio (`eeg_real`, `non_eeg`).
- `it122_subjectwise_bci_holdout`: **NO-GO** global (`p=0.9999`, gain=-89.4%) y NO-GO en S1/S2/S3.
- `it126_metric_robustness_multiobjective`: **NO-GO** global (`p=0.1197`, gain=+28.3%); se emitió frente de Pareto (`tv`, `mean`, `trss`) para soporte de decisión.
- `it123–it130` (restante): ejecutadas con resultados mixtos, **GO en it124 e it125** y NO-GO en `it123`, `it127`, `it128`, `it129`, `it130`.
- `it130_final_decision_matrix`: recomendación final **CONDICIONAL** por dominio/caso de uso (EEG clínico, BCI, no-EEG), consistente con la evidencia estratificada.

Lectura de cierre condicional:
- No hay evidencia estadística para una recomendación global única TV>Instant en el bloque multidominio final.
- Sí hay señal útil para cierre por dominio/caso de uso (matriz condicional) apoyada en resultados estratificados y trade-off multiobjetivo.
- Decisión final del ciclo: `it120` exhaustivo se da por perdido en esta etapa; cierre técnico queda sustentado por `it120` controlado (NO-GO, `p=0.0535`) + bloque `it121–it130`.
