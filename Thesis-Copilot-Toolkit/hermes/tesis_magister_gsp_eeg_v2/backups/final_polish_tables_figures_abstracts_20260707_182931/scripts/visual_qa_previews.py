#!/usr/bin/env python3
"""Render figure and table/page previews for visual QA of tesis_completa."""
from __future__ import annotations
import re
from pathlib import Path
import fitz
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build_logs" / "visual_qa"
OUT.mkdir(parents=True, exist_ok=True)

# Use robust manifest from final driver and included chapters.
def collect_tex(path: Path, seen=None) -> str:
    if seen is None:
        seen = set()
    path = path if path.suffix else path.with_suffix('.tex')
    if not path.exists() or path in seen:
        return ""
    seen.add(path)
    txt = path.read_text(encoding='utf-8', errors='replace')
    base = path.parent
    out = txt + "\n"
    for m in re.finditer(r"\\(?:input|include)\{([^}]+)\}", txt):
        sub = (ROOT / m.group(1)).with_suffix('.tex')
        out += collect_tex(sub, seen)
    return out

tex = collect_tex(ROOT / 'tesis_completa.tex')
figs = []
for m in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", tex):
    raw = m.group(1)
    p = ROOT / raw
    candidates = []
    bases = [p, ROOT / 'figures' / raw]
    for b in bases:
        if b.suffix.lower() in ['.pdf', '.png', '.jpg', '.jpeg']:
            candidates.append(b)
        else:
            candidates.extend([b.with_suffix(ext) for ext in ['.pdf','.png','.jpg','.jpeg']])
            candidates.extend([Path(str(b) + ext) for ext in ['.pdf','.png','.jpg','.jpeg']])
    for cand in candidates:
        if cand.exists():
            p = cand
            break
    if p.exists() and p not in figs:
        figs.append(p)

# Tables included by \input{tables/...}
tables = []
for m in re.finditer(r"\\input\{(tables/[^}]+)\}", tex):
    p = ROOT / m.group(1)
    if p.suffix == "": p = p.with_suffix('.tex')
    if p.exists() and p not in tables:
        tables.append(p)

manifest = OUT / 'visual_inventory.txt'
manifest.write_text(
    "FIGURES\n" + "\n".join(str(p.relative_to(ROOT)) for p in figs) +
    "\n\nTABLES\n" + "\n".join(str(p.relative_to(ROOT)) for p in tables) + "\n",
    encoding='utf-8'
)

font = ImageFont.load_default()

def render_pdf_page(path: Path, page_index=0, zoom=1.6):
    doc = fitz.open(path)
    page = doc[page_index]
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
    doc.close()
    return img

def render_figure(path: Path):
    if path.suffix.lower() == '.pdf':
        return render_pdf_page(path, 0, 1.8)
    return Image.open(path).convert('RGB')

def contact_sheet(images, labels, out_path, thumb_w=520, cols=2):
    thumbs = []
    for img, label in zip(images, labels):
        im = img.copy()
        w, h = im.size
        scale = thumb_w / w
        im = im.resize((thumb_w, max(1, int(h*scale))), Image.Resampling.LANCZOS)
        label_h = 34
        canvas = Image.new('RGB', (thumb_w, im.height + label_h), 'white')
        canvas.paste(im, (0, label_h))
        d = ImageDraw.Draw(canvas)
        d.rectangle([0,0,thumb_w,label_h-1], fill=(245,245,245), outline=(180,180,180))
        d.text((6,6), label[:80], fill=(0,0,0), font=font)
        thumbs.append(canvas)
    rows = (len(thumbs)+cols-1)//cols
    row_h = [0]*rows
    for i,t in enumerate(thumbs): row_h[i//cols] = max(row_h[i//cols], t.height)
    W = cols*thumb_w
    H = sum(row_h)
    sheet = Image.new('RGB', (W,H), 'white')
    y = 0
    for r in range(rows):
        x = 0
        for c in range(cols):
            i = r*cols+c
            if i < len(thumbs): sheet.paste(thumbs[i], (x,y))
            x += thumb_w
        y += row_h[r]
    sheet.save(out_path)

# Figure sheet(s)
fig_imgs = [render_figure(p) for p in figs]
fig_labels = [str(p.relative_to(ROOT)) for p in figs]
# split to keep vision readable
for k in range(0, len(fig_imgs), 6):
    contact_sheet(fig_imgs[k:k+6], fig_labels[k:k+6], OUT / f'figures_sheet_{k//6+1}.png', thumb_w=560, cols=2)

# Render selected final PDF pages likely containing tables/figures.
pdf = ROOT / 'tesis_completa.pdf'
doc = fitz.open(pdf)
def page_sheet(start, end, name, zoom=1.15):
    imgs=[]; labels=[]
    for pno in range(start, min(end, len(doc))+1):
        page = doc[pno-1]
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
        imgs.append(Image.frombytes('RGB',[pix.width,pix.height],pix.samples))
        labels.append(f'página {pno}')
    contact_sheet(imgs, labels, OUT / name, thumb_w=420, cols=3)
page_sheet(12, 31, 'pages_theory_methods_12_31.png')
page_sheet(33, 46, 'pages_results_33_46.png')
page_sheet(47, 57, 'pages_discussion_conclusion_47_57.png')
doc.close()

print(f'Wrote {manifest.relative_to(ROOT)} and previews in {OUT.relative_to(ROOT)}')
