# Reporte Canónico Final — Experimento Unificado EEG-GSP

> Generado automáticamente por `run_canonical_experiment.py`
> Fecha: 2026-04-09 13:36
> Protocolo: Validación Anidada (inner=60% ajuste, outer=40% reporte)

## Resumen Ejecutivo

- **Corridas válidas (outer fold):** 2816
- **Datasets sintéticos:** 3 (synthetic_alpha, synthetic_beta, synthetic_broad)
- **Datasets reales incluidos:** 1 (physionet_eegmmidb — sujetos [1, 2, 3, 4, 5])
- **BCI Competition IV 2a:** NO DISPONIBLE — declarado formalmente como PROXY/EXCLUIDO de afirmaciones fuertes
- **Métodos de interpolación:** 22
- **Métodos de grafo:** 7
- **Niveles de pérdida:** ['10pct', '20pct', '30pct', '40pct']
- **Unidades de señal PhysioNet:** Voltios (EEG en V desde MNE; MAE ~1e-6 V es normal)

**Mejor método global** (menor MAE — outer fold): `mean` (familia: instant, MAE=1.2503e-01 ± 9.5316e-02)

## Declaración Explícita: BCI Competition IV 2a

> ⚠️ **BCI Competition IV 2a — PROXY / NO DISPONIBLE**
>
> BCI Competition IV Dataset 2a (.gdf) requires manual download from https://www.bbci.de/competition/iv/. Files not found in BCI_IV_2A_PATH. This dataset is formally declared as PROXY/NOT AVAILABLE for this run. Any results referencing bci_competition_iv_2a in this context are excluded from strong empirical claims.
>
> **Decisión formal:** Este dataset se excluye de todas las afirmaciones empíricas fuertes
> de este experimento. Los resultados sobre physionet_eegmmidb son los únicos resultados
> con datos EEG reales validados en esta corrida.

## 1. Ranking Global por MAE (outer fold)

|   rank | method                  | family   |     mae_mean |      mae_std |    rmse_mean |     snr_mean |   n_runs |
|-------:|:------------------------|:---------|-------------:|-------------:|-------------:|-------------:|---------:|
|      1 | mean                    | instant  |   1.2503e-01 |   9.5316e-02 |   2.7296e-01 |   3.4525e-01 |      128 |
|      2 | gsmooth                 | instant  |   1.2621e-01 |   9.5983e-02 |   2.7682e-01 |   3.3583e-01 |      128 |
|      3 | tv                      | tv_time  |   1.2645e-01 |   9.6275e-02 |   2.7794e-01 |   2.3760e-01 |      128 |
|      4 | idw                     | instant  |   1.2686e-01 |   9.6667e-02 |   2.7933e-01 |   2.8500e-01 |      128 |
|      5 | trss                    | tv_time  |   1.3032e-01 |   9.9785e-02 |   2.8924e-01 |   1.9624e-02 |      128 |
|      6 | directed_tv             | tv_time  |   1.3104e-01 |   9.9644e-02 |   2.9124e-01 |  -3.9185e-01 |      128 |
|      7 | gsp                     | instant  |   1.3390e-01 |   1.0299e-01 |   3.0121e-01 |  -2.7163e-01 |      128 |
|      8 | wavelet_temporal        | tv_time  |   1.3812e-01 |   1.0019e-01 |   2.7209e-01 |   1.7924e+01 |      128 |
|      9 | linear                  | instant  |   1.4643e-01 |   1.1171e-01 |   3.3592e-01 |  -6.2659e-01 |      128 |
|     10 | nearest                 | instant  |   1.6342e-01 |   1.2374e-01 |   3.8213e-01 |  -1.5746e+00 |      128 |
|     11 | rbfi_tps                | instant  |   1.6642e-01 |   1.3214e-01 |   3.8979e-01 |  -2.0054e+00 |      128 |
|     12 | rbfi_mq                 | instant  |   1.7383e-01 |   1.3266e-01 |   4.1283e-01 |  -2.7581e+00 |      128 |
|     13 | spherical_spline        | instant  |   1.8588e-01 |   1.5998e-01 |   4.3865e-01 |  -3.0430e+00 |      128 |
|     14 | tikhonov                | instant  |   2.1299e-01 |   1.7068e-01 |   3.3127e-01 |   1.2946e+01 |      128 |
|     15 | spline_surface          | instant  |   2.3216e-01 |   1.9937e-01 |   6.1561e-01 |  -4.9740e+00 |      128 |
|     16 | heat_diffusion_temporal | tv_time  |   2.4695e-01 |   4.5138e-01 |   5.0057e-01 |  -1.2512e+00 |      128 |
|     17 | graph_time_tikhonov     | tv_time  |   3.0738e-01 |   2.0137e-01 |   3.8365e-01 |   5.3185e+00 |      128 |
|     18 | puy                     | instant  |   3.1188e-01 |   2.1418e-01 |   4.1101e-01 |   6.6976e+00 |      128 |
|     19 | temporal_laplacian      | tv_time  |   3.4558e-01 |   2.1266e-01 |   4.0377e-01 |   3.2495e+00 |      128 |
|     20 | bgsrp                   | instant  |   3.8201e-01 |   2.2593e-01 |   4.7622e-01 |   2.8818e+00 |      128 |
|     21 | sobolev                 | instant  |   4.1030e-01 |   2.4511e-01 |   4.6569e-01 |   1.9821e+00 |      128 |
|     22 | spline_temporal         | tv_time  | nan          | nan          | nan          | nan          |        0 |

