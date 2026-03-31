# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 00:19:17 2024

@author: sarlo
"""
#%%
import scipy.io

datasets = [r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis-20240527T204137Z-001\GraphTRSS\PM2_5_concentration_experiment\PM2_5_concentration.mat",
            r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis-20240527T204137Z-001\GraphTRSS\sea_surface_temperature_experiment\sea_surface_temperature.mat", 
            r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis-20240527T204137Z-001\GraphTRSS\covid_19_experiment_global\covid_19_confirmed_cases.mat",
            r"C:\Users\sarlo\OneDrive\Escritorio\Work\Tesis-20240527T204137Z-001\GraphTRSS\covid_19_experiment_global\covid_19_new_cases.mat",
            ]
#Falta datos sinteticos y USA

mat = scipy.io.loadmat(datasets[0])
pos = mat['Position']
data = mat['Data']