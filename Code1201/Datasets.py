# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:50:38 2024

@author: sarlo
"""
## %%
import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix
from scipy.spatial.distance import squareform, pdist

df_pos = pd.read_pickle(r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis\code\filt0-40.pkl")
# Remove EOC channel. Shouldn't be here. Investigate: I think we're including
# the EOC channels
df_pos = df_pos.drop(index='EEG 053')

df_100 = pd.read_pickle(r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis\code\df_100.pkl")
signal = df_100.iloc[0, 1:].to_numpy()

X = df_pos[['x', 'y','z']].to_numpy()
Za = distance_matrix(X,X)
Zb = squareform(pdist(X))

from sklearn.metrics.pairwise import euclidean_distances, pairwise_distances
Zc = euclidean_distances(X, X)
Zd = pairwise_distances(X)
# X = np.random.RandomState(42).uniform(size=(30, 3))

# Really we should use a weighted graph, based on electrode distance
# k_nn = 5
# G = graphs.NNGraph(X, 'radius', sigma=0.1, epsilon=0.5)
# G.estimate_lmax()

# Make a mesurement with missing channels
# mask = np.ones(len(signal), dtype=bool)
# missing_idx = 1
# mask[missing_idx] = False
# measures = signal.copy()
# measures[~mask] = np.nan


# %% MNE Sensor Position
import numpy as np
import mne
montage = mne.channels.make_standard_montage('biosemi64')
ch_names = montage.ch_names
EEG_pos = montage.get_positions()['ch_pos']
# Restructure into array
EEG_pos = np.array([pos for _, pos in EEG_pos.items()])


# %% MNE EEGBCI
import os
import numpy as np
import mne

current_dir = os.getcwd()
os.chdir(os.path.dirname(current_dir))
data_dir ="./datasets"
#os.makedirs(data_dir, exist_ok=True)
#os.environ['MNE_EEGBCI_PATH'] = data_dir

# Load Electrode montage and dataset
subjects = np.arange(1, 10)
runs = [4, 8, 12]

# Download eegbci dataset through MNE
# Comment the following line if already downloaded

raw_fnames = [mne.datasets.eegbci.load_data(
    s, runs, path=data_dir, update_path=True) for s in subjects]
raw_fnames = np.reshape(raw_fnames, -1)
raws = [mne.io.read_raw_edf(f, preload=True) for f in raw_fnames]
raw = mne.concatenate_raws(raws)
mne.datasets.eegbci.standardize(raw)
raw.annotations.rename(dict(T1="left", T2="right"))

montage = mne.channels.make_standard_montage('standard_1005')
raw.set_montage(montage)
eeg_pos = np.array(
    [pos for _, pos in raw.get_montage().get_positions()['ch_pos'].items()])
ch_names = montage.ch_names

# Filter data and extract events
L_FREQ = 1  # Hz
H_FREQ = 30  # Hz
raw.filter(L_FREQ, H_FREQ, fir_design='firwin', skip_by_annotation='edge')
raw, ref_data = mne.set_eeg_reference(raw)

events, events_id = mne.events_from_annotations(raw)

# Epoch data
# Exclude bad channels
TMIN, TMAX = -1.0, 3.0
picks = mne.pick_types(raw.info, meg=False, eeg=True,
                       stim=False, eog=False, exclude="bads")
epochs = mne.Epochs(raw, events, events_id,
                    picks=picks, tmin=TMIN,
                    tmax=TMAX, baseline=(-1, 0),
                    detrend=1)

data = epochs.average().get_data()

# %% Import libraries
import sys
import os
from pathlib import Path
import mne
from scipy.io import loadmat
from eegrasp import EEGrasp
from eegrasp.utils_examples import fetch_data

# Load Electrode montage and dataset
current_dir = os.getcwd()
os.chdir(os.path.dirname(current_dir))
assets_dir = Path('..') / Path('data')
fetch_data(assets_dir, database="graph_learning")
file_name = os.path.join(assets_dir, "100Hz", 'data_set_IVa_aa.mat')

try:
    data = loadmat(file_name)
except (FileNotFoundError, OSError):
    print(f'File {file_name} not found')
    sys.exit(-1)

eeg = (data['cnt']).astype(float) * 1e-7  # Recomendation: to set to V
events = np.squeeze(data['mrk'][0, 0][0])
info = data['nfo'][0, 0]
ch_names = [ch_name[0] for ch_name in info[2][0, :]]
FS = info[1][0, 0]
pos = np.array([info[3][:, 0], info[4][:, 0]]).T

#  Preprocessing in MNE

# Create structure
mne_info = mne.create_info(ch_names=ch_names, sfreq=FS, ch_types='eeg')
data = mne.io.RawArray(eeg.T, mne_info)

# Extract events and annotate
mne_events = np.zeros((len(events), 3))
mne_events[:, 0] = events
annotations = mne.annotations_from_events(mne_events, FS)
data = data.set_annotations(annotations)
events2, events_id = mne.events_from_annotations(data)

# Reference data to average
data, _ = mne.set_eeg_reference(data, ref_channels='average')

# Filter between 8 and 30 Hz
data = data.filter(l_freq=8, h_freq=30, n_jobs=-1)

# Epoch and Crop epochs
epochs = mne.Epochs(data, events2, tmin=0.0, tmax=2.5,
                    baseline=(0, 0.5), preload=True)
epochs = epochs.crop(0.5, None)

epochs_data = epochs.get_data(copy=False)




#%%
import matplotlib.pyplot as plt
from pygsp2 import graphs
G = graphs.Minnesota()
fig = plt.figure()
fig, axes = plt.subplots(1, 2)
_ = axes[0].spy(G.W, markersize=0.5)
_ = G.plot(ax=axes[1])
plt.show()
# %%
### PROBLEMA CON FUNCION 
G = graphs.Bunny() #
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, projection='3d')
_ = ax1.spy(G.W, markersize=0.1)
_ = _ = G.plot(ax=ax2)
#%%
G = graphs.Sensor(N=400, seed=42)
fig, axes = plt.subplots(1, 2)
_ = axes[0].spy(G.W, markersize=2)
_ = G.plot(ax=axes[1])
plt.show()
#%%
import scipy.io

datasets = [r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis-20240527T204137Z-001\GraphTRSS\PM2_5_concentration_experiment\PM2_5_concentration.mat",
            r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis-20240527T204137Z-001\GraphTRSS\sea_surface_temperature_experiment\sea_surface_temperature.mat", 
            r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis-20240527T204137Z-001\GraphTRSS\covid_19_experiment_global\covid_19_confirmed_cases.mat",
            r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis-20240527T204137Z-001\GraphTRSS\covid_19_experiment_global\covid_19_new_cases.mat",
            ]
#Falta datos sinteticos y USA

mat = scipy.io.loadmat(datasets[0])
pos = mat['Position']
data = mat['Data']

# %% 
import pandas as pd

file = r"C:\Users\sarlo\OneDrive\Escritorio\Work\Code1201\Datasets\Iris\iris.data"
iris_data = pd.read_csv(file, delimiter = ",")
iris_data = iris_data.to_numpy()