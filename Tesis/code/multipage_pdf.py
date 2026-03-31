import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def save_figs_as_pdf(figs, fn):
    if isinstance(figs, list):
        pdf = PdfPages(fn)
        for f in figs:
            pdf.savefig(f)
        pdf.close()
    else:
        figs.savefig(fn, format='pdf')
    print('File %s created' % fn)

thetas = np.linspace(0, 2 * np.pi, 6, endpoint=False)
t = np.linspace(0, 3, 200)
figs = []
for theta in thetas:
    fig = plt.figure()
    figs.append(fig)
    y = np.sin(2 * np.pi * t + theta)
    plt.plot(t, y)
    plt.xlabel('t')
    plt.title(r'$\sin(2 \pi t + %.1f)$' % theta)

save_figs_as_pdf(figs, 'senos.pdf')

## En latex despues se usa
## \includegraphics[width=0.5\columnwidth,page=3]{senos}}
