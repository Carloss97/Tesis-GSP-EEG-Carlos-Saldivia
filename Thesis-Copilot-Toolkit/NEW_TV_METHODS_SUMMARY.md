## Implementación de 7 nuevos métodos TV (Temporal Variation) basados en bibliografía

### Resumen ejecutivo

Se implementaron 7 nuevos métodos de interpolación basados en variación temporal (TV), inspirados en papers recientes de Graph Signal Processing y análisis de señales espacio-temporales. Todos los métodos han sido validados exitosamente con datos EEG sintéricos.

### Papers bibliográficos y métodos correspondientes

| Método | Paper | Referencia | Descripción |
|--------|-------|-----------|-------------|
| **sobolev_temporal** | "Reconstruction of Time-Varying Graph Signals via Sobolev Smoothness" | Giraldo et al. 2022 | Usa normas de Sobolev en diferencias temporales (segunda derivada discretizada) |
| **temporal_laplacian** | "Learning time varying graphs" + Product Graph Theory | Kalofolias et al. 2017 | Producto Kronecker: L_space ⊗ I_t + I_space ⊗ L_t |
| **heat_diffusion_temporal** | Heat Kernel Diffusion Theory | Clásico GSP | Kernel de calor gaussiano en dimensión temporal combinado con difusión espacial |
| **spline_temporal** | "Localized Iterative Methods for Interpolation" | Narang et al. 2013 | Splines univariados temporales + regularización espacial Tikhonov |
| **wavelet_temporal** | Graph Wavelet Transform | Shuman et al. 2013 | Transformada wavelet Haar discreta en tiempo + regularización espacial |
| **directed_tv** | "Graph Signal Processing of Indefinite and Complex Graphs using Directed Variation" | Schultz & Villafane-Delgado 2020 | Total variation dirigida para grafos complejos/asimétricos |
| **adaptive_temporal** | "Non-Negative Kernel Graphs for Time-Varying Signals Using Visibility Graphs" | Bozkurt & Ortega 2022 | Suavizado temporal adaptativo con matriz de coherencia local |

### Rendimiento (MAE en datos sintéticos EEG)

```
Ranking de desempeño:
1. sobolev_temporal          MAE=0.4767 ← MEJOR
2. heat_diffusion_temporal   MAE=0.4973
3. adaptive_temporal         MAE=0.5228
4. temporal_laplacian        MAE=0.5497
5. wavelet_temporal          MAE=0.6265
6. spline_temporal           MAE=0.8911
7. directed_tv               MAE=0.9764
```

### Parámetros por defecto recomendados

#### sobolev_temporal
- `alpha=0.5`: peso de la regularización espacial
- `beta=0.2`: peso de la regularización temporal (Sobolev de 2da derivada)
- `n_iter=100`: iteraciones de descenso de gradiente
- Decaimiento adaptativo de paso: `step / (1 + 0.01*iter_no)`

#### temporal_laplacian
- `alpha=0.7`: peso Laplaciano espacial
- `beta=0.25`: peso Laplaciano temporal
- Resuelve sistema lineal directo con producto Kronecker
- Mejor para datos con muchas muestras temporales

#### heat_diffusion_temporal
- `alpha=0.5`: peso difusión espacial
- `beta=0.3`: peso difusión temporal (heat kernel)
- `n_iter=80`: iteraciones
- Kernel de calor: `exp(-0.1 * (i-j)^2)` para distancia temporal

#### spline_temporal
- `alpha=0.6`: regularización espacial post-spline
- `s_temporal=0.1`: suavizado de splines univariados
- Splines cúbicos con grados de libertad adaptativos
- Muy efectivo para datos suaves en tiempo

#### wavelet_temporal
- `alpha=0.65`: regularización espacial
- `wavelet_level=2`: niveles de descomposición Haar
- Análisis multirresolución en tiempo
- Captura características a diferentes escalas

#### directed_tv
- `alpha=0.5`: TV simétrica
- `beta=0.15`: TV temporal
- `n_iter=50`: iteraciones IRLS
- Versión "dirigida": soporta grafos asimétricos

#### adaptive_temporal
- `alpha=0.55`: regularización espacial
- `beta=0.2`: regularización temporal
- `gamma=0.05`: término de fidelidad adicional
- `n_iter=100`: iteraciones
- Matriz de coherencia adaptada localmente

### Notas de implementación

1. **Dimensiones**: Todos los métodos operan en formato (n_t, n_ch) donde n_t = timestamps, n_ch = channels

2. **Laplacianos**: 
   - Espacial `lap_g` ∈ ℝ^{n_ch × n_ch} se aplica por timestep: `grad_graph[t,:] = lap_g @ x[t,:]`
   - Temporal `lap_t` ∈ ℝ^{n_t × n_t} se aplica directamente: `grad_temporal = lap_t @ x`

3. **Convergencia**: Los métodos iterativos usan clipping adaptativo: `[-8*σ, 8*σ]` donde σ = std(datos)

4. **Fallbackespeciales**: 
   - `spline_temporal` usa `UnivariateSpline` de scipy con k=min(3, n_obs-1)
   - `wavelet_temporal` usa descomposición Haar simplificada (pasa-bajos iterativo)

5. **Error handling**: Todos los métodos incluyen fallback a media temporal si Laplaciano es singular

### Uso en pipeline experimental

```python
from src.interpolation_methods import interpolate_signals

# Ejemplo: usar sobolev_temporal (mejor resultado)
result = interpolate_signals(
    "sobolev_temporal",
    signals_masked,
    adjacency=graph_adjacency,
    alpha=0.5,
    beta=0.2,
    n_iter=100
)
reconstructed = result["reconstructed"]
```

### Notas para optimización futura

1. **sobolev_temporal** tiene mayor costo computacional (2da derivada) pero mejor MAE
2. **heat_diffusion_temporal** buen equilibrio entre velocidad y precisión
3. **temporal_laplacian** requiere inversión de matriz pero es exacto para sistemas pequeños
4. **adaptive_temporal** promete mejor generalización en datos heterogéneos (ver Bozkurt & Ortega 2022)

### Validación completada

✓ Test de sintaxis y tipo checking (sin errores)
✓ Test funcional con datos sintéticos (50 timesteps, 10 canales)
✓ Métricas MAE y RMSE calculadas correctamente
✓ Comparación relativa de desempeño entre métodos

### Archivos modificados

- `src/interpolation_methods.py`: +7 funciones nuevas + dispatcher actualizado
- `backlog.md`: Lista actualizada con nuevos métodos
- `test_new_tv_methods.py`: Script de validación completo

---

Fecha: Abril 1, 2026
Estado: Listo para incorporar en pipeline experimental full
Siguiente paso: Ejecutar optimización de parámetros y robustness testing
