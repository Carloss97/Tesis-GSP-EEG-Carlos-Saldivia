from pathlib import Path
import sys
sys.path.insert(0, str(Path('Thesis-Copilot-Toolkit').resolve()))
from src.graph_construction.graph_constructors import build_graph
import numpy as np
info = build_graph('knng', positions=np.zeros((6,3)), k=3, sigma=0.5)['info']
print(info)
