# Referencias por metodo - Thesis-Copilot-Toolkit

Este archivo mapea cada metodo activo con su fuente principal y estado de alineacion.

## Actualizacion abril 2026

- BGSRP se normaliza a referencia primaria RKHS:
  - Zhang et al., *Recovery of bandlimited graph signals based on the reproducing kernel Hilbert space* (DSP, 2024).
  - Codigo de contraste: `Papers/Code-for-BGSRP-master/gsp_BGSRP_recon.m`.
- TRSS/sobolev_temporal queda consolidado como mismo nucleo de implementacion.

---

## 1) Construccion de grafos

| Metodo | Referencia principal | Tipo de alineacion |
|---|---|---|
| `knn` | Sakiyama et al., ICASSP 2016 | baseline clasico |
| `knng` | Sakiyama et al., ICASSP 2016 | baseline clasico |
| `vknng` | Tamaru et al., arXiv 2024 | adaptacion inspirada |
| `gaussian` | Karasuyama y Mamitsuka, ML 2017 | baseline clasico |
| `epsilon_ball` | Shuman et al., IEEE SPM 2013 | baseline clasico |
| `mst` | Ortega et al., arXiv 2018 (survey) | baseline clasico |
| `fully_connected_inverse_distance` | metodo geometrico clasico | N/A (sin paper unico) |
| `nnk` | Shekkizhar y Ortega, ICASSP 2020 / arXiv 2023 | paper-aligned |
| `aew` | Karasuyama y Mamitsuka, ML 2017 | implementacion inspirada |
| `kalofolias` | Kalofolias 2016; Kalofolias et al. ICASSP 2017 | aproximacion numerica |

---

## 2) Interpolacion por instante

| Metodo | Referencia principal | Tipo de alineacion |
|---|---|---|
| `linear` | SciPy/NumPy (estandar) | baseline |
| `nearest` | SciPy/NumPy (estandar) | baseline |
| `mean` | baseline estadistico | baseline |
| `random` | baseline estocastico | baseline |
| `idw` | interpolacion IDW clasica | baseline |
| `spherical_spline` | Perrin et al., Electroencephalogr Clin Neurophysiol 1989 | paper-aligned |
| `rbfi_tps` | Jager et al., Clin Neurophysiol 2016 | paper-inspired |
| `rbfi_mq` | Jager et al., Clin Neurophysiol 2016 | paper-inspired |
| `spline_surface` | spline 2D clasico | baseline |
| `gsp` | Narang et al., ICASSP 2013 | paper-inspired |
| `tikhonov` | Narang et al., arXiv 2013 | paper-inspired |
| `gsmooth` | Narang et al., arXiv 2013 | paper-inspired |
| `bgsrp` | Zhang et al., DSP 2024 (RKHS) | paper-aligned (pendiente 1:1) |
| `puy` | Puy et al., ACHA 2018 | paper-inspired |
| `sobolev` | Giraldo et al., IEEE TSIPN 2022 | paper-inspired |

---

## 3) Interpolacion TV/tiempo

| Metodo | Referencia principal | Tipo de alineacion |
|---|---|---|
| `graph_time_tikhonov` | extension temporal de Tikhonov en grafo | derivado |
| `trss` | Giraldo et al., IEEE TSIPN 2022 | paper-aligned |
| `sobolev_temporal` | alias funcional de `trss` | paper-aligned |
| `tv` | Mortaheb et al., EMBC 2019 | paper-inspired |
| `temporal_laplacian` | Jiang et al., IEEE Sensors Journal 2021 | paper-inspired |
| `heat_diffusion_temporal` | diffusion temporal en grafo | derivado |
| `spline_temporal` | spline temporal + regularizacion espacial | derivado |
| `wavelet_temporal` | filtro temporal tipo Haar + regularizacion espacial | derivado |
| `directed_tv` | Schultz y Villafane-Delgado, arXiv 2020 | paper-inspired |
| `adaptive_temporal` | Bozkurt y Ortega, EUSIPCO 2022 | paper-inspired |

---

## Referencias clave (citas cortas)

- Perrin F, et al. (1989). *Spherical splines for scalp potential and current density mapping*. DOI: 10.1016/0013-4694(89)90180-6
- Narang SK, et al. (2013). *Signal processing techniques for interpolation in graph structured data*. DOI: 10.1109/ICASSP.2013.6638704
- Puy G, et al. (2018). *Random sampling of bandlimited signals on graphs*. DOI: 10.1016/j.acha.2016.05.005
- Shekkizhar S, Ortega A (2020). *Graph Construction from Data by Non-Negative Kernel Regression*. DOI: 10.1109/ICASSP40776.2020.9054425
- Giraldo JH, et al. (2022). *Reconstruction of Time-Varying Graph Signals via Sobolev Smoothness*. DOI: 10.1109/TSIPN.2022.3156886
- Bozkurt E, Ortega A (2022). *Non-Negative Kernel Graphs for Time-Varying Signals Using Visibility Graphs*. DOI: 10.23919/EUSIPCO55093.2022.9909594
- Zhang Q, et al. (2024). *Recovery of bandlimited graph signals based on the reproducing kernel Hilbert space*. DOI: 10.1016/j.dsp.2024.104565

---

## Evidencia relacionada en repo

- `results/bgsrp_vs_narang_check_summary.csv`
- `results/graphtrss_main_figure_summary.csv`
- `tests/test_paper_faithful.py`
