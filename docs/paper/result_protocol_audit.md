# Auditoría de resultados y protocolos para el manuscrito BSPC

Fecha de auditoría: 2026-07-23

## 1. Alcance y criterio de esta auditoría

Esta auditoría corresponde a la Fase 1 del handoff para convertir la tesis aprobada en un artículo original para *Biomedical Signal Processing and Control* (BSPC). No se redactó todavía la sección Results ni se creó el manuscrito BSPC.

Fuentes revisadas:

- tesis aprobada en `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/`;
- reporte final del profesor guía y QA visual/LaTeX;
- tablas, scripts y archivos de resultados usados por el Capítulo 4;
- paper IEEE histórico en `Thesis-Copilot-Toolkit/paper/ieee/`;
- handoffs históricos recuperados desde Git;
- guía oficial vigente de BSPC;
- historial Git y estado de seguimiento de los artefactos numéricos.

La matriz detallada de afirmaciones se encuentra en `docs/paper/claim_evidence_matrix.csv`.

## 2. Dictamen ejecutivo

El proyecto tiene una contribución editorialmente defendible como benchmark metodológico, pero los resultados principales todavía no deben copiarse al paper BSPC.

Razones principales:

1. La tesis describe una campaña amplia de tres datasets y 120 escenarios, mientras que el CSV pareado que sustenta las cifras finales contiene cinco etiquetas de régimen derivadas de dos fuentes EEG públicas y dos controles sintéticos.
2. BCI Competition IV 2a no aparece en el benchmark pareado de 300 casos, aunque la tesis y el paper histórico pueden dar la impresión de que sí forma parte de esa comparación final.
3. Los artefactos CSV/JSON principales existen localmente, pero están ignorados por Git y no poseen un commit propio. Hay checksums locales, pero aún falta un paquete congelado y versionado.
4. Las cifras de 2700, 3000 y 3300 evaluaciones se usan de manera ambigua en fuentes distintas. El CSV crudo contiene 2700 filas; el CSV derivado contiene 3300 porque añade filas seleccionadas y de oráculo.
5. Las figuras temporales y PSD no se regeneran desde las mismas matrices de señal utilizadas por el benchmark pareado.
6. El estudio del término temporal es exploratorio y presenta limitaciones que impiden usarlo como evidencia principal sin recálculo.

Conclusión: el protocolo pareado TRSS fijo frente a MNE es la base correcta para el artículo, pero debe regenerarse como un protocolo de paper real-EEG, congelado y trazable. La campaña de 120 escenarios debe permanecer como contexto exploratorio y no como fuente mezclada de cifras principales.

## 3. Inventario de protocolos encontrados

### 3.1. Protocolo amplio de la tesis

Definición declarada:

- 3 datasets: PhysioNet EEGBCI, BCI Competition IV 2a y MNE Sample;
- 2 modos de pérdida: aleatoria y contigua;
- 4 severidades: 10%, 20%, 30% y 40%;
- 5 semillas;
- total nominal: 3 × 2 × 4 × 5 = 120 escenarios.

Rol recomendado: `exploratory_only`.

Este diseño es útil para describir el alcance de la tesis y la selección de candidatos, pero la auditoría no encontró un único artefacto final que permita reconstruir todas las cifras de los 18 métodos sobre exactamente esos 120 escenarios sin mezclar campañas históricas.

### 3.2. Benchmark pareado balanceado actual

Fuente principal:

- `results/trss_vs_mne_bads_extensive/raw_balanced.csv`;
- `results/trss_vs_mne_bads_extensive/derived_balanced.csv`;
- `results/trss_vs_mne_bads_extensive/robust_stats/`;
- `experiments/trss_vs_mne_bads_extensive.py`;
- `experiments/analyze_trss_mne_robust_stats.py`.

Diseño observado:

- 5 etiquetas de régimen:
  - sintético suave;
  - sintético rugoso;
  - PhysioNet sujeto 1, run 4, ventana inicial;
  - PhysioNet sujeto 2, run 4, ventana inicial;
  - MNE Sample, ventana inicial y máximo de 40 canales;
