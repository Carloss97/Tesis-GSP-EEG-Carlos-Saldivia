# Reporte Final de Resultados — Experimento Unificado

> Generado automáticamente por `run_unified_final.py`

> Fecha: 2026-04-03 02:54


## Resumen Ejecutivo

- **Corridas válidas:** 2304
- **Métodos de interpolación:** 22
- **Métodos de grafo:** 7
- **Datasets:** 3
- **Niveles de pérdida:** [np.float64(0.1), np.float64(0.2), np.float64(0.3), np.float64(0.4)]

**Mejor método global** (menor MAE medio): `trss` (familia: tv_time, MAE=1.1549e-01 ± 6.9881e-02)

## 1. Ranking Global por MAE

|   rank | method                  | family   |   mae_mean |    mae_std |   dtw_mean |    dtw_std |   rmse_mean |    snr_mean |   n_runs |
|-------:|:------------------------|:---------|-----------:|-----------:|-----------:|-----------:|------------:|------------:|---------:|
|      1 | trss                    | tv_time  | 1.1549e-01 | 6.9881e-02 | 1.8869e+00 | 7.8330e-01 |  2.7806e-01 |  9.5311e+00 |       96 |
|      2 | mean                    | instant  | 1.3259e-01 | 7.2796e-02 | 2.0216e+00 | 7.4916e-01 |  3.1539e-01 |  7.9467e+00 |       96 |
|      3 | tv                      | tv_time  | 1.3336e-01 | 7.3147e-02 | 2.0238e+00 | 7.3956e-01 |  3.1861e-01 |  7.8641e+00 |       96 |
|      4 | gsmooth                 | instant  | 1.3580e-01 | 7.4424e-02 | 2.0325e+00 | 7.2383e-01 |  3.2660e-01 |  7.6644e+00 |       96 |
|      5 | idw                     | instant  | 1.3710e-01 | 7.5411e-02 | 2.0304e+00 | 7.1339e-01 |  3.3166e-01 |  7.5419e+00 |       96 |
|      6 | gsp                     | instant  | 1.4453e-01 | 7.9375e-02 | 2.0667e+00 | 6.9980e-01 |  3.5589e-01 |  7.0177e+00 |       96 |
|      7 | directed_tv             | tv_time  | 1.5605e-01 | 7.9398e-02 | 2.3465e+00 | 7.2035e-01 |  3.9236e-01 |  6.1700e+00 |       96 |
|      8 | linear                  | instant  | 1.5619e-01 | 8.5657e-02 | 2.1233e+00 | 6.8410e-01 |  3.9338e-01 |  6.0575e+00 |       96 |
|      9 | wavelet_temporal        | tv_time  | 1.6551e-01 | 7.0859e-02 | 2.2868e+00 | 7.5931e-01 |  3.2529e-01 |  7.4444e+00 |       96 |
|     10 | nearest                 | instant  | 1.7203e-01 | 9.5479e-02 | 2.2255e+00 | 7.3588e-01 |  4.4027e-01 |  5.1289e+00 |       96 |
|     11 | rbfi_tps                | instant  | 1.7656e-01 | 9.9141e-02 | 2.3859e+00 | 8.0793e-01 |  4.4582e-01 |  5.2110e+00 |       96 |
|     12 | rbfi_mq                 | instant  | 1.8923e-01 | 1.0660e-01 | 2.5629e+00 | 9.0946e-01 |  4.8307e-01 |  4.5846e+00 |       96 |
|     13 | spherical_spline        | instant  | 1.9169e-01 | 1.1275e-01 | 2.8234e+00 | 1.0511e+00 |  4.8720e-01 |  4.6701e+00 |       96 |
|     14 | heat_diffusion_temporal | tv_time  | 2.7392e-01 | 4.3242e-01 | 4.2639e+00 | 6.1708e+00 |  6.0262e-01 |  5.3951e+00 |       96 |
|     15 | spline_temporal         | tv_time  | 2.8624e-01 | 1.0527e-01 | 4.9192e+00 | 2.6211e+00 |  8.7145e-01 |  4.8964e+00 |       96 |
|     16 | tikhonov                | instant  | 3.7913e-01 | 1.4335e-01 | 3.4524e+00 | 1.0615e+00 |  4.8567e-01 |  3.7915e+00 |      192 |
|     17 | graph_time_tikhonov     | tv_time  | 4.6607e-01 | 8.7206e-02 | 4.3704e+00 | 7.3563e-01 |  5.4060e-01 |  2.6071e+00 |       96 |
|     18 | puy                     | instant  | 4.6923e-01 | 1.2547e-01 | 4.0025e+00 | 9.0113e-01 |  5.7551e-01 |  2.1227e+00 |       96 |
|     19 | temporal_laplacian      | tv_time  | 4.9124e-01 | 7.1626e-02 | 4.5698e+00 | 6.3853e-01 |  5.6291e-01 |  2.1373e+00 |       96 |
|     20 | sobolev                 | instant  | 5.6834e-01 | 4.6668e-02 | 5.3281e+00 | 3.8981e-01 |  6.4009e-01 |  9.5233e-01 |       96 |
|     21 | bgsrp                   | instant  | 5.7767e-01 | 1.3782e-02 | 4.6203e+00 | 2.6838e-01 |  6.7043e-01 |  5.4773e-01 |      192 |
|     22 | spline_surface          | instant  | 3.0804e+00 | 6.4133e+00 | 2.8624e+02 | 6.3513e+02 |  6.8240e+01 | -3.3001e+00 |       96 |

