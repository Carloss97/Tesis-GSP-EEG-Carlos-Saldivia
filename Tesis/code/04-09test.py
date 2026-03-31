import pandas as pd
import time
import numpy as np
import mne
import matplotlib.pyplot as plt
from eegrasp import EEGrasp
from pygsp2 import graphs, plotting
# %%

montage = mne.channels.make_standard_montage('biosemi64')
ch_names = montage.ch_names
EEG_pos = montage.get_positions()['ch_pos']
# Restructure into array
EEG_pos = np.array([pos for _, pos in EEG_pos.items()])

# %% Plot Montage

# fig = montage.plot(kind='3d', show=False)
# fig.gca().view_init(azim=70, elev=15)  # set view angle for tutorial
# plt.title('Electrode Positions in 3d')
# plt.show()

# %% Calculate electrode distance

gsp = EEGrasp(coordinates=EEG_pos)
gsp_norm = EEGrasp(coordinates=EEG_pos)
Dij = gsp.compute_distance(normalize=False)
Dij_norm = gsp_norm.compute_distance()


G = gsp.compute_graph(epsilon= 0.1, sigma = 1)
G.set_coordinates(EEG_pos)
G.plot()
plt.show()
G_norm = gsp_norm.compute_graph(epsilon= 0.2, sigma = 1)
G_norm.set_coordinates(EEG_pos)


# %% test

plt.figure()
plt.spy(G.W, markersize=5)
plt.figure()
plt.spy(G_norm.W, markersize=5)
plt.figure()
fig, ax = G.plot()

plt.show()
G.set_coordinates(EEG_pos/np.amax(EEG_pos))
G.plot()

G_norm.set_coordinates(EEG_pos/np.amax(EEG_pos))
G_norm.plot()
plt.show()

Graph = graphs.Graph(G.W)
Graph.set_coordinates(EEG_pos)
Graph.plot()
plt.show()

# im = plt.imshow(W, cmap='gray')
# plt.title('Electrode Distance Matrix')
# plt.colorbar(label='Euc. Distance [m]')
# plt.show()

# df_pos = pd.read_pickle('dummy.pkl')
# # Remove EOC channel. Shouldn't be here. Investigate: I think we're including
# # the EOC channels
# df_pos = df_pos.drop(index='EEG 053')

# df_100 = pd.read_pickle('df_100.pkl')
# signal = df_100.iloc[0, 1:].to_numpy()

# X = df_pos[['x', 'y','z']].to_numpy()

# eegsp = EEGrasp(signal, X)
# dist = eegsp.compute_distance(normalize = False)
# G = eegsp.compute_graph(epsilon=0.2, sigma=1)
# G.plot()