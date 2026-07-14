from pathlib import Path
import sys
try:
    import fitz  # PyMuPDF
    from PIL import Image
except Exception as exc:
    print('Missing dependency:', exc)
    sys.exit(2)

REPORT_FIG_DIR = Path('informes/weekly_summary_2026-04-01_2026-04-07/figures')
if not REPORT_FIG_DIR.exists():
    print('Figures folder not found:', REPORT_FIG_DIR)
    sys.exit(1)

PDFS = sorted(REPORT_FIG_DIR.glob('*.pdf'))
if not PDFS:
    print('No PDF files found in', REPORT_FIG_DIR)
    sys.exit(0)

for pdf in PDFS:
    out = pdf.with_suffix('.png')
    try:
        print('Converting', pdf.name, '->', out.name)
        doc = fitz.open(pdf)
        page = doc.load_page(0)
        zoom = 150.0 / 72.0
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
        # Resize preserving aspect ratio and pad to 1200x720
        target_w, target_h = 1200, 720
        img.thumbnail((target_w, target_h), Image.LANCZOS)
        new_img = Image.new('RGB', (target_w, target_h), (255, 255, 255))
        left = (target_w - img.width) // 2
        top = (target_h - img.height) // 2
        new_img.paste(img, (left, top))
        new_img.save(out, format='PNG', quality=95)
        doc.close()
    except Exception as e:
        print('Failed to convert', pdf, '->', e)

print('Conversion done')
