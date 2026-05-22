MAIN=tesis_magister_hermes

.PHONY: all pdf clean validate

all: pdf

pdf:
	latexmk -pdf -interaction=nonstopmode $(MAIN).tex

validate:
	python3 scripts/validate_thesis.py

clean:
	latexmk -C $(MAIN).tex || true
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk
