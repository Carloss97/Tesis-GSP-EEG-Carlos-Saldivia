"""
from https://mne.tools/stable/auto_tutorials/evoked/plot_eeg_erp.html#sphx-glr-auto-tutorials-evoked-plot-eeg-erp-py
"""
import pandas as pd
import mne
from mne.datasets import sample
import matplotlib.pyplot as plt

plt.close('all')

# Setup for reading the raw data
data_path = sample.data_path()
raw_fname = (data_path / "MEG" / "sample" / "sample_audvis_filt-0-40_raw.fif")
event_fname = (data_path / "MEG" / "sample" /
               "sample_audvis_filt-0-40_raw-eve.fif")
raw = mne.io.read_raw_fif(raw_fname, preload=True)

# Let's restrict the data to the EEG channels
raw.pick_types(meg=False, eeg=True, eog=True)

# By looking at the measurement info you will see that we have now
# 59 EEG channels and 1 EOG channel
print(raw.info)

# The EEG channels in the sample dataset already have locations.
# These locations are available in the 'loc' of each channel description.
# For the first channel we get
print(raw.info['chs'][0]['loc'])

# Channel location. For MEG this is the position plus the normal given by a 3x3
# rotation matrix. For EEG this is the position followed by reference position
# (with 6 unused). The values are specified in device coordinates for MEG and in
# head coordinates for EEG channels, respectively.

# And it's actually possible to plot the channel locations using
# :func:`mne.io.Raw.plot_sensors`.

# raw.plot_sensors()
# raw.plot_sensors('3d')  # in 3D

# We define Epochs and compute an ERP for the left auditory condition.
reject = dict(eeg=180e-6, eog=150e-6)
event_id, tmin, tmax = {'left/auditory': 1}, -0.2, 0.5
events = mne.read_events(event_fname)
epochs_params = dict(events=events, event_id=event_id, tmin=tmin, tmax=tmax,
                     reject=reject)

evoked = mne.Epochs(raw, **epochs_params).average()

title = 'EEG average reference'
evoked.plot(titles=dict(eeg=title), time_unit='s')
evoked.plot_topomap(times=[0.1], size=3., time_unit='s')
plt.tight_layout()
plt.savefig('topo.pdf')

df = evoked.to_data_frame()
df_100 = df.loc[45]
df_100.to_pickle('df_100.pkl')
sensor_pos = mne.channels.layout._find_topomap_coords(raw.info, None)
ch_names = [ch['ch_name'] for ch in raw.info['chs']]
df_pos = pd.DataFrame(ch_names, columns=['ch_names'])
df_pos['x'] = sensor_pos[:, 0]
df_pos['y'] = sensor_pos[:, 1]
df_pos.to_pickle('df_pos.pkl')
