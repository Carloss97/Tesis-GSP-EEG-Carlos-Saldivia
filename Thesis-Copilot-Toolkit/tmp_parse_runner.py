import re, json, pathlib
p = pathlib.Path(__file__).resolve().parents[0] / 'experiments' / 'run_reruns_selected.py'
s = p.read_text(encoding='utf-8')
datasets=set(); graphs=set(); methods=set()

# datasets: find bracketed list immediately before ", seeds="
for m in re.finditer(r"\[([^\]]*?)\]\s*,\s*seeds\s*=", s):
    dsraw = m.group(1)
    for d in re.findall(r"'([^']+)'", dsraw):
        datasets.add(d)

# graph specs: extract contents inside graph_specs=[ ... ]
for m in re.finditer(r"graph_specs\s*=\s*\[([^\]]*?)\]", s, re.S):
    gsraw = m.group(1)
    for g in re.findall(r"\('([^']+)'", gsraw):
        graphs.add(g)

# methods: extract contents inside methods=[ ... ]
for m in re.finditer(r"methods\s*=\s*\[([^\]]*?)\]", s):
    mr = m.group(1)
    for meth in re.findall(r"'([^']+)'", mr):
        methods.add(meth)
print(json.dumps({
    'n_defs': s.count('IterDef('),
    'datasets': sorted(datasets),
    'graphs': sorted(graphs),
    'methods': sorted(methods)
}, indent=2))
