# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:44:39 2023

@author: sarlo
"""

from pygsp import graphs, filters, learning
import matplotlib.pyplot as plt
import numpy as np
G = graphs.Sensor(N=100, seed=42)
G.estimate_lmax()
filt = lambda x: 1 / (1 + 10*x)
filt = filters.Filter(G, filt)
rng = np.random.default_rng(42)
signal = filt.analyze(rng.normal(size=G.n_vertices))
mask = rng.uniform(0, 1, G.n_vertices) > 0.5
measures = signal.copy()
measures[~mask] = np.nan
recovery = learning.regression_tikhonov(G, measures, mask, tau=0)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(10, 3))
limits = [signal.min(), signal.max()]
_ = G.plot(signal, ax=ax1, limits=limits, title='Ground truth')
_ = G.plot(measures, ax=ax2, limits=limits, title='Measures')
_ = G.plot(recovery, ax=ax3, limits=limits, title='Recovery')
_ = fig.tight_layout()