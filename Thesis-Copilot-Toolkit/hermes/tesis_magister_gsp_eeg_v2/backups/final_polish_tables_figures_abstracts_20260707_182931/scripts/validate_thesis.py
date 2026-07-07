from pathlib import Path
import re, sys, json
from collections import Counter

root = Path(__file__).resolve().parents[1]

INPUT_RE = re.compile(r'(?<!%)\\(?:input|include)\{([^}]+)\}')
GRAPHICSPATH_RE = re.compile(r'\\graphicspath\{((?:\{[^}]+\})+)\}')

for main_name in ['tesis_completa.tex', 'tesis_caps_1_5.tex']:
    main = root / main_name
    if not main.exists():
        print(f"SKIP {main_name}: not found")
        continue

    visited = []
    missing_inputs = []
    graphics_paths = [root, root / 'figures']

    def resolve_tex(name: str, including_file: Path) -> Path | None:
        p = Path(name)
        if p.suffix == '':
            p = p.with_suffix('.tex')
        candidates = [root / p, including_file.parent / p]
        for cand in candidates:
            if cand.exists():
                return cand
        return candidates[0]

    def load(path: Path) -> str:
        path = path.resolve()
        if path in visited:
            return ''
        visited.append(path)
        try:
            txt = path.read_text(encoding='utf-8', errors='replace')
        except FileNotFoundError:
            missing_inputs.append(str(path))
            return ''

        for gp_match in GRAPHICSPATH_RE.findall(txt):
            for gp in re.findall(r'\{([^}]+)\}', gp_match):
                cand = (root / gp).resolve()
                if cand.exists() and cand.is_dir() and cand not in graphics_paths:
                    graphics_paths.append(cand)

        acc = [txt]
        for m in INPUT_RE.finditer(txt):
            child = resolve_tex(m.group(1), path)
            if child is None or not child.exists():
                missing_inputs.append(str(child))
            else:
                acc.append(load(child))
        return '\n'.join(acc)

    tex = load(main)
    bib_path = root / 'bibliography' / 'references.bib'
    bib = bib_path.read_text(encoding='utf-8', errors='replace') if bib_path.exists() else ''
    bibkey_list = re.findall(r'@\w+\s*\{\s*([^,]+),', bib)
    bibkey_counts = Counter(bibkey_list)
    bibkeys = set(bibkey_list)

    cites = sorted({k.strip() for g in re.findall(r'\\cite\w*\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]+)\}', tex) for k in g.split(',') if k.strip()})
    figs = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', tex)
    missing_figs = []
    for f in figs:
        found = False
        fpath = Path(f)
        search_roots = graphics_paths + [root]
        for gp in search_roots:
            cand = (gp / fpath).resolve()
            if cand.suffix and cand.exists():
                found = True
                break
            for ext in ['.pdf', '.png', '.jpg', '.jpeg']:
                if (gp / f"{f}{ext}").exists():
                    found = True
                    break
            if found:
                break
        if not found:
            missing_figs.append(f)

    labels = re.findall(r'\\label\{([^}]+)\}', tex)
    label_counts = Counter(labels)
    refs = sorted({x.strip() for g in re.findall(r'\\(?:ref|eqref|cref|Cref|autoref)\{([^}]+)\}', tex) for x in g.split(',') if x.strip()})
    stripped = re.sub(r'\\[a-zA-Z]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?', ' ', tex)
    words = len(re.findall(r'\b\w+\b', stripped))

    report = {
        'document': main_name,
        'tex_files_loaded': len(visited),
        'missing_inputs': missing_inputs,
        'citations_used': len(cites),
        'missing_citations': [c for c in cites if c not in bibkeys],
        'duplicate_bibkeys': {k: v for k, v in bibkey_counts.items() if v > 1},
        'figures_used': len(figs),
        'missing_figures': missing_figs,
        'labels': len(labels),
        'duplicate_labels': {k: v for k, v in label_counts.items() if v > 1},
        'missing_refs': [r for r in refs if r not in label_counts],
        'approx_words_tex': words,
        'heuristic_pages_text_only': round(words / 390, 1),
    }

    print(f"\n{'='*60}")
    print(f"  Validation: {main_name}")
    print(f"{'='*60}")
    print(json.dumps(report, indent=2, ensure_ascii=False))

    critical = (report['missing_inputs'] or report['missing_citations'] or report['duplicate_bibkeys']
                or report['missing_figures'] or report['missing_refs'])
    if critical:
        print(f"  [FAIL] {main_name}")
        sys.exit(1)
    else:
        print(f"  [PASS] {main_name}")
