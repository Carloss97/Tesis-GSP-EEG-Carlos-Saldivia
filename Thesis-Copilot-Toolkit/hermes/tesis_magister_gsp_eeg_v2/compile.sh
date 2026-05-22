#!/bin/bash
set -e
cd "$(dirname "$0")"
echo "=== Compilando tesis completa ==="
latexmk -pdf -interaction=nonstopmode tesis_completa.tex
echo "=== Compilando versión recortada (caps 1-5) ==="
latexmk -pdf -interaction=nonstopmode tesis_caps_1_5.tex
echo "=== Validando ==="
python3 scripts/validate_thesis.py
echo "=== Listo ==="
ls -lh tesis_completa.pdf tesis_caps_1_5.pdf