## 2. Ranking por Dataset (outer fold)

### physionet_eegmmidb [REAL]

|   rank | method                  | family   |     mae_mean |      mae_std |    rmse_mean |     snr_mean |
|-------:|:------------------------|:---------|-------------:|-------------:|-------------:|-------------:|
|      0 | spline_temporal         | tv_time  | nan          | nan          | nan          | nan          |
|      1 | linear                  | instant  |   7.4641e-06 |   3.8705e-06 |   2.2009e-05 |   3.4589e+00 |
|      2 | tv                      | tv_time  |   7.5747e-06 |   3.1695e-06 |   2.1420e-05 |   2.0854e+00 |
|      3 | mean                    | instant  |   7.5810e-06 |   3.1670e-06 |   2.1466e-05 |   2.0423e+00 |
|      4 | gsmooth                 | instant  |   7.8317e-06 |   3.5511e-06 |   2.1678e-05 |   2.4218e+00 |
|      5 | heat_diffusion_temporal | tv_time  |   7.8599e-06 |   3.6874e-06 |   2.2378e-05 |   2.0246e+00 |
|      6 | nearest                 | instant  |   7.9708e-06 |   3.7905e-06 |   2.4883e-05 |   3.0449e+00 |
|      7 | trss                    | tv_time  |   8.2145e-06 |   3.9568e-06 |   2.2630e-05 |   2.2907e+00 |
|      8 | idw                     | instant  |   8.3010e-06 |   3.8201e-06 |   2.3012e-05 |   2.4164e+00 |
|      9 | gsp                     | instant  |   8.4291e-06 |   4.1373e-06 |   2.3113e-05 |   2.0973e+00 |
|     10 | directed_tv             | tv_time  |   8.7588e-06 |   4.2093e-06 |   2.4611e-05 |   7.5866e-01 |
|     11 | rbfi_tps                | instant  |   9.4286e-06 |   4.7650e-06 |   2.4999e-05 |   1.5066e+00 |
|     12 | wavelet_temporal        | tv_time  |   9.5798e-06 |   4.3989e-06 |   2.6038e-05 |   2.4673e+01 |
|     13 | rbfi_mq                 | instant  |   1.0440e-05 |   4.8317e-06 |   2.7860e-05 |   1.0230e-01 |
|     14 | spherical_spline        | instant  |   1.2775e-05 |   6.4788e-06 |   3.8936e-05 |  -1.1662e+00 |

### synthetic_alpha [SYNTHETIC]