## 2. Top-5 por Dataset × Nivel de Pérdida × Familia

| dataset         |   missing_ratio | family   |   rank | method                  |   mae_mean |
|:----------------|----------------:|:---------|-------:|:------------------------|-----------:|
| synthetic_alpha |      1.0000e-01 | instant  |      1 | mean                    | 3.3574e-02 |
| synthetic_alpha |      1.0000e-01 | instant  |      2 | idw                     | 3.4765e-02 |
| synthetic_alpha |      1.0000e-01 | instant  |      3 | gsmooth                 | 3.4862e-02 |
| synthetic_alpha |      1.0000e-01 | instant  |      4 | gsp                     | 3.7605e-02 |
| synthetic_alpha |      1.0000e-01 | instant  |      5 | linear                  | 3.8915e-02 |
| synthetic_alpha |      1.0000e-01 | tv_time  |      1 | trss                    | 2.0540e-02 |
| synthetic_alpha |      1.0000e-01 | tv_time  |      2 | tv                      | 3.4112e-02 |
| synthetic_alpha |      1.0000e-01 | tv_time  |      3 | wavelet_temporal        | 5.3391e-02 |
| synthetic_alpha |      1.0000e-01 | tv_time  |      4 | directed_tv             | 5.4287e-02 |
| synthetic_alpha |      1.0000e-01 | tv_time  |      5 | heat_diffusion_temporal | 7.1687e-02 |
| synthetic_alpha |      2.0000e-01 | instant  |      1 | mean                    | 9.2631e-02 |
| synthetic_alpha |      2.0000e-01 | instant  |      2 | idw                     | 9.7497e-02 |
| synthetic_alpha |      2.0000e-01 | instant  |      3 | gsmooth                 | 9.8254e-02 |
| synthetic_alpha |      2.0000e-01 | instant  |      4 | gsp                     | 1.0716e-01 |
| synthetic_alpha |      2.0000e-01 | instant  |      5 | linear                  | 1.1148e-01 |
| synthetic_alpha |      2.0000e-01 | tv_time  |      1 | trss                    | 6.3448e-02 |
| synthetic_alpha |      2.0000e-01 | tv_time  |      2 | tv                      | 9.4254e-02 |
| synthetic_alpha |      2.0000e-01 | tv_time  |      3 | wavelet_temporal        | 1.1611e-01 |
| synthetic_alpha |      2.0000e-01 | tv_time  |      4 | directed_tv             | 1.3461e-01 |
| synthetic_alpha |      2.0000e-01 | tv_time  |      5 | spline_temporal         | 1.9913e-01 |
| synthetic_alpha |      3.0000e-01 | instant  |      1 | mean                    | 1.5236e-01 |
| synthetic_alpha |      3.0000e-01 | instant  |      2 | idw                     | 1.5952e-01 |
| synthetic_alpha |      3.0000e-01 | instant  |      3 | gsmooth                 | 1.6070e-01 |
| synthetic_alpha |      3.0000e-01 | instant  |      4 | gsp                     | 1.7636e-01 |
| synthetic_alpha |      3.0000e-01 | instant  |      5 | linear                  | 1.9172e-01 |
| synthetic_alpha |      3.0000e-01 | tv_time  |      1 | trss                    | 1.0946e-01 |
| synthetic_alpha |      3.0000e-01 | tv_time  |      2 | tv                      | 1.5432e-01 |
| synthetic_alpha |      3.0000e-01 | tv_time  |      3 | wavelet_temporal        | 1.7124e-01 |
| synthetic_alpha |      3.0000e-01 | tv_time  |      4 | directed_tv             | 1.9976e-01 |
| synthetic_alpha |      3.0000e-01 | tv_time  |      5 | spline_temporal         | 2.3857e-01 |
| synthetic_alpha |      4.0000e-01 | instant  |      1 | mean                    | 2.2419e-01 |
| synthetic_alpha |      4.0000e-01 | instant  |      2 | gsmooth                 | 2.3355e-01 |
| synthetic_alpha |      4.0000e-01 | instant  |      3 | idw                     | 2.3414e-01 |
| synthetic_alpha |      4.0000e-01 | instant  |      4 | gsp                     | 2.5004e-01 |
| synthetic_alpha |      4.0000e-01 | instant  |      5 | linear                  | 2.6570e-01 |
| synthetic_alpha |      4.0000e-01 | tv_time  |      1 | trss                    | 1.7647e-01 |
| synthetic_alpha |      4.0000e-01 | tv_time  |      2 | tv                      | 2.2615e-01 |
| synthetic_alpha |      4.0000e-01 | tv_time  |      3 | wavelet_temporal        | 2.4537e-01 |
| synthetic_alpha |      4.0000e-01 | tv_time  |      4 | spline_temporal         | 2.7479e-01 |
| synthetic_alpha |      4.0000e-01 | tv_time  |      5 | directed_tv             | 2.7584e-01 |
| synthetic_beta  |      1.0000e-01 | instant  |      1 | mean                    | 3.4227e-02 |
| synthetic_beta  |      1.0000e-01 | instant  |      2 | gsmooth                 | 3.4450e-02 |
| synthetic_beta  |      1.0000e-01 | instant  |      3 | idw                     | 3.4478e-02 |
| synthetic_beta  |      1.0000e-01 | instant  |      4 | gsp                     | 3.5957e-02 |
| synthetic_beta  |      1.0000e-01 | instant  |      5 | rbfi_tps                | 3.9382e-02 |
| synthetic_beta  |      1.0000e-01 | tv_time  |      1 | trss                    | 2.7500e-02 |
| synthetic_beta  |      1.0000e-01 | tv_time  |      2 | tv                      | 3.3991e-02 |
| synthetic_beta  |      1.0000e-01 | tv_time  |      3 | directed_tv             | 4.5687e-02 |
| synthetic_beta  |      1.0000e-01 | tv_time  |      4 | heat_diffusion_temporal | 6.6158e-02 |
| synthetic_beta  |      1.0000e-01 | tv_time  |      5 | wavelet_temporal        | 7.9538e-02 |

