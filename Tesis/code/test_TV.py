# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:23:18 2024

@author: sarlo
"""

import numpy as np
import mne
import matplotlib.pyplot as plt
from eegrasp import EEGrasp
from sklearn.neighbors import kneighbors_graph, radius_neighbors_graph
from pygsp2 import graphs, plotting
import scipy.io
mat = scipy.io.loadmat(r"C:\Users\sarlo\OneDrive\Documentos\Tesis-20240527T204137Z-001\GraphTRSS\PM2_5_concentration_experiment\PM2_5_concentration.mat")
pos = mat['Position']

# %%
# montage = mne.channels.make_standard_montage('biosemi64')
# ch_names = montage.ch_names
# EEG_pos = montage.get_positions()['ch_pos']
# # Restructure into array
# EEG_pos = np.array([pos for _, pos in EEG_pos.items()])
# pos  = EEG_pos

k = 10
e = 1
D = kneighbors_graph(pos, k, mode='distance')
Dr = radius_neighbors_graph(pos,e, mode = 'distance')
D = D.toarray()
Dr = Dr.toarray()

sigma = np.mean(D[D != 0])
sigmar = np.mean(Dr[Dr !=0])
W = np.exp(-(D ** 2) / (2 * sigma ** 2))
Wr = np.exp(-(Dr ** 2) / (2 * sigmar ** 2))
np.fill_diagonal(W,0)
np.fill_diagonal(Wr,0)
#W[W==1.] = 0 #SUS
#Wr[Wr==1.] = 0
G = graphs.Graph(W)
G.set_coordinates(pos)
W = G.W.toarray()

Gr = graphs.Graph(Wr)
Gr.set_coordinates(pos)
Wr = Gr.W.toarray()

plt.spy(W)

G.plot()
plt.figure()
plt.spy(Wr)
Gr.plot()
plt.show()

# n = G.n_edges
# sigmaa = np.sum(D)/n - 1

# %%

gsp = EEGrasp(coordinates=pos)
gsp_norm = EEGrasp(coordinates=pos)
Dij = gsp.compute_distance(normalize=False)
Dij_norm = gsp_norm.compute_distance()

G = gsp.compute_graph(epsilon= e, sigma = sigmar)
G_norm = gsp_norm.compute_graph(epsilon= e/10, sigma = sigmar)
G.set_coordinates(pos)
G_norm.set_coordinates(pos)

plt.figure()
plt.spy(G.W, markersize=5)
plt.figure()
plt.spy(G_norm.W, markersize=5)
plt.figure()
fig, ax = G.plot()
fig1, ax1 = G_norm.plot()

plt.show()
