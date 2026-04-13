"""Notificador simple: avisa cuando cada iteración it131-it150 complete.

Solo imprime una línea por iteración cuando aparece el archivo
`{it_tag}_raw.csv` dentro de la carpeta de resultados. Diseñado para
ejecución en paralelo al runner principal.
"""
from __future__ import annotations

import time
from pathlib import Path
from typing import List, Set


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def main():
    tags: List[str] = [f"it{n}" for n in range(131, 151)]
    seen: Set[str] = set()

    # Polling loop: comprobar existencia de {tag}_raw.csv
    try:
        while len(seen) < len(tags):
            for t in tags:
                if t in seen:
                    continue
                p = RESULTS / f"{t}_raw.csv"
                if p.exists():
                    print(f"ITERACION_COMPLETA: {t}")
                    seen.add(t)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitor interrumpido por usuario.")

    print("MONITOR_FINALIZADO: todas las iteraciones detectadas.")


if __name__ == "__main__":
    main()
