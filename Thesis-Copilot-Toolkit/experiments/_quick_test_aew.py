import sys, os
import numpy as np

sys.path.insert(0, os.path.join(os.getcwd(), 'Thesis-Copilot-Toolkit', 'src'))
from graph_construction.aew import AEW

if __name__ == '__main__':
    # small synthetic test
    rng = np.random.RandomState(0)
    X = rng.rand(10, 6)  # d=10, n=6
    param = {'max_iter': 3, 'k': 3, 'sigma': 'median', 'tol': 1e-6}
    W, W0 = AEW(X, param)
    print('W shape', W.shape)
    print('W0 shape', W0.shape)
    print('W finite:', np.all(np.isfinite(W)))
    print('W0 finite:', np.all(np.isfinite(W0)))
    print('Done')
