#!/usr/bin/env python3
"""Generate Chapter 4 V3.1 experiment-stage tables.

This complements `generate_ch4_v3_artifacts.py` with evidence for the
preliminary/intermediate experimental phases: broad screening, candidate
reduction, runtime screening and transition to the final TRSS-vs-MNE benchmark.
It only reads existing CSV/MD artifacts and does not invent results.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

THIS = Path(__file__).resolve()
THESIS = THIS.parents[1]
TOOLKIT = THIS.parents[3]
TABLES = THESIS / "tables"
LOGS = THESIS / "build_logs"


def tex_escape(s: object) -> str:
    s = "" if s is None else str(s)
    repl = {
        "\\": r"\textbackslash{}",
        "_": r"\_",
        "%": r"\%",
        "&": r"\&",
        "#": r"\#",
        "$": r"\$",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(repl.get(ch, ch) for ch in s)


def fmt_float(x: object) -> str:
    try:
        v = float(str(x))
    except Exception:
        return tex_escape(x)
    if not math.isfinite(v):
        return "--"
    if abs(v) < 1e-3 and v != 0:
        return f"${v:.2e}$"
    return f"{v:.3f}"


def fmt_ms(x: object) -> str:
    try:
        v = float(str(x))
    except Exception:
        return tex_escape(x)
    if not math.isfinite(v):
        return "--"
    if v >= 1000:
        return f"{v/1000:.2f} s"
    return f"{v:.2f} ms"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def short_graph(name: str) -> str:
    return (name
            .replace("knn__k3", "knn k=3")
            .replace("knn__k5", "knn k=5")
            .replace("knng__k3", "knng k=3")
            .replace("gaussian__sigma1.0", "gauss sigma=1")
            .replace("gaussian__sigma1", "gauss sigma=1")
            .replace("aew__k4_sigma_corr0_5_sigma_dist1", "aew"))


def write(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(THESIS)}")


def phase_overview() -> None:
    write(TABLES / "ch4_experimental_phase_overview.tex", r"""
\begin{table}[H]
\centering
\footnotesize
\setlength{\tabcolsep}{3pt}
\caption{Fases experimentales que conectan la exploración inicial con la comparación final.}
\label{tab:ch4_experimental_phase_overview}
\begin{tabular}{@{}p{2.8cm}p{4.1cm}p{4.6cm}@{}}
\toprule
Fase & Propósito & Artefactos y decisión \\
\midrule
Exploración preliminar & Explorar combinaciones método--grafo sobre datos sintéticos y EEG proxy/real, sin usarlas como conclusión final. & Ranking exploratorio de combinaciones; identifica familias temporales y grafos candidatos. \\
Reducción de candidatos & Descartar métodos inestables, demasiado costosos o dependientes de información circular. & Microbenchmarks y bitácora de selección; mantener métodos trazables y comparables. \\
Optimización intermedia & Ajustar hiperparámetros y evaluar sensibilidad entre óptimos por escenario y configuraciones globales. & Resultados Optuna y evaluación global; congelar variantes TRSS para la comparación. \\
Comparación final & Comparar TRSS fijo/calibrado contra MNE sobre casos pareados independientes. & Resultados balanceados y resumen pareado; tablas y figuras V3 del capítulo. \\
Inspección cualitativa & Verificar que las métricas agregadas correspondan a señales y espectros interpretables. & Casos temporales y PSD original--MNE--TRSS seleccionados reproduciblemente. \\
\bottomrule
\end{tabular}
\end{table}
""")


def screening_top_candidates() -> None:
    path = TOOLKIT / "results" / "tablas_resumen" / "top5_combinaciones_recomendadas_gsp.csv"
    rows = read_csv(path)
    wanted = [
        "physionet_eegmmidb", "physionet_eegmmidb_real",
        "mne_sample_proxy",
        "bci_competition_iv_2a_proxy", "bci_iv2a_real_s1", "bci_iv2a_real_s2", "bci_iv2a_real_s3",
        "synthetic_16ch", "synthetic_32ch",
    ]
    labels = {
        "physionet_eegmmidb": "PhysioNet proxy",
        "physionet_eegmmidb_real": "PhysioNet real",
        "mne_sample_proxy": "MNE Sample proxy",
        "bci_competition_iv_2a_proxy": "BCI IV proxy",
        "bci_iv2a_real_s1": "BCI IV real S1",
        "bci_iv2a_real_s2": "BCI IV real S2",
        "bci_iv2a_real_s3": "BCI IV real S3",
        "synthetic_16ch": "Sintético 16 ch",
        "synthetic_32ch": "Sintético 32 ch",
    }
    selected = []
    for ds in wanted:
        candidates = [r for r in rows if r.get("Dataset") == ds and str(r.get("Rank")) == "1"]
        if candidates:
            selected.append(candidates[0])
    tex_rows = []
    for r in selected:
        ds = labels.get(r["Dataset"], r["Dataset"])
        tex_rows.append(
            f"{tex_escape(ds)} & {tex_escape(r['Familia'])} & {tex_escape(short_graph(r['Grafo']))} & "
            f"{tex_escape(r['Metodo'])} & {fmt_float(r['MAE'])} & {fmt_float(r['SNR'])} \\\\"
        )
    write(TABLES / "ch4_preliminary_screening_top_candidates.tex", r"""
