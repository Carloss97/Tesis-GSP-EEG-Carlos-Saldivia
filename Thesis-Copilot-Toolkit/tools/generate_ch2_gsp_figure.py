#!/usr/bin/env python3
"""Genera diagrama conceptual de GSP para Capítulo 2."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 9, 'axes.labelsize': 10, 'axes.titlesize': 11,
    'legend.fontsize': 8, 'figure.dpi': 150, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'savefig.pad_inches': 0.05,
})

fig, axes = plt.subplots(1, 3, figsize=(8, 3.2))

# --- Panel (a): Grafo de electrodos ---
ax = axes[0]
ax.set_title("(a) Grafo de electrodos\n$\\mathcal{G} = (\\mathcal{V}, \\mathcal{E}, \\mathbf{W})$", fontweight='bold', loc='left')

# Posiciones estilo montaje 10-20 simplificado
np.random.seed(42)
n_nodes = 14
theta = np.linspace(0, 2*np.pi, n_nodes, endpoint=False)
r_base = np.array([0.15, 0.28, 0.38, 0.32, 0.42, 0.48, 0.45, 0.50, 0.44, 0.52, 0.46, 0.48, 0.40, 0.50])
x = 0.5 + r_base * np.cos(theta)
y = 0.5 + r_base * np.sin(theta)

# Construir grafo k-NN (k=3)
from scipy.spatial.distance import cdist
dist = cdist(np.column_stack([x, y]), np.column_stack([x, y]))
k = 3
for i in range(n_nodes):
    neighbors = np.argsort(dist[i])[1:k+1]
    for j in neighbors:
        w = np.exp(-dist[i, j]**2 / 0.02)
        ax.plot([x[i], x[j]], [y[i], y[j]], '-', color='#AAAAAA', lw=0.5 + w*2, alpha=0.6)

ax.scatter(x, y, c='#2277AA', s=80, zorder=5, edgecolors='white', linewidth=1)
for i in range(n_nodes):
    ax.annotate(f'$v_{{{i+1}}}$', (x[i], y[i]), textcoords="offset points", xytext=(0, 8),
                ha='center', fontsize=6)

ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect('equal'); ax.axis('off')

# --- Panel (b): Señal y Laplaciano ---
ax = axes[1]
ax.set_title("(b) Señal sobre el grafo $\\mathbf{x}$\ny suavidad $S(\\mathbf{x})$", fontweight='bold', loc='left')

# Heatmap pequeño estilo topografía de señal en el grafo
# Valores de señal: gradiente espacial simple
xx, yy = np.meshgrid(np.linspace(0, 1, 30), np.linspace(0, 1, 30))
signal_field = np.sin(xx * 4) * np.cos(yy * 3) * 0.5 + 0.5
im = ax.imshow(signal_field, extent=[0, 1, 0, 1], origin='lower', cmap='RdBu_r', aspect='equal', alpha=0.7)

# Nodos superpuestos
for i in range(n_nodes):
    val = np.sin(x[i] * 4) * np.cos(y[i] * 3) * 0.5 + 0.5
    color = plt.cm.RdBu_r(val)
    ax.plot(x[i], y[i], 'o', color='black', markersize=10, zorder=6)
    ax.plot(x[i], y[i], 'o', color=color, markersize=7, zorder=7)

ax.annotate(f'$S(\\mathbf{{x}}) = \\mathbf{{x}}^\\top \\mathbf{{L}} \\mathbf{{x}}$\nPenaliza saltos entre vecinos', 
            xy=(0.5, 0.15), ha='center', fontsize=7.5,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9))

ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')

# --- Panel (c): Espectro GFT ---
ax = axes[2]
ax.set_title("(c) Transformada de Fourier\nen Grafos (GFT)", fontweight='bold', loc='left')

n_eig = 12
eigvals = np.linspace(0, 3, n_eig)
# Señal con más energía en bajas frecuencias
gft_magnitude = 5 * np.exp(-eigvals * 1.2) + 0.3 * np.random.rand(n_eig)
ax.stem(eigvals, gft_magnitude, basefmt=' ', linefmt='#2277AA', markerfmt='o')
ax.fill_between(eigvals[:6], gft_magnitude[:6], alpha=0.15, color='#33AA33')
ax.fill_between(eigvals[6:], gft_magnitude[6:], alpha=0.15, color='#CC3333')

ax.annotate('Baja frecuencia\n(señal suave)', xy=(0.6, 3.5), fontsize=7, color='#33AA33', ha='center')
ax.annotate('Alta frecuencia\n(ruido / artefactos)', xy=(2.4, 1.5), fontsize=7, color='#CC3333', ha='center')
ax.annotate(f'$\\mathbf{{\\hat{{x}}}} = \\mathbf{{U}}^\\top \\mathbf{{x}}$',
            xy=(1.5, 4.8), ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='#FFF8DC', alpha=0.8))

ax.set_xlabel('Autovalor $\\lambda_l$ (frecuencia)')
ax.set_ylabel('Magnitud $|\\hat{x}_l|$')
ax.set_xlim(-0.3, 3.3); ax.set_ylim(0, 5.5)

plt.tight_layout(pad=1.5, w_pad=2.0)

out_path = '/mnt/c/Users/sarlo/OneDrive/Escritorio/Proyectos/Tesis-GSP-EEG-Carlos-Saldivia/Thesis-Copilot-Toolkit/thesis/usm/figures/capitulo2_gsp_conceptos.pdf'
plt.savefig(out_path, format='pdf')
print(f"Figura guardada: {out_path}")