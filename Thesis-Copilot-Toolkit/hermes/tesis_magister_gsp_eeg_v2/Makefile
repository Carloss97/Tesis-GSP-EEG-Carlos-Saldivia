MAIN=tesis_completa
SHORT=tesis_caps_1_5

.PHONY: all full short pdf pdf-short validate clean

all: full

full: pdf

short: pdf-short

pdf:
	latexmk -pdf -interaction=nonstopmode $(MAIN).tex

pdf-short:
	latexmk -pdf -interaction=nonstopmode $(SHORT).tex

validate:
	python3 scripts/validate_thesis.py

clean:
	latexmk -C $(MAIN).tex || true
	latexmk -C $(SHORT).tex || true
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk
