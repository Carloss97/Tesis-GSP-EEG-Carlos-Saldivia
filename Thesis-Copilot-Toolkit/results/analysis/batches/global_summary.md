# Resumen global de métodos


Generado: 2026-04-10T18:26:44.791941Z


## Top métodos (por media MAE)


|method|count|mean|std|median|
|---|---|---|---|---|
|spline_temporal|32|1.1654829380302845e-05|2.7209503884245993e-06|1.1134885641167803e-05|
|gsmooth|5274|0.09259058115502374|0.09648843752920808|0.0652929243435412|
|idw|5406|0.09545196817289028|0.0991223097162261|0.0660994520829936|
|gsp|3173|0.11583293477015401|0.10817258236108003|0.088259445073733|
|directed_tv|2560|0.12060995383095234|0.17043577359727477|0.1181534984305608|
|linear|3512|0.120845823006665|0.11800635226800493|0.0942564113430665|
|wavelet_temporal|2550|0.12231655323920902|0.10331373770962676|0.123798954736391|
|spherical_spline|3306|0.13465792977927354|0.14202871587133703|0.1021720677531056|
|rbfi_tps|3306|0.14401542249789828|0.14919248365159427|0.0950698397827097|
|rbfi_mq|3306|0.1607660111084691|0.1705946737790419|0.1076814030559054|


## Top-3 apariciones por bloque


|method|top3_block_count|
|---|---|
|tv|2420|
|trss|2337|
|temporal_laplacian|2297|
|graph_time_tikhonov|2278|
|mean|2253|
|tikhonov|2235|
|nearest|2073|
|idw|756|
|gsmooth|752|
|linear|752|
|directed_tv|752|
|heat_diffusion_temporal|744|
|wavelet_temporal|743|
|spherical_spline|610|
|puy|590|
|spline_surface|590|
|rbfi_tps|590|
|rbfi_mq|590|
|bgsrp|589|
|sobolev|572|
|gsp|534|
|spline_temporal|32|


## Top-3 apariciones por dataset


|method|top3_dataset_count|
|---|---|
|tv|14|
|mean|11|
|trss|10|
|gsmooth|7|
|graph_time_tikhonov|3|
|nearest|3|
|directed_tv|3|
|spherical_spline|2|
|idw|2|
|linear|1|
|wavelet_temporal|1|
|heat_diffusion_temporal|1|
|tikhonov|1|
|temporal_laplacian|1|


## Estadísticas por combinación (graph + dataset + missing_ratio)

Se ha calculado la media de MAE por método para cada combinación (graph, dataset, missing_ratio),
seleccionando el *mejor* (menor MAE) y el segundo mejor para comparar. Para cada combinación se
incluye:

- `best_method`, `best_mean_mae`, `best_n`, `ci_lower`, `ci_upper`
- `second_method`, `second_mean_mae`, `second_n`
- `delta_mean` (segundo - mejor)
- `p_raw`, `p_adj` (p-valor de Mann–Whitney y p ajustado por Holm), `significant`
- `rank_biserial` (efecto, rango-biserial)

Resumen rápido:

- Combinaciones evaluadas: 315
- Combinaciones con mejora significativa (p_adj < 0.05): 129
- Top métodos reportados como "mejor": `trss` (107), `tv` (54), `heat_diffusion_temporal` (34), `directed_tv` (31), `mean` (28)

Archivos con resultados completos:

- Tabla completa (CSV): [Thesis-Copilot-Toolkit/results/analysis/batches/best_method_by_combo_stats.csv](Thesis-Copilot-Toolkit/results/analysis/batches/best_method_by_combo_stats.csv)
- Tabla resumen (mejor por combinación): [Thesis-Copilot-Toolkit/results/analysis/batches/best_method_by_combo.csv](Thesis-Copilot-Toolkit/results/analysis/batches/best_method_by_combo.csv)
- Libro Excel con todas las hojas (descargable): [Thesis-Copilot-Toolkit/results/analysis/batches/summary_report.xlsx](Thesis-Copilot-Toolkit/results/analysis/batches/summary_report.xlsx)
- Dashboard interactivo (index): [Thesis-Copilot-Toolkit/results/analysis/batches/interactive/index.html](Thesis-Copilot-Toolkit/results/analysis/batches/interactive/index.html)

Notas:

- Los IC95 se calcularon por bootstrap sobre la media del MAE (2000 repeticiones cuando hay suficiente muestra).
- La prueba usada para comparar mejor vs segundo fue Mann–Whitney U (no paramétrica). Los p-valores se ajustaron con Holm.
- Para combinaciones con muestras pequeñas (n < 3) no se reportaron p-valores.

Si quieres, puedo:

- Exportar únicamente las 129 combinaciones significativas a un XLSX separado.
- Añadir una figura (heatmap) que muestre solo combinaciones significativas por `best_method`.
- Subir `summary_report.xlsx` a un servicio (Google Drive, transfer.sh, etc.) y devolver un enlace descargable.