|   rank | method           | family   |     mae_mean |      mae_std |    rmse_mean |     snr_mean |
|-------:|:-----------------|:---------|-------------:|-------------:|-------------:|-------------:|
|      0 | spline_temporal  | tv_time  | nan          | nan          | nan          | nan          |
|      1 | mean             | instant  |   1.6397e-01 |   7.3170e-02 |   3.5488e-01 |   7.4172e-02 |
|      2 | tv               | tv_time  |   1.6924e-01 |   7.5699e-02 |   3.6897e-01 |  -2.6386e-01 |
|      3 | idw              | instant  |   1.6971e-01 |   7.6462e-02 |   3.6969e-01 |  -2.9360e-01 |
|      4 | gsmooth          | instant  |   1.6983e-01 |   7.5595e-02 |   3.6977e-01 |  -3.3371e-01 |
|      5 | wavelet_temporal | tv_time  |   1.7902e-01 |   7.4563e-02 |   3.5632e-01 |   1.7703e+01 |
|      6 | trss             | tv_time  |   1.8191e-01 |   8.4745e-02 |   3.9955e-01 |  -9.9734e-01 |
|      7 | directed_tv      | tv_time  |   1.8736e-01 |   8.2998e-02 |   4.1301e-01 |  -1.2516e+00 |
|      8 | gsp              | instant  |   1.8984e-01 |   9.0592e-02 |   4.2356e-01 |  -1.4396e+00 |
|      9 | linear           | instant  |   1.9756e-01 |   8.7972e-02 |   4.4415e-01 |  -1.7542e+00 |
|     10 | nearest          | instant  |   2.2335e-01 |   9.4004e-02 |   5.1933e-01 |  -3.1280e+00 |
|     11 | rbfi_tps         | instant  |   2.2412e-01 |   9.7849e-02 |   5.2380e-01 |  -3.2545e+00 |
|     12 | rbfi_mq          | instant  |   2.3090e-01 |   9.4457e-02 |   5.5092e-01 |  -3.6279e+00 |
|     13 | spherical_spline | instant  |   2.7294e-01 |   1.0849e-01 |   6.6421e-01 |  -5.0246e+00 |
|     14 | tikhonov         | instant  |   2.8937e-01 |   1.2927e-01 |   4.5206e-01 |   1.2006e+01 |

### synthetic_beta [SYNTHETIC]

|   rank | method           | family   |     mae_mean |      mae_std |    rmse_mean |     snr_mean |
|-------:|:-----------------|:---------|-------------:|-------------:|-------------:|-------------:|
|      0 | spline_temporal  | tv_time  | nan          | nan          | nan          | nan          |
|      1 | directed_tv      | tv_time  |   1.7041e-01 |   7.4867e-02 |   3.7142e-01 |  -3.5095e-01 |
|      2 | gsmooth          | instant  |   1.7110e-01 |   7.6045e-02 |   3.7011e-01 |  -2.8786e-01 |
|      3 | idw              | instant  |   1.7124e-01 |   7.5899e-02 |   3.7083e-01 |  -3.1165e-01 |
|      4 | mean             | instant  |   1.7203e-01 |   7.7722e-02 |   3.6965e-01 |  -2.8357e-01 |
|      5 | tv               | tv_time  |   1.7204e-01 |   7.6808e-02 |   3.7198e-01 |  -3.3458e-01 |
|      6 | trss             | tv_time  |   1.7306e-01 |   7.4973e-02 |   3.8000e-01 |  -5.3612e-01 |
|      7 | gsp              | instant  |   1.7554e-01 |   7.5428e-02 |   3.8978e-01 |  -7.4424e-01 |
|      8 | wavelet_temporal | tv_time  |   1.9083e-01 |   7.3657e-02 |   3.6875e-01 |   1.4157e+01 |
|      9 | linear           | instant  |   2.0319e-01 |   9.1986e-02 |   4.6564e-01 |  -2.3342e+00 |
|     10 | nearest          | instant  |   2.2513e-01 |   1.0272e-01 |   5.2092e-01 |  -3.2874e+00 |
|     11 | rbfi_mq          | instant  |   2.2765e-01 |   1.1050e-01 |   5.3099e-01 |  -3.2741e+00 |
|     12 | rbfi_tps         | instant  |   2.3452e-01 |   1.2838e-01 |   5.4124e-01 |  -3.2529e+00 |
|     13 | tikhonov         | instant  |   2.8405e-01 |   1.4450e-01 |   4.3487e-01 |   1.2382e+01 |
|     14 | spherical_spline | instant  |   3.0646e-01 |   1.7270e-01 |   7.2307e-01 |  -5.5293e+00 |

