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
    graph_time = time.time()
    G = graphs.NNGraph(X,'radius', sigma=sigma, epsilon=0.5)
    G.estimate_lmax()
    # Solve the classification problem by reconstructing the signal:
    recov_time = time.time()
    recovery = learning.regression_tikhonov(G, measures, mask, tau=0)
    error = np.linalg.norm(signal[~mask] - recovery[~mask])
    final = time.time()
    print('Tiempo graph:{}, recovery:{}'.format(recov_time-graph_time,final-recov_time))
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
max_sigma = 0.08
sigmas = np.linspace(0.001, max_sigma, 100)
figs,mins = [],[]
idxs = []
error_mins = []
theta_mins = []
error_difs = []
start = time.time()
for miss_idx in range(len(signal)):
    errors = []
    measures, mask = make_missing_ch(signal, miss_idx)
    for sigma in sigmas:
        error, error_rbf = make_graph(X,signal,sigma, measures, mask)
        errors.append(error)
    figs.append(make_fig(sigmas, errors, error_rbf, miss_idx))    
    idxs.append(miss_idx)
    error_mins.append(np.min(errors))
    theta_mins.append(sigmas[np.argmin(errors)])
    error_difs.append(error_rbf-np.min(errors))
end = time.time()
print('Tiempo total:',end-start) 
fig = plt.figure()
plt.xlabel('idx')
plt.grid()
plt.tight_layout()
plt.title('error_min_by_idx')
plt.stem(idxs, error_mins)
plt.ylabel('error')
plt.close()
figs.append(fig)

fig = plt.figure()
plt.xlabel('idx')
plt.grid()
plt.tight_layout()
plt.title('theta_min_by_idx')
plt.stem(idxs, theta_mins)
plt.ylabel('theta_min')
plt.close()
figs.append(fig)

fig = plt.figure()
plt.xlabel('idx')
plt.grid()
plt.tight_layout()
plt.title('Error_rbf-error_method_by_idx')
plt.stem(idxs, error_difs)
plt.ylabel('Error_dif')
plt.close()
figs.append(fig)

save_figs_as_pdf(figs, 'errors_for_sigma_max_{}_xyz_pdf'.format(max_sigma))
problem_idx = []
for i in idxs:
    if error_difs[i] <= 0:
        problem_idx.append(i)
# # Plot the results
do_plot = True
if do_plot:
    G = graphs.NNGraph(X,'radius', sigma=0.04, epsilon=0.5)
    G.estimate_lmax()
    recovery = learning.regression_tikhonov(G, measures, mask, tau=0)
    plt.close('all')
    plt.figure()
    # Note that we recover the class with ``np.argmax(recovery, axis=1)``.
    # fig, ax = plt.subplots(1, 3, sharey=True, figsize=(10, 3))
    # G.plot(signal, ax=ax[0], title='Ground truth')
    # G.plot(measures, ax=ax[1], limits=[signal.min(), signal.max()], title='Measurements')
    # G.plot(recovery, ax=ax[2], title='Recovered class')
    fig, ax = plt.subplots(1, 1, sharey=True, figsize=(7, 6))
    # G.plot(signal, ax=ax[0], title='Ground truth')
    # G.plot(measures, ax=ax[1], limits=[signal.min(), signal.max()], title='Measurements')
    #G.plot(recovery, ax=ax, title='Recovered class')
    G.plot(recovery, ax=ax,indices=True, title='', highlight=problem_idx)
    fig.tight_layout()
    plt.savefig('graph_test.pdf')

