# HISTÓRICO — Protocolo congelado `paper_core_v1`

> **Fuera del alcance de la iteración activa.** El nuevo manuscrito IEEE TBME se construye desde cero usando la tesis como fuente principal y no ejecuta experimentos nuevos. Este protocolo no debe alimentar cifras, tablas ni figuras del nuevo artículo. Véase `docs/paper/ieee_tbme_thesis_protocol.md`.

Fecha: 2026-07-23  
Estado inicial: definido; pendiente de smoke test y ejecución.

## 1. Pregunta experimental

¿En qué regímenes de pérdida de canales la regularización espacio-temporal TRSS con parámetros fijos entrega una mejora práctica frente a la interpolación por splines esféricos de MNE-Python, y qué compromiso existe entre error de reconstrucción, fidelidad espectral y costo de aplicación?

## 2. Fuentes de datos y unidades

### PhysioNet EEGBCI

- Sujetos: 1–9.
- Run: 4.
- Unidad de registro: sujeto–run.
- Canales EEG esperados: 64.
- Frecuencia original: 160 Hz.

### BCI Competition IV 2a

- Sujetos: 1–9.
- Sesión: entrenamiento (`T`).
- Unidad de registro: sujeto–sesión.
- Canales utilizados: 22 EEG; se excluyen canales EOG.
- Frecuencia original: 250 Hz.

### MNE Sample

- Registro: `sample_audvis_raw.fif`.
- Unidad de registro: un único registro.
- Canales: EEG con coordenadas válidas.
- El registro no se interpreta como cohorte ni como nueve sujetos equivalentes a los otros datasets.

Total previsto: 19 unidades de registro.

## 3. Preprocesamiento común

1. Cargar únicamente canales EEG.
2. Asignar o conservar nombres y coordenadas de montaje verificables.
3. Extraer un tramo predefinido de 20 s desde el inicio del registro.
4. Aplicar referencia promedio común.
5. Filtrar entre 0.5 y 45 Hz usando el mismo procedimiento MNE en todos los datasets.
6. Remuestrear a 160 Hz.
7. Extraer la ventana central de 4 s, de 8 a 12 s, para reducir efectos de borde.
8. Rechazar la unidad si quedan valores no finitos, menos de 16 canales con posición válida o menos de 640 muestras.

No se realiza normalización por método. Ambos métodos reciben exactamente la misma señal preprocesada.

## 4. Simulación de canales faltantes

Modos:

- `random`: selección uniforme sin reemplazo.
- `nearby`: canal central aleatorio y vecinos más próximos según distancia 3D.

Severidades:

- 10%, 20%, 30% y 40% de los canales disponibles.

Semillas:

- 0, 1, 2, 3 y 4.

La máscara se genera una vez por caso y se comparte entre TRSS y MNE.

Total previsto:

- PhysioNet: 360 casos pareados.
- BCI IV 2a: 360 casos pareados.
- MNE Sample: 40 casos pareados.
- Total: 760 casos pareados y 1520 aplicaciones de método.

## 5. Métodos principales

### MNE-Python

- `Raw.interpolate_bads`.
- Método EEG: `spline`.
- Origen: `auto`.
- Parámetros comunitarios por defecto.

### TRSS fijo

- Grafo: k-NN gaussiano construido exclusivamente desde coordenadas.
- `k = 4`.
- `sigma = 1.0`.
- `alpha = 0.8`.
- `beta = 0.15`.
- `n_iter = 120`.
- `lr = 0.05`.

Los parámetros se fijan antes de ejecutar `paper_core_v1`. No habrá selección por caso ni oráculo en el análisis principal.

## 6. Métricas

Calculadas exclusivamente sobre canales ocultos:

- MAE;
- RMSE;
- NRMSE;
- SNR;
- DTW;
- LSD;
- coherencia media;
- correlación media;
- R²;
- tiempo de aplicación por caso.

La dirección de cada métrica se define antes del análisis. El tiempo de calibración no se mezcla con el tiempo de aplicación.

## 7. Unidad estadística y síntesis

- Observación básica: caso pareado método–registro–máscara–semilla.
- Unidad independiente principal: sujeto–run o registro.
- Las máscaras no se tratan como sujetos independientes.
- Se reportan medianas, IQR, diferencias relativas pareadas y tasa de victoria.
- Los intervalos descriptivos al 95% se obtienen mediante bootstrap jerárquico por dataset y unidad de registro, conservando dentro de cada unidad todas sus máscaras.
- No se organiza la conclusión alrededor de pruebas de hipótesis.
- Se reportan resultados por dataset, modo y severidad antes del resumen global.

## 8. Casos cualitativos

La selección se realiza después del análisis mediante reglas predefinidas:

1. mayor mejora MAE de TRSS;
2. caso más favorable a MNE;
3. empate práctico con menor diferencia absoluta;
4. caso cercano severo más próximo a la mediana del estrato.

Para cada caso se guardan en NPZ:

- señal original;
- máscara;
- reconstrucción MNE;
- reconstrucción TRSS;
- canal objetivo;
- frecuencia de muestreo;
- metadatos de dataset, registro, modo, severidad y semilla.

Las figuras temporales y PSD se generan exclusivamente desde esos NPZ.

## 9. Artefactos obligatorios

- `config.json` inmutable;
- `raw_results.csv`;
- `paired_results.csv`;
- `summary_overall.csv`;
- `summary_by_dataset.csv`;
- `summary_by_scenario.csv`;
- `bootstrap_summary.csv`;
- `representative_cases.csv`;
- NPZ de casos representativos;
- tablas LaTeX;
- figuras PDF/PNG;
- `manifest.json` con SHA-256, versiones y commit del código;
- log de ejecución.

## 10. Criterios de aceptación

`paper_core_v1` solo puede alimentar Results cuando:

- [ ] las 19 unidades cargan o las exclusiones quedan documentadas;
- [ ] todas las máscaras son compartidas por ambos métodos;
- [ ] todas las métricas usan solo canales ocultos;
- [ ] no existen filas duplicadas o no finitas;
- [ ] los denominadores observados coinciden con el manifiesto;
- [ ] las figuras se reconstruyen desde NPZ congelados;
- [ ] los artefactos tienen checksums;
- [ ] la matriz claim–evidence se actualiza con valores verificados.

Cualquier desviación del protocolo requiere incrementar la versión y documentar la razón.