- 4 patrones: random, nearby, edge y high_variance;
- 5 valores de pérdida: 1 canal, 2 canales, 10%, 30% y 40%;
- 3 semillas: 0, 1 y 2;
- 5 × 4 × 5 × 3 = 300 casos de máscara;
- 100 clusters de escenario = 5 etiquetas × 4 patrones × 5 valores;
- 300 pares TRSS fijo–MNE por métrica.

El CSV crudo contiene 2700 evaluaciones exitosas:

- 300 casos MNE;
- 300 casos para cada uno de 8 candidatos TRSS;
- total: 300 + 8 × 300 = 2700.

El CSV derivado contiene 3300 filas porque agrega:

- 300 filas `trss_cv_tuned_seed0`;
- 300 filas `trss_oracle_grid`;
- las 2700 filas originales.

Por tanto, 3300 no equivale a 3300 evaluaciones crudas independientes.

### 3.3. Estudio exploratorio del término temporal

Fuente:

- `results/ablation_real_data_extended_results.csv`;
- `scripts/ablation_real_data.py`.

Diseño observado:

- BCI IV 2a, sujeto 1;
- PhysioNet EEGBCI, sujeto 1;
- cuatro ratios de pérdida;
- diez máscaras por ratio;
- TRSS completo, TRSS sin término temporal y spline propia;
- 240 filas totales;
- 80 contextos pareados TRSS completo–sin temporalidad.

Problemas metodológicos detectados:

1. Las coordenadas de electrodos se reemplazan por posiciones uniformes en un círculo, en vez de usar el montaje EEG real.
2. Las métricas se calculan sobre la matriz completa, no exclusivamente sobre los canales ocultos.
3. Solo se estudian máscaras aleatorias.
4. Se usa un único sujeto por dataset.
5. El resumen histórico aplica Mann–Whitney a realizaciones que comparten máscara; el análisis principal del paper debería ser pareado.
6. El resultado no está congelado en Git.

Clasificación: `exploratory_only`. No usar sus porcentajes como resultado principal BSPC.

### 3.4. Microbenchmark preliminar

Fuente:

- `results/tablas_resumen/phase2_microbench_latency.csv`.

El archivo contiene latencias de varias familias, pero no incluye MNE y no está acompañado por un manifiesto completo de entrada, hardware y repeticiones. Sirve para explicar la reducción de candidatos, no para establecer el costo final del paper.

Clasificación: `exploratory_only`.

## 4. Contradicciones críticas

### C1. Tres datasets declarados frente a dos fuentes EEG en la comparación pareada

La tesis declara PhysioNet, BCI IV 2a y MNE Sample. El benchmark pareado de 300 casos contiene MNE Sample, dos sujetos PhysioNet y dos controles sintéticos. BCI IV 2a está ausente.

Consecuencia: no puede escribirse “evaluated across PhysioNet, BCI Competition IV 2a, and MNE Sample” para las cifras de 300 pares.

Estado: `No publicable sin nueva evidencia`.

### C2. 120 escenarios frente a 100 clusters y 300 pares

Son protocolos distintos:

- 120: campaña amplia declarada en la tesis;
- 100 clusters/300 pares: benchmark balanceado TRSS–MNE.

No deben sumarse, promediarse ni presentarse como etapas equivalentes de una misma tabla.

Estado: `Confirmado por fuente`, con separación obligatoria.

### C3. 2700 filas crudas frente a 3300 filas derivadas

El macro `ResConfirmatoryRawEvals=3300` no coincide con el CSV crudo de 2700 filas. Las 600 filas adicionales son selecciones derivadas, no ejecuciones independientes.

Estado: `No publicable sin nueva evidencia` para la expresión “3300 raw evaluations”.

### C4. Severidades incompatibles

La tesis amplia usa 10%, 20%, 30% y 40%. El perfil balanceado usa 1 canal, 2 canales, 10%, 30% y 40%; omite 20%.

Estado: `Decisión editorial pendiente` hasta fijar el protocolo del paper.

### C5. Patrones de pérdida incompatibles

