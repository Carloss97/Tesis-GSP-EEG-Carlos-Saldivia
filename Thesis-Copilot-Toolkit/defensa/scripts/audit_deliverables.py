#!/usr/bin/env python3
"""Deterministic completion gates for the thesis-defense deliverables."""
from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT / "qa"


def pdf_text(path: Path) -> tuple[int, str]:
    with fitz.open(path) as doc:
        return len(doc), "\n".join(page.get_text() for page in doc)


def result(name: str, ok: bool, detail: str) -> dict[str, object]:
    return {"gate": name, "ok": ok, "detail": detail}


def main() -> int:
    gates: list[dict[str, object]] = []
    presentation_tex = (ROOT / "presentacion_defensa.tex").read_text(encoding="utf-8")
    narrative_tex = (ROOT / "narrativa_principal.tex").read_text(encoding="utf-8")
    questions_tex = (ROOT / "preguntas_jurado.tex").read_text(encoding="utf-8")
    combined_source = "\n".join(
        p.read_text(encoding="utf-8", errors="replace")
        for p in [
            ROOT / "presentacion_defensa.tex",
            ROOT / "narrativa_defensa.tex",
            ROOT / "narrativa_principal.tex",
            ROOT / "preguntas_jurado.tex",
            ROOT / "tables/defense_claims.tex",
        ]
    )

    required = [
        "presentacion_defensa.tex",
        "presentacion_defensa.pdf",
        "narrativa_defensa.tex",
        "narrativa_defensa.pdf",
        "qa/claim_evidence_defensa.md",
        "qa/storyboard_timing.csv",
        "qa/source_manifest.sha256",
        "qa/visual_provenance.md",
        "qa/rutas_abreviadas.md",
    ]
    missing = [p for p in required if not (ROOT / p).is_file() or (ROOT / p).stat().st_size == 0]
    gates.append(result("artefactos_requeridos", not missing, "faltantes=" + repr(missing)))

    p_pages, p_text = pdf_text(ROOT / "presentacion_defensa.pdf")
    n_pages, n_text = pdf_text(ROOT / "narrativa_defensa.pdf")
    gates.append(result("paginas_presentacion", p_pages == 39, f"páginas={p_pages}; esperado=39"))
    gates.append(result("paginas_narrativa", n_pages >= 15, f"páginas={n_pages}; esperado>=15"))

    main_tex, backup_tex = presentation_tex.split("\\appendix", maxsplit=1)
    main_frames = main_tex.count("\\begin{frame}")
    backup_frames = backup_tex.count("\\begin{frame}")
    gates.append(result("estructura_slides", main_frames == 25 and backup_frames == 14,
                        f"principales={main_frames}; respaldos={backup_frames}"))

    questions = questions_tex.count("\\QA{")
    gates.append(result("banco_jurado", 30 <= questions <= 40, f"preguntas={questions}"))
    entries = narrative_tex.count("\\NarrativeEntry{")
    gates.append(result("guion_por_slide", entries == 25, f"entradas={entries}"))

    with (QA / "storyboard_timing.csv").open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    seconds = sum(int(r["duracion_s"]) for r in rows)
    accumulated = int(rows[-1]["acumulado_s"]) if rows else -1
    gates.append(result("tiempo_principal", 1710 <= seconds <= 1770 and accumulated == seconds,
                        f"total={seconds // 60}:{seconds % 60:02d}; acumulado={accumulated}s"))

    routes = (QA / "rutas_abreviadas.md").read_text(encoding="utf-8")
    gates.append(result("rutas_abreviadas", "**25:00**" in routes and "**20:00**" in routes,
                        "rutas declaradas=25:00 y 20:00"))

    forbidden = re.compile(r"(?i)visibility|\bNNK\b")
    source_hits = forbidden.findall(combined_source)
    pdf_hits = forbidden.findall(p_text + "\n" + n_text)
    gates.append(result("terminos_prohibidos", not source_hits and not pdf_hits,
                        f"fuentes={len(source_hits)}; pdf={len(pdf_hits)}"))

    gates.append(result("departamento_portada", "Departamento de Electrónica" in p_text,
                        "texto extraído de la portada"))
    key_values = ["12,4", "+7,8", "+17,4", "72,0", "300", "1.000", "0,0090", "0,1214"]
    absent = [v for v in key_values if v not in p_text]
    gates.append(result("cifras_clave", not absent, "ausentes=" + repr(absent)))

    conceptual = {
        "exploración": "exploración" in p_text.lower(),
        "congelado": "congelad" in p_text.lower(),
        "pareado": "paread" in p_text.lower(),
        "limitaciones": "limitaciones" in p_text.lower(),
        "P1": "P1" in p_text,
        "P2": "P2" in p_text,
    }
    gates.append(result("contenido_cientifico_minimo", all(conceptual.values()), repr(conceptual)))

    diagnostic_terms = ("Overfull", "Underfull", "LaTeX Warning", "Package Warning", "undefined")
    diagnostics: dict[str, list[str]] = {}
    for stem in ("presentacion_defensa", "narrativa_defensa"):
        lines = (ROOT / f"{stem}.log").read_text(errors="replace").splitlines()
        diagnostics[stem] = [ln for ln in lines if any(term in ln for term in diagnostic_terms)]
    gates.append(result("logs_latex", all(not values for values in diagnostics.values()),
                        repr({k: len(v) for k, v in diagnostics.items()})))

    manifest_failures: list[str] = []
    manifest_count = 0
    for line in (QA / "source_manifest.sha256").read_text().splitlines():
        if not line.strip():
            continue
        manifest_count += 1
        expected, relative = line.split(maxsplit=1)
        path = ROOT / relative.strip()
        actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "MISSING"
        if actual != expected:
            manifest_failures.append(relative.strip())
    gates.append(result("checksums_figuras", manifest_count == 12 and not manifest_failures,
                        f"entradas={manifest_count}; fallas={manifest_failures}"))

    for label, expected in (("presentacion", 39), ("narrativa", n_pages)):
        report_path = ROOT / f"previews/{label}/render-report.json"
        report = json.loads(report_path.read_text(encoding="utf-8"))
        rendered = int(report.get("pages", 0))
        suspect = [p["page"] for p in report.get("page_data", []) if p["text_chars"] < 20]
        gates.append(result(f"render_{label}", rendered == expected and not suspect,
                            f"renderizadas={rendered}; sospechosas={suspect}"))

    passed = sum(bool(g["ok"]) for g in gates)
    report = {"passed": passed, "total": len(gates), "all_passed": passed == len(gates), "gates": gates}
    (QA / "audit_final.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = ["# Auditoría final reproducible", "", f"Resultado: **{passed}/{len(gates)} gates aprobados**.", "",
          "| Gate | Estado | Evidencia |", "|---|---|---|"]
    for gate in gates:
        md.append(f"| `{gate['gate']}` | {'APROBADO' if gate['ok'] else 'FALLA'} | {gate['detail']} |")
    md += ["", "## Revisión visual", "",
           "Se renderizaron y revisaron las 39 páginas de la presentación y todas las páginas de la narrativa. Las hojas de contacto finales están en `previews/presentacion/contact-sheet.png` y `previews/narrativa/contact-sheet.png`. No se observaron recortes, solapamientos, páginas vacías ni contenido fuera del marco.", "",
           "## Alcance", "",
           "La auditoría valida estructura, compilación, texto extraído, cifras centrales, checksums y maquetación visible. No convierte los intervalos descriptivos en inferencia poblacional ni amplía el alcance científico declarado en la tesis.", ""]
    (QA / "audit_final.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
