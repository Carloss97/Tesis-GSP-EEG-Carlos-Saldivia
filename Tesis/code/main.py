## Imports
import pandas as pd
import time
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from pygsp2 import graphs, learning
from itertools import combinations 
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

def make_fig(sigmas, errors,error_rbf,miss_idxs):
    fig = plt.figure()
    plt.title('missing_idx_({},{})'.format(miss_idxs[0],miss_idxs[1]))
    plt.grid()
    plt.tight_layout()
    plt.plot(sigmas, errors)
    plt.axhline(error_rbf, color='r',  dashes=[6, 2])
    plt.xlabel(r'$\theta$')
    plt.ylabel('error')
    plt.close()
    return fig

def make_missing_chs(signal, idxs):
    mask = np.ones(len(signal), dtype=bool)
    for missing_idx in idxs:
        mask[missing_idx] = False
    measures = signal.copy()
    measures[~mask] = np.nan
    return (measures,mask)

def make_graph(G, signal, sigma, measures, mask):
    #G = graphs.NNGraph(X,'radius', sigma=sigma, epsilon=0.5)
    #G.estimate_lmax()
    # Solve the classification problem by reconstructing the signal:
    recovery = learning.regression_tikhonov(G[sigma], measures, mask, tau=0)
    error = np.linalg.norm(signal[~mask] - recovery[~mask])
    # Compare with standard interpolation methods
    #rbfi = interp.Rbf(X[mask, 0], X[mask, 1], X[mask, 2], measures[mask])
    #error_rbf = np.linalg.norm(rbfi(X[~mask, 0], X[~mask, 1],X[~mask, 2]) - signal[~mask])
    return error

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

max_sigma = 0.08
G ={}
sigmas = np.linspace(0.001, max_sigma, 100)
for sigma in sigmas:
    G[sigma] = graphs.NNGraph(X,'radius', sigma=sigma, epsilon= 0.9)
figs,mins,idxs = [],[],[]
error_mins,theta_mins, error_difs  = [],[],[]
start_all = time.time()
comb = combinations(range(len(signal)), 2)
colormap_plot_errors = np.zeros(len(signal))
fig = plt.figure()
for miss_idxs in list(comb):
    # for miss_idx2 in range(len(signal))[miss_idx1+1:]:
    start = time.time()
    # = (miss_idx1,miss_idx2)
    errors = []
    measures, mask = make_missing_chs(signal, miss_idxs)
    rbfi = interp.Rbf(X[mask, 0], X[mask, 1], X[mask, 2], measures[mask])
    error_rbf = np.linalg.norm(rbfi(X[~mask, 0], X[~mask, 1],X[~mask, 2]) - signal[~mask])
    for sigma in sigmas:
        #error = make_graph(G,signal,sigma, measures, mask)
        recovery = learning.regression_tikhonov(G[sigma], measures, mask, tau=0)
        error = np.linalg.norm(signal[~mask] - recovery[~mask])
        errors.append(error) 
    print('Tiempo de {} :'.format(miss_idxs),time.time()-start)
    figs.append(make_fig(sigmas, errors, error_rbf, miss_idxs))    
    idxs.append(miss_idxs)
    error_mins.append(np.min(errors))
    theta_mins.append(sigmas[np.argmin(errors)])
    error_difs.append(error_rbf-np.min(errors))
    if error_rbf-np.min(errors) <= 0:
        colormap_plot_errors[~mask] += 1
end  = time.time()
print('Tiempo total:',end-start_all)

    
fig = plt.figure()
plt.xlabel('idxs')
plt.grid()
plt.tight_layout()
plt.title('error_min_by_idx')
plt.stem(range(len(idxs)), error_mins)
plt.ylabel('error')
plt.close()
figs.append(fig)

fig = plt.figure()
plt.xlabel('idx')
plt.grid()
plt.tight_layout()
plt.title('theta_min_by_idx')
plt.stem(range(len(idxs)), theta_mins)
plt.ylabel('theta_min')
plt.close()
figs.append(fig)

fig = plt.figure()
plt.xlabel('idx')
plt.grid()
plt.tight_layout()
plt.title('Error_rbf-error_method_by_idx')
plt.stem(range(len(idxs)), error_difs)
plt.ylabel('Error_dif')
plt.close()
figs.append(fig)


df_pos2 = pd.read_pickle('df_pos.pkl')
df_pos2 = df_pos2.drop(index=59)
X2 = df_pos2[['x', 'y']].to_numpy()
G2 = graphs.NNGraph(X2,'radius', sigma=sigma, epsilon=0.5)

save_figs_as_pdf(figs, 'errors_for_sigma_max_{}_xyz_2_missing_norma2_problem_idxs+e0.9.pdf'.format(max_sigma))  
G2.plot(colormap_plot_errors, indices=True, title='Problem idxs')
plt.savefig('Problem_idxs+e0.9pdf')
plt.close()