#!/usr/bin/env python3
"""Generate visually clean explanatory figures for the complete thesis.

Design rules used here:
- short labels inside boxes; explanatory prose belongs in LaTeX captions;
- high-contrast, colorblind-safe palette;
- no long notes inside axes;
- arrows are routed outside labels;
- all outputs are vector PDF.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

mpl.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

C = {
    "blue": "#0072B2", "orange": "#E69F00", "green": "#009E73",
    "red": "#D55E00", "purple": "#CC79A7", "cyan": "#56B4E9",
    "yellow": "#F0E442", "gray": "#444444", "light": "#F7F7F7",
    "line": "#333333",
}


def save(fig: plt.Figure, name: str):
    fig.savefig(FIG / name, format="pdf", bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    print(f"saved figures/{name}")


def clean_ax(ax):
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)


def box(ax, xy, wh, text, color, fontsize=10, lw=1.2, fc_alpha=0.16, weight="normal"):
    x, y = xy; w, h = wh
    patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.018,rounding_size=0.035",
                           linewidth=lw, edgecolor=color, facecolor=color, alpha=fc_alpha)
    ax.add_patch(patch)
    ax.text(x+w/2, y+h/2, text, ha="center", va="center", fontsize=fontsize,
            color="#111111", weight=weight, linespacing=1.12)
    return patch


def arrow(ax, start, end, color=C["line"], rad=0.0, lw=1.6):
    arr = FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13,
                          linewidth=lw, color=color, connectionstyle=f"arc3,rad={rad}")
    ax.add_patch(arr)
    return arr


# ---------------------------------------------------------------------------
# Chapter 1: roadmap.
# ---------------------------------------------------------------------------
def fig_roadmap():
    fig, ax = plt.subplots(figsize=(7.4, 3.0)); clean_ax(ax)
    xs = [0.04, 0.28, 0.52, 0.76]
    top = [
        ("Problema", "canales EEG\nfaltantes"),
        ("Métodos", "MNE, GSP\ny TRSS"),
        ("Evaluación", "métricas +\nestadística"),
        ("Decisión", "cuándo usar\ncada método"),
    ]
    cols = [C["red"], C["blue"], C["green"], C["orange"]]
    for i, (title, body) in enumerate(top):
        box(ax, (xs[i], 0.54), (0.18, 0.27), f"{title}\n{body}", cols[i], fontsize=10.2, weight="bold")
        if i < 3: arrow(ax, (xs[i]+0.19, 0.675), (xs[i+1]-0.01, 0.675))
    # Evidence lane, short and readable.
    lane = [(0.08, "datos"), (0.31, "máscaras"), (0.54, "métricas"), (0.77, "trade-off")]
    for x, label in lane:
        box(ax, (x, 0.20), (0.15, 0.16), label, C["gray"], fontsize=9.8, fc_alpha=0.10)
    for i in range(len(lane)-1): arrow(ax, (lane[i][0]+0.155, 0.28), (lane[i+1][0]-0.005, 0.28), lw=1.2)
    ax.text(0.5, 0.05, "Lectura: la tesis delimita una frontera práctica MNE--TRSS; no afirma dominancia universal.",
            ha="center", va="center", fontsize=9.2, color=C["gray"])
    save(fig, "ch1_thesis_roadmap.pdf")


# ---------------------------------------------------------------------------
# Chapter 2: GSP concepts.
# ---------------------------------------------------------------------------
def fig_gsp_concepts():
    """Three-panel GSP figure with generous spacing and no crossing arrows.

    Layout intentionally uses two rows: graph + spectrum on top, reconstruction
    full-width at bottom. This avoids the cramped third panel that previously
    caused labels to leave boxes and arrows to cross text.
    """
    fig = plt.figure(figsize=(7.6, 4.75))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.08, 0.92], width_ratios=[1.05, 1.0],
                          hspace=0.48, wspace=0.34)

    # (a) EEG graph. Keep a generous data margin so the scalp circle is not clipped.
    ax = fig.add_subplot(gs[0, 0])
    ax.set_aspect('equal')
    ax.set_xlim(-0.12, 1.12); ax.set_ylim(-0.12, 1.12)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_title("(a) EEG como grafo", pad=6)
    theta = np.linspace(0, 2*np.pi, 12, endpoint=False)
    r = np.array([0.42,0.31,0.43,0.29,0.39,0.47,0.32,0.42,0.28,0.45,0.35,0.40])
    xy = np.c_[0.5 + r*np.cos(theta), 0.5 + r*np.sin(theta)]
    for i in range(len(xy)):
        d = np.linalg.norm(xy - xy[i], axis=1)
        for j in np.argsort(d)[1:4]:
            if j > i:
                ax.plot([xy[i,0], xy[j,0]], [xy[i,1], xy[j,1]], color="#BBBBBB", lw=0.85, zorder=1)
    val = np.sin(theta) + 0.35*np.cos(2*theta)
    ax.add_patch(Circle((0.5,0.5),0.56, fill=False, lw=1.15, color=C["line"]))
    ax.scatter(xy[:,0], xy[:,1], c=val, cmap="RdBu_r", s=82, edgecolors="black", linewidths=0.5, zorder=2)
    ax.text(0.5, -0.035, "nodos = electrodos; aristas = cercanía espacial",
            ha="center", va="top", fontsize=9.0, color="#111111", clip_on=False)

    # (b) Laplacian spectrum. All labels live away from axes/ticks.
    ax = fig.add_subplot(gs[0, 1])
    ax.set_title("(b) Espectro del Laplaciano", pad=6)
    k = np.arange(1, 11)
    lam = np.array([0, .16, .29, .45, .65, .92, 1.25, 1.7, 2.2, 2.8])
    ax.vlines(k, 0, lam, color=C["blue"], lw=2)
    ax.scatter(k, lam, color=C["blue"], s=28, zorder=3)
    ax.set_xlabel(r"modo $k$", labelpad=4)
    ax.set_ylabel(r"autovalor $\lambda_k$", labelpad=6)
    ax.set_xlim(0.4, 10.6); ax.set_ylim(-0.03, 3.08)
    ax.grid(axis='y', color="#E5E5E5", lw=0.6)
    ax.annotate("modos\nsuaves", xy=(2.0, .22), xytext=(3.0, 1.10),
                arrowprops=dict(arrowstyle="->", lw=0.9), fontsize=8.8, ha="center")
    ax.annotate("modos\nrápidos", xy=(9.0, 2.28), xytext=(7.45, 2.62),
                arrowprops=dict(arrowstyle="->", lw=0.9), fontsize=8.8, ha="center")

    # (c) Reconstruction. Use separated lanes and vertical arrows; no arrow crosses a label.
    ax = fig.add_subplot(gs[1, :]); clean_ax(ax)
    ax.set_title("(c) Reconstrucción regularizada", pad=7)
    # top lane
    box(ax, (0.07, .58), (.20, .23), "canales\nobservados", C["green"], fontsize=9.6, weight="bold")
    box(ax, (0.40, .58), (.22, .23), "ajuste a\ndatos", C["green"], fontsize=9.6, weight="bold")
    box(ax, (0.73, .58), (.20, .23), "señal\nreconstruida", C["purple"], fontsize=9.5, weight="bold")
    arrow(ax, (.275,.695), (.395,.695), lw=1.2)
    arrow(ax, (.625,.695), (.725,.695), lw=1.2)
    # bottom lane
    box(ax, (0.07, .16), (.20, .23), "canales\nfaltantes", C["red"], fontsize=9.6, weight="bold")
    box(ax, (0.40, .16), (.22, .23), "suavidad\ndel grafo", C["blue"], fontsize=9.6, weight="bold")
    box(ax, (0.73, .16), (.20, .23), "estimación\noculta", C["orange"], fontsize=9.5, weight="bold")
    arrow(ax, (.275,.275), (.395,.275), lw=1.2)
    arrow(ax, (.625,.275), (.725,.275), lw=1.2)
    # combine lanes into final output with arrows routed between boxes.
    arrow(ax, (.83,.58), (.83,.40), lw=1.1)
    ax.text(.50, .015, "La solución conserva datos observados y penaliza variaciones no suaves en el grafo.",
            ha="center", va="bottom", fontsize=9.2, color="#111111")
    fig.subplots_adjust(left=0.055, right=0.985, top=0.93, bottom=0.07)
    save(fig, "ch2_gsp_concepts_clean.pdf")


# ---------------------------------------------------------------------------
# Chapter 2: TRSS operator.
# ---------------------------------------------------------------------------
def fig_trss_operator():
    fig, ax = plt.subplots(figsize=(7.4, 3.0)); clean_ax(ax)
    ax.set_title("Descomposición del objetivo TRSS", pad=5)
    box(ax, (0.04, .38), (.18, .24), "señal\nobservada\nY", C["gray"], fontsize=10)
    # three readable terms
    terms = [
        (0.33, .68, "fidelidad\na datos", r"$\|P_\Omega X-Y\|_F^2$", C["green"]),
        (0.33, .38, "suavidad\nespacial", r"$\alpha\,\mathrm{tr}(X^\top L X)$", C["blue"]),
        (0.33, .08, "suavidad\ntemporal", r"$\beta\,\|X D_t\|_F^2$", C["orange"]),
    ]
    for x,y,label,eq,col in terms:
        box(ax, (x,y), (.26,.18), label, col, fontsize=10, weight="bold")
        ax.text(x+.13, y-.045, eq, ha="center", va="top", fontsize=9.4, color=C["line"])
        arrow(ax, (.22,.50), (x-.012,y+.09), lw=1.2)
    box(ax, (0.72, .36), (.22, .26), "señal\nreconstruida\n$\\hat{X}$", C["purple"], fontsize=10.5, weight="bold")
    for x,y,_,_,_ in terms:
        arrow(ax, (x+.265, y+.09), (.72, .49), lw=1.2)
    ax.text(0.50, 0.96, "Los tres términos se optimizan conjuntamente; el término temporal restringe soluciones admisibles.",
            ha="center", va="center", fontsize=9.4, color="#111111")
    save(fig, "ch2_trss_operator.pdf")


# ---------------------------------------------------------------------------
# Chapter 3: methodology flow.
# ---------------------------------------------------------------------------
def fig_methodology_flow():
    """Chapter 3 flow figure redesigned with separated boxes and clear arrows."""
    fig, ax = plt.subplots(figsize=(7.4, 2.9)); clean_ax(ax)
    ax.set_title("Flujo metodológico de la evaluación", pad=8)
    nodes = [
        (.06, .62, .19, .22, "datos\nEEG", C["cyan"]),
        (.31, .62, .19, .22, "máscaras\nde pérdida", C["orange"]),
        (.56, .62, .22, .22, "métodos\ncomparados", C["blue"]),
        (.18, .27, .22, .20, "métricas\npor caso", C["green"]),
        (.58, .27, .28, .20, "comparación\npareada", C["purple"]),
    ]
    for x,y,w,h,t,c in nodes:
        box(ax, (x,y), (w,h), t, c, fontsize=10.2, weight="bold")
    # Top row arrows, placed in gaps rather than on top of bubbles.
    arrow(ax, (.255,.73), (.305,.73), lw=1.2)
    arrow(ax, (.505,.73), (.555,.73), lw=1.2)
    # Downstream arrows routed with arcs outside text boxes.
    arrow(ax, (.670,.615), (.310,.470), rad=0.13, lw=1.15)
    arrow(ax, (.405,.37), (.575,.37), lw=1.15)
    box(ax, (.08,.055), (.84,.13), "control pareado transversal: misma señal, misma máscara y misma semilla", C["gray"], fontsize=10, fc_alpha=.06)
    arrow(ax, (.720,.265), (.720,.190), lw=1.0)
    fig.subplots_adjust(left=0.04, right=0.98, top=0.86, bottom=0.11)
    save(fig, "ch3_methodology_flow.pdf")


# ---------------------------------------------------------------------------
# Chapter 4: traceability pipeline.
# ---------------------------------------------------------------------------
def fig_traceability():
    fig, ax = plt.subplots(figsize=(7.4, 3.0)); clean_ax(ax)
    left = [(0.05,.70,"código"), (0.05,.43,"config."), (0.05,.16,"semillas\ny máscaras")]
    for x,y,t in left:
        box(ax, (x,y), (.18,.16), t, C["blue"], fontsize=10)
        arrow(ax, (x+.185,y+.08), (.39,.50), lw=1.15)
    box(ax, (.39,.39), (.22,.22), "ejecución\nreproducible", C["green"], fontsize=10.5, weight="bold")
    right = [(0.75,.70,"CSV\ncrudos"), (0.75,.43,"tablas\nLaTeX"), (0.75,.16,"figuras\nPDF")]
    for x,y,t in right:
        arrow(ax, (.61,.50), (x-.01,y+.08), lw=1.15)
        box(ax, (x,y), (.18,.16), t, C["orange"], fontsize=10)
    ax.text(0.50,.08,"Trazabilidad exigida: texto → tabla/figura → CSV → script/configuración",
            ha="center", fontsize=9.7, color="#111111")
    save(fig, "ch4_traceability_pipeline.pdf")


# ---------------------------------------------------------------------------
# Chapter 5: experimental design.
# ---------------------------------------------------------------------------
def fig_experimental_design():
    fig = plt.figure(figsize=(7.4, 3.0))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.05, 1.0], wspace=0.36)
    ax = fig.add_subplot(gs[0,0])
    patterns = ["Aleatoria", "Agrupada", "Periférica", "Alta var."]
    severities = ["1 ch", "2 ch", "10%", "30%", "40%"]
    data = np.array([[.25,.30,.45,.65,.80],[.20,.34,.55,.82,.95],[.22,.33,.50,.72,.88],[.18,.29,.43,.60,.78]])
    im = ax.imshow(data, cmap="YlGnBu", vmin=0, vmax=1, aspect="auto")
    ax.set_title("(a) Estratos de pérdida", pad=5)
    ax.set_xticks(range(len(severities))); ax.set_xticklabels(severities)
    ax.set_yticks(range(len(patterns))); ax.set_yticklabels(patterns)
    ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
    cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.02)
    cb.set_label("severidad", fontsize=9)

    ax = fig.add_subplot(gs[0,1]); clean_ax(ax)
    ax.set_title("(b) Comparación pareada", pad=5)
    box(ax, (.08,.64), (.28,.18), "MNE", C["blue"], fontsize=11, weight="bold")
    box(ax, (.08,.24), (.28,.18), "TRSS", C["green"], fontsize=11, weight="bold")
    box(ax, (.55,.44), (.34,.20), "$d_i$ por caso", C["purple"], fontsize=10.5, weight="bold")
    arrow(ax, (.36,.73), (.55,.55)); arrow(ax, (.36,.33), (.55,.53))
    box(ax, (.55,.12), (.34,.18), "Wilcoxon\n+ bootstrap", C["orange"], fontsize=10)
    arrow(ax, (.72,.44), (.72,.30))
    save(fig, "ch5_experimental_design_matrix.pdf")


# ---------------------------------------------------------------------------
# Chapter 7: practical decision map.
# ---------------------------------------------------------------------------
def fig_decision_map():
    """Clean decision map with simplified axes and separated annotations."""
    fig, ax = plt.subplots(figsize=(7.1, 4.05))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
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

    ax.set_xticks([.08, .50, .92]); ax.set_xticklabels(["baja", "media", "alta"])
    ax.set_yticks([.08, .50, .92]); ax.set_yticklabels(["latencia", "balance", "precisión"])
    ax.grid(color="#FFFFFF", lw=1.0)
    for spine in ax.spines.values():
        spine.set_color("#555555")
    fig.subplots_adjust(left=0.16, right=0.98, bottom=0.18, top=0.94)
    save(fig, "ch7_decision_map.pdf")


if __name__ == "__main__":
    fig_gsp_concepts()
    fig_trss_operator()
    fig_methodology_flow()
    fig_traceability()
    fig_decision_map()