## 3. Mejor Método por Dataset × Nivel de Pérdida

| dataset         |   missing_ratio | method   | family   |   best_mae |   best_dtw |   best_rmse |   best_snr |
|:----------------|----------------:|:---------|:---------|-----------:|-----------:|------------:|-----------:|
| synthetic_alpha |      1.0000e-01 | trss     | tv_time  | 1.6658e-02 | 5.0972e-01 |  8.5543e-02 | 2.0382e+01 |
| synthetic_alpha |      2.0000e-01 | trss     | tv_time  | 4.8988e-02 | 9.9206e-01 |  1.4901e-01 | 1.4104e+01 |
| synthetic_alpha |      3.0000e-01 | trss     | tv_time  | 8.5873e-02 | 1.3483e+00 |  2.0407e-01 | 1.1242e+01 |
| synthetic_alpha |      4.0000e-01 | trss     | tv_time  | 1.4363e-01 | 1.7886e+00 |  2.8280e-01 | 8.1725e+00 |
| synthetic_beta  |      1.0000e-01 | trss     | tv_time  | 2.5777e-02 | 1.0364e+00 |  1.2896e-01 | 1.6318e+01 |
| synthetic_beta  |      2.0000e-01 | trss     | tv_time  | 7.9098e-02 | 1.9721e+00 |  2.3074e-01 | 1.0054e+01 |
| synthetic_beta  |      3.0000e-01 | trss     | tv_time  | 1.3576e-01 | 2.4531e+00 |  3.1105e-01 | 7.3720e+00 |
| synthetic_beta  |      4.0000e-01 | trss     | tv_time  | 2.0809e-01 | 3.0950e+00 |  4.0152e-01 | 5.1986e+00 |
| synthetic_broad |      1.0000e-01 | trss     | tv_time  | 3.6118e-02 | 1.1101e+00 |  1.7077e-01 | 1.4374e+01 |
| synthetic_broad |      2.0000e-01 | trss     | tv_time  | 1.1366e-01 | 2.1495e+00 |  3.0912e-01 | 8.2638e+00 |
| synthetic_broad |      3.0000e-01 | trss     | tv_time  | 1.4230e-01 | 2.4094e+00 |  3.4184e-01 | 6.8925e+00 |
| synthetic_broad |      4.0000e-01 | trss     | tv_time  | 2.2725e-01 | 3.0314e+00 |  4.3810e-01 | 4.7975e+00 |

