#!/usr/bin/env python3
"""Genera figura conceptual para el Capítulo 2: origen neurofisiológico del EEG.
Versión corregida: etiquetas no solapadas."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'legend.fontsize': 7,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

fig, axes = plt.subplots(2, 2, figsize=(7, 5.5),
                          gridspec_kw={'height_ratios': [1.2, 2.5],
                                       'width_ratios': [1.5, 1]})

ax_anatomy, ax_dipole = axes[0, 0], axes[0, 1]
ax_signal, ax_topo = axes[1, 0], axes[1, 1]

# ========== Panel (a): Anatomía simplificada ==========
ax_anatomy.set_title("(a) Origen cortical y conducción de volumen", fontweight='bold', loc='left', fontsize=10)
layers = [
    ("Corteza", 0.0, '#885522'),
    ("Líquido cefalorraquídeo", 0.18, '#CCEEFF'),
    ("Cráneo", 0.30, '#DDDDCC'),
    ("Cuero cabelludo", 0.44, '#FFCCAA'),
]
for label, y, color in layers:
    rect = plt.Rectangle((0.02, y), 0.96, 0.10, facecolor=color, edgecolor='#666666',
                          linewidth=0.5, alpha=0.7)
    ax_anatomy.add_patch(rect)
    ax_anatomy.text(0.5, y + 0.05, label, ha='center', va='center', fontsize=7, color='#333333')

# Dipolos corticales
for dx in [0.2, 0.35, 0.5, 0.65, 0.8]:
    ax_anatomy.plot(dx, 0.03, 'v', color='red', markersize=4, markeredgewidth=0)
    ax_anatomy.plot(dx, 0.03, '^', color='red', markersize=4, markeredgewidth=0, alpha=0.6)

# Flecha de dipolos - hacia la derecha, evitando solapamiento
ax_anatomy.annotate('Dipolos\ncorticales', xy=(0.35, 0.03), xytext=(0.72, 0.25),
                    fontsize=7, ha='center', va='center', color='#CC3333',
                    arrowprops=dict(arrowstyle='->', color='#CC3333', lw=1.0,
                                   connectionstyle='arc3,rad=-0.2'))

# Electrodos en cuero cabelludo
electrode_x = np.linspace(0.05, 0.95, 9)
ax_anatomy.plot(electrode_x, [0.52]*len(electrode_x), 's', color='#4444AA', markersize=4, markeredgewidth=0)
ax_anatomy.annotate('Electrodos EEG', xy=(0.5, 0.52), xytext=(0.5, 0.59),
                    ha='center', fontsize=7, color='#4444AA',
                    arrowprops=dict(arrowstyle='->', color='#4444AA', lw=0.8))

ax_anatomy.set_xlim(0, 1)
ax_anatomy.set_ylim(-0.02, 0.64)
ax_anatomy.axis('off')

# ========== Panel (b): Esquema dipolo ==========
ax_dipole.set_title("(b) Modelo de dipolo cortical", fontweight='bold', loc='left', fontsize=10)
# Carga positiva
ax_dipole.plot(0.45, 0.55, 'o', color='#CC3333', markersize=10, markeredgewidth=0)
ax_dipole.annotate('+', xy=(0.45, 0.55), ha='center', va='center', fontsize=13, color='white', fontweight='bold')
# Carga negativa
ax_dipole.plot(0.55, 0.45, 'o', color='#3366CC', markersize=10, markeredgewidth=0)
ax_dipole.annotate('−', xy=(0.55, 0.45), ha='center', va='center', fontsize=15, color='white', fontweight='bold')

# Líneas de campo
for r_mult in [0.15, 0.25, 0.35, 0.45, 0.55, 0.65]:
    t = np.linspace(0, 2*np.pi, 200)
    cx, cy = 0.5, 0.5
    x = cx + r_mult * np.cos(t)
    y = cy + r_mult * np.sin(t) * 1.15
    # Deformar según signo del coseno
    y_offset = 0.10 * r_mult * np.sin(2*t) * np.sign(np.cos(t))
    ax_dipole.plot(x, y + y_offset, 'k-', lw=0.5, alpha=0.4)

# Etiqueta clara
ax_dipole.text(0.5, 0.92, 'Campo eléctrico\nse propaga en\nel medio conductor',
               ha='center', va='top', fontsize=7, color='#555555',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFFFF0', alpha=0.7))

ax_dipole.set_xlim(0, 1)
ax_dipole.set_ylim(0, 1)
ax_dipole.axis('off')

# ========== Panel (c): Señal EEG simulada (alfa + ERP) ==========
ax_signal.set_title("(c) Señal EEG: actividad espontánea + ERPs", fontweight='bold', loc='left', fontsize=10)
fs = 500
t = np.linspace(0, 2, fs*2)
alpha = 3.0 * np.sin(2*np.pi*10*t)
erp = np.zeros_like(t)
p300_t = (t > 0.5) & (t < 0.9)
erp[p300_t] = 8 * np.exp(-((t[p300_t]-0.7)**2)/(2*0.02**2)) * np.sin(2*np.pi*4*(t[p300_t]-0.5))
n100_t = (t > 0.1) & (t < 0.3)
erp[n100_t] = -4 * np.exp(-((t[n100_t]-0.2)**2)/(2*0.015**2))
noise = 0.8 * np.random.RandomState(42).randn(len(t))
signal = alpha + erp + noise

ax_signal.plot(t, signal, '#2277AA', lw=0.5, alpha=0.5)
ax_signal.plot(t[p300_t], erp[p300_t] + np.mean(alpha) + np.mean(noise), '#CC3333', lw=1.5, label='Componente P300')
ax_signal.plot(t[n100_t], erp[n100_t] + np.mean(alpha) + np.mean(noise), '#33AA33', lw=1.5, label='Componente N100')
ax_signal.plot(t[100:250], alpha[100:250] + np.mean(noise), '#DDAA00', lw=1.2, label='Ritmo $\\alpha$ (10 Hz)', alpha=0.8)

ax_signal.set_xlabel('Tiempo [s]')
ax_signal.set_ylabel('Amplitud [$\\mu$V]')
ax_signal.legend(loc='upper right', framealpha=0.9, fontsize=7)
ax_signal.set_xlim(0, 1.2)

# ========== Panel (d): Topografía (vista superior cabeza) ==========
ax_topo.set_title("(d) Distribución espacial de potencial\n(topografía con canal fallado)", fontweight='bold', loc='left', fontsize=10)
head = plt.Circle((0.5, 0.5), 0.42, fill=False, color='#333333', lw=1.5)
nose = plt.Polygon([[0.47, 0.08], [0.5, 0.0], [0.53, 0.08]], fill=True, color='#333333')
ax_topo.add_patch(head)
ax_topo.add_patch(nose)

ex = np.array([0.5, 0.35, 0.65, 0.28, 0.72, 0.22, 0.78, 0.5, 0.35, 0.65,
               0.5, 0.5, 0.42, 0.58, 0.32, 0.68, 0.26, 0.74, 0.44, 0.56, 0.5])
ey = np.array([0.16, 0.24, 0.24, 0.33, 0.33, 0.42, 0.42, 0.33, 0.45, 0.45,
               0.52, 0.62, 0.55, 0.55, 0.65, 0.65, 0.72, 0.72, 0.73, 0.73, 0.48])
bad_idx = [8, 14]
good_idx = [i for i in range(len(ex)) if i not in bad_idx]

ax_topo.scatter(ex[good_idx], ey[good_idx], c='#2277AA', s=40, zorder=5, edgecolors='white', linewidth=0.5)
ax_topo.scatter(ex[bad_idx], ey[bad_idx], c='#CC3333', s=60, zorder=6, edgecolors='white', linewidth=1.2, marker='X')
ax_topo.annotate('Canal\nfallado', xy=(ex[8], ey[8]), xytext=(0.15, 0.30),
                 fontsize=7, ha='center', va='center', color='#CC3333',
                 arrowprops=dict(arrowstyle='->', color='#CC3333', lw=1.0))
ax_topo.annotate('Canales\nbuenos', xy=(ex[0], ey[0]), xytext=(0.82, 0.22),
                 fontsize=7, ha='center', va='center', color='#2277AA',
                 arrowprops=dict(arrowstyle='->', color='#2277AA', lw=0.8))

ax_topo.set_xlim(0.05, 0.95)
ax_topo.set_ylim(-0.02, 0.95)
ax_topo.set_aspect('equal')
ax_topo.axis('off')

plt.tight_layout(pad=1.5, h_pad=2.0, w_pad=1.5)

out_path = '/mnt/c/Users/sarlo/OneDrive/Escritorio/Proyectos/Tesis-GSP-EEG-Carlos-Saldivia/Thesis-Copilot-Toolkit/thesis/usm/figures/capitulo2_origen_eeg.pdf'
plt.savefig(out_path, format='pdf')
print(f"Figura guardada: {out_path}")