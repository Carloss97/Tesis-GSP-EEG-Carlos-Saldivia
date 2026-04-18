# Revisión bibliográfica por método — resumen breve

Este documento agrupa referencias locales (carpeta `Referencias`) que justifican las familias y métodos seleccionados para las próximas iteraciones. Es un resumen para insertar citas y notas breves en la documentación principal.

**Nota:** los enlaces apuntan a las entradas BibTeX locales encontradas en el repositorio.

---

## Construcción de grafos

- `knn` / k‑NN, `epsilon_ball` (ε‑neighborhood): revisión y comparativa de construcciones de grafos: Qiao et al., 2018. Fuente: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L386).
- `nnk` (Non‑Negative Kernel Regression): propuesta y propiedades geométricas de NNK — Shekkizhar & Ortega (2020). Fuente: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L298).
- `aew` (Adaptive Edge Weighting): estrategia local de peso de aristas — Karasuyama & Mamitsuka (2017). Fuente: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L19).
- `kalofolias` (graph learning from smooth signals): aprendizaje de grafos bajo prior de suavidad — Kalofolias (2016/2019). Fuente: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L352).
- `gaussian` / umbralizado (kernel/thresholded Gaussian): uso en construcción y sensibilidad a parámetro; ver Jiang et al., 2021 (sensor networks, kernel threshold). Fuente: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L123).
- `mst` (minimum spanning tree): método geométrico clásico — cubierto en revisiones generales (Qiao 2018) y en textos de GSP.

## Interpolación espacial / instantánea

- `linear`: baseline espacial simple; marco de interpolación en grafos y proyección aparece en Narang et al., 2013. Fuente: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L36).
- `ICA`: usada como referencia estadística (componentes) en análisis neuroimagen — ejemplo de uso/comparación: Ménoret et al., 2017. Fuente: [Referencias/Mi biblioteca.bib](Referencias/Mi%20biblioteca.bib#L205).
- `rbfi_tps` (RBF / thin‑plate / multiquadric): RBFs aplicadas a reconstrucción EEG; Jäger et al., 2016 (multiquadrics) muestra buen desempeño frente a spline. Fuente: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L69).
- `spherical_spline`: clásico en EEG (Perrin et al., 1989) — referencia canónica para `spherical_spline`. Fuente: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L89).
- `idw` (inverse distance weighting): método geométrico rápido y útil como baseline de referencia; no se encontró una entrada local explícita para `idw` en los .bib revisados — recomendar añadir una cita clásica (p.ej. Shepard 1968) si se desea incluirla en la bibliografía.
- `spline_surface`: cubierto por estudios de RBF / multiquadrics y thin‑plate (Jäger 2016). Fuente: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L69).

## GSP / interpolación regularizada

- `gsp` (marco general): libros y tutoriales de GSP — Ortega (2022) y Shuman et al. (2013) son referencia de base. Fuente: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L226) y [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L242).
- `tikhonov` (regularización en grafos / Laplacian): formulaciones de reconstrucción por proyección y regularización aparecen en Narang et al., 2013 y trabajos recientes sobre recuperación/RKHS (Zhang et al., 2024). Fuentes: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L36), [Referencias/Mi biblioteca.bib](Referencias/Mi%20biblioteca.bib#L102).
- `gsmooth` (graph smoothing): métodos de filtrado y suavizado en grafos (Isufi et al., 2024). Fuente: [Referencias/Mi biblioteca.bib](Referencias/Mi%20biblioteca.bib#L307).
- `bgsrp` (BGSRP / RKHS‑based recovery): código y réplica en `Papers/Code-for-BGSRP-master` (repositorio de código incluido). Ver README y scripts de réplica; en el repo hay experimentos y validación cruzada (VALIDATION_REPORT). Fuente: [Papers/Code-for-BGSRP-master/README.md](Papers/Code-for-BGSRP-master/README.md#L1) y `Thesis-Copilot-Toolkit/VALIDATION_REPORT.md`.

## TV / espacio‑tiempo (time‑varying)

- `trss` / GraphTRSS (Sobolev): método de reconstrucción de señales tiempo‑variantes basado en suavidad Sobolev — Giraldo et al., 2022 (GraphTRSS). Fuente: [Referencias/Mi biblioteca.bib](Referencias/Mi%20biblioteca.bib#L323).
- `sobolev_temporal`: mismo marco que GraphTRSS — Giraldo et al., 2022. Fuente: [Referencias/Mi biblioteca.bib](Referencias/Mi%20biblioteca.bib#L323).
- `graph_time_tikhonov`: enfoque espacio‑tiempo que combina grafo espacial y regularización temporal aparece en Jiang et al., 2021 (spatio‑temporal graph / producto de grafos) y en trabajos de Narang (2013) sobre proyección/regularización; es una buena elección para marcos GSP↔TV. Fuentes: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L123), [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L36).
- `directed_tv`: existe referencia teórica (Schultz & Villafane‑Delgado, 2020) para variación dirigida en grafos dirigidos — **no** es la mejor opción si el grafo es no‑dirigido (tu observación es correcta). Fuente: [Referencias/Mi biblioteca.bib](Referencias/Mi%20biblioteca.bib#L359).

## Métodos prometedores detectados en la bibliografía (recomendación)

- `temporal_laplacian`, `heat_diffusion_temporal`, `wavelet_temporal`: aparecen como variantes en marcos espacio‑tiempo y en revisiones sobre GSP temporal; útiles para explorar como complementos a `graph_time_tikhonov` y `trss` (no siempre hay entrada .bib local específica, pero aparecen en reviews y artículos recientes sobre señales en grafos tiempo‑variantes).
- Aprendizaje de grafos tiempo‑variantes / joint time‑vertex dictionaries: Zhao et al., 2025 (Generalized graph reconstruction via uncertainty principle) y Krishnan et al., 2026 (Koopman autoencoders para señales en grafos tiempo‑variantes) proporcionan marcos teóricos/avanzados para reconstrucción y predicción — posibles candidatos a incluir en estudios futuros. Fuentes: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L482), [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L531).
- Graph learning escalable y ajuste de parámetros (k): Kalofolias (2016/2019) y Tamaru et al. (2024) tratan aprendizaje de grafos y optimización de `k` para kNN — relevantes para elegir `epsilon_ball`/`k` y para métodos aprendidos. Fuentes: [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L352), [Referencias/Tesis_biblio/Tesis_biblio.bib](Referencias/Tesis_biblio/Tesis_biblio.bib#L176).

---

## Sugerencia de pasos siguientes

- Si aprobás, inserto estas notas resumidas en `AGENT_ITERATION_GUIDE.md` y en `docs/normalization_and_dataset_policy.md` junto a las familias finales.
- Puedo también añadir entradas faltantes (p.ej. `idw` si querés la cita clásica) al archivo `Referencias/Tesis_biblio/Tesis_biblio.bib` o `Referencias/Mi biblioteca.bib`.

---

Archivo generado automáticamente por el agente — dime si querés que haga los commits y las inserciones en la documentación principal ahora.