### synthetic_broad [SYNTHETIC]

|   rank | method           | family   |     mae_mean |      mae_std |    rmse_mean |     snr_mean |
|-------:|:-----------------|:---------|-------------:|-------------:|-------------:|-------------:|
|      0 | spline_temporal  | tv_time  | nan          | nan          | nan          | nan          |
|      1 | gsmooth          | instant  |   1.6392e-01 |   6.5517e-02 |   3.6737e-01 |  -4.5690e-01 |
|      2 | mean             | instant  |   1.6411e-01 |   6.5337e-02 |   3.6731e-01 |  -4.5190e-01 |
|      3 | spherical_spline | instant  |   1.6411e-01 |   6.5337e-02 |   3.6731e-01 |  -4.5190e-01 |
|      4 | tv               | tv_time  |   1.6451e-01 |   6.5640e-02 |   3.7077e-01 |  -5.3655e-01 |
|      5 | trss             | tv_time  |   1.6630e-01 |   6.7011e-02 |   3.7739e-01 |  -6.7877e-01 |
|      6 | directed_tv      | tv_time  |   1.6637e-01 |   6.5544e-02 |   3.8049e-01 |  -7.2352e-01 |
|      7 | idw              | instant  |   1.6650e-01 |   6.7188e-02 |   3.7676e-01 |  -6.7110e-01 |
|      8 | gsp              | instant  |   1.7021e-01 |   6.8324e-02 |   3.9149e-01 |  -9.9998e-01 |
|      9 | wavelet_temporal | tv_time  |   1.8263e-01 |   6.1706e-02 |   3.6327e-01 |   1.5162e+01 |
|     10 | linear           | instant  |   1.8497e-01 |   7.2343e-02 |   4.3386e-01 |  -1.8768e+00 |
|     11 | nearest          | instant  |   2.0517e-01 |   7.9612e-02 |   4.8823e-01 |  -2.9277e+00 |
|     12 | rbfi_tps         | instant  |   2.0701e-01 |   8.3457e-02 |   4.9410e-01 |  -3.0210e+00 |
|     13 | spline_surface   | instant  |   2.0701e-01 |   8.3457e-02 |   4.9410e-01 |  -3.0210e+00 |
|     14 | rbfi_mq          | instant  |   2.3677e-01 |   9.6610e-02 |   5.6937e-01 |  -4.2327e+00 |

## 3. Top-5 por Dataset × Nivel de Pérdida × Familia

