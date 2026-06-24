#!/usr/bin/env python3
"""Generate a compact Chapter 2 EEG neurophysiology figure.

Design principle for this revision: no explanatory text is placed on top of the
scientific drawing. Labels are moved to separate legend areas or captions.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Polygon, Rectangle

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
    "legend.fontsize": 8.2,
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


def add_head_outline(ax: plt.Axes, cx: float, cy: float, r: float,
                     lw: float = 1.2, fill: bool = False, facecolor: str = "white") -> None:
    ax.add_patch(Circle((cx, cy), r, fill=fill, facecolor=facecolor,
                        edgecolor=C["gray"], lw=lw, zorder=1))
    ax.add_patch(Polygon([[cx - 0.035, cy + r * 0.96], [cx, cy + r * 1.13],
                          [cx + 0.035, cy + r * 0.96]], closed=True,
                         facecolor=facecolor if fill else "white", edgecolor=C["gray"], lw=lw, zorder=2))
    ax.add_patch(Ellipse((cx - r * 1.03, cy), r * 0.16, r * 0.34, fill=False,
                         edgecolor=C["gray"], lw=lw, zorder=2))
    ax.add_patch(Ellipse((cx + r * 1.03, cy), r * 0.16, r * 0.34, fill=False,
                         edgecolor=C["gray"], lw=lw, zorder=2))


def legend_row(ax: plt.Axes, y: float, color: str, text: str, x: float = 0.04) -> None:
    ax.add_patch(Rectangle((x, y - 0.020), 0.040, 0.040, facecolor=color,
                           edgecolor="#555555", lw=0.5, transform=ax.transAxes, clip_on=False))
    ax.text(x + 0.055, y, text, transform=ax.transAxes, ha="left", va="center",
            fontsize=8.6, color="#111111")


def panel_origin(ax: plt.Axes) -> None:
    clean_panel(ax)
    ax.set_title("(a) Origen cortical y conducción", loc="left", fontweight="bold", pad=3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")

    # Legend separated from the drawing; no text overlays anatomical layers.
    legend_row(ax, 0.78, C["scalp"], "cuero cabelludo")
    legend_row(ax, 0.66, C["skull"], "cráneo")
    legend_row(ax, 0.54, C["csf"], "LCR")
    legend_row(ax, 0.42, C["cortex"], "corteza")
    ax.plot([0.06, 0.10], [0.30, 0.30], transform=ax.transAxes, color=C["orange"], lw=1.7, clip_on=False)
    ax.text(0.115, 0.30, "dipolos corticales", transform=ax.transAxes,
            ha="left", va="center", fontsize=8.6, color="#111111")
    ax.scatter([0.08], [0.20], transform=ax.transAxes, marker="s", s=28, color=C["blue"], clip_on=False)
    ax.text(0.115, 0.20, "electrodos EEG", transform=ax.transAxes,
            ha="left", va="center", fontsize=8.6, color="#111111")

    # Head cross-section, placed to the right so legend and anatomy do not collide.
    cx, cy = 0.66, 0.52
    add_head_outline(ax, cx, cy, 0.33, fill=True, facecolor=C["scalp"])
    ax.add_patch(Circle((cx, cy), 0.260, facecolor=C["skull"], edgecolor="#6E6E6E", lw=0.75, zorder=2))
    ax.add_patch(Circle((cx, cy), 0.200, facecolor=C["csf"], edgecolor="#6E6E6E", lw=0.75, zorder=3))
    ax.add_patch(Circle((cx, cy), 0.130, facecolor=C["cortex"], edgecolor="#5B3B25", lw=0.85, zorder=4))

    theta = np.linspace(48, 132, 6) * np.pi / 180
    ex = cx + 0.348 * np.cos(theta)
    ey = cy + 0.348 * np.sin(theta)
    ax.scatter(ex, ey, marker="s", s=28, color=C["blue"], edgecolor="white", linewidth=0.5, zorder=6)

    dipoles = [(0.61, 0.50, 70), (0.68, 0.47, 105), (0.72, 0.55, 55)]
    for x, y, ang in dipoles:
        dx = 0.036 * np.cos(np.deg2rad(ang))
        dy = 0.036 * np.sin(np.deg2rad(ang))
        ax.add_patch(FancyArrowPatch((x - dx, y - dy), (x + dx, y + dy),
                                     arrowstyle="-|>", mutation_scale=10,
                                     lw=1.15, color=C["orange"], zorder=7))
        ax.add_patch(FancyArrowPatch((x + dx * 0.35, y + dy * 0.35), (x - dx * 0.35, y - dy * 0.35),
                                     arrowstyle="-|>", mutation_scale=8,
                                     lw=0.95, color=C["blue"], alpha=0.9, zorder=7))

    # Propagation arrows are graphical only; explanations live in caption/legend.
    for x0 in [0.61, 0.66, 0.71]:
        ax.annotate("", xy=(x0, 0.80), xytext=(x0, 0.60),
                    arrowprops=dict(arrowstyle="->", color="#666666", lw=0.75, ls="--", alpha=0.70))


def panel_dipole(ax: plt.Axes) -> None:
    clean_panel(ax)
    ax.set_title("(b) Campo del dipolo", loc="left", fontweight="bold", pad=3)
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-0.80, 0.80)
    ax.set_aspect("equal")

    x = np.linspace(-1.0, 1.0, 240)
    y = np.linspace(-0.76, 0.76, 200)
    X, Y = np.meshgrid(x, y)
    eps = 0.055
    V = 1.0 / np.sqrt((X + 0.26) ** 2 + Y ** 2 + eps) - 1.0 / np.sqrt((X - 0.26) ** 2 + Y ** 2 + eps)
    ax.contour(X, Y, V, levels=[-2.0, -1.2, -0.7, -0.35], colors=[C["blue"]], linewidths=0.90, alpha=0.72)
    ax.contour(X, Y, V, levels=[0.35, 0.7, 1.2, 2.0], colors=[C["orange"]], linewidths=0.90, alpha=0.72)
    ax.contour(X, Y, V, levels=[0], colors=["#777777"], linewidths=0.80, alpha=0.60)

    ax.scatter([-0.26, 0.26], [0, 0], s=230, c=[C["orange"], C["blue"]],
               edgecolors="white", linewidth=0.8, zorder=4)
    ax.text(-0.26, 0, "+", ha="center", va="center", color="white", fontsize=15, fontweight="bold", zorder=5)
    ax.text(0.26, 0, "−", ha="center", va="center", color="white", fontsize=17, fontweight="bold", zorder=5)

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
    add_head_outline(ax, 0.50, 0.55, 0.34, lw=1.35)

    pos = np.array([
        [0.42, 0.80], [0.58, 0.80],
        [0.25, 0.69], [0.40, 0.69], [0.50, 0.71], [0.60, 0.69], [0.75, 0.69],
        [0.20, 0.54], [0.36, 0.54], [0.50, 0.54], [0.64, 0.54], [0.80, 0.54],
        [0.27, 0.39], [0.42, 0.38], [0.50, 0.37], [0.58, 0.38], [0.73, 0.39],
        [0.42, 0.25], [0.58, 0.25],
    ])
    bad = np.array([3, 10, 16])
    good = np.array([i for i in range(len(pos)) if i not in set(bad)])
    ax.scatter(pos[good, 0], pos[good, 1], s=48, color=C["blue"], edgecolors="white", linewidth=0.7, zorder=4)
    ax.scatter(pos[bad, 0], pos[bad, 1], s=88, marker="X", color=C["orange"], edgecolors="white", linewidth=0.9, zorder=5)
    ax.text(0.50, 0.94, "nasion", ha="center", va="center", fontsize=8.0, color="#444444")
    legend = [
        Line2D([0], [0], marker="o", color="none", label="canal observado",
               markerfacecolor=C["blue"], markeredgecolor="white", markersize=7),
        Line2D([0], [0], marker="X", color="none", label="canal fallado",
               markerfacecolor=C["orange"], markeredgecolor="white", markersize=8),
    ]
    ax.legend(handles=legend, loc="lower center", bbox_to_anchor=(0.5, -0.02),
              ncol=2, frameon=False, handletextpad=0.3, columnspacing=0.9)


def main() -> None:
    fig, axes = plt.subplots(2, 2, figsize=(7.55, 5.25), constrained_layout=True)
    panel_origin(axes[0, 0])
    panel_dipole(axes[0, 1])
    panel_erp(axes[1, 0])
    panel_topography(axes[1, 1])
    fig.set_constrained_layout_pads(w_pad=0.035, h_pad=0.035, wspace=0.12, hspace=0.10)
    out = FIG / "capitulo2_origen_eeg.pdf"
    fig.savefig(out, format="pdf", bbox_inches="tight", pad_inches=0.020)
    plt.close(fig)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
