"""Wait until all it131-it150 raw CSVs appear in results, then exit.

This script polls the results folder every 15 seconds. When it detects
that every tag `it131`..`it150` has at least one file matching
`itXXX*_raw.csv`, it prints `ALL_DONE` and writes a sentinel file.
"""
from __future__ import annotations

import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "results"
TAGS = [f"it{n}" for n in range(131, 151)]
SENTINEL = ROOT / "it131_it150_complete.txt"


def all_present() -> bool:
    for t in TAGS:
        matches = list(ROOT.glob(f"{t}*_raw.csv"))
        if not matches:
            return False
    return True


def main() -> None:
    # quick initial check
    if all_present():
        print("ALL_DONE")
        SENTINEL.write_text("done")
        return

    try:
        while True:
            if all_present():
                print("ALL_DONE")
                SENTINEL.write_text("done")
                return
            time.sleep(15)
    except KeyboardInterrupt:
        print("INTERRUPTED")


if __name__ == "__main__":
    main()
