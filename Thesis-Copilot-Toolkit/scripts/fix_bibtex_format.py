#!/usr/bin/env python3
"""
Convert Biblatex-formatted .bib entries to standard BibTeX format.
Handles: journaltitle → journal, date → year, removes Biblatex-specific fields.
"""

import re
import sys

def fix_bibtex(bib_file_path):
    """Fix Biblatex entries to BibTeX format."""
    
    with open(bib_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace journaltitle with journal
    content = re.sub(r'journaltitle\s*=', 'journal =', content)
    
    # Replace date = {YYYY} or date = {YYYY-MM} or date = {YYYY-MM-DD} with year = {YYYY}
    content = re.sub(r'date\s*=\s*\{(\d{4})(?:-\d{2}(?:-\d{2})?)?\}', r'year = {\1}', content)
    
    # Remove langid field (Biblatex-specific)
    content = re.sub(r'\s*langid\s*=\s*\{[^}]*\},?\n', '\n', content)
    
    # Remove file field (Biblatex-specific) - multi-line often
    content = re.sub(r'\s*file\s*=\s*\{[^}]*(?:\{[^}]*\}[^}]*)*\},?\n', '\n', content)
    
    # Remove duplicate blank lines
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # Check if anything changed
    if content == original_content:
        return content, 0, 0
    
    # Count changes
    journaltitle_count = len(re.findall(r'journaltitle\s*=', original_content))
    date_count = len(re.findall(r'date\s*=\s*\{\d{4}', original_content))
    
    return content, journaltitle_count, date_count

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python fix_bibtex.py <bib_file>")
        sys.exit(1)
    
    bib_file = sys.argv[1]
    fixed_content, jt_count, d_count = fix_bibtex(bib_file)
    
    # Write back
    with open(bib_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"Fixed {bib_file}")
    print(f"  - journaltitle → journal: {jt_count}")
    print(f"  - date → year: {d_count}")