La tesis central usa pérdida aleatoria y contigua. El perfil balanceado añade edge y high_variance. Esos patrones pueden ser útiles, pero deben declararse como extensión o reanálisis y no atribuirse retrospectivamente al protocolo original de 120 escenarios.

Estado: `Decisión editorial pendiente`.

### C6. Unidad estadística insuficientemente jerarquizada

El análisis robusto actual agrupa por etiqueta de dataset × patrón × pérdida y remuestrea semillas dentro del cluster. Esto es mejor que remuestrear filas de forma ingenua, pero las etiquetas PhysioNet S1 y S2 operan como “datasets” y no como sujetos dentro de una fuente común. Tampoco existe una cohorte equivalente para BCI IV 2a.

Consecuencia: los intervalos actuales describen los 300 casos observados, pero no deben presentarse como evidencia de generalización entre sujetos o poblaciones.

Estado: `Requiere recalculo`.

### C7. Figuras cualitativas no idénticas al caso cuantitativo

La selección de casos se obtiene del CSV balanceado, pero el generador de figuras vuelve a cargar MNE Sample, filtra 1–30 Hz, crea épocas y promedia respuestas. El benchmark balanceado usa una ventana cruda inicial del loader, sin ese mismo flujo.

Consecuencia: la etiqueta del caso y su porcentaje de mejora no garantizan que la curva mostrada sea la misma observación evaluada.

Estado: `No publicable sin nueva evidencia` para las figuras actuales.

### C8. Claims del paper IEEE histórico

El manuscrito histórico contiene expresiones de superioridad, significancia generalizada, límite teórico, precisión submilisegundo e interpretación clínica que no están respaldadas por el protocolo final aprobado.

Consecuencia: el paper IEEE puede usarse para localizar bibliografía o recursos, pero no como fuente automática de texto ni cifras.

Estado: `unsupported`.

## 5. Decisión sobre el protocolo principal

### Decisión adoptada

El protocolo principal del paper BSPC será una comparación pareada, posterior a la selección de candidatos, entre:

- TRSS con hiperparámetros fijados antes de la evaluación;
- MNE-Python `interpolate_bads(method='spline')` como referencia operativa.

La unidad científica principal será el caso pareado definido por el mismo registro o sujeto, segmento, máscara y semilla. Las síntesis deberán respetar la jerarquía sujeto/registro → máscara → método.

### Lo que no será el protocolo principal

- El ranking de 18 métodos y 736 iteraciones no será evidencia principal.
- El diseño nominal de 120 escenarios no se mezclará con el benchmark pareado.
- El oráculo no será presentado como método desplegable.
- El estudio temporal actual no será una prueba confirmatoria.

### Estado del benchmark balanceado actual

El benchmark de 300 pares se adopta como prototipo estructural, no como conjunto final publicable. Debe regenerarse para el paper con una cohorte real-EEG coherente.

Requisitos mínimos de la regeneración:

1. incluir las tres fuentes públicas declaradas, o reducir explícitamente el alcance del paper a las fuentes realmente evaluadas;
2. separar sujetos, runs y ventanas en columnas propias;
3. definir una partición independiente para selección y evaluación;
4. usar coordenadas de montaje reales;
5. calcular todas las métricas exclusivamente en canales ocultos;
6. usar TRSS fijo como comparación principal;
7. reservar TRSS calibrado para sensibilidad y el oráculo para un anexo metodológico, si se conserva;
8. fijar patrones y severidades antes de ejecutar;
9. almacenar señales originales, máscaras y reconstrucciones de los casos cualitativos;
10. versionar configuración, scripts, resultados y manifiesto de checksums.

No se fija aún un nuevo número total de casos: hacerlo antes de auditar disponibilidad real por sujeto y dataset sería inventar el denominador.

## 6. Resultados actuales potencialmente utilizables después de regeneración

Las siguientes tendencias son científicamente plausibles y coherentes con la tesis, pero sus cifras exactas permanecen en `needs_recalculation`:

