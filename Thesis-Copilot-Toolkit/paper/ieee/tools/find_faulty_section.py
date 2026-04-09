import re
import subprocess
from pathlib import Path

root = Path('.').resolve()
main = root / 'main.tex'
text = main.read_text(encoding='utf-8')
pre, post = text.split('\\begin{document}',1)
body, _ = post.split('\\end{document}',1)
# Find input lines (preserve order)
inputs = [line.strip() for line in body.splitlines() if line.strip().startswith('\\input{')]

print(f'Found {len(inputs)} \input lines')
for i in range(1, len(inputs)+1):
    tmp = root / 'build' / f'tmp_main_{i}.tex'
    tmp.parent.mkdir(exist_ok=True)
    # include \\maketitle to reproduce full-document behavior
    content = pre + '\\begin{document}\n\\maketitle\n' + '\n'.join(inputs[:i]) + '\n\\end{document}\n'
    tmp.write_text(content, encoding='utf-8')
    print(f'Compiling with first {i} inputs...')
    # run pdflatex
    res = subprocess.run(['pdflatex','-interaction=nonstopmode','-file-line-error','-halt-on-error','-output-directory','build', str(tmp)], cwd=str(root))
    print('Returncode', res.returncode)
    if res.returncode != 0:
        print('Compilation failed at input index', i)
        break
print('Done')
