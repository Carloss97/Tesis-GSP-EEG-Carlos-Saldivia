#!/usr/bin/env python3
"""
Sanitize LaTeX files: replace \texttt{...} with \code{...} (preserve nested braces).
Run from repository root.
"""
import os
import io

ROOT = os.path.join('Thesis-Copilot-Toolkit','thesis','usm')
replaced_total = 0
files_total = 0

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        if not fn.endswith('.tex'):
            continue
        path = os.path.join(dirpath, fn)
        with io.open(path, 'r', encoding='utf-8') as f:
            s = f.read()
        i = 0
        out = []
        changed = 0
        while True:
            idx = s.find('\\texttt{', i)
            if idx == -1:
                out.append(s[i:])
                break
            out.append(s[i:idx])
            j = idx + len('\\texttt{')
            # find matching closing brace
            k = j
            level = 1
            while k < len(s) and level > 0:
                ch = s[k]
                if ch == '{':
                    level += 1
                elif ch == '}':
                    level -= 1
                k += 1
            if level != 0:
                # unmatched brace: abort replacement for this occurrence, keep original and move on
                out.append(s[idx: j])
                i = j
            else:
                inner = s[j:k-1]
                out.append('\\code{')
                out.append(inner)
                out.append('}')
                changed += 1
                i = k
        if changed:
            files_total += 1
            replaced_total += changed
            with io.open(path, 'w', encoding='utf-8') as f:
                f.write(''.join(out))
            print(f'Updated {path}: {changed} replacements')

print(f'Done. Files modified: {files_total}, total replacements: {replaced_total}')
