from pygsp2 import graphs, learning, filters
import matplotlib.pyplot as plt
import numpy as np

G = graphs.Sensor(seed=42)  # By default it has 64 nodes
G.estimate_lmax()

# Create a ground truth signal:
g = filters.Heat(G, 10)
signal = g.filter(np.random.randn(G.n_vertices))

# Construct a measurement signal from a binary mask:
rs = np.random.RandomState(42)
mask = rs.uniform(0, 1, G.n_vertices) > 0.5
measures = signal.copy()
measures[~mask] = np.nan

# Solve the classification problem by reconstructing the signal:
recovery = learning.regression_tikhonov(G, measures, mask, tau=0)

# Plot the results.
# Note that we recover the class with ``np.argmax(recovery, axis=1)``.
fig, ax = plt.subplots(1, 3, sharey=True, figsize=(10, 3))
G.plot_signal(signal, ax=ax[0], title='Ground truth')
G.plot_signal(measures, ax=ax[1], title='Measurements')
G.plot_signal(recovery, ax=ax[2], title='Recovered class')
fig.tight_layout()
plt.show()
