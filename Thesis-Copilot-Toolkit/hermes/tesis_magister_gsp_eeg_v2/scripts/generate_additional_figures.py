#!/usr/bin/env python3
"""Generate additional conceptual and result figures for tesis_completa.tex.

The figures are intentionally explanatory, not decorative:
- Chapter 1: thesis roadmap and contribution logic.
- Chapter 2: clean GSP concepts figure replacing the crowded TikZ spectrum.
- Chapter 2: TRSS operator decomposition.
- Chapter 3: methodology flow.
- Chapter 4: reproducibility/traceability pipeline.
- Chapter 5: experimental design matrix.
- Chapter 6: full metric portfolio TRSS vs MNE.
- Chapter 7: practical decision map.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle, Circle, Polygon
from scipy.spatial.distance import cdist

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
TABLES = ROOT / "tables"
FIG.mkdir(exist_ok=True)

COLORS = {
    "blue": "#0B3D91",
    "light_blue": "#D9EAF7",
    "green": "#1B7F5C",
    "light_green": "#DFF3EA",
    "orange": "#E69F00",
    "light_orange": "#FDECC8",
    "red": "#D55E00",
    "light_red": "#F7D9CC",
    "purple": "#6A3D9A",
    "light_purple": "#E8DDF5",
    "gray": "#4D4D4D",
    "light_gray": "#F2F2F2",
}

plt.rcParams.update({
    "font.size": 9,
    "axes.titlesize": 11,
    "axes.labelsize": 9,
    "legend.fontsize": 8,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.04,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})


def save(fig: plt.Figure, name: str) -> None:
    path = FIG / name
    fig.savefig(path, format="pdf")
    preview = FIG / name.replace(".pdf", "_preview.png")
    fig.savefig(preview, format="png", dpi=160)
    plt.close(fig)
    print(f"saved {path.relative_to(ROOT)}")


def rounded_box(ax, xy, wh, text, fc, ec=None, fontsize=8, lw=1.2):
    x, y = xy
    w, h = wh
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.04",
        facecolor=fc,
        edgecolor=ec or COLORS["gray"],
        linewidth=lw,
    )
    ax.add_patch(patch)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fontsize, color="#222222")
    return patch


def arrow(ax, start, end, color=None, lw=1.5, style="->"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=12,
                                 linewidth=lw, color=color or COLORS["gray"],
                                 shrinkA=4, shrinkB=4))


def figure_ch1_roadmap():
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(0.02, 0.96, "Mapa lógico de la tesis", fontsize=12, fontweight="bold", color=COLORS["blue"])
    ax.text(0.02, 0.89, "De la falla de canales EEG a una frontera práctica de uso entre MNE y TRSS", fontsize=9)

    xs = [0.05, 0.29, 0.53, 0.77]
    labels = [
        "Problema\ncanales EEG\nfaltantes",
        "Métodos\nespaciales, GSP\ny TRSS",
        "Evaluación\npareada, multi-métrica\ny reproducible",
        "Decisión\ncuándo usar\nMNE o TRSS",
    ]
    colors = [COLORS["light_red"], COLORS["light_blue"], COLORS["light_green"], COLORS["light_orange"]]
    for i, (x, label, fc) in enumerate(zip(xs, labels, colors)):
        rounded_box(ax, (x, 0.55), (0.18, 0.20), label, fc, fontsize=8.5)
        if i < len(xs)-1:
            arrow(ax, (x+0.18, 0.65), (xs[i+1], 0.65), COLORS["blue"])

    lower = [
        (0.05, "Ruido, desconexión,\ncanales descartados"),
        (0.29, "Suavidad espacial\n+ continuidad temporal"),
        (0.53, "MAE, NRMSE, DTW,\nLSD, coherencia, tiempo"),
        (0.77, "Precisión vs costo\nsegún régimen de pérdida"),
    ]
    for x, txt in lower:
        rounded_box(ax, (x, 0.18), (0.18, 0.20), txt, COLORS["light_gray"], fontsize=7.8, lw=0.9)
        arrow(ax, (x+0.09, 0.55), (x+0.09, 0.38), COLORS["gray"], lw=1.1)

    ax.text(0.50, 0.05,
            "Criterio de lectura: la tesis no busca reemplazar MNE de forma universal; delimita el régimen donde TRSS aporta valor adicional.",
            ha="center", fontsize=8.2, color=COLORS["gray"])
    save(fig, "ch1_thesis_roadmap.pdf")


def electrode_positions(n=16):
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    base = np.array([0.20, 0.34, 0.45, 0.36, 0.48, 0.52, 0.42, 0.55,
                     0.20, 0.34, 0.45, 0.36, 0.48, 0.52, 0.42, 0.55])
    r = np.resize(base, n)
    return 0.5 + r*np.cos(theta), 0.5 + r*np.sin(theta)


def figure_ch2_gsp_concepts():
    fig, axes = plt.subplots(1, 3, figsize=(7.4, 2.75))
    x, y = electrode_positions(15)
    coords = np.c_[x, y]
    dist = cdist(coords, coords)

    ax = axes[0]
    ax.set_title("(a) Electrodos como grafo", loc="left", fontweight="bold")
    for i in range(len(x)):
        for j in np.argsort(dist[i])[1:4]:
            if i < j:
                w = np.exp(-dist[i, j]**2 / 0.04)
                ax.plot([x[i], x[j]], [y[i], y[j]], color="#9AA7B2", lw=0.5 + 2*w, alpha=0.8)
    ax.scatter(x, y, s=70, color=COLORS["blue"], edgecolor="white", linewidth=0.8, zorder=3)
    for i, name in enumerate(["Fz","FC1","C3","CP1","Pz","P4","C4","FC2","Cz","O1","O2","T7","T8","P3","F4"]):
        ax.text(x[i], y[i]+0.055, name, ha="center", va="center", fontsize=5.8)
    ax.add_patch(Circle((0.5, 0.5), 0.58, fill=False, color=COLORS["gray"], lw=1))
    ax.set_aspect("equal"); ax.set_xlim(-0.12, 1.12); ax.set_ylim(-0.12, 1.12); ax.axis("off")

    ax = axes[1]
    ax.set_title("(b) Espectro del Laplaciano", loc="left", fontweight="bold")
    eig = np.array([0.0, 0.18, 0.42, 0.75, 1.12, 1.55, 2.05, 2.70])
    amp = np.exp(-0.9*eig) + np.array([0, .08, -.02, .04, -.03, .02, -.015, .0])
    ax.vlines(eig, 0, amp, color=COLORS["blue"], lw=1.8)
    ax.scatter(eig, amp, color=COLORS["blue"], s=24, zorder=3)
    ax.axvspan(-0.05, 0.9, color=COLORS["light_green"], alpha=0.7, label="modos suaves")
    ax.axvspan(1.75, 2.85, color=COLORS["light_red"], alpha=0.6, label="modos rápidos")
    for xx, lab, yy in [(0, r"$\lambda_1=0$", 1.08), (0.42, r"$\lambda_3$", .82), (1.12, r"$\lambda_5$", .56), (2.70, r"$\lambda_N$", .28)]:
        ax.text(xx, yy, lab, fontsize=7, ha="center", va="bottom")
    ax.set_xlabel(r"autovalor $\lambda_k$")
    ax.set_ylabel(r"magnitud $|\hat{x}_k|$")
    ax.set_xlim(-0.08, 2.9); ax.set_ylim(0, 1.25)
    ax.spines[["top", "right"]].set_visible(False)

    ax = axes[2]
    ax.set_title("(c) Reconstrucción por suavidad", loc="left", fontweight="bold")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    rounded_box(ax, (0.05, 0.58), (0.25, 0.20), "Canales\nobservados", COLORS["light_blue"], fontsize=8)
    rounded_box(ax, (0.38, 0.58), (0.25, 0.20), "Grafo +\nregularización", COLORS["light_green"], fontsize=8)
    rounded_box(ax, (0.71, 0.58), (0.25, 0.20), "Canales\nreconstruidos", COLORS["light_orange"], fontsize=8)
    arrow(ax, (0.30, 0.68), (0.38, 0.68), COLORS["blue"])
    arrow(ax, (0.63, 0.68), (0.71, 0.68), COLORS["blue"])
    ax.text(0.50, 0.34,
            r"$\min_{\mathbf{x}} \|\mathbf{M}(\mathbf{x}-\mathbf{y})\|_2^2 + \alpha\,\mathbf{x}^\top\mathbf{L}\mathbf{x}$",
            ha="center", va="center", fontsize=8.5,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor=COLORS["gray"], alpha=.95))
    ax.text(0.50, 0.14, "La reconstrucción favorece señales suaves sobre el grafo,\npero respeta los canales observados.",
            ha="center", fontsize=7.8, color=COLORS["gray"])
    fig.tight_layout(w_pad=2.0)
    save(fig, "ch2_gsp_concepts_clean.pdf")


def figure_ch2_trss_operator():
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.02, 0.95, "Descomposición del operador TRSS", fontsize=12, fontweight="bold", color=COLORS["blue"])

    # Matrix X with missing rows
    rng = np.random.default_rng(1)
    mat = np.sin(np.linspace(0, 3*np.pi, 80))[None, :] + 0.25*rng.normal(size=(8, 80))
    mat += np.linspace(-0.8, 0.8, 8)[:, None]
    ax_in = fig.add_axes([0.08, 0.38, 0.18, 0.34])
    ax_in.imshow(mat, aspect="auto", cmap="RdBu_r", vmin=-2, vmax=2)
    ax_in.axhspan(2.5, 4.5, color="black", alpha=.18)
    ax_in.text(40, 3.55, "canales\nocultos", ha="center", va="center", fontsize=7, color="white",
               bbox=dict(facecolor="black", alpha=.45, edgecolor="none"))
    ax_in.set_xticks([]); ax_in.set_yticks([]); ax_in.set_title(r"datos $\mathbf{Y}$", fontsize=9)

    rounded_box(ax, (0.36, 0.66), (0.22, 0.16), r"Fidelidad\na canales observados\n$\|\mathbf{M}\odot(\mathbf{X}-\mathbf{Y})\|_F^2$", COLORS["light_blue"], fontsize=7.4)
    rounded_box(ax, (0.36, 0.43), (0.22, 0.16), r"Suavidad espacial\n$\alpha\,\mathrm{tr}(\mathbf{X}^\top\mathbf{L}\mathbf{X})$", COLORS["light_green"], fontsize=7.4)
    rounded_box(ax, (0.36, 0.20), (0.22, 0.16), r"Suavidad temporal\n$\beta\,\|\mathbf{X}\mathbf{D}_t\|_F^2$", COLORS["light_orange"], fontsize=7.4)
    for y0 in [0.74, 0.51, 0.28]:
        arrow(ax, (0.27, 0.55), (0.36, y0), COLORS["blue"], lw=1.2)

    ax.text(0.66, 0.52, r"$\hat{\mathbf{X}} = \arg\min_{\mathbf{X}}$", fontsize=13, ha="center", color=COLORS["blue"])
    arrow(ax, (0.58, 0.52), (0.72, 0.52), COLORS["blue"], lw=1.8)
    rounded_box(ax, (0.73, 0.43), (0.20, 0.18), r"señal completa\nreconstruida\n$\hat{\mathbf{X}}$", COLORS["light_purple"], fontsize=8.2)
    ax.text(0.50, 0.06,
            "TRSS no agrega información nueva: restringe el espacio de soluciones para que sean compatibles con la geometría de electrodos y con trayectorias temporales suaves.",
            ha="center", fontsize=8, color=COLORS["gray"])
    save(fig, "ch2_trss_operator.pdf")


def figure_ch3_methodology_flow():
    fig, ax = plt.subplots(figsize=(7.4, 3.2))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.02, 0.94, "Flujo metodológico de evaluación", fontsize=12, fontweight="bold", color=COLORS["blue"])
    nodes = [
        ("Conjuntos\nde datos", "PhysioNet\nBCI IV 2a\nMNE Sample", COLORS["light_blue"]),
        ("Máscaras\nde pérdida", "aleatoria\ncontigua\n10--40%", COLORS["light_orange"]),
        ("Métodos", "geométricos\nestadísticos\nGSP/TRSS", COLORS["light_green"]),
        ("Métricas", "amplitud\ntemporal\nespectral\ntiempo", COLORS["light_purple"]),
        ("Inferencia", "Wilcoxon\nbootstrap\nBH", COLORS["light_red"]),
    ]
    xs = np.linspace(0.05, 0.78, len(nodes))
    for i, (title, body, fc) in enumerate(nodes):
        x = xs[i]
        rounded_box(ax, (x, 0.50), (0.16, 0.25), f"{title}\n\n{body}", fc, fontsize=7.8)
        if i < len(nodes)-1:
            arrow(ax, (x+0.16, 0.625), (xs[i+1], 0.625), COLORS["blue"], lw=1.4)
    rounded_box(ax, (0.24, 0.18), (0.52, 0.16), "Comparación justa: misma señal, misma máscara y misma semilla para cada método", COLORS["light_gray"], fontsize=8.5)
    arrow(ax, (0.86, 0.50), (0.72, 0.34), COLORS["gray"], lw=1.2)
    save(fig, "ch3_methodology_flow.pdf")


def figure_ch4_traceability_pipeline():
    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.02, 0.94, "Trazabilidad de artefactos experimentales", fontsize=12, fontweight="bold", color=COLORS["blue"])
    left = [(0.06, 0.68, "Código\nalgoritmos"), (0.06, 0.45, "Configuración\nYAML/CSV"), (0.06, 0.22, "Semillas y\nmáscaras")]
    for x, y, txt in left:
        rounded_box(ax, (x, y), (0.18, 0.14), txt, COLORS["light_blue"], fontsize=8)
        arrow(ax, (0.24, y+0.07), (0.38, 0.52), COLORS["blue"], lw=1.2)
    rounded_box(ax, (0.38, 0.43), (0.22, 0.18), "Motor de\nejecución\nreproducible", COLORS["light_green"], fontsize=8.5)
    right = [(0.72, 0.68, "CSV\ncrudos"), (0.72, 0.45, "Tablas\nLaTeX"), (0.72, 0.22, "Figuras\nPDF")]
    for x, y, txt in right:
        arrow(ax, (0.60, 0.52), (x, y+0.07), COLORS["blue"], lw=1.2)
        rounded_box(ax, (x, y), (0.18, 0.14), txt, COLORS["light_orange"], fontsize=8)
    ax.text(0.50, 0.08, "Cada afirmación cuantitativa debe trazarse: texto → tabla/figura → CSV → script/configuración.",
            ha="center", fontsize=8.4, color=COLORS["gray"])
    save(fig, "ch4_traceability_pipeline.pdf")


def figure_ch5_design_matrix():
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.1), gridspec_kw={"width_ratios": [1.2, 1]})
    ax = axes[0]
    patterns = ["Aleatoria", "Cercana", "Periférica", "Alta var."]
    severities = ["1 ch", "2 ch", "10%", "30%", "40%"]
    mat = np.array([[1,1,1,1,1], [1,1,0.8,1,1], [0.7,0.8,1,1,1], [0.6,0.7,0.9,1,1]])
    im = ax.imshow(mat, cmap="YlGnBu", vmin=0.5, vmax=1.0, aspect="auto")
    ax.set_xticks(range(len(severities)), severities, rotation=35, ha="right")
    ax.set_yticks(range(len(patterns)), patterns)
    ax.set_title("(a) Estratificación de pérdida", loc="left", fontweight="bold")
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            ax.text(j, i, "✓", ha="center", va="center", fontsize=11, color="#1B3A57")
    ax.set_xlabel("severidad")
    ax.set_ylabel("patrón")
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
    cbar.set_label("cobertura relativa", fontsize=8)

    ax = axes[1]
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.set_title("(b) Inferencia pareada", loc="left", fontweight="bold")
    rounded_box(ax, (0.10, 0.68), (0.32, 0.17), "MNE\nmismo caso", COLORS["light_blue"], fontsize=8)
    rounded_box(ax, (0.58, 0.68), (0.32, 0.17), "TRSS\nmismo caso", COLORS["light_green"], fontsize=8)
    arrow(ax, (0.42, 0.765), (0.58, 0.765), COLORS["gray"], style="<->")
    rounded_box(ax, (0.27, 0.40), (0.46, 0.16), r"Diferencia pareada\n$d_i = m_{TRSS,i} - m_{MNE,i}$", COLORS["light_orange"], fontsize=8)
    arrow(ax, (0.50, 0.68), (0.50, 0.56), COLORS["blue"])
    rounded_box(ax, (0.20, 0.12), (0.60, 0.15), "Wilcoxon + bootstrap + BH\npara magnitud, incertidumbre y error múltiple", COLORS["light_red"], fontsize=8)
    arrow(ax, (0.50, 0.40), (0.50, 0.27), COLORS["blue"])
    fig.tight_layout(w_pad=2)
    save(fig, "ch5_experimental_design_matrix.pdf")


def figure_ch6_metric_portfolio():
    rows = []
    with (TABLES / "ch6_pairwise_comparisons_balanced.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["method_a"] == "trss_default" and r["method_b"] == "mne_interpolate_bads_spline":
                rows.append(r)
    order = ["mae", "rmse", "nrmse", "dtw", "snr", "lsd", "coherence_mean", "corr_mean", "r2", "runtime_s"]
    label = {"mae":"MAE", "rmse":"RMSE", "nrmse":"NRMSE", "dtw":"DTW", "snr":"SNR", "lsd":"LSD",
             "coherence_mean":"Coherencia", "corr_mean":"Correlación", "r2":"R²", "runtime_s":"Tiempo"}
    data = {r["metric"]: r for r in rows}
    metrics = [m for m in order if m in data]
    values = [100*float(data[m]["median_relative_improvement_of_a"]) for m in metrics]
    wins = [100*float(data[m]["a_win_rate"]) for m in metrics]
    fig, ax = plt.subplots(figsize=(7.4, 3.8))
    y = np.arange(len(metrics))
    colors = [COLORS["green"] if v >= 0 else COLORS["red"] for v in values]
    ax.barh(y, values, color=colors, alpha=0.85)
    ax.axvline(0, color="black", lw=0.8)
    for yi, v, w in zip(y, values, wins):
        ha = "left" if v >= 0 else "right"
        x = v + (1.0 if v >= 0 else -1.0)
        ax.text(x, yi, f"{v:+.1f}% | win {w:.0f}%", va="center", ha=ha, fontsize=7.5)
    ax.set_yticks(y, [label[m] for m in metrics])
    ax.invert_yaxis()
    ax.set_xlabel("Mejora mediana relativa de TRSS fijo vs MNE (%)")
    ax.set_title("Portafolio confirmatorio de métricas", loc="left", fontweight="bold")
    ax.text(0.99, 0.02, "Valores positivos favorecen TRSS; negativos favorecen MNE.",
            transform=ax.transAxes, ha="right", fontsize=8, color=COLORS["gray"])
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xlim(min(values)-10, max(values)+12)
    fig.tight_layout()
    save(fig, "ch6_metric_portfolio_improvement.pdf")


def figure_ch7_decision_map():
    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xlabel("Severidad / agrupamiento de la pérdida")
    ax.set_ylabel("Prioridad de precisión temporal-amplitud\nfrente a latencia y LSD")
    # Regions
    ax.add_patch(Rectangle((0, 0), 0.55, 0.55, facecolor=COLORS["light_blue"], alpha=0.8, edgecolor="none"))
    ax.add_patch(Rectangle((0.45, 0.45), 0.55, 0.55, facecolor=COLORS["light_green"], alpha=0.75, edgecolor="none"))
    ax.add_patch(Rectangle((0.55, 0), 0.45, 0.35, facecolor=COLORS["light_orange"], alpha=0.8, edgecolor="none"))
    ax.text(0.22, 0.30, "MNE\npor defecto", ha="center", va="center", fontsize=12, color=COLORS["blue"], fontweight="bold")
    ax.text(0.74, 0.72, "TRSS\njustificado", ha="center", va="center", fontsize=12, color=COLORS["green"], fontweight="bold")
    ax.text(0.78, 0.17, "Validar\ncaso a caso", ha="center", va="center", fontsize=11, color=COLORS["orange"], fontweight="bold")
    ax.plot([0.08, 0.92], [0.18, 0.86], "--", color=COLORS["gray"], lw=1.2)
    ax.text(0.52, 0.57, "frontera práctica\nno universal", rotation=37, fontsize=8, color=COLORS["gray"], ha="center")
    ax.set_xticks([0, .5, 1], ["baja", "media", "alta"])
    ax.set_yticks([0, .5, 1], ["latencia/LSD", "balance", "MAE/NRMSE/DTW"])
    ax.set_title("Mapa de decisión práctica MNE--TRSS", loc="left", fontweight="bold")
    ax.grid(color="white", lw=0.8)
    fig.tight_layout()
    save(fig, "ch7_decision_map.pdf")


def main():
    figure_ch1_roadmap()
    figure_ch2_gsp_concepts()
    figure_ch2_trss_operator()
    figure_ch3_methodology_flow()
    figure_ch4_traceability_pipeline()
    figure_ch5_design_matrix()
    figure_ch6_metric_portfolio()
    figure_ch7_decision_map()


if __name__ == "__main__":
    main()
