import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from eegrasp import EEGrasp
import mne

import numpy as np
from scipy.sparse import lil_matrix, csr_matrix

def compute_vknn(Z, k_min, k_max, beta_factor):
    """
    Constructs a sparse vKNN graph based on the provided distance matrix and parameters.

    Parameters:
    - Z (ndarray): NxN distance matrix.
    - k_min (int): Minimum number of neighbors.
    - k_max (int): Maximum number of neighbors.
    - beta_factor (float): Proportionality constant for beta_i.

    Returns:
    - sparse_graph (scipy.sparse.lil_matrix): Sparse adjacency matrix representing the vKNN graph.
    """
    N = Z.shape[0]
    # Initialize a sparse matrix to store the graph
    vknn = lil_matrix((N, N))

    # Compute beta_i as proportional to the sum of distances in each row
    beta = beta_factor * np.sum(Z, axis=1)

    for i in range(N):
        # Sort the distances for node i and get sorted indices
        sorted_indices = np.argsort(Z[i])
        sorted_distances = Z[i, sorted_indices]

        # Initialize delta_i and k_i
        delta_i = sorted_distances[k_min - 1]
        k_i = k_min

        # Iteratively add neighbors until the conditions are met
        neighbors = sorted_indices[:k_min]  # Start with the first k_min neighbors
        while delta_i < beta[i] and k_i < k_max:
            neighbors = sorted_indices[:k_i + 1]  # Add one more neighbor
            delta_i += sorted_distances[k_i]
            k_i += 1

        # Update the sparse graph with the selected neighbors
        for neighbor in neighbors:
            if neighbor != i:  # Exclude self-loop
                vknn[i, neighbor] = 1

    return vknn

montage = mne.channels.make_standard_montage('biosemi64')
ch_names = montage.ch_names
EEG_pos = montage.get_positions()['ch_pos']
EEG_pos = np.array([pos for _, pos in EEG_pos.items()])
gsp = EEGrasp(coordinates=EEG_pos)
Dij = gsp.compute_distance()


# Compute the vKNN graph for the larger distance matrix
vKNN = compute_vknn(Dij, beta_factor=0.1, k_min=3, k_max=100)
#sparse_vknn_csr = sparse_vknn_graph.tocsr()
G = gsp.compute_graph(vKNN)
G.set_coordinates(EEG_pos/np.amax(EEG_pos))
w = G.W.toarray()
plt.imshow(w)
G.plot()
plt.show()