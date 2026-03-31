# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:02:07 2024

@author: sarlo
"""
###mask
#rng = np.random.default_rng(42)
# mask = rng.uniform(0, 1, G.n_vertices) > 0.5
# measures = signal.copy()
# measures[~mask] = np.nan
# recovery = learning.regression_tikhonov(G, measures, mask, tau=0)

### MAE
#np.mean(np.abs(f - y))

### pygsp2
#G = graphs.NNGraph(X, k = 10, sigma = 1)
#G = graphs.NNGraph(X, "radius", epsilon = 0.5)
#G.set_coordinates(EEG_pos/np.amax(EEG_pos))
#W = G.W.toarray()
#plt.imshow(W)

### Z
# from scipy.spatial import distance_matrix
# from scipy.spatial.distance import squareform, pdist
# Za = distance_matrix(X,X)
# Zb = squareform(pdist(X))

# from sklearn.metrics.pairwise import euclidean_distances, pairwise_distances
# Zc = euclidean_distances(X, X)
# Zd = pairwise_distances(X)

# from sklearn.metrics.pairwise import rbf_kernel
# rbf = rbf_kernel(X)

### EEGraSP
#Dij = gsp.compute_distance(normalize=False)  #Equivalente con lo anterior
#pygs2. W = graph_learning.graph_log_degree(
 #     Z, a, b, gamma=gamma, w_max=w_max, maxiter=maxiter)
 # W[W < 1e-5] = 0


    #rbfi = interp.Rbf(X[mask, 0], X[mask, 1], X[mask, 2], measures[mask])
    #error_rbf = np.linalg.norm(rbfi(X[~mask, 0], X[~mask, 1],X[~mask, 2]) - signal[~mask])