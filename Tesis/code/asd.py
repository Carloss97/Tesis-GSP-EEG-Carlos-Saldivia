# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 01:38:14 2023

@author: sarlo
"""

import pyunlocbox
import numpy as np
from pygsp import graphs, plotting
# Create a random sensor graph
G = graphs.Sensor(N=256, distributed=True, seed=42)
G.compute_fourier_basis()
# Create label signal
label_signal = np.copysign(np.ones(G.N), G.U[:, 3])
fig, ax = G.plot(label_signal)
rng = np.random.default_rng(42)
# Create the mask
M = rng.uniform(size=G.N)
M = (M > 0.6).astype(float)  # Probability of having no label on a vertex.

# Applying the mask to the data
sigma = 0.1
subsampled_noisy_label_signal = M * \
    (label_signal + sigma * rng.standard_normal(G.N))
fig, ax = G.plot(subsampled_noisy_label_signal)
# Set the functions in the problem
gamma = 3.0
d = pyunlocbox.functions.dummy()
r = pyunlocbox.functions.norm_l1()
f = pyunlocbox.functions.norm_l2(
    w=M, y=subsampled_noisy_label_signal, lambda_=gamma)
# Define the solver
G.compute_differential_operator()
L = G.D.T.toarray()
step = 0.999 / (1 + np.linalg.norm(L))
solver = pyunlocbox.solvers.mlfbf(L=L, step=step)
# Solve the problem
x0 = subsampled_noisy_label_signal.copy()
prob1 = pyunlocbox.solvers.solve(
    [d, r, f], solver=solver, x0=x0, rtol=0, maxit=1000)
fig, ax = G.plot(prob1['sol'])
# Set the functions in the problem
r = pyunlocbox.functions.norm_l2(A=L, tight=False)
# Define the solver
step = 0.999 / np.linalg.norm(np.dot(L.T, L) + gamma * np.diag(M), 2)
solver = pyunlocbox.solvers.gradient_descent(step=step)
# Solve the problem
x0 = subsampled_noisy_label_signal.copy()
prob2 = pyunlocbox.solvers.solve(
    [r, f], solver=solver, x0=x0, rtol=0, maxit=1000)
fig, ax = G.plot(prob2['sol'])
