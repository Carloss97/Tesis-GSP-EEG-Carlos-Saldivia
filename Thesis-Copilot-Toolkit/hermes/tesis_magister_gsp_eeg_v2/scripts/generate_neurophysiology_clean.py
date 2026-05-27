#!/usr/bin/env python3
"""Generate a visually cleaner Chapter 2 neurophysiology overview figure."""
from pathlib import Path
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

mpl.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9.5,
    "axes.titlesize": 10.5,
    "axes.labelsize": 9.5,
    "legend.fontsize": 8.5,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

np.random.seed(7)
fig, axes = plt.subplots(2, 2, figsize=(7.45, 5.45),
                         gridspec_kw={"height_ratios": [1.0, 1.35], "wspace": 0.36, "hspace": 0.38})
ax_a, ax_b = axes[0]
ax_c, ax_d = axes[1]

# (a) Volume conduction layers
ax_a.set_title("(a) Origen cortical y conducción", loc="left", fontweight="bold", pad=5)
ax_a.set_xlim(0, 1); ax_a.set_ylim(0, 1); ax_a.axis("off")
layers = [
    ("Corteza", 0.08, "#9B6A3D"),
    ("LCR", 0.27, "#BFE8FF"),
    ("Cráneo", 0.46, "#DDD8C4"),
    ("Cuero cabelludo", 0.65, "#F3C5A6"),
]
for label, y, color in layers:
    ax_a.add_patch(Rectangle((0.08, y), 0.84, 0.13, facecolor=color, edgecolor="#555555", lw=0.7, alpha=0.82))
    ax_a.text(0.50, y+0.065, label, ha="center", va="center", fontsize=8.5, color="#222222")
# dipoles and electrodes
for dx in np.linspace(0.22, 0.78, 5):
    ax_a.plot(dx, 0.135, marker="v", color="#D55E00", markersize=5.5, markeredgewidth=0)
    ax_a.plot(dx, 0.135, marker="^", color="#D55E00", markersize=5.5, alpha=0.65, markeredgewidth=0)
ax_a.annotate("dipolos\ncorticales", xy=(0.50, 0.14), xytext=(0.18, 0.34),
              ha="center", va="center", fontsize=8.0, color="#9A3E00",
              arrowprops=dict(arrowstyle="->", color="#9A3E00", lw=1.0))
electrode_x = np.linspace(0.15, 0.85, 8)
ax_a.scatter(electrode_x, [0.84]*len(electrode_x), marker="s", s=24, c="#0072B2", zorder=3)
ax_a.text(0.50, 0.93, "electrodos EEG", ha="center", va="center", fontsize=8.3, color="#005A8A")

# (b) dipole field
ax_b.set_title("(b) Campo del dipolo", loc="left", fontweight="bold", pad=5)
ax_b.set_xlim(0,1); ax_b.set_ylim(0,1); ax_b.axis("off"); ax_b.set_aspect("equal")
ax_b.scatter([0.43,0.57], [0.50,0.50], s=240, c=["#D55E00", "#0072B2"], edgecolors="white", linewidth=0.8, zorder=3)
ax_b.text(0.43,0.50,"+", ha="center", va="center", color="white", fontsize=16, fontweight="bold")
ax_b.text(0.57,0.50,"−", ha="center", va="center", color="white", fontsize=18, fontweight="bold")
for r in [0.17,0.28,0.40,0.52]:
    t = np.linspace(0, np.pi, 160)
    ax_b.plot(0.50 + r*np.cos(t), 0.48 + 0.95*r*np.sin(t), color="#555555", lw=0.7, alpha=0.55)
    ax_b.plot(0.50 + r*np.cos(t), 0.52 - 0.75*r*np.sin(t), color="#555555", lw=0.55, alpha=0.30)

# (c) signal
ax_c.set_title("(c) Señal EEG: ritmo α + ERPs", loc="left", fontweight="bold", pad=5)
fs=500
t=np.linspace(0,1.2,int(1.2*fs))
alpha=2.8*np.sin(2*np.pi*10*t)
n100=-4.5*np.exp(-((t-0.20)**2)/(2*0.018**2))
p300=6.5*np.exp(-((t-0.70)**2)/(2*0.045**2))
noise=0.55*np.random.randn(len(t))
sig=alpha+n100+p300+noise
ax_c.plot(t, sig, color="#0072B2", lw=0.8, alpha=0.65, label="Señal EEG")
ax_c.plot(t, n100, color="#009E73", lw=1.4, label="N100")
ax_c.plot(t, p300, color="#D55E00", lw=1.4, label="P300")
ax_c.plot(t, alpha, color="#E69F00", lw=1.0, alpha=0.8, label="Ritmo α")
ax_c.axhline(0, color="#777777", lw=0.6)
ax_c.set_xlim(0,1.2)
ax_c.set_xlabel("Tiempo [s]")
ax_c.set_ylabel("Amplitud [µV]")
ax_c.grid(True, color="#E5E5E5", lw=0.5)
ax_c.legend(loc="upper right", frameon=True, framealpha=0.88, borderpad=0.4)

# (d) topography
ax_d.set_title("(d) Topografía y canal fallado", loc="left", fontweight="bold", pad=5)
ax_d.set_xlim(0,1); ax_d.set_ylim(0,1); ax_d.axis("off"); ax_d.set_aspect("equal")
ax_d.add_patch(Circle((0.50,0.50),0.39, fill=False, color="#333333", lw=1.4))
ax_d.add_patch(Polygon([[0.47,0.13],[0.50,0.06],[0.53,0.13]], closed=True, color="#333333"))
ex=np.array([.50,.36,.64,.28,.72,.23,.77,.50,.36,.64,.50,.42,.58,.31,.69,.27,.73,.44,.56,.50])
ey=np.array([.18,.27,.27,.36,.36,.46,.46,.36,.49,.49,.58,.59,.59,.67,.67,.75,.75,.77,.77,.50])
bad=[8,13]
good=[i for i in range(len(ex)) if i not in bad]
ax_d.scatter(ex[good], ey[good], c="#0072B2", s=42, edgecolors="white", linewidth=0.6, zorder=4)
ax_d.scatter(ex[bad], ey[bad], c="#D55E00", s=70, marker="X", edgecolors="white", linewidth=0.8, zorder=5)
ax_d.annotate("canales\nsanos", xy=(0.72,0.36), xytext=(0.90,0.28), fontsize=8.2,
              ha="center", va="center", color="#005A8A",
              arrowprops=dict(arrowstyle="->", color="#005A8A", lw=0.9))
ax_d.annotate("canal\nfallado", xy=(ex[13],ey[13]), xytext=(0.13,0.73), fontsize=8.2,
              ha="center", va="center", color="#9A3E00",
              arrowprops=dict(arrowstyle="->", color="#9A3E00", lw=0.9))

fig.subplots_adjust(left=0.07, right=0.98, top=0.95, bottom=0.08)
fig.savefig(FIG / "capitulo2_origen_eeg.pdf", format="pdf", bbox_inches="tight", pad_inches=0.06)
print(f"saved {FIG / 'capitulo2_origen_eeg.pdf'}")
