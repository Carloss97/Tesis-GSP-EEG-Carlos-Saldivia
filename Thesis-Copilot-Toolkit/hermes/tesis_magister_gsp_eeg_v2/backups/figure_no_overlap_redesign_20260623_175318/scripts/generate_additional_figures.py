#!/usr/bin/env python3
"""Generate compact, thesis-ready explanatory figures for Chapters 2--3.

Design response to advisor feedback:
- EEG drawings use recognizable head outlines (nose/ears) and sensor layouts.
- Spectrum panel separates Laplacian eigenvalues from illustrative signal energy.
- No gray explanatory bars/subtitles that duplicate captions.
- Flow/architecture/traceability figures are compact and readable.
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
    "lightgray": "#F3F3F3",
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
            fontsize=fontsize, color="#111111", weight=weight, linespacing=1.13)
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


# ---------------------------------------------------------------------------
# Figure 2.2: GSP concepts.
# ---------------------------------------------------------------------------
def fig_gsp_concepts() -> None:
    fig = plt.figure(figsize=(7.55, 4.35))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.00, 0.90], width_ratios=[1.02, 1.0],
                          hspace=0.30, wspace=0.35)

    # (a) EEG graph on a recognizable head.
    ax = fig.add_subplot(gs[0, 0])
    clean_ax(ax)
    ax.set_aspect("equal")
    ax.set_title("(a) EEG como grafo", loc="left", fontweight="bold", pad=4)
    add_head_outline(ax, 0.50, 0.53, 0.34, lw=1.2)
    pos = np.array([
        [0.42, 0.80], [0.58, 0.80],
        [0.27, 0.68], [0.40, 0.68], [0.50, 0.70], [0.60, 0.68], [0.73, 0.68],
        [0.22, 0.54], [0.36, 0.54], [0.50, 0.54], [0.64, 0.54], [0.78, 0.54],
        [0.29, 0.40], [0.42, 0.38], [0.50, 0.37], [0.58, 0.38], [0.71, 0.40],
        [0.42, 0.25], [0.58, 0.25],
    ])
    # k-nearest edges in the 2D montage.
    for i in range(len(pos)):
        d = np.linalg.norm(pos - pos[i], axis=1)
        for j in np.argsort(d)[1:4]:
            if j > i:
                ax.plot([pos[i, 0], pos[j, 0]], [pos[i, 1], pos[j, 1]],
                        color="#9A9A9A", lw=0.7, zorder=1)
    signal = np.sin(2 * np.pi * (pos[:, 0] - 0.18)) + 0.55 * np.cos(2 * np.pi * pos[:, 1])
    ax.scatter(pos[:, 0], pos[:, 1], c=signal, cmap="RdBu_r", s=66,
               edgecolors="black", linewidth=0.45, zorder=4)
    ax.text(0.50, 0.055, "electrodos conectados por cercanía espacial",
            ha="center", va="center", fontsize=8.3, color="#111111")

    # (b) Laplacian eigenvalues vs illustrative energy.
    ax = fig.add_subplot(gs[0, 1])
    ax.set_title("(b) Espectro: autovalor vs. energía", loc="left", fontweight="bold", pad=4)
    k = np.arange(1, 11)
    lam = np.array([0.00, 0.14, 0.26, 0.43, 0.63, 0.88, 1.20, 1.62, 2.12, 2.72])
    energy = np.exp(-0.42 * (k - 1))
    ax.vlines(k, 0, lam, color=C["blue"], lw=2.0, label="autovalor $\\lambda_k$")
    ax.scatter(k, lam, color=C["blue"], s=24, zorder=3)
    ax.set_xlabel("modo $k$")
    ax.set_ylabel("autovalor $\\lambda_k$", color=C["blue"])
    ax.tick_params(axis="y", labelcolor=C["blue"])
    ax.set_xlim(0.5, 10.5)
    ax.set_ylim(-0.05, 2.95)
    ax.grid(axis="y", color="#E3E3E3", lw=0.55)
    ax2 = ax.twinx()
    ax2.plot(k, energy, color=C["orange"], marker="o", lw=1.5, ms=4,
             label="energía modal ilustrativa")
    ax2.set_ylim(0, 1.08)
    ax2.set_ylabel("energía normalizada", color=C["orange"])
    ax2.tick_params(axis="y", labelcolor=C["orange"])
    lines = [
        Line2D([0], [0], color=C["blue"], marker="o", lw=1.8, label="$\\lambda_k$"),
        Line2D([0], [0], color=C["orange"], marker="o", lw=1.5, label="energía modal"),
    ]
    ax.legend(handles=lines, loc="upper left", frameon=False, borderaxespad=0.2, handlelength=1.6)
    ax.text(0.04, 0.92, "modos bajos", transform=ax.transAxes, fontsize=8.0, color="#333333")
    ax.text(0.67, 0.08, "modos altos", transform=ax.transAxes, fontsize=8.0, color="#333333")

    # (c) Regularized reconstruction, no bottom gray subtitle.
    ax = fig.add_subplot(gs[1, :])
    clean_ax(ax)
    ax.set_title("(c) Reconstrucción regularizada", loc="left", fontweight="bold", pad=4)
    box(ax, (0.05, 0.58), (0.20, 0.22), "canales\nobservados\n$P_\\Omega x$", C["green"], fontsize=9.5, weight="bold")
    box(ax, (0.05, 0.20), (0.20, 0.22), "canales\nfaltantes\n$P_{\\Omega^c}x$", C["red"], fontsize=9.5, weight="bold")
    box(ax, (0.39, 0.39), (0.26, 0.25), "problema regularizado\n$fidelidad + x^T Lx$", C["blue"], fontsize=10.0, weight="bold")
    box(ax, (0.77, 0.39), (0.18, 0.25), "estimación\n$\\hat{x}_{\\Omega^c}$", C["purple"], fontsize=10.0, weight="bold")
    box(ax, (0.39, 0.08), (0.26, 0.17), "grafo EEG\n$W, L$", C["orange"], fontsize=9.3, weight="bold")
    arrow(ax, (0.25, 0.69), (0.39, 0.54))
    arrow(ax, (0.25, 0.31), (0.39, 0.49))
    arrow(ax, (0.52, 0.25), (0.52, 0.39))
    arrow(ax, (0.65, 0.515), (0.77, 0.515))
    fig.subplots_adjust(left=0.060, right=0.93, top=0.95, bottom=0.08)
    save(fig, "ch2_gsp_concepts_clean.pdf")


# ---------------------------------------------------------------------------
# Figure 2.3: TRSS objective.
# ---------------------------------------------------------------------------
def fig_trss_operator() -> None:
    fig, ax = plt.subplots(figsize=(7.45, 3.05))
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
        arrow(ax, (0.215, 0.51), (x - 0.010, y + 0.09), rad=0.0, lw=1.05)

    box(ax, (0.77, 0.38), (0.19, 0.25), "señal\nreconstruida\n$\\hat{X}$", C["purple"], fontsize=10.3, weight="bold")
    for x, y, _, _ in terms:
        arrow(ax, (x + 0.305, y + 0.09), (0.77, 0.505), rad=0.0, lw=1.05)

    # Small operators placed away from arrows, not as a gray subtitle.
    ax.text(0.50, 0.025, "$P_\\Omega$: máscara de canales observados; $L$: Laplaciano espacial; $D_t$: diferencias temporales",
            ha="center", va="bottom", fontsize=8.5, color="#222222")
    fig.subplots_adjust(left=0.035, right=0.985, top=0.88, bottom=0.12)
    save(fig, "ch2_trss_operator.pdf")


# ---------------------------------------------------------------------------
# Figure 3.1: methodology flow.
# ---------------------------------------------------------------------------
def fig_methodology_flow() -> None:
    fig, ax = plt.subplots(figsize=(7.45, 1.55))
    clean_ax(ax)
    nodes = [
        (0.025, 0.43, 0.17, 0.40, "Datos EEG\nPhysioNet\nBCI IV 2a\nMNE Sample", C["cyan"]),
        (0.225, 0.43, 0.17, 0.40, "Máscaras\npérdida aleatoria\ny contigua\nsemilla", C["green"]),
        (0.425, 0.43, 0.17, 0.40, "Métodos\n18 impl.\ninterfaz común\nTRSS/MNE", C["blue"]),
        (0.625, 0.43, 0.17, 0.40, "Métricas\nMAE/RMSE/SNR\nDTW/LSD/coh.\ntiempo", C["orange"]),
        (0.825, 0.43, 0.15, 0.40, "Comparación\npareada\nmedianas\nwin-rate", C["purple"]),
    ]
    for x, y, w, h, text, color in nodes:
        box(ax, (x, y), (w, h), text, color, fontsize=8.5, weight="bold")
    for i in range(len(nodes) - 1):
        x, y, w, h, *_ = nodes[i]
        x2, y2, *_ = nodes[i + 1]
        arrow(ax, (x + w + 0.006, y + h / 2), (x2 - 0.006, y2 + h / 2), lw=1.15)
    ax.text(0.50, 0.17, "Control pareado: misma señal, máscara y semilla para todos los métodos",
            ha="center", va="center", fontsize=8.8, color="#111111")
    fig.subplots_adjust(left=0.025, right=0.99, top=0.96, bottom=0.14)
    save(fig, "ch3_methodology_flow.pdf")


# ---------------------------------------------------------------------------
# Figure 3.2: architecture blocks.
# ---------------------------------------------------------------------------
def fig_architecture_blocks() -> None:
    fig, ax = plt.subplots(figsize=(7.55, 2.30))
    clean_ax(ax)

    # Phase regions aligned exactly with the blocks, without a floating note.
    ax.add_patch(Rectangle((0.020, 0.78), 0.585, 0.18, facecolor="#F1F8FC", edgecolor="#9CCBE3", lw=0.8))
    ax.add_patch(Rectangle((0.630, 0.78), 0.345, 0.18, facecolor="#FFF8E6", edgecolor="#D7B548", lw=0.8))
    ax.text(0.312, 0.87, "Fase exploratoria: selección y ajuste", ha="center", va="center", fontsize=8.6, weight="bold")
    ax.text(0.802, 0.87, "Fase comparativa: parámetros congelados", ha="center", va="center", fontsize=8.2, weight="bold")

    nodes = [
        (0.035, 0.38, 0.16, 0.31, "Datos EEG\nPhysioNet 64\nBCI IV 2a 22\nMNE Sample 60", C["cyan"]),
        (0.225, 0.38, 0.16, 0.31, "Simulación\nde pérdida\naleatoria\ncontigua", C["green"]),
        (0.415, 0.38, 0.18, 0.31, "Grafo +\ninterpolación\n10 grafos\n18 métodos", C["blue"]),
        (0.660, 0.38, 0.15, 0.31, "Evaluación\nerror\nforma/espectro\ntiempo", C["orange"]),
        (0.845, 0.38, 0.13, 0.31, "Artefactos\nJSON/CSV\nNPZ\nPDF/TeX", C["purple"]),
    ]
    for x, y, w, h, text, color in nodes:
        box(ax, (x, y), (w, h), text, color, fontsize=8.5, weight="bold")
    for i in range(len(nodes) - 1):
        x, y, w, h, *_ = nodes[i]
        x2, y2, *_ = nodes[i + 1]
        arrow(ax, (x + w + 0.006, y + h / 2), (x2 - 0.006, y2 + h / 2), lw=1.10)

    ax.plot([0.625, 0.625], [0.30, 0.98], color="#666666", lw=0.9, ls=":")
    ax.text(0.50, 0.18, "Los resultados comparativos no reabren la búsqueda de hiperparámetros",
            ha="center", va="center", fontsize=8.4, color="#111111")
    fig.subplots_adjust(left=0.02, right=0.99, top=0.96, bottom=0.12)
    save(fig, "ch3_architecture_blocks.pdf")


# ---------------------------------------------------------------------------
# Figure 3.3: traceability pipeline.
# ---------------------------------------------------------------------------
def fig_traceability() -> None:
    fig, ax = plt.subplots(figsize=(7.45, 3.0))
    clean_ax(ax)

    ax.text(0.13, 0.91, "ENTRADA", ha="center", fontsize=9.0, weight="bold")
    ax.text(0.44, 0.91, "EJECUCIÓN", ha="center", fontsize=9.0, weight="bold")
    ax.text(0.76, 0.91, "ARTEFACTOS", ha="center", fontsize=9.0, weight="bold")

    inputs = [
        (0.045, 0.69, "Código\nrepositorio Git"),
        (0.045, 0.49, "Configuración\nYAML"),
        (0.045, 0.29, "Semillas\ny máscaras"),
    ]
    for x, y, text in inputs:
        box(ax, (x, y), (0.18, 0.13), text, C["cyan"], fontsize=8.8, weight="bold")
        arrow(ax, (0.225, y + 0.065), (0.345, 0.555), lw=1.05)

    box(ax, (0.345, 0.44), (0.20, 0.23), "Ejecución\nreproducible\nSHA-256", C["green"], fontsize=9.5, weight="bold")

    artifacts = [
        (0.645, 0.68, "Métricas\nJSON/CSV", C["yellow"]),
        (0.645, 0.47, "Señales\nNPZ", C["yellow"]),
        (0.825, 0.68, "Tablas\nLaTeX", C["orange"]),
        (0.825, 0.47, "Figuras\nPDF", C["orange"]),
    ]
    for x, y, text, color in artifacts:
        arrow(ax, (0.545, 0.555), (x - 0.010, y + 0.065), lw=1.05)
        box(ax, (x, y), (0.135, 0.13), text, color, fontsize=8.7, weight="bold")

    box(ax, (0.645, 0.18), (0.315, 0.16), "Documento de tesis\nafirmación → tabla/figura → archivo → script", C["purple"], fontsize=8.9, weight="bold")
    for x, y, *_ in artifacts:
        arrow(ax, (x + 0.067, y), (0.80, 0.34), lw=0.95, color="#444444")

    fig.subplots_adjust(left=0.025, right=0.99, top=0.94, bottom=0.08)
    save(fig, "ch4_traceability_pipeline.pdf")


# ---------------------------------------------------------------------------
# Discussion figure kept for downstream chapters.
# ---------------------------------------------------------------------------
def fig_decision_map() -> None:
    fig, ax = plt.subplots(figsize=(7.1, 4.05))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Severidad / agrupamiento de pérdida", labelpad=8)
    ax.set_ylabel("Prioridad de precisión", labelpad=8)
    ax.add_patch(Rectangle((0, 0), .45, .55, fc="#D9EAF7", ec="none"))
    ax.add_patch(Rectangle((.45, .55), .55, .45, fc="#DDEFE6", ec="none"))
    ax.add_patch(Rectangle((.45, 0), .55, .55, fc="#FFF0D0", ec="none"))
    ax.plot([.18, .82], [.28, .82], ls="--", lw=1.5, color=C["line"])
    ax.text(.23, .23, "MNE\npor defecto", ha="center", va="center", fontsize=11,
            weight="bold", color="#004C7F")
    ax.text(.77, .86, "TRSS\njustificado", ha="center", va="center", fontsize=11,
            weight="bold", color="#006B4A")
    ax.text(.72, .30, "validar\ncaso a caso", ha="center", va="center", fontsize=10.4,
            weight="bold", color="#8A5600")
    ax.annotate("frontera\npráctica", xy=(.58, .60), xytext=(.30, .86),
                arrowprops=dict(arrowstyle="->", lw=1.0, connectionstyle="arc3,rad=-0.15"),
                fontsize=9.2, ha="center", va="center",
                bbox=dict(fc="white", ec="#BBBBBB", boxstyle="round,pad=0.25"))
    ax.set_xticks([.08, .50, .92])
    ax.set_xticklabels(["baja", "media", "alta"])
    ax.set_yticks([.08, .50, .92])
    ax.set_yticklabels(["latencia", "balance", "precisión"])
    ax.grid(color="#FFFFFF", lw=1.0)
    for spine in ax.spines.values():
        spine.set_color("#555555")
    fig.subplots_adjust(left=0.16, right=0.98, bottom=0.18, top=0.94)
    save(fig, "ch7_decision_map.pdf")


if __name__ == "__main__":
    fig_gsp_concepts()
    fig_trss_operator()
    fig_methodology_flow()
    fig_architecture_blocks()
    fig_traceability()