\begin{table}[htbp]
\centering
\scriptsize
\setlength{\tabcolsep}{3pt}
\caption{Mejor combinación método--grafo por conjunto durante la selección exploratoria. El ranking corresponde al puntaje compuesto de los resultados preliminares; no constituye la comparación final contra MNE.}
\label{tab:ch4_preliminary_screening_top_candidates}
\begin{tabular}{@{}p{2.2cm}p{1.85cm}p{2.4cm}p{1.85cm}rr@{}}
\toprule
Conjunto & Familia & Grafo & Método & MAE & SNR \\
\midrule
""" + "\n".join(tex_rows) + r"""
\bottomrule
\end{tabular}
\end{table}
""")


def runtime_screening() -> None:
    path = TOOLKIT / "results" / "tablas_resumen" / "phase2_microbench_latency.csv"
    rows = read_csv(path)
    keep = ["mean", "linear", "rbfi_tps", "trss", "temporal_laplacian", "spherical_spline", "tv", "visibility_nnk"]
    by_method = {r["method"]: r for r in rows}
    names = {
        "mean": "Media",
        "linear": "Lineal",
        "rbfi_tps": "RBF TPS",
        "trss": "TRSS",
        "temporal_laplacian": "Laplaciano temporal",
        "spherical_spline": "Spline esférica propia",
        "tv": "TV temporal",
        "visibility_nnk": "Visibility NNK",
    }
    tex_rows = []
    for m in keep:
        if m in by_method:
            tex_rows.append(f"{tex_escape(names[m])} & {tex_escape(names[m])} & {fmt_ms(by_method[m]['median_ms'])} \\\\")
    write(TABLES / "ch4_runtime_screening_summary.tex", r"""
\begin{table}[htbp]
\centering
\small
\caption{Microbenchmark de latencia usado como criterio de reducción de candidatos.}
\label{tab:ch4_runtime_screening_summary}
\begin{tabular}{@{}p{4.0cm}p{3.3cm}r@{}}
\toprule
Método & Identificador & Mediana \\
\midrule
""" + "\n".join(tex_rows) + r"""
\bottomrule
\end{tabular}
\end{table}
""")


def reduction_decisions() -> None:
    write(TABLES / "ch4_candidate_reduction_decisions.tex", r"""
\begin{table}[H]
\centering
\scriptsize
\setlength{\tabcolsep}{3pt}
\caption{Reducción de candidatos antes de la comparación final.}
\label{tab:ch4_candidate_reduction_decisions}
\begin{tabular}{@{}p{2.9cm}p{4.1cm}p{4.0cm}@{}}
\toprule
Grupo & Evidencia experimental & Decisión para la fase final \\
\midrule
Geométricos propios & Rápidos y útiles como contexto, pero menos robustos que MNE-Python. & Mantener como antecedentes; usar MNE como referencia principal. \\
Grafos de correlación & Informativos, pero dependen de la misma señal evaluada. & Excluir de conclusiones finales por circularidad potencial. \\
Grafos data-driven & Competitivos en algunos conjuntos, con mayor costo y menor determinismo. & Reservar para trabajo futuro. \\
Temporales no TRSS & Competitivos en la selección preliminar, pero con costo o interpretación menos favorable. & Mantener como evidencia intermedia. \\
TRSS y MNE & TRSS resume la regularización espacio--temporal; MNE es referencia madura y rápida. & Comparación final pareada. \\
\bottomrule
\end{tabular}
\end{table}
""")


def main() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    phase_overview()
    screening_top_candidates()
    runtime_screening()
    reduction_decisions()
    manifest = "\n".join([
        "ch4_experimental_phase_overview.tex",
        "ch4_preliminary_screening_top_candidates.tex",
        "ch4_runtime_screening_summary.tex",
        "ch4_candidate_reduction_decisions.tex",
    ])
    write(LOGS / "cap4_v31_experiment_artifacts_manifest.txt", manifest)


if __name__ == "__main__":
    main()
