#!/usr/bin/env python3
"""Trim unused bibliography entries from paper/thesis .bib files."""

from __future__ import annotations

import re
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "paper": {
        "tex_root": ROOT / "paper" / "ieee",
        "bib": ROOT / "paper" / "ieee" / "bibliography" / "references.bib",
    },
    "thesis": {
        "tex_root": ROOT / "thesis" / "usm",
        "bib": ROOT / "thesis" / "usm" / "bibliography" / "references.bib",
    },
}

CITE_RE = re.compile(r"\\cite[a-zA-Z*]*\{([^}]*)\}")
ENTRY_START_RE = re.compile(r"^@\w+\{([^,]+),", re.MULTILINE)


def collect_cited_keys(tex_root: Path) -> set[str]:
    cited: set[str] = set()
    for tex_file in sorted(tex_root.rglob("*.tex")):
        text = tex_file.read_text(encoding="utf-8", errors="ignore")
        for match in CITE_RE.findall(text):
            for key in [part.strip() for part in match.split(",") if part.strip()]:
                cited.add(key)
    return cited


def split_entries(bib_text: str) -> list[tuple[str, str]]:
    matches = list(ENTRY_START_RE.finditer(bib_text))
    entries: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        key = match.group(1).strip()
        entry_start = match.start()
        entry_end = matches[index + 1].start() if index + 1 < len(matches) else len(bib_text)
        entries.append((key, bib_text[entry_start:entry_end].strip()))
    return entries


def trim_target(name: str) -> None:
    tex_root = TARGETS[name]["tex_root"]
    bib_path = TARGETS[name]["bib"]
    cited = collect_cited_keys(tex_root)
    bib_text = bib_path.read_text(encoding="utf-8", errors="ignore")
    entries = split_entries(bib_text)
    kept = [(key, entry) for key, entry in entries if key in cited]
    removed = [(key, entry) for key, entry in entries if key not in cited]
    bib_path.write_text("\n\n".join(entry for _, entry in kept).rstrip() + "\n", encoding="utf-8")
    print(f"[{name.upper()}] kept {len(kept)} entries, removed {len(removed)} unused entries")
    if removed:
        print("  removed:")
        for key, _ in removed:
            print(f"    - {key}")
    print()


def main() -> None:
    for name in TARGETS:
        trim_target(name)


if __name__ == "__main__":
    main()
