from pathlib import Path
import re, sys, json
root = Path(__file__).resolve().parents[1]
main = root/'tesis_magister_hermes.tex'
visited=[]
missing_inputs=[]

def load(path):
    path = path.resolve()
    if path in visited:
        return ''
    visited.append(path)
    try:
        txt = path.read_text(encoding='utf-8', errors='replace')
    except FileNotFoundError:
        missing_inputs.append(str(path)); return ''
    acc=[txt]
    for m in re.finditer(r'(?<!%)\\input\{([^}]+)\}', txt):
        name=m.group(1)
        p=root/name
        if p.suffix=='': p=p.with_suffix('.tex')
        acc.append(load(p))
    return '\n'.join(acc)
tex=load(main)
bib=(root/'bibliography/references.bib').read_text(encoding='utf-8', errors='replace')
bibkeys=set(re.findall(r'@\w+\s*\{\s*([^,]+),', bib))
cites=sorted({k.strip() for g in re.findall(r'\\cite\w*\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]+)\}', tex) for k in g.split(',') if k.strip()})
figs=re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', tex)
missing_figs=[]
for f in figs:
    p=root/f
    if p.suffix:
        if not p.exists(): missing_figs.append(f)
    else:
        if not any((root/(f+ext)).exists() for ext in ['.pdf','.png','.jpg','.jpeg']): missing_figs.append(f)
labels=re.findall(r'\\label\{([^}]+)\}', tex)
from collections import Counter
cnt=Counter(labels)
refs=sorted({x.strip() for g in re.findall(r'\\(?:ref|eqref|cref|Cref|autoref)\{([^}]+)\}', tex) for x in g.split(',') if x.strip()})
words=len(re.findall(r'\b\w+\b', re.sub(r'\\[a-zA-Z]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?', ' ', tex)))
report={
 'tex_files_loaded':len(visited),
 'missing_inputs':missing_inputs,
 'citations_used':len(cites),
 'missing_citations':[c for c in cites if c not in bibkeys],
 'figures_used':len(figs),
 'missing_figures':missing_figs,
 'labels':len(labels),
 'duplicate_labels':{k:v for k,v in cnt.items() if v>1},
 'missing_refs':[r for r in refs if r not in cnt],
 'approx_words_tex':words,
 'heuristic_pages_text_only':round(words/430,1),
}
print(json.dumps(report, indent=2, ensure_ascii=False))
if report['missing_inputs'] or report['missing_citations'] or report['missing_figures'] or report['missing_refs']:
    sys.exit(1)
