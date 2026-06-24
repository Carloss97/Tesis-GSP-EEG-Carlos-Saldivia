#!/usr/bin/env python3
"""Generate a compact, thesis-ready Chapter 2 EEG neurophysiology figure.

The figure is an original schematic (not copied from cited papers). It follows
advisor feedback by avoiding crowded labels, making the cortex/dipoles readable,
and replacing the confusing head-contained dipole field with a classical dipole
potential schematic.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Polygon

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

mpl.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10.0,
    "axes.titlesize": 10.8,
    "axes.labelsize": 9.5,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "legend.fontsize": 8.3,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

C = {
    "blue": "#0072B2",
    "orange": "#D55E00",
    "green": "#009E73",
    "purple": "#CC79A7",
    "gray": "#333333",
    "scalp": "#F4C7A1",
    "skull": "#D8D2BE",
    "csf": "#BFE6F4",
    "cortex": "#A7673A",
}


def clean_panel(ax: plt.Axes) -> None:
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def add_head_outline(ax: plt.Axes, cx: float = 0.5, cy: float = 0.5, r: float = 0.38,
                     lw: float = 1.3, fill: bool = False, facecolor: str = "white") -> None:
    ax.add_patch(Circle((cx, cy), r, fill=fill, facecolor=facecolor,
                        edgecolor=C["gray"], lw=lw, zorder=1))
    ax.add_patch(Polygon([[cx - 0.035, cy + r * 0.96], [cx, cy + r * 1.13],
                          [cx + 0.035, cy + r * 0.96]],
                         closed=True, facecolor=facecolor if fill else "white",
                         edgecolor=C["gray"], lw=lw, zorder=2))
    ax.add_patch(Ellipse((cx - r * 1.03, cy), r * 0.16, r * 0.34, fill=False,
                         edgecolor=C["gray"], lw=lw, zorder=2))
    ax.add_patch(Ellipse((cx + r * 1.03, cy), r * 0.16, r * 0.34, fill=False,
                         edgecolor=C["gray"], lw=lw, zorder=2))


def panel_origin(ax: plt.Axes) -> None:
    clean_panel(ax)
    ax.set_title("(a) Origen cortical y conducción", loc="left", fontweight="bold", pad=3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")

    cx, cy = 0.56, 0.51
    add_head_outline(ax, cx, cy, 0.36, lw=1.2, fill=True, facecolor=C["scalp"])
    ax.add_patch(Circle((cx, cy), 0.285, facecolor=C["skull"], edgecolor="#6E6E6E", lw=0.75, alpha=0.96))
    ax.add_patch(Circle((cx, cy), 0.220, facecolor=C["csf"], edgecolor="#6E6E6E", lw=0.75, alpha=0.95))
    ax.add_patch(Circle((cx, cy), 0.150, facecolor=C["cortex"], edgecolor="#5B3B25", lw=0.85, alpha=0.94))

    label_specs = [
        ("cuero cabelludo", (0.055, 0.82), (cx - 0.22, cy + 0.29), "#6B3A1E"),
        ("cráneo", (0.055, 0.68), (cx - 0.19, cy + 0.18), "#4C473B"),
        ("LCR", (0.055, 0.54), (cx - 0.12, cy + 0.10), "#1E5E73"),
        ("corteza", (0.055, 0.40), (cx - 0.02, cy + 0.02), "#5B2B12"),
    ]
    for label, xytext, xy, color in label_specs:
        ax.annotate(label, xy=xy, xytext=xytext, ha="left", va="center",
                    fontsize=9.0, color=color,
                    arrowprops=dict(arrowstyle="-", color="#555555", lw=0.65,
                                    shrinkA=1, shrinkB=2))

    # EEG electrodes on scalp; label is away from title and electrodes.
    theta = np.linspace(45, 135, 6) * np.pi / 180
    ex = cx + 0.377 * np.cos(theta)
    ey = cy + 0.377 * np.sin(theta)
    ax.scatter(ex, ey, marker="s", s=28, color=C["blue"], edgecolor="white", linewidth=0.5, zorder=5)
    ax.annotate("electrodos EEG", xy=(ex[2], ey[2]), xytext=(0.80, 0.91),
                ha="center", va="center", fontsize=8.9, color=C["blue"],
                arrowprops=dict(arrowstyle="->", color=C["blue"], lw=0.8))

    # Cortical dipoles inside a now-legible cortex region.
    dipoles = [(0.50, 0.47, 70), (0.57, 0.42, 105), (0.63, 0.52, 55)]
    for x, y, ang in dipoles:
        dx = 0.040 * np.cos(np.deg2rad(ang))
        dy = 0.040 * np.sin(np.deg2rad(ang))
        ax.add_patch(FancyArrowPatch((x - dx, y - dy), (x + dx, y + dy),
                                     arrowstyle="-|>", mutation_scale=10,
                                     lw=1.15, color=C["orange"], zorder=6))
        ax.add_patch(FancyArrowPatch((x + dx * 0.35, y + dy * 0.35), (x - dx * 0.35, y - dy * 0.35),
                                     arrowstyle="-|>", mutation_scale=8,
                                     lw=0.95, color=C["blue"], alpha=0.9, zorder=6))

    ax.annotate("dipolos\ncorticales", xy=(0.56, 0.45), xytext=(0.25, 0.19),
                ha="center", va="center", fontsize=9.0, color="#5B2B12",
                arrowprops=dict(arrowstyle="->", color="#7A2F00", lw=1.0,
                                connectionstyle="arc3,rad=-0.12"))
    # Volume conduction cue.
    for x0 in [0.50, 0.57, 0.64]:
        ax.annotate("", xy=(x0, 0.81), xytext=(x0, 0.60),
                    arrowprops=dict(arrowstyle="->", color="#666666", lw=0.75, ls="--", alpha=0.72))


def panel_dipole(ax: plt.Axes) -> None:
    clean_panel(ax)
    ax.set_title("(b) Campo del dipolo", loc="left", fontweight="bold", pad=3)
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-0.78, 0.78)
    ax.set_aspect("equal")

    # Classical potential-field schematic: positive/negative equipotential contours.
    x = np.linspace(-1.0, 1.0, 220)
    y = np.linspace(-0.75, 0.75, 180)
    X, Y = np.meshgrid(x, y)
    eps = 0.055
    V = 1.0 / np.sqrt((X + 0.26) ** 2 + Y ** 2 + eps) - 1.0 / np.sqrt((X - 0.26) ** 2 + Y ** 2 + eps)
    neg = [-2.0, -1.2, -0.7, -0.35]
    pos = [0.35, 0.7, 1.2, 2.0]
    ax.contour(X, Y, V, levels=neg, colors=[C["blue"]], linewidths=0.90, alpha=0.72)
    ax.contour(X, Y, V, levels=pos, colors=[C["orange"]], linewidths=0.90, alpha=0.72)
    ax.contour(X, Y, V, levels=[0], colors=["#777777"], linewidths=0.80, alpha=0.60)

    ax.scatter([-0.26, 0.26], [0, 0], s=230, c=[C["orange"], C["blue"]],
               edgecolors="white", linewidth=0.8, zorder=4)
    ax.text(-0.26, 0, "+", ha="center", va="center", color="white", fontsize=15, fontweight="bold", zorder=5)
    ax.text(0.26, 0, "−", ha="center", va="center", color="white", fontsize=17, fontweight="bold", zorder=5)
    ax.annotate("momento\ndipolar", xy=(-0.03, 0.0), xytext=(0.00, 0.58),
                ha="center", va="center", fontsize=8.8, color="#333333",
                arrowprops=dict(arrowstyle="->", color="#333333", lw=0.9))
    ax.annotate("contornos\nequipotenciales", xy=(0.55, 0.33), xytext=(0.78, 0.64),
                fontsize=8.6, ha="center", va="center", color="#333333",
                arrowprops=dict(arrowstyle="->", color="#333333", lw=0.9))
    legend = [
        Line2D([0], [0], color=C["orange"], lw=1.2, label="potencial +"),
        Line2D([0], [0], color=C["blue"], lw=1.2, label="potencial −"),
        Line2D([0], [0], color="#777777", lw=1.0, label="cero"),
    ]
    ax.legend(handles=legend, loc="lower center", bbox_to_anchor=(0.5, -0.02),
              ncol=3, frameon=False, handlelength=1.3, columnspacing=0.8)


def panel_erp(ax: plt.Axes) -> None:
    ax.set_title("(c) Potenciales Relacionados a Eventos (ERP)", loc="left", fontweight="bold", pad=3)
    rng = np.random.default_rng(9)
    t = np.linspace(-0.10, 0.60, 700)
    n100 = -3.6 * np.exp(-((t - 0.10) ** 2) / (2 * 0.018 ** 2))
    p200 = 2.2 * np.exp(-((t - 0.19) ** 2) / (2 * 0.030 ** 2))
    p300 = 6.5 * np.exp(-((t - 0.31) ** 2) / (2 * 0.055 ** 2))
    slow = 0.40 * np.sin(2 * np.pi * 2.2 * (t + 0.08)) * np.exp(-((t - 0.28) ** 2) / (2 * 0.35 ** 2))
    y = n100 + p200 + p300 + slow + rng.normal(0, 0.07, size=t.size)
    ax.plot(t, y, color=C["blue"], lw=1.6)
    ax.axhline(0, color="#777777", lw=0.7)
    ax.axvline(0, color="#666666", lw=0.8, ls="--")
    ax.text(0.005, -4.7, "estímulo", rotation=90, ha="left", va="bottom", fontsize=8.2, color="#444444")

    labels = [
        (0.10, -3.6, "N100", (0.055, -5.0), C["green"]),
        (0.19, 2.2, "P200", (0.145, 3.35), C["purple"]),
        (0.31, 6.5, "P300", (0.405, 6.9), C["orange"]),
    ]
    for x, yy, lab, textxy, color in labels:
        ax.scatter([x], [yy], s=22, color=color, zorder=4)
        ax.annotate(lab, xy=(x, yy), xytext=textxy,
                    fontsize=8.9, color=color, fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=color, lw=0.85,
                                    connectionstyle="arc3,rad=0.12"))
    ax.set_xlim(-0.10, 0.60)
    ax.set_ylim(-5.4, 7.5)
    ax.set_xlabel("Tiempo [s]")
    ax.set_ylabel("Amplitud [µV]")
    ax.grid(True, color="#E5E5E5", lw=0.55)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)


def panel_topography(ax: plt.Axes) -> None:
    clean_panel(ax)
    ax.set_title("(d) Topografía: canales buenos y fallados", loc="left", fontweight="bold", pad=3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    add_head_outline(ax, 0.50, 0.52, 0.34, lw=1.35)

    pos = np.array([
        [0.42, 0.78], [0.58, 0.78],
        [0.25, 0.67], [0.40, 0.67], [0.50, 0.69], [0.60, 0.67], [0.75, 0.67],
        [0.20, 0.52], [0.36, 0.52], [0.50, 0.52], [0.64, 0.52], [0.80, 0.52],
        [0.27, 0.37], [0.42, 0.36], [0.50, 0.35], [0.58, 0.36], [0.73, 0.37],
        [0.42, 0.23], [0.58, 0.23],
    ])
    bad = np.array([3, 10, 16])
    good = np.array([i for i in range(len(pos)) if i not in set(bad)])
    ax.scatter(pos[good, 0], pos[good, 1], s=48, color=C["blue"], edgecolors="white", linewidth=0.7, zorder=4)
    ax.scatter(pos[bad, 0], pos[bad, 1], s=88, marker="X", color=C["orange"], edgecolors="white", linewidth=0.9, zorder=5)
    ax.text(0.50, 0.91, "nasion", ha="center", va="center", fontsize=8.0, color="#444444")
    ax.annotate("canales fallados\n(a interpolar)", xy=(0.64, 0.52), xytext=(0.86, 0.26),
                fontsize=8.6, ha="center", va="center", color="#7A2F00",
                arrowprops=dict(arrowstyle="->", color="#7A2F00", lw=0.9,
                                connectionstyle="arc3,rad=-0.18"))
    legend = [
        Line2D([0], [0], marker="o", color="none", label="canal observado",
               markerfacecolor=C["blue"], markeredgecolor="white", markersize=7),
        Line2D([0], [0], marker="X", color="none", label="canal fallado",
               markerfacecolor=C["orange"], markeredgecolor="white", markersize=8),
    ]
    ax.legend(handles=legend, loc="lower center", bbox_to_anchor=(0.5, -0.02),
              ncol=2, frameon=False, handletextpad=0.3, columnspacing=0.9)


def main() -> None:
    fig, axes = plt.subplots(2, 2, figsize=(7.55, 5.35), constrained_layout=True)
    panel_origin(axes[0, 0])
    panel_dipole(axes[0, 1])
    panel_erp(axes[1, 0])
    panel_topography(axes[1, 1])
    fig.set_constrained_layout_pads(w_pad=0.030, h_pad=0.030, wspace=0.10, hspace=0.10)
    out = FIG / "capitulo2_origen_eeg.pdf"
    fig.savefig(out, format="pdf", bbox_inches="tight", pad_inches=0.020)
    plt.close(fig)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