| dataset            | scenario   | family   |   rank | method                  |   mae_mean |
|:-------------------|:-----------|:---------|-------:|:------------------------|-----------:|
| physionet_eegmmidb | 10pct      | instant  |      1 | rbfi_tps                | 1.7885e-06 |
| physionet_eegmmidb | 10pct      | instant  |      2 | gsp                     | 2.1071e-06 |
| physionet_eegmmidb | 10pct      | instant  |      3 | linear                  | 2.1450e-06 |
| physionet_eegmmidb | 10pct      | instant  |      4 | idw                     | 2.1823e-06 |
| physionet_eegmmidb | 10pct      | instant  |      5 | gsmooth                 | 2.2093e-06 |
| physionet_eegmmidb | 10pct      | tv_time  |      1 | trss                    | 2.1067e-06 |
| physionet_eegmmidb | 10pct      | tv_time  |      2 | heat_diffusion_temporal | 2.2504e-06 |
| physionet_eegmmidb | 10pct      | tv_time  |      3 | directed_tv             | 2.4204e-06 |
| physionet_eegmmidb | 10pct      | tv_time  |      4 | tv                      | 2.5704e-06 |
| physionet_eegmmidb | 10pct      | tv_time  |      5 | wavelet_temporal        | 2.9511e-06 |
| physionet_eegmmidb | 20pct      | instant  |      1 | nearest                 | 7.1364e-06 |
| physionet_eegmmidb | 20pct      | instant  |      2 | linear                  | 7.1883e-06 |
| physionet_eegmmidb | 20pct      | instant  |      3 | mean                    | 7.9187e-06 |
| physionet_eegmmidb | 20pct      | instant  |      4 | gsmooth                 | 8.2506e-06 |
| physionet_eegmmidb | 20pct      | instant  |      5 | gsp                     | 8.5647e-06 |
| physionet_eegmmidb | 20pct      | tv_time  |      1 | tv                      | 7.9286e-06 |
| physionet_eegmmidb | 20pct      | tv_time  |      2 | heat_diffusion_temporal | 7.9952e-06 |
| physionet_eegmmidb | 20pct      | tv_time  |      3 | trss                    | 8.3565e-06 |
| physionet_eegmmidb | 20pct      | tv_time  |      4 | directed_tv             | 8.7528e-06 |
| physionet_eegmmidb | 20pct      | tv_time  |      5 | wavelet_temporal        | 9.4972e-06 |
| physionet_eegmmidb | 30pct      | instant  |      1 | linear                  | 7.6128e-06 |
| physionet_eegmmidb | 30pct      | instant  |      2 | mean                    | 8.6745e-06 |
| physionet_eegmmidb | 30pct      | instant  |      3 | nearest                 | 8.9686e-06 |
| physionet_eegmmidb | 30pct      | instant  |      4 | gsmooth                 | 9.2253e-06 |
| physionet_eegmmidb | 30pct      | instant  |      5 | idw                     | 9.7521e-06 |
| physionet_eegmmidb | 30pct      | tv_time  |      1 | tv                      | 8.6866e-06 |
| physionet_eegmmidb | 30pct      | tv_time  |      2 | heat_diffusion_temporal | 8.9550e-06 |
| physionet_eegmmidb | 30pct      | tv_time  |      3 | directed_tv             | 9.8872e-06 |
| physionet_eegmmidb | 30pct      | tv_time  |      4 | trss                    | 1.0025e-05 |
| physionet_eegmmidb | 30pct      | tv_time  |      5 | wavelet_temporal        | 1.0876e-05 |
| physionet_eegmmidb | 40pct      | instant  |      1 | mean                    | 1.1139e-05 |
| physionet_eegmmidb | 40pct      | instant  |      2 | gsmooth                 | 1.1642e-05 |
| physionet_eegmmidb | 40pct      | instant  |      3 | idw                     | 1.2383e-05 |
| physionet_eegmmidb | 40pct      | instant  |      4 | linear                  | 1.2910e-05 |
| physionet_eegmmidb | 40pct      | instant  |      5 | gsp                     | 1.2942e-05 |
| physionet_eegmmidb | 40pct      | tv_time  |      1 | tv                      | 1.1113e-05 |
| physionet_eegmmidb | 40pct      | tv_time  |      2 | heat_diffusion_temporal | 1.2239e-05 |
| physionet_eegmmidb | 40pct      | tv_time  |      3 | trss                    | 1.2370e-05 |
| physionet_eegmmidb | 40pct      | tv_time  |      4 | directed_tv             | 1.3975e-05 |
| physionet_eegmmidb | 40pct      | tv_time  |      5 | wavelet_temporal        | 1.4995e-05 |
| synthetic_alpha    | 10pct      | instant  |      1 | mean                    | 6.1771e-02 |
| synthetic_alpha    | 10pct      | instant  |      2 | idw                     | 6.7943e-02 |
| synthetic_alpha    | 10pct      | instant  |      3 | gsmooth                 | 6.8500e-02 |
| synthetic_alpha    | 10pct      | instant  |      4 | gsp                     | 8.2877e-02 |
| synthetic_alpha    | 10pct      | instant  |      5 | linear                  | 8.5152e-02 |
| synthetic_alpha    | 10pct      | tv_time  |      1 | tv                      | 6.6117e-02 |
| synthetic_alpha    | 10pct      | tv_time  |      2 | trss                    | 7.8107e-02 |
| synthetic_alpha    | 10pct      | tv_time  |      3 | wavelet_temporal        | 8.1576e-02 |
| synthetic_alpha    | 10pct      | tv_time  |      4 | directed_tv             | 8.8752e-02 |
| synthetic_alpha    | 10pct      | tv_time  |      5 | heat_diffusion_temporal | 1.3885e-01 |
| synthetic_alpha    | 20pct      | instant  |      1 | idw                     | 1.4420e-01 |
| synthetic_alpha    | 20pct      | instant  |      2 | gsmooth                 | 1.4595e-01 |
| synthetic_alpha    | 20pct      | instant  |      3 | mean                    | 1.4647e-01 |
| synthetic_alpha    | 20pct      | instant  |      4 | gsp                     | 1.4820e-01 |
| synthetic_alpha    | 20pct      | instant  |      5 | nearest                 | 1.7314e-01 |
| synthetic_alpha    | 20pct      | tv_time  |      1 | trss                    | 1.4330e-01 |
| synthetic_alpha    | 20pct      | tv_time  |      2 | directed_tv             | 1.4370e-01 |
| synthetic_alpha    | 20pct      | tv_time  |      3 | wavelet_temporal        | 1.4524e-01 |
| synthetic_alpha    | 20pct      | tv_time  |      4 | tv                      | 1.4783e-01 |
| synthetic_alpha    | 20pct      | tv_time  |      5 | heat_diffusion_temporal | 2.6333e-01 |