- TRSS fijo reduce MAE, RMSE, NRMSE y DTW en una mayoría de los pares actuales.
- La ventaja aumenta en pérdidas cercanas o periféricas severas.
- MNE conserva una ventaja clara de tiempo de aplicación.
- MNE puede ser igual o mejor en señales espacialmente suaves y en LSD.
- No existe dominancia universal.

Wording de trabajo permitido, sujeto a resultados congelados:

> MNE-Python remained the faster operational reference, whereas fixed TRSS provided lower reconstruction error in a subset of difficult spatial-loss regimes. The trade-off was metric- and regime-dependent, and no method dominated across all evaluated conditions.

## 7. Resultados no utilizables en el manuscrito actual

No deben entrar en Results, Abstract, Highlights o Conclusion sin nueva evidencia:

1. “3300 raw evaluations”.
2. Inclusión de BCI IV 2a en las cifras de 300 pares.
3. “Five independent datasets” para las cinco etiquetas del CSV balanceado.
4. Superioridad universal o estructural de TRSS.
5. Claims de validación clínica o preservación fisiológica demostrada.
6. Claims de precisión submilisegundo.
7. Claims de equivalencia estricta Python–MATLAB/GSPBox sin reporte versionado de cierre estricto.
8. Porcentajes del estudio temporal actual como evidencia confirmatoria.
9. Figuras temporales/PSD actuales como reproducción exacta de los pares del CSV.
10. Métricas inferenciales históricas calculadas sobre iteraciones heterogéneas.
11. Resultados de métodos exploratorios invalidados.
12. El oráculo como método aplicable.
13. Tiempos de calibración mezclados con tiempo de aplicación.

## 8. Congelamiento y control de versiones pendiente

Los principales resultados bajo `Thesis-Copilot-Toolkit/results/` están ignorados por `.gitignore`. En la auditoría, `git ls-files` y `git log --all --full-history` no devolvieron commits para los CSV principales.

Checksums locales registrados en la matriz:

- `raw_balanced.csv`: `44fda738...20f41`;
- `derived_balanced.csv`: `05b8fae1...a28f2`;
- `robust_pairwise_summary.csv`: `d92d0ebd...45095`;
- `ablation_real_data_extended_results.csv`: `57e811ee...5a173`;
- `phase2_microbench_latency.csv`: `b410851b...39d1`;
- `phase2_iteration_metrics_pivot.csv`: `300b90bc...6d67`.

Antes de redactar resultados se debe crear un paquete `paper_core_v1` con:

- manifiesto de archivos y SHA-256;
- commit del código generador;
- configuración inmutable;
- tabla de cohortes y exclusiones;
- resultados crudos y derivados;
- script único de análisis;
- README de reproducción.

## 9. Plan de archivos para la siguiente fase

Después de aprobar esta auditoría:

1. Crear `Thesis-Copilot-Toolkit/paper/bspc/README.md` con el alcance científico congelado.
2. Crear `paper/bspc/evidence/paper_core_v1_manifest.json`.
3. Crear o adaptar un script de benchmark real-EEG sin mezclar campañas históricas.
4. Crear un script de análisis pareado jerárquico y tablas reproducibles.
5. Regenerar figuras directamente desde arrays congelados.
6. Crear la estructura LaTeX BSPC separada del paper IEEE.
7. Redactar primero Materials and Methods y Experimental Design.
8. Redactar Results solo después del gate de trazabilidad.

## 10. Gate de cierre de Fase 1

- [x] Tesis y reportes finales revisados.
- [x] Paper IEEE histórico auditado.
- [x] Protocolos 120/100/300 separados.
- [x] CSV crudo y derivado diferenciados.
- [x] Ausencia de BCI IV 2a en el benchmark pareado identificada.
- [x] Unidad estadística actual descrita.
- [x] Resultados no utilizables listados.
- [x] Protocolo principal recomendado.
- [ ] Cohorte real-EEG del paper aprobada.
- [ ] Reanálisis mínimo ejecutado.
- [ ] Resultados congelados y versionados.
- [ ] Methods/Results BSPC autorizados para redacción.

La Fase 1 queda cerrada como auditoría, pero el Gate 1 de integridad científica del manuscrito sigue abierto hasta completar el reanálisis y congelamiento.
