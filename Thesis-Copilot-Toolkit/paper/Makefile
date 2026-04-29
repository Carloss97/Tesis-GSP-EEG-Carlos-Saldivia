.PHONY: all clean pdf-en pdf-es pdf-both help

# Default target
all: pdf-both

# Compile English version
pdf-en:
	@echo "Building English paper..."
	cd ieee && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex && cd ..
	@echo "✓ English paper compiled: ieee/main.pdf"

# Compile Spanish version
pdf-es:
	@echo "Building Spanish paper..."
	cd ieee_es && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex && cd ..
	@echo "✓ Spanish paper compiled: ieee_es/main.pdf"

# Compile both versions
pdf-both: pdf-en pdf-es
	@echo "✓ Both versions compiled successfully!"
	@echo "  English:  ieee/main.pdf"
	@echo "  Spanish:  ieee_es/main.pdf"

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	cd ieee && latexmk -c && cd ..
	cd ieee_es && latexmk -c && cd ..
	@echo "✓ Cleaned"

# Deep clean (remove PDFs too)
distclean:
	@echo "Deep cleaning..."
	cd ieee && latexmk -C && cd ..
	cd ieee_es && latexmk -C && cd ..
	@echo "✓ Cleaned (including PDFs)"

# Help
help:
	@echo "Publication Paper Builder"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  pdf-en    - Compile English version (ieee/main.pdf)"
	@echo "  pdf-es    - Compile Spanish version (ieee_es/main.pdf)"
	@echo "  pdf-both  - Compile both versions (default)"
	@echo "  all       - Same as pdf-both"
	@echo "  clean     - Remove build artifacts"
	@echo "  distclean - Remove all generated files including PDFs"
	@echo "  help      - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make             # Build both versions"
	@echo "  make pdf-es      # Build only Spanish version"
	@echo "  make clean       # Remove intermediate files"
