import pandas as pd
import time
import numpy as np
import mne
import matplotlib.pyplot as plt
from eegrasp import EEGrasp
from sklearn.neighbors import kneighbors_graph, radius_neighbors_graph
from pygsp2 import graphs, plotting
# %%
montage = mne.channels.make_standard_montage('biosemi64')
ch_names = montage.ch_names
EEG_pos = montage.get_positions()['ch_pos']
# Restructure into array
EEG_pos = np.array([pos for _, pos in EEG_pos.items()])
# %% Plot Montage

def gaussian_kernel(x, sigma=0.1):
    """Gaussian Kernel Weighting function.

    Notes
    -----
    This function is supposed to be used in the PyGSP2 module but is
    repeated here since there is an error in the available version of the
    toolbox.

    References
    ----------
    * D. I. Shuman, S. K. Narang, P. Frossard, A. Ortega and
    P. Vandergheynst, "The emerging field of signal processing on graphs:
    Extending high-dimensional data analysis to networks and other
    irregular domains," in IEEE Signal Processing Magazine, vol. 30, no. 3,
    pp. 83-98, May 2013, doi: 10.1109/MSP.2012.2235192.
    """
    return np.exp(-np.power(x, 2.) / (2.*np.power(float(sigma), 2)))

# %% Calculate electrode distance

gsp = EEGrasp(coordinates=EEG_pos)
gsp_norm = EEGrasp(coordinates=EEG_pos)
Dij = gsp.compute_distance(normalize=False)
Dij_norm = gsp_norm.compute_distance()

G = gsp.compute_graph(epsilon= 0.1, sigma = 1)
W = G.W.toarray()
L = G.L.toarray()
G_norm = gsp_norm.compute_graph(epsilon= 1, sigma = 1)
W_norm = G_norm.W.toarray()
L_norm = G_norm.W.toarray()

Ak = kneighbors_graph(EEG_pos, 10, mode='distance', include_self=False)
Ar = radius_neighbors_graph(EEG_pos, radius = 0.1, mode = 'distance',  include_self = False)
Ar = Ar.toarray()
Ak = Ak.toarray()

plt.show()
#G.set_coordinates(EEG_pos/np.amax(EEG_pos))
# %%
sigma = np.mean(Dij)
gss = gaussian_kernel(Dij,sigma)
test = radius_neighbors_graph(gss, radius = 1, mode = 'distance',  include_self = False)
test = test.toarray()
plt.imshow(test)
plt.show()