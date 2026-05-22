from pathlib import Path
import re, sys, json

root = Path(__file__).resolve().parents[1]

for main_name in ['tesis_completa.tex', 'tesis_caps_1_5.tex']:
    main = root / main_name
    if not main.exists():
        print(f"SKIP {main_name}: not found")
        continue
    
    visited = []
    missing_inputs = []
    graphics_paths = [root]  # Default: root dir
    
    def load(path):
        path = path.resolve()
        if path in visited:
            return ''
        visited.append(path)
        try:
            txt = path.read_text(encoding='utf-8', errors='replace')
        except FileNotFoundError:
            missing_inputs.append(str(path))
            return ''
        acc = [txt]
        # Extract graphicspath from config files
        nonlocal_gp = re.findall(r'\\graphicspath\{\{([^}]+)\}\}', txt)
        for gp_list in nonlocal_gp:
            for gp in gp_list.split(','):
                gp = gp.strip()
                cand = (root / gp).resolve()
                if cand.exists() and cand.is_dir():
                    graphics_paths.append(cand)
        for m in re.finditer(r'(?<!%)\\input\{([^}]+)\}', txt):
            name = m.group(1)
            p = root / name
            if p.suffix == '':
                p = p.with_suffix('.tex')
            acc.append(load(p))
        return '\n'.join(acc)
    
    tex = load(main)
    bib = (root / 'bibliography' / 'references.bib').read_text(encoding='utf-8', errors='replace')
    bibkeys = set(re.findall(r'@\w+\s*\{\s*([^,]+),', bib))
    cites = sorted({k.strip() for g in re.findall(r'\\cite\w*\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]+)\}', tex) for k in g.split(',') if k.strip()})
    figs = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', tex)
    missing_figs = []
    for f in figs:
        found = False
        for gp in graphics_paths:
            cand = gp / f
            if cand.suffix and cand.exists():
                found = True; break
            for ext in ['.pdf', '.png', '.jpg', '.jpeg']:
                if (gp / (f + ext)).exists():
                    found = True; break
        if not found:
            missing_figs.append(f)
    
    labels = re.findall(r'\\label\{([^}]+)\}', tex)
    from collections import Counter
    cnt = Counter(labels)
    refs = sorted({x.strip() for g in re.findall(r'\\(?:ref|eqref|cref|Cref|autoref)\{([^}]+)\}', tex) for x in g.split(',') if x.strip()})
    words = len(re.findall(r'\b\w+\b', re.sub(r'\\[a-zA-Z]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?', ' ', tex)))
    
    report = {
        'document': main_name,
        'tex_files_loaded': len(visited),
        'missing_inputs': missing_inputs,
        'citations_used': len(cites),
        'missing_citations': [c for c in cites if c not in bibkeys],
        'figures_used': len(figs),
        'missing_figures': missing_figs,
        'labels': len(labels),
        'duplicate_labels': {k: v for k, v in cnt.items() if v > 1},
        'missing_refs': [r for r in refs if r not in cnt],
        'approx_words_tex': words,
        'heuristic_pages_text_only': round(words / 390, 1),
    }
    
    print(f"\n{'='*60}")
    print(f"  Validation: {main_name}")
    print(f"{'='*60}")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    
    if report['missing_inputs'] or report['missing_citations'] or report['missing_figures'] or report['missing_refs']:
        print(f"  [FAIL] {main_name}")
        sys.exit(1)
    else:
        print(f"  [PASS] {main_name}")