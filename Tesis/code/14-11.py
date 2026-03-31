# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:49:20 2024

@author: sarlo
"""

import numpy as np
import mne
import matplotlib.pyplot as plt
import pandas as pd
from eegrasp import EEGrasp
from pygsp2 import graphs, plotting
from sklearn.neighbors import kneighbors_graph, radius_neighbors_graph
# %%
montage = mne.channels.make_standard_montage('biosemi64')
ch_names = montage.ch_names
EEG_pos = montage.get_positions()['ch_pos']
# Restructure into array
EEG_pos = np.array([pos for _, pos in EEG_pos.items()])

# %% Calculate electrode distance
gsp = EEGrasp(coordinates=EEG_pos)
# Calculate distance matrix
Dij = gsp.compute_distance()
sigma = np.mean(Dij)
#Make Graph without Gaussian Kernel
## Using K-nn
# G_e = graphs.NNGraph(EEG_pos, 'radius', sigma=sigma, epsilon=0.5)
#G_k = graphs.NNGraph(EEG_pos, k = 10, sigma = sigma )
#G_e = gsp.compute_graph(epsilon= 0.1, sigma = sigma)
## Using e-neighbours
# Ae = radius_neighbors_graph(EEG_pos, radius = 0.1, mode = 'distance',  include_self = False)
# Ae_arr = Ae.toarray()
# G_e = gsp.compute_graph(Ae)
# Ak = kneighbors_graph(EEG_pos, 10, mode='distance', include_self=False)
# Ak_arr = Ak.toarray()
# G_k = gsp.compute_graph(Ak)
#G_k.plot()


# G = gsp.compute_graph(epsilon= 0.1, sigma = 1)
# W = G.W.toarray()
# L = G.L.toarray()

#plt.show()
