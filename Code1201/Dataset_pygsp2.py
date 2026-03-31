# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:46:23 2024

@author: sarlo
"""
import matplotlib.pyplot as plt
from pygsp2 import graphs

#%%
G = graphs.Minnesota()
fig = plt.figure()
fig, axes = plt.subplots(1, 2)
_ = axes[0].spy(G.W, markersize=0.5)
_ = G.plot(ax=axes[1])
plt.show()
# %%
### PROBLEMA CON FUNCION 
G = graphs.Bunny()
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, projection='3d')
_ = ax1.spy(G.W, markersize=0.1)
_ = _ = G.plot(ax=ax2)
#%%
G = graphs.Sensor(N=400, seed=42)
fig, axes = plt.subplots(1, 2)
_ = axes[0].spy(G.W, markersize=2)
_ = G.plot(ax=axes[1])
plt.show()