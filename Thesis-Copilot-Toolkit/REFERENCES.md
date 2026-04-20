# Referencias por metodo - Thesis-Copilot-Toolkit

Este archivo mapea cada metodo activo con su fuente principal y estado de alineacion.

## Leyenda de tickets

- ✓: Implementado y validado en corridas internas
- ✓✓: Implementado, validado y con evidencia paper-faithful fuerte
- ⚠: Implementado, pero con validacion paper-faithful parcial o pendiente

## Actualizacion abril 2026

- BGSRP se normaliza a referencia primaria RKHS:
  - Zhang et al., *Recovery of bandlimited graph signals based on the reproducing kernel Hilbert space* (DSP, 2024).
  - Codigo de contraste: `Papers/Code-for-BGSRP-master/gsp_BGSRP_recon.m`.
- TRSS/sobolev_temporal queda consolidado como mismo nucleo de implementacion.
- Cierre B3/B4 completado con significancia estadistica (STAT-02) y tabla final consolidada (REP-01).
- INS-13 se mantiene como cierre proxy controlado en Python, pendiente equivalencia estricta 1:1 MATLAB/GSPBox.

---

## 1) Construccion de grafos

| Ticket | Metodo | Referencia principal | Tipo de alineacion | Estado Validacion |
|---|---|---|---|---|
| GRA-01 | `knn` | Sakiyama et al., ICASSP 2016 | baseline clasico | ✓ |
| GRA-02 | `knng` | Sakiyama et al., ICASSP 2016 | baseline clasico | ✓ |
| GRA-03 | `vknng` | Tamaru et al., arXiv 2024 | adaptacion inspirada | ✓ |
| GRA-04 | `gaussian` | Karasuyama y Mamitsuka, ML 2017 | baseline clasico | ✓ |
| GRA-05 | `epsilon_ball` | Shuman et al., IEEE SPM 2013 | baseline clasico | ✓ |
| GRA-06 | `mst` | Ortega et al., arXiv 2018 (survey) | baseline clasico | ✓ |
| GRA-07 | `fully_connected_inverse_distance` | metodo geometrico clasico | N/A (sin paper unico) | ⚠ |
| GRA-08 | `nnk` | Shekkizhar y Ortega, ICASSP 2020 / arXiv 2023 | paper-aligned | ✓✓ |
| GRA-09 | `aew` | Karasuyama y Mamitsuka, ML 2017 | implementacion inspirada | ✓ |
| GRA-10 | `kalofolias` | Kalofolias 2016; Kalofolias et al. ICASSP 2017 | aproximacion numerica | ✓ |

---

## 2) Interpolacion por instante

| Ticket | Metodo | Referencia principal | Tipo de alineacion | Estado Validacion |
|---|---|---|---|---|
| INS-01 | `linear` | SciPy/NumPy (estandar) | baseline | ✓ |
| INS-02 | `nearest` | SciPy/NumPy (estandar) | baseline | ✓ |
| INS-03 | `mean` | baseline estadistico | baseline | ✓ |
| INS-04 | `random` | baseline estocastico | baseline | ✓ |
| INS-05 | `idw` | interpolacion IDW clasica | baseline | ✓ |
| INS-06 | `spherical_spline` | Perrin et al., Electroencephalogr Clin Neurophysiol 1989 | paper-aligned | ✓✓ |
| INS-07 | `rbfi_tps` | Jager et al., Clin Neurophysiol 2016 | paper-inspired | ✓ |
| INS-08 | `rbfi_mq` | Jager et al., Clin Neurophysiol 2016 | paper-inspired | ✓ |
| INS-09 | `spline_surface` | spline 2D clasico | baseline | ✓ |
| INS-10 | `gsp` | Narang et al., ICASSP 2013 | paper-inspired | ✓ |
| INS-11 | `tikhonov` | Narang et al., arXiv 2013 | paper-inspired | ✓ |
| INS-12 | `gsmooth` | Narang et al., arXiv 2013 | paper-inspired | ✓ |
| INS-13 | `bgsrp` | Zhang et al., DSP 2024 (RKHS) | paper-aligned (pendiente 1:1) | ⚠ |
| INS-14 | `puy` | Puy et al., ACHA 2018 | paper-inspired | ✓ |
| INS-15 | `sobolev` | Giraldo et al., IEEE TSIPN 2022 | paper-inspired | ✓ |

---

## 3) Interpolacion TV/tiempo

| Ticket | Metodo | Referencia principal | Tipo de alineacion | Estado Validacion |
|---|---|---|---|---|
| TVT-01 | `graph_time_tikhonov` | Narang et al., arXiv 2013 + Jiang et al., IEEE Sensors Journal 2021 | extension paper-inspired | ✓ |
| TVT-02 | `trss` | Giraldo et al., IEEE TSIPN 2022 | paper-aligned | ✓✓ |
| TVT-03 | `sobolev_temporal` | alias funcional de `trss` | paper-aligned | ✓✓ |
| TVT-04 | `tv` | Mortaheb et al., EMBC 2019 | paper-inspired | ✓ |
| TVT-05 | `temporal_laplacian` | Jiang et al., IEEE Sensors Journal 2021 | paper-inspired | ✓ |
| TVT-06 | `heat_diffusion_temporal` | Shuman et al., IEEE SPM 2013 (graph spectral filtering / heat kernels) | paper-inspired | ✓ |
| TVT-07 | `spline_temporal` | Narang et al., arXiv 2013 (regularizacion en grafo) + spline smoothing clasico | paper-inspired | ✓ |
| TVT-08 | `wavelet_temporal` | Hammond et al., ACHA 2011 (wavelets on graphs) | paper-inspired | ✓ |
| TVT-09 | `directed_tv` | Schultz y Villafane-Delgado, arXiv 2020 | paper-inspired | ✓ |
| TVT-10 | `visibility_nnk` / `visibility_graphs` | Bozkurt y Ortega, EUSIPCO 2022 | paper-aligned (graph-constructor `visibility_nnk` + `TRSS` wrapper) | ✓ |

---

## Referencias clave (citas cortas)

- Perrin F, et al. (1989). *Spherical splines for scalp potential and current density mapping*. DOI: 10.1016/0013-4694(89)90180-6
- Narang SK, et al. (2013). *Signal processing techniques for interpolation in graph structured data*. DOI: 10.1109/ICASSP.2013.6638704
- Puy G, et al. (2018). *Random sampling of bandlimited signals on graphs*. DOI: 10.1016/j.acha.2016.05.005
- Shekkizhar S, Ortega A (2020). *Graph Construction from Data by Non-Negative Kernel Regression*. DOI: 10.1109/ICASSP40776.2020.9054425
- Giraldo JH, et al. (2022). *Reconstruction of Time-Varying Graph Signals via Sobolev Smoothness*. DOI: 10.1109/TSIPN.2022.3156886
- Hammond DK, Vandergheynst P, Gribonval R (2011). *Wavelets on Graphs via Spectral Graph Theory*. DOI: 10.1016/j.acha.2010.04.005
- Bozkurt E, Ortega A (2022). *Non-Negative Kernel Graphs for Time-Varying Signals Using Visibility Graphs*. DOI: 10.23919/EUSIPCO55093.2022.9909594
- Zhang Q, et al. (2024). *Recovery of bandlimited graph signals based on the reproducing kernel Hilbert space*. DOI: 10.1016/j.dsp.2024.104565

---

## Evidencia relacionada en repo

- `results/bgsrp_vs_narang_check_summary.csv`
- `results/graphtrss_main_figure_summary.csv`
- `tests/test_paper_faithful.py`
