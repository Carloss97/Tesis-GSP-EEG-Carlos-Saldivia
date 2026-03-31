# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:55:10 2023

@author: sarlo
"""

import pandas as pd
import numpy as np
import time
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from pygsp import graphs, learning
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

def make_fig(sigmas, errors,error_rbf,miss_idx):
    fig = plt.figure()
    plt.title('missing_idx_{}'.format(miss_idx))
    plt.grid()
    plt.tight_layout()
    plt.plot(sigmas, errors)
    plt.axhline(error_rbf, color='r',  dashes=[6, 2])
    #plt.axhline(0.02, color='purple',  dashes=[6, 2])
    plt.xlabel(r'$\theta$')
    plt.ylabel('error')
    plt.close()
    return fig
    
def make_missing_chs(signal, idx, mode = 'single', n_electrodes = 1):
    mask = np.ones(len(signal), dtype=bool)
    idxs = []
    if mode == 'single':
        mask[idx] = False
    elif mode == 'cluster':
        for electrode in range(n_electrodes):
            if idx+electrode >= len(signal):
                idx.append(idx-electrode)
                mask[idx-electrode] = False
            else:
                idx.append(idx+electrode)
                mask[idx+electrode] = False
    elif mode == 'sparse':
        mask[idx] = False
        mask[len(signal)-idx] = False
    measures = signal.copy()
    measures[~mask] = np.nan
    return (measures,mask,idxs)

def make_missing_ch(signal, idx ):
    mask = np.ones(len(signal), dtype=bool)
    missing_idx = idx
    mask[missing_idx] = False
    measures = signal.copy()
    measures[~mask] = np.nan
    return (measures,mask)

def make_graph(X, signal, sigma, measures, mask):
    G = graphs.NNGraph(X,'radius', sigma=sigma, epsilon=0.6)
    G.estimate_lmax()
    # Solve the classification problem by reconstructing the signal:
    recovery = learning.regression_tikhonov(G, measures, mask, tau=0)
    error = np.linalg.norm(signal[~mask] - recovery[~mask])
    # Compare with standard interpolation methods
    rbfi = interp.Rbf(X[mask, 0], X[mask, 1], X[mask, 2], measures[mask])
    error_rbf = np.abs(rbfi(X[~mask, 0], X[~mask, 1],X[~mask, 2]) - signal[~mask])[0]
    return (error, error_rbf)

def get_mins(errors, error_rbf):
    error_min = np.min(errors)
    theta_min = sigmas[np.argmin(errors)]
    error_dif = error_rbf-error_min
    return (error_min, theta_min, error_dif)

df_pos = pd.read_pickle('dummy.pkl')
# Remove EOC channel. Shouldn't be here. Investigate: I think we're including
# the EOC channels
df_pos = df_pos.drop(index='EEG 053')

df_100 = pd.read_pickle('df_100.pkl')
signal = df_100.iloc[0, 1:].to_numpy()

X = df_pos[['x', 'y','z']].to_numpy()
# X = np.random.RandomState(42).uniform(size=(30, 3))
max_sigma = 0.1
sigmas = np.linspace(0.001, max_sigma, 200)
figs,mins = [],[]
idxs = []
error_mins = []
theta_mins = []
error_difs = []
fig = plt.figure()
for miss_idx in range(len(signal)):
    errors = []
    measures, mask = make_missing_ch(signal, miss_idx)
    for sigma in sigmas:
        error, error_rbf = make_graph(X,signal,sigma, measures, mask)
        if error <error_rbf:
            errors.append(error)
        else:
            errors.append(np.nan)
    
    plt.title('Rango theta en que error <rbf')
    plt.grid()
    plt.tight_layout()
    plt.plot(sigmas, errors)
    plt.xlabel(r'$\theta$')
    plt.ylabel('error')
save_figs_as_pdf(fig, 'rango_theta')
plt.show()
plt.close()