## 4. Sensibilidad al Método de Grafo (Top-20)

| graph_method   | method   |   mae_mean |
|:---------------|:---------|-----------:|
| gaussian       | trss     | 1.0527e-01 |
| vknng          | trss     | 1.1263e-01 |
| knng           | trss     | 1.1313e-01 |
| knn            | trss     | 1.1330e-01 |
| nnk            | trss     | 1.1894e-01 |
| kalofolias     | trss     | 1.2301e-01 |
| aew            | trss     | 1.2431e-01 |
| gaussian       | tv       | 1.3256e-01 |
| knn            | mean     | 1.3259e-01 |
| knng           | mean     | 1.3259e-01 |
| gaussian       | mean     | 1.3259e-01 |
| nnk            | mean     | 1.3259e-01 |
| kalofolias     | mean     | 1.3259e-01 |
| vknng          | mean     | 1.3259e-01 |
| aew            | mean     | 1.3259e-01 |
| kalofolias     | tv       | 1.3259e-01 |
| vknng          | tv       | 1.3273e-01 |
| knng           | tv       | 1.3284e-01 |
| gaussian       | gsmooth  | 1.3294e-01 |
| knn            | tv       | 1.3295e-01 |

## 5. Comparación de Familias

| family   |   mae_mean |    mae_std |   dtw_mean |   snr_mean |   n_runs |
|:---------|-----------:|-----------:|-----------:|-----------:|---------:|
| instant  | 4.6671e-01 | 1.7429e+00 | 2.0749e+01 | 4.0173e+00 |     1536 |
| tv_time  | 2.6098e-01 | 2.1906e-01 | 3.3334e+00 | 5.7557e+00 |      768 |

## 6. Figuras Generadas

- **unified_mae_ranking_bar.png**: Ranking global de métodos por MAE (barras horizontales)
- **unified_mae_vs_missing_ratio.png**: MAE en función del nivel de pérdida para métodos top
- **unified_heatmap_mae_graph_method.png**: Heatmap MAE: grafo × método de interpolación
- **unified_family_boxplot.png**: Boxplot comparativo de familias Instant vs. TV/Tiempo
- **unified_dataset_comparison.png**: Comparación de métodos top por dataset
- **unified_snr_ranking_bar.png**: Ranking de métodos por SNR

## 7. Notas Metodológicas

- Todos los resultados son sobre datasets sintéticos (alpha/beta/broad) debido a restricciones de descarga en entorno cloud.
- Los grafos se construyen con los parámetros de su configuración (ver `run_unified_final.py`).
- La métrica primaria es MAE; DTW y SNR se reportan como métricas secundarias.
- Para métodos con múltiples configuraciones de parámetros, se reporta el mejor resultado en el ranking global.
