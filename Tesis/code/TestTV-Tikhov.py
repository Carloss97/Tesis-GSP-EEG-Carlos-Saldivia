# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:10:18 2023

@author: sarlo
"""
import pandas as pd
import numpy as np
from pygsp import graphs, plotting, learning
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pyunlocbox
import scipy.interpolate as interp
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis

df_pos = pd.read_pickle(r"C:\Users\sarlo\Desktop\Tesis\code\dummy.pkl")
# Remove EOC channel. Shouldn't be here. Investigate: I think we're including
# the EOC channels
df_pos = df_pos.drop(index='EEG 053')

df_100 = pd.read_pickle(r"C:\Users\sarlo\Desktop\Tesis\code\df_100.pkl")
signal = df_100.iloc[0, 1:].to_numpy()

X = df_pos[['x', 'y','z']].to_numpy()

sigma = 0.04
sigmas, errors, errorsl1, errorsl2 = [], [], [],[]
# Create a random sensor graph
for sigma in np.linspace(0.001, 0.08, 50):
    G = graphs.NNGraph(X,'radius', sigma=sigma, epsilon=0.5)
    G.compute_fourier_basis()
    # Create label signal

    G.plot(signal,indices = True, title='Ground-Truth sigma={}'.format(sigma))
    mask = np.ones(len(signal), dtype=float)
    missing_idx = 5
    mask[missing_idx] = 0.0
    measures = signal.copy()
    measures[missing_idx] = 0.0
    # Applying the mask to the data
    sigma_noise = 0.1
    G.plot(measures, indices = True, title='Measures' , highlight= [0, 1])

    # Set the functions in the problem
    gamma = 3.0
    d = pyunlocbox.functions.dummy()
    r = pyunlocbox.functions.norm_l1()
    f = pyunlocbox.functions.norm_l2(w=mask, y=measures, lambda_=gamma)
    # Define the solver
    G.compute_differential_operator()
    L = G.D.T.toarray()
    step = 0.999 / (1 + np.linalg.norm(L))
    solver = pyunlocbox.solvers.mlfbf(L=L, step=step)
    # Solve the problem
    x0 = measures.copy()
    prob1 = pyunlocbox.solvers.solve([d, r, f], solver=solver, x0=x0, rtol=0, maxit=1000)
    G.plot(prob1['sol'],indices = True, title='TV' )

    # Set the functions in the problem
    r = pyunlocbox.functions.norm_l2(A=L, tight=False)
    # Define the solver
    step = 0.999 / np.linalg.norm(np.dot(L.T, L) + gamma * np.diag(mask), 2)
    solver = pyunlocbox.solvers.gradient_descent(step=step)
    # Solve the problem
    x0 = measures.copy()
    prob2 = pyunlocbox.solvers.solve([r, f], solver=solver, x0=x0, rtol=0, maxit=1000)
    G.plot(prob2['sol'],indices = True,title='Tikhov')

    G = graphs.NNGraph(X,'radius', sigma=sigma, epsilon=0.2)
    G.estimate_lmax()
    # Solve the classification problem by reconstructing the signal:

    mask = mask!=0
    recovery = learning.regression_tikhonov(G, measures, mask, tau=0)
    error = np.linalg.norm(signal[~mask] - recovery[~mask])
    error_l1 = np.linalg.norm(signal[~mask] - prob1['sol'][~mask])
    error_l2 = np.linalg.norm(signal[~mask] - prob2['sol'][~mask])

    sigmas.append(sigma)
    errors.append(error)
    errorsl1.append(error_l1)
    errorsl2.append(error_l2)

rbfi = interp.Rbf(X[mask, 0], X[mask, 1],X[mask,2], measures[mask])
error_rbf = np.linalg.norm(rbfi(X[~mask, 0], X[~mask, 1],X[~mask, 2]) - signal[~mask])
plt.close('all')
plt.figure()
plt.plot(sigmas, errors)
plt.plot(sigmas,errorsl1)
plt.plot(sigmas,errorsl2)
plt.axhline(error_rbf, color='r',  dashes=[6, 2])
#plt.axhline(0.02, color='purple',  dashes=[6, 2])
plt.xlabel(r'$\theta$')
plt.ylabel('error')
plt.grid()
plt.tight_layout()
print(error_rbf-error)
print(error_rbf-error_l1)
print(error_rbf-error_l2)