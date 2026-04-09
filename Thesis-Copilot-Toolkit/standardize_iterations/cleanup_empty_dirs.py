#!/usr/bin/env python3
"""
Detecta y elimina carpetas vacías bajo `standardized_results`.
Modo: --dry-run (simula), --apply (ejecuta).
Por seguridad, **no** elimina las carpetas `itNNN` que estén en la raíz de `standardized_results`, a menos que se pase `--remove-empty-it`.
Genera un JSON resumen en `--report`.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

IT_RE = re.compile(r"^it\d{3}$")


def is_it_dir(name: str) -> bool:
    return bool(IT_RE.match(name))


def main():
    p = argparse.ArgumentParser(description="Cleanup empty dirs under standardized_results")
    p.add_argument("--root", default="Thesis-Copilot-Toolkit/standardized_results")
    p.add_argument("--report", default="Thesis-Copilot-Toolkit/standardize_iterations/cleanup_empty_dirs_report.json")
    p.add_argument("--dry-run", action="store_true", help="Simular limpieza")
    p.add_argument("--apply", action="store_true", help="Eliminar realmente las carpetas vacías")
    p.add_argument("--remove-empty-it", action="store_true", help="Permitir eliminar itNNN vacíos en la raíz (por defecto se preservan)")
    args = p.parse_args()

    root = Path(args.root).resolve()
    report_path = Path(args.report)

    if not root.exists():
        print(json.dumps({"error": "root-not-found", "root": str(root)}))
        sys.exit(1)

    removed_sim = set()
    removed_actual = []
    errors = []
    scanned_dirs = 0

    # Recorrer bottom-up para que la simulación de borrado sea consistente
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        scanned_dirs += 1
        cur = Path(dirpath)

        # No intentar borrar la raíz
        if cur == root:
            continue

        # Si es un itNNN en la raíz, y no se pidió eliminar it vacíos, saltar
        try:
            rel = cur.relative_to(root)
        except Exception:
            rel = None

        if rel is not None and len(rel.parts) == 1 and is_it_dir(rel.parts[0]) and not args.remove_empty_it:
            continue

        try:
            entries = list(cur.iterdir())
        except Exception as e:
            errors.append({"path": str(cur), "error": str(e)})
            continue

        has_nonremovable = False
        for ent in entries:
            try:
                if ent.is_file():
                    has_nonremovable = True
                    break
                if ent.is_dir():
                    # Si el subdirectorio NO está programado para ser removido, entonces la carpeta no está vacía
                    if str(ent) not in removed_sim:
                        # aún no marcado para eliminación => considera que es no vacío
                        has_nonremovable = True
                        break
            except Exception as e:
                # problemas para comprobar; no borrar
                has_nonremovable = True
                break

        if not has_nonremovable:
            # esta carpeta sería eliminable
            removed_sim.add(str(cur))
            if args.apply:
                try:
                    cur.rmdir()
                    removed_actual.append(str(cur))
                except Exception as e:
                    errors.append({"path": str(cur), "error": str(e)})

    report = {
        "root": str(root),
        "scanned_dirs": scanned_dirs,
        "candidates_for_removal": len(removed_sim),
        "removed_count": len(removed_actual),
        "removed_sample": list(sorted(removed_actual))[:200],
        "dry_run": bool(args.dry_run and not args.apply),
        "apply": bool(args.apply),
        "errors": errors
    }

    try:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with report_path.open("w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(json.dumps({"error": "write-report-failed", "detail": str(e)}))
        sys.exit(1)

    # Mensaje corto para la automation
    out = {"status": "dry-run-complete" if args.dry_run and not args.apply else ("apply-complete" if args.apply else "completed"), "report": str(report_path.resolve())}
    print(json.dumps(out))


if __name__ == "__main__":
    main()
