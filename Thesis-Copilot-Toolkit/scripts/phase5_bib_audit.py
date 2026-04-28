#!/usr/bin/env python3
"""Audit citation coverage and bibliography entry completeness for Phase 5."""

from __future__ import annotations

import re
from pathlib import Path
from collections import Counter

ROOT = Path(r"C:\Users\sarlo\OneDrive\Escritorio\Proyectos\Tesis-GSP-EEG-Carlos-Saldivia\Thesis-Copilot-Toolkit")
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
ENTRY_RE = re.compile(r"^@\w+\{([^,]+),", re.MULTILINE)
FIELD_RE = re.compile(r"^\s*([A-Za-z][A-Za-z0-9_-]*)\s*=\s*\{", re.MULTILINE)

REQUIRED_FIELDS = {
    "article": {"author", "title", "journal", "year"},
    "inproceedings": {"author", "title", "booktitle", "year"},
    "proceedings": {"title", "year"},
    "book": {"author", "title", "publisher", "year"},
    "phdthesis": {"author", "title", "school", "year"},
    "mastersthesis": {"author", "title", "school", "year"},
    "misc": {"author", "title", "year"},
}


def collect_tex_files(root: Path) -> list[Path]:
    return sorted(root.rglob("*.tex"))


def extract_citations(tex_root: Path) -> Counter:
    keys = Counter()
    for tex_file in collect_tex_files(tex_root):
        text = tex_file.read_text(encoding="utf-8", errors="ignore")
        for match in CITE_RE.findall(text):
            for key in [part.strip() for part in match.split(",") if part.strip()]:
                keys[key] += 1
    return keys


def extract_bib_entries(bib_path: Path) -> dict[str, dict[str, object]]:
    text = bib_path.read_text(encoding="utf-8", errors="ignore")
    entries: dict[str, dict[str, object]] = {}
    matches = list(ENTRY_RE.finditer(text))
    for idx, match in enumerate(matches):
        entry_key = match.group(1).strip()
        entry_type = text[match.start():].split("{", 1)[0].strip()[1:].lower()
        entry_start = match.end()
        entry_end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        entry_text = text[entry_start:entry_end]
        fields = {field.lower() for field in FIELD_RE.findall(entry_text)}
        entries[entry_key] = {"type": entry_type, "fields": fields, "text": entry_text}
    return entries


def audit_target(name: str) -> None:
    tex_root = TARGETS[name]["tex_root"]
    bib_path = TARGETS[name]["bib"]
    citations = extract_citations(tex_root)
    entries = extract_bib_entries(bib_path)
    cited_keys = set(citations)
    bib_keys = set(entries)
    missing = sorted(cited_keys - bib_keys)
    unused = sorted(bib_keys - cited_keys)

    print(f"[{name.upper()}]")
    print(f"tex files: {len(collect_tex_files(tex_root))}")
    print(f"cited keys: {len(cited_keys)}")
    print(f"bib entries: {len(bib_keys)}")
    print(f"missing citations: {len(missing)}")
    if missing:
        print("  MISSING:")
        for key in missing:
            print(f"    - {key}")
    print(f"unused entries: {len(unused)}")
    if unused:
        print("  UNUSED:")
        for key in unused:
            print(f"    - {key}")

    incomplete = []
    for key, meta in entries.items():
        entry_type = str(meta["type"]).lower()
        fields = set(meta["fields"])
        required = REQUIRED_FIELDS.get(entry_type, {"author", "title", "year"})
        missing_fields = sorted(required - fields)
        if missing_fields:
            incomplete.append((key, entry_type, missing_fields))

    print(f"incomplete entries (required field gaps): {len(incomplete)}")
    for key, entry_type, missing_fields in incomplete[:20]:
        print(f"  - {key} [{entry_type}]: missing {', '.join(missing_fields)}")
    if len(incomplete) > 20:
        print(f"  ... {len(incomplete) - 20} more")
    print()


def main() -> None:
    for name in TARGETS:
        audit_target(name)


if __name__ == "__main__":
    main()
