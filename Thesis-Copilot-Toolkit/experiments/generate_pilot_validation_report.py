"""Generate a concise pilot validation report from results artifacts.

Writes a markdown report to `results/pilot_validation_report_it01-it50.md`.
Designed to be idempotent and robust to NaN tokens in JSON files.
"""
from pathlib import Path
import json
import re
from datetime import datetime


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
SCHEDULE = ROOT / "experiments" / "schedules" / "it01-it50_schedule.json"
SKIPPED = RESULTS / "pilot_skipped_iterations.json"


def load_json_allow_nan(p: Path):
    txt = p.read_text(encoding="utf8")
    # Replace bare NaN tokens with null to make valid JSON
    sanitized = re.sub(r"\bNaN\b", "null", txt)
    return json.loads(sanitized)


def main():
    if not SCHEDULE.exists():
        print("Schedule file not found:", SCHEDULE)
        return 2

    schedule = json.loads(SCHEDULE.read_text(encoding="utf8"))
    iter_keys = [it.get("key") for it in schedule.get("iterations", [])]

    skipped_map = {}
    if SKIPPED.exists():
        try:
            skipped_entries = json.loads(SKIPPED.read_text(encoding="utf8"))
            for e in skipped_entries:
                skipped_map[e.get("iteration")] = e.get("error")
        except Exception:
            skipped_map = {}

    successes = []
    missing = []
    for k in iter_keys:
        meta_path = RESULTS / f"{k}_run_metadata.json"
        if meta_path.exists():
            try:
                meta = load_json_allow_nan(meta_path)
            except Exception as exc:
                missing.append((k, f"invalid metadata: {exc}"))
                continue

            info = {
                "iteration": k,
                "datasets": meta.get("datasets") or meta.get("requested_datasets"),
                "n_rows": meta.get("n_rows"),
                "n_methods": meta.get("n_methods"),
                "qa": (meta.get("qa") or {}).get("status"),
                "best_method": meta.get("best_method"),
                "best_mae": meta.get("best_mae"),
            }
            successes.append(info)
        else:
            # Not present in results
            if k in skipped_map:
                # will report under skipped section
                continue
            missing.append((k, "no metadata file"))

    # Build markdown
    ts = datetime.utcnow().isoformat() + "Z"
    md_lines = []
    md_lines.append(f"# Pilot Validation Report (it01-it50)\n")
    md_lines.append(f"Generated: {ts}\n")
    md_lines.append("## Summary\n")
    md_lines.append(f"- Scheduled iterations: {len(iter_keys)}")
    md_lines.append(f"- Executed (with metadata): {len(successes)}")
    md_lines.append(f"- Skipped (reported): {len(skipped_map)}")
    md_lines.append(f"- Missing metadata files: {len(missing)}\n")

    md_lines.append("## Executed Iterations\n")
    md_lines.append("|Iteration|Datasets|Rows|Methods|QA|Best method|Best MAE|")
    md_lines.append("|---|---|---:|---:|---|---|---:|")
    for s in successes:
        ds = ",".join(s["datasets"]) if s.get("datasets") else "-"
        rows = str(s.get("n_rows") or "-")
        nmethods = str(s.get("n_methods") or "-")
        qa = str(s.get("qa") or "-")
        bm = str(s.get("best_method") or "-")
        bmae = ("{:.3e}".format(s.get("best_mae")) if isinstance(s.get("best_mae"), (int, float)) else str(s.get("best_mae") or "-"))
        md_lines.append(f"|{s['iteration']}|{ds}|{rows}|{nmethods}|{qa}|{bm}|{bmae}|")

    md_lines.append("\n## Skipped Iterations\n")
    if skipped_map:
        for k, err in skipped_map.items():
            md_lines.append(f"- **{k}**: {err}")
    else:
        md_lines.append("- (none)\n")

    md_lines.append("\n## Missing Metadata Files\n")
    if missing:
        for k, reason in missing:
            md_lines.append(f"- **{k}**: {reason}")
    else:
        md_lines.append("- (none)\n")

    out_path = RESULTS / "pilot_validation_report_it01-it50.md"
    out_path.write_text("\n".join(md_lines), encoding="utf8")
    print("Wrote report:", out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