## 4. Mejor Método por Dataset × Nivel de Pérdida

| dataset            | data_source   | scenario   | method      | family   |   best_mae |   best_rmse |    best_snr |
|:-------------------|:--------------|:-----------|:------------|:---------|-----------:|------------:|------------:|
| physionet_eegmmidb | real          | 10pct      | gsp         | instant  | 1.7405e-06 |  7.9240e-06 |  3.7406e+00 |
| physionet_eegmmidb | real          | 20pct      | nearest     | instant  | 7.1364e-06 |  3.1325e-05 |  4.6460e+00 |
| physionet_eegmmidb | real          | 30pct      | linear      | instant  | 7.6128e-06 |  1.7837e-05 |  4.2555e+00 |
| physionet_eegmmidb | real          | 40pct      | trss        | tv_time  | 1.0629e-05 |  2.2921e-05 |  4.1627e+00 |
| synthetic_alpha    | synthetic     | 10pct      | mean        | instant  | 6.1771e-02 |  2.1528e-01 |  5.8591e-01 |
| synthetic_alpha    | synthetic     | 20pct      | directed_tv | tv_time  | 1.3032e-01 |  3.2578e-01 |  1.9009e-01 |
| synthetic_alpha    | synthetic     | 30pct      | tv          | tv_time  | 1.8608e-01 |  3.7825e-01 |  4.4625e-01 |
| synthetic_alpha    | synthetic     | 40pct      | tv          | tv_time  | 2.6114e-01 |  4.5913e-01 |  1.4521e-01 |
| synthetic_beta     | synthetic     | 10pct      | directed_tv | tv_time  | 6.6913e-02 |  2.3004e-01 |  1.1295e-02 |
| synthetic_beta     | synthetic     | 20pct      | directed_tv | tv_time  | 1.3066e-01 |  3.2455e-01 |  1.1524e-01 |
| synthetic_beta     | synthetic     | 30pct      | trss        | tv_time  | 1.9647e-01 |  4.0090e-01 |  1.6403e-01 |
| synthetic_beta     | synthetic     | 40pct      | directed_tv | tv_time  | 2.4580e-01 |  4.5698e-01 |  1.0561e+00 |
| synthetic_broad    | synthetic     | 10pct      | directed_tv | tv_time  | 7.9660e-02 |  2.5295e-01 | -3.7838e-03 |
| synthetic_broad    | synthetic     | 20pct      | directed_tv | tv_time  | 1.1558e-01 |  3.1046e-01 | -3.8827e-02 |
| synthetic_broad    | synthetic     | 30pct      | directed_tv | tv_time  | 1.9496e-01 |  3.9470e-01 |  5.6674e-02 |
| synthetic_broad    | synthetic     | 40pct      | directed_tv | tv_time  | 2.4004e-01 |  4.3995e-01 | -3.0938e-02 |

