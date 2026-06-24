#!/usr/bin/env python3
"""Generate thesis-ready explanatory figures for Chapters 2--3.

Final no-overlap design:
- avoid text on top of graphical elements;
- prefer captions for explanation;
- use vertical/process layouts for methodology and architecture;
- keep traceability as a simple sequential chain with no crossing arrows.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

mpl.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 10.5,
    "axes.labelsize": 9.5,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "legend.fontsize": 8.2,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

C = {
    "blue": "#0072B2",
    "cyan": "#56B4E9",
    "green": "#009E73",
    "orange": "#E69F00",
    "red": "#D55E00",
    "purple": "#CC79A7",
    "yellow": "#F0E442",
    "gray": "#333333",
    "midgray": "#6B6B6B",
    "line": "#222222",
}


def save(fig: plt.Figure, name: str, pad: float = 0.025) -> None:
    out = FIG / name
    fig.savefig(out, format="pdf", bbox_inches="tight", pad_inches=pad)
    plt.close(fig)
    print(f"saved figures/{name}")


def clean_ax(ax: plt.Axes) -> None:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def box(ax: plt.Axes, xy: tuple[float, float], wh: tuple[float, float], text: str,
        color: str, fontsize: float = 9.5, lw: float = 1.15,
        fc_alpha: float = 0.16, weight: str = "normal",
        linestyle: str = "solid") -> FancyBboxPatch:
    x, y = xy
    w, h = wh
    patch = FancyBboxPatch((x, y), w, h,
                           boxstyle="round,pad=0.016,rounding_size=0.025",
                           linewidth=lw, edgecolor=color, facecolor=color,
                           alpha=fc_alpha, linestyle=linestyle)
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, color="#111111", weight=weight, linespacing=1.12)
    return patch


def arrow(ax: plt.Axes, start: tuple[float, float], end: tuple[float, float],
          color: str = C["line"], rad: float = 0.0, lw: float = 1.25,
          style: str = "-|>") -> FancyArrowPatch:
    arr = FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=12,
                          linewidth=lw, color=color,
                          connectionstyle=f"arc3,rad={rad}")
    ax.add_patch(arr)
    return arr


def add_head_outline(ax: plt.Axes, cx: float, cy: float, r: float,
                     lw: float = 1.25, fill: bool = False, facecolor: str = "white") -> None:
    ax.add_patch(Circle((cx, cy), r, fill=fill, facecolor=facecolor,
                        edgecolor=C["gray"], lw=lw, zorder=1))
    ax.add_patch(Polygon([[cx - 0.035, cy + 0.96 * r], [cx, cy + 1.14 * r],
                          [cx + 0.035, cy + 0.96 * r]],
                         closed=True, facecolor=facecolor if fill else "white",
                         edgecolor=C["gray"], lw=lw, zorder=2))
    ax.add_patch(Ellipse((cx - 1.03 * r, cy), 0.17 * r, 0.34 * r,
                         fill=False, edgecolor=C["gray"], lw=lw, zorder=2))
    ax.add_patch(Ellipse((cx + 1.03 * r, cy), 0.17 * r, 0.34 * r,
                         fill=False, edgecolor=C["gray"], lw=lw, zorder=2))


def fig_gsp_concepts() -> None:
    fig = plt.figure(figsize=(7.45, 4.55))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 0.82], width_ratios=[1.0, 1.05],
                          hspace=0.52, wspace=0.38)

    # (a) EEG graph; no textual legend inside the head or below the panel.
    ax = fig.add_subplot(gs[0, 0])
    clean_ax(ax)
    ax.set_aspect("equal")
    ax.set_title("(a) EEG como grafo", loc="left", fontweight="bold", pad=4)
    add_head_outline(ax, 0.50, 0.52, 0.36, lw=1.25)
    pos = np.array([
        [0.42, 0.80], [0.58, 0.80],
        [0.27, 0.68], [0.40, 0.68], [0.50, 0.70], [0.60, 0.68], [0.73, 0.68],
        [0.22, 0.54], [0.36, 0.54], [0.50, 0.54], [0.64, 0.54], [0.78, 0.54],
        [0.29, 0.40], [0.42, 0.38], [0.50, 0.37], [0.58, 0.38], [0.71, 0.40],
        [0.42, 0.25], [0.58, 0.25],
    ])
    for i in range(len(pos)):
        d = np.linalg.norm(pos - pos[i], axis=1)
        for j in np.argsort(d)[1:4]:
            if j > i:
                ax.plot([pos[i, 0], pos[j, 0]], [pos[i, 1], pos[j, 1]],
                        color="#9A9A9A", lw=0.7, zorder=1)
    signal = np.sin(2 * np.pi * (pos[:, 0] - 0.18)) + 0.55 * np.cos(2 * np.pi * pos[:, 1])
    ax.scatter(pos[:, 0], pos[:, 1], c=signal, cmap="RdBu_r", s=66,
               edgecolors="black", linewidth=0.45, zorder=4)

    # (b) Spectrum with no in-plot explanatory labels.
    ax = fig.add_subplot(gs[0, 1])
    ax.set_title("(b) Espectro: autovalor vs. energía", loc="left", fontweight="bold", pad=4)
    k = np.arange(1, 11)
    lam = np.array([0.00, 0.14, 0.26, 0.43, 0.63, 0.88, 1.20, 1.62, 2.12, 2.72])
    energy = np.exp(-0.42 * (k - 1))
    ax.vlines(k, 0, lam, color=C["blue"], lw=2.0)
    ax.scatter(k, lam, color=C["blue"], s=24, zorder=3)
    ax.set_xlabel("modo $k$")
    ax.set_ylabel("autovalor $\\lambda_k$", color=C["blue"])
    ax.tick_params(axis="y", labelcolor=C["blue"])
    ax.set_xlim(0.5, 10.5)
    ax.set_ylim(-0.05, 2.95)
    ax.grid(axis="y", color="#E3E3E3", lw=0.55)
    ax2 = ax.twinx()
    ax2.plot(k, energy, color=C["orange"], marker="o", lw=1.5, ms=4)
    ax2.set_ylim(0, 1.08)
    ax2.set_ylabel("energía normalizada", color=C["orange"])
    ax2.tick_params(axis="y", labelcolor=C["orange"])
    handles = [
        Line2D([0], [0], color=C["blue"], marker="o", lw=1.8, label="$\\lambda_k$"),
        Line2D([0], [0], color=C["orange"], marker="o", lw=1.5, label="energía modal"),
    ]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.50, -0.25),
              ncol=2, frameon=False, handlelength=1.5, columnspacing=1.2)

    # (c) Compact reconstruction diagram, no reading subtitle.
    ax = fig.add_subplot(gs[1, :])
    clean_ax(ax)
    ax.set_title("(c) Reconstrucción regularizada", loc="left", fontweight="bold", pad=4)
    box(ax, (0.035, 0.57), (0.225, 0.25), "canales\nobservados\n$P_{\\Omega} x$", C["green"], fontsize=8.8, weight="bold")
    box(ax, (0.035, 0.18), (0.225, 0.25), "canales\nfaltantes\n$P_{\\Omega^c} x$", C["red"], fontsize=8.8, weight="bold")
    box(ax, (0.385, 0.38), (0.300, 0.29), "problema regularizado\n$fidelidad + x^T Lx$", C["blue"], fontsize=9.0, weight="bold")
    box(ax, (0.775, 0.38), (0.190, 0.29), "estimación\n$\\hat{x}_{\\Omega^c}$", C["purple"], fontsize=9.0, weight="bold")
    box(ax, (0.410, 0.065), (0.250, 0.18), "grafo EEG\n$W, L$", C["orange"], fontsize=8.8, weight="bold")
    arrow(ax, (0.260, 0.695), (0.385, 0.555))
    arrow(ax, (0.260, 0.305), (0.385, 0.495))
    arrow(ax, (0.535, 0.245), (0.535, 0.38))
    arrow(ax, (0.685, 0.525), (0.775, 0.525))
    fig.subplots_adjust(left=0.060, right=0.92, top=0.95, bottom=0.12)
    save(fig, "ch2_gsp_concepts_clean.pdf")


def fig_trss_operator() -> None:
    fig, ax = plt.subplots(figsize=(7.45, 2.35))
    clean_ax(ax)
    ax.set_title("Descomposición del objetivo TRSS", pad=4, fontweight="bold")

    box(ax, (0.035, 0.41), (0.18, 0.20), "señal\nobservada\n$Y$", C["midgray"], fontsize=10.0, fc_alpha=0.09, weight="bold")
    terms = [
        (0.33, 0.73, "fidelidad a datos\n$\\|P_\\Omega X - Y\\|_F^2$", C["green"]),
        (0.33, 0.43, "suavidad espacial\n$\\alpha\\,\\mathrm{tr}(X^T L X)$", C["blue"]),
        (0.33, 0.13, "suavidad temporal\n$\\beta\\,\\|X D_t\\|_F^2$", C["orange"]),
    ]
    for x, y, text, color in terms:
        box(ax, (x, y), (0.30, 0.18), text, color, fontsize=9.7, weight="bold")
        arrow(ax, (0.215, 0.51), (x - 0.010, y + 0.09), lw=1.05)
    box(ax, (0.77, 0.38), (0.19, 0.25), "señal\nreconstruida\n$\\hat{X}$", C["purple"], fontsize=10.3, weight="bold")
    for x, y, _, _ in terms:
        arrow(ax, (x + 0.305, y + 0.09), (0.77, 0.505), lw=1.05)
    ax.text(0.50, 0.035, "$P_\\Omega$: máscara de canales observados; $L$: Laplaciano espacial; $D_t$: diferencias temporales",
            ha="center", va="bottom", fontsize=8.4, color="#222222")
    fig.subplots_adjust(left=0.035, right=0.985, top=0.86, bottom=0.18)
    save(fig, "ch2_trss_operator.pdf")


def fig_methodology_flow() -> None:
    fig, ax = plt.subplots(figsize=(5.30, 3.75))
    clean_ax(ax)
    steps = [
        ("Datos EEG", "PhysioNet · BCI IV 2a · MNE Sample", C["cyan"]),
        ("Máscaras de pérdida", "aleatoria / contigua · semilla", C["green"]),
        ("Métodos", "18 implementaciones · interfaz común", C["blue"]),
        ("Métricas", "MAE/RMSE/SNR · DTW/LSD/coh. · tiempo", C["orange"]),
        ("Comparación pareada", "misma señal/máscara/semilla\nmedianas · win-rate", C["purple"]),
    ]
    y_positions = [0.80, 0.64, 0.48, 0.32, 0.16]
    for idx, ((title, detail, color), y) in enumerate(zip(steps, y_positions)):
        box(ax, (0.14, y), (0.72, 0.105), f"{title}\n{detail}", color, fontsize=8.7, weight="bold")
        if idx < len(y_positions) - 1:
            arrow(ax, (0.50, y), (0.50, y_positions[idx + 1] + 0.105), lw=1.10)
    fig.subplots_adjust(left=0.04, right=0.96, top=0.97, bottom=0.05)
    save(fig, "ch3_methodology_flow.pdf")


def fig_architecture_blocks() -> None:
    fig, ax = plt.subplots(figsize=(5.50, 5.25))
    clean_ax(ax)
    # Phase containers.
    ax.add_patch(Rectangle((0.08, 0.50), 0.84, 0.44, facecolor="#F3FAFD", edgecolor="#9CCBE3", lw=0.9))
    ax.text(0.50, 0.905, "Fase exploratoria: selección y ajuste", ha="center", va="center", fontsize=9.5, weight="bold")
    exploratory = [
        ("Datos EEG", "PhysioNet 64 · BCI IV 2a 22 · MNE Sample 60", C["cyan"]),
        ("Simulación de pérdida", "aleatoria · contigua", C["green"]),
        ("Grafo + interpolación", "10 grafos · 18 métodos · Optuna", C["blue"]),
    ]
    ys = [0.79, 0.66, 0.53]
    for idx, ((title, detail, color), y) in enumerate(zip(exploratory, ys)):
        box(ax, (0.18, y), (0.64, 0.085), f"{title}\n{detail}", color, fontsize=8.9, weight="bold")
        if idx < 2:
            arrow(ax, (0.50, y), (0.50, ys[idx + 1] + 0.085), lw=1.05)

    # Divider between phases.
    ax.text(0.50, 0.455, "parámetros congelados", ha="center", va="center", fontsize=8.8,
            bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="#AAAAAA", lw=0.8))
    arrow(ax, (0.50, 0.50), (0.50, 0.40), lw=1.05)

    ax.add_patch(Rectangle((0.08, 0.08), 0.84, 0.31, facecolor="#FFF9E8", edgecolor="#D7B548", lw=0.9))
    ax.text(0.50, 0.355, "Fase comparativa", ha="center", va="center", fontsize=9.5, weight="bold")
    comparative = [
        ("Evaluación", "error · forma/espectro · tiempo", C["orange"]),
        ("Artefactos", "JSON/CSV · NPZ · PDF/TeX", C["purple"]),
    ]
    ys2 = [0.245, 0.115]
    for idx, ((title, detail, color), y) in enumerate(zip(comparative, ys2)):
        box(ax, (0.18, y), (0.64, 0.085), f"{title}\n{detail}", color, fontsize=8.9, weight="bold")
        if idx == 0:
            arrow(ax, (0.50, y), (0.50, ys2[idx + 1] + 0.085), lw=1.05)
    fig.subplots_adjust(left=0.04, right=0.96, top=0.97, bottom=0.04)
    save(fig, "ch3_architecture_blocks.pdf")


def fig_traceability() -> None:
    fig, ax = plt.subplots(figsize=(5.40, 4.65))
    clean_ax(ax)
    steps = [
        ("ENTRADA", "Código Git\nConfiguración YAML\nSemillas y máscaras", C["cyan"]),
        ("EJECUCIÓN", "Ejecución reproducible\nidentificador SHA-256", C["green"]),
        ("ARTEFACTOS", "Métricas JSON/CSV\nSeñales NPZ\nTablas LaTeX · Figuras PDF", C["orange"]),
        ("DOCUMENTO", "afirmación → tabla/figura\n→ archivo → script", C["purple"]),
    ]
    y_positions = [0.77, 0.55, 0.32, 0.10]
    for idx, ((title, detail, color), y) in enumerate(zip(steps, y_positions)):
        box(ax, (0.16, y), (0.68, 0.145), f"{title}\n{detail}", color, fontsize=9.2, weight="bold")
        if idx < len(y_positions) - 1:
            arrow(ax, (0.50, y), (0.50, y_positions[idx + 1] + 0.145), lw=1.15)
    fig.subplots_adjust(left=0.04, right=0.96, top=0.97, bottom=0.05)
    save(fig, "ch4_traceability_pipeline.pdf")


if __name__ == "__main__":
    fig_gsp_concepts()
    fig_trss_operator()
    fig_methodology_flow()
    fig_architecture_blocks()
    fig_traceability()
