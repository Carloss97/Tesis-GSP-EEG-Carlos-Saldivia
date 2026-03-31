import pandas as pd
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from pygsp2 import graphs, learning

df_pos = pd.read_pickle('df_pos.pkl')
# Remove EOC channel. Shouldn't be here. Investigate: I think we're including
# the EOC channels
df_pos = df_pos.drop(index=59)

df_100 = pd.read_pickle('df_100.pkl')
signal = df_100.iloc[0, 1:].to_numpy()

X = df_pos[['x', 'y']].to_numpy()
# X = np.random.RandomState(42).uniform(size=(30, 3))

# Really we should use a weighted graph, based on electrode distance
k_nn = 5
G = graphs.NNGraph(X, k=5)
G.estimate_lmax()

# Make a mesurement with missing channels
mask = np.ones(len(signal), dtype=bool)
missing_idx = 5
mask[missing_idx] = False
measures = signal.copy()
measures[~mask] = np.nan

ks, errors = [], []
for k_nn in range(2, 35):
    G = graphs.NNGraph(X, k=k_nn)
    G.estimate_lmax()
    # Solve the classification problem by reconstructing the signal:
    recovery = learning.regression_tikhonov(G, measures, mask, tau=0)
    error = np.linalg.norm(signal[~mask] - recovery[~mask])
    # Compare with standard interpolation methods
    rbfi = interp.Rbf(X[mask, 0], X[mask, 1], measures[mask])
    error_rbf = np.abs(rbfi(X[~mask, 0], X[~mask, 1]) - signal[~mask])[0]
    print(f'k_nn:{k_nn}, error GSP: {error:.2f}, error RBF: {error_rbf:.2f}')
    ks.append(k_nn)
    errors.append(error)

print(f'Minimum error: {min(errors):.2f}')

plt.style.use('style.mplstyle')
plt.close('all')
plt.figure()
plt.plot(ks, errors)
plt.axhline(error_rbf, color='r',  dashes=[6, 2])
plt.xlabel('k')
plt.ylabel('error')
plt.grid()
plt.tight_layout()
plt.savefig('error.pdf')

# Plot the results
do_plot = False
if do_plot:
    rng = np.random.default_rng(42)
    mask = rng.uniform(0, 1, G.n_vertices) > 0.5
    measures = signal.copy()
    recovery = learning.regression_tikhonov(G, measures, mask, tau=0)
    measures[~mask] = np.nan
    plt.close('all')
    fig, axes = plt.subplots(1, 2)
    _ = axes[0].spy(G.W, markersize=5)
    _ = G.plot(ax=axes[1])

    plt.figure()
    plt.spy(G.W, markersize=5)
    plt.tight_layout()
    plt.savefig('adjacency.pdf')

    # Note that we recover the class with ``np.argmax(recovery, axis=1)``.
    fig, ax = plt.subplots(1, 3, sharey=True, figsize=(10, 3))
    G.plot(signal, ax=ax[0], title='Ground truth')
    G.plot(measures, ax=ax[1], limits=[signal.min(), signal.max()], title='Measurements')
    G.plot(recovery, ax=ax[2], title='Recovered class')
    # fig, ax = plt.subplots(1, 1, sharey=True, figsize=(7, 6))
    # G.plot(signal, ax=ax[0], title='Ground truth')
    # G.plot(measures, ax=ax[1], limits=[signal.min(), signal.max()], title='Measurements')
    # G.plot(recovery, ax=ax, title='Recovered class')
    # G.plot(recovery, ax=ax, title='', highlight=[missing_idx])
    fig.tight_layout()
    plt.savefig('graph.pdf')

plt.show()