## 5. Sensibilidad al Método de Grafo (Top-20)

| graph_method   | method                  |   mae_mean |
|:---------------|:------------------------|-----------:|
| aew            | heat_diffusion_temporal | 1.2331e-01 |
| kalofolias     | directed_tv             | 1.2360e-01 |
| aew            | trss                    | 1.2362e-01 |
| gaussian       | directed_tv             | 1.2396e-01 |
| nnk            | heat_diffusion_temporal | 1.2402e-01 |
| knng           | heat_diffusion_temporal | 1.2411e-01 |
| gaussian       | heat_diffusion_temporal | 1.2427e-01 |
| vknng          | heat_diffusion_temporal | 1.2455e-01 |
| knn            | heat_diffusion_temporal | 1.2457e-01 |
| aew            | gsmooth                 | 1.2492e-01 |
| knn            | mean                    | 1.2503e-01 |
| kalofolias     | mean                    | 1.2503e-01 |
| knng           | mean                    | 1.2503e-01 |
| gaussian       | mean                    | 1.2503e-01 |
| aew            | mean                    | 1.2503e-01 |
| nnk            | mean                    | 1.2503e-01 |
| vknng          | mean                    | 1.2503e-01 |
| gaussian       | gsmooth                 | 1.2503e-01 |
| kalofolias     | tv                      | 1.2505e-01 |
| gaussian       | tv                      | 1.2505e-01 |

## 6. Comparación de Familias por Tipo de Dato

| data_source   | family   |   mae_mean |    mae_std |   rmse_mean |    snr_mean |   n_runs |
|:--------------|:---------|-----------:|-----------:|------------:|------------:|---------:|
| real          | tv_time  | 1.2856e-05 | 8.2822e-06 |  2.7182e-05 |  5.9710e+00 |      224 |
| real          | instant  | 1.2868e-05 | 7.8045e-06 |  2.9055e-05 |  3.2112e+00 |      448 |
| synthetic     | tv_time  | 2.7158e-01 | 2.3236e-01 |  4.6065e-01 |  2.7918e+00 |      672 |
| synthetic     | instant  | 2.7593e-01 | 1.5963e-01 |  5.1327e-01 | -9.7041e-02 |     1344 |

## 7. Figuras Generadas

- **canonical_mae_ranking_bar.png**: Ranking global de métodos por MAE (outer fold)
- **canonical_dataset_comparison.png**: Comparación métodos top por dataset
- **canonical_heatmap_mae.png**: Heatmap MAE: grafo × método
- **canonical_mae_vs_missing.png**: MAE vs. nivel de pérdida
- **canonical_family_boxplot.png**: Boxplot familias por tipo de dato

## 8. Notas Metodológicas

- Selección de parámetros: inner-fold temporal (60% primeras muestras) con búsqueda exhaustiva en grilla; evaluación final en outer-fold (40% últimas muestras).
- Datasets sintéticos (alpha/beta/broad): señales EEG simuladas con frecuencias en bandas características y geometría esférica/circular. Son la base robusta del análisis.
- Dataset real: physionet_eegmmidb (sujetos [1, 2, 3, 4, 5], run motor imagery). Cargado desde archivos EDF locales (22 canales subseleccionados, 160 Hz). Señales en Voltios; MAE del orden de 1e-6 V es esperado y correcto para EEG en V.
- BCI Competition IV 2a: archivos .gdf no disponibles. Declarado formalmente como proxy/excluido. No se hacen afirmaciones empíricas sobre este dataset.
- Métrica primaria: MAE. RMSE y SNR como métricas secundarias. DTW omitido en corrida completa para eficiencia (ver resultados previos en unified_final_raw.csv).
- Los grafos se construyen sobre el conjunto completo de señales para topología estable.
