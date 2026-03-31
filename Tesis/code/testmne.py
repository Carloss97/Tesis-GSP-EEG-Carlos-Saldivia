# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:43:37 2023

@author: sarlo
"""

import os
import pandas as pd
import mne
from mne.datasets import eegbci
from mne.io import concatenate_raws, read_raw_edf
from mne.channels import make_standard_montage
# sample_data_folder = mne.datasets.sample.data_path()
# sample_data_raw_file = os.path.join(
#     sample_data_folder, "MEG", "sample", "sample_audvis_filt-0-40_raw.fif"
# )
# raw = mne.io.read_raw_fif(sample_data_raw_file)
# raw.crop(tmax=60).load_data()
subject = 1
runs = [6, 10, 14]  # motor imagery: hands vs feet
raw_fnames = eegbci.load_data(subject, runs)
raw = concatenate_raws([read_raw_edf(f, preload=True) for f in raw_fnames])
eegbci.standardize(raw)  # set channel names
montage = make_standard_montage("standard_1005")
raw.set_montage(montage)
#eeg = raw.copy().pick('eeg')
pos = raw.get_montage().get_positions()['ch_pos']
df = pd.DataFrame.from_dict(pos, orient='index', columns=['x','y','z'])
df.to_pickle("./eegbci.pkl")