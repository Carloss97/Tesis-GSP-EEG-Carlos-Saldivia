# Simulación de canales faltantes (enmascaramiento aleatorio)
def simulate_missing_channels(signals: np.ndarray, missing_ratio: float = 0.1, random_state: int = 42) -> np.ndarray:
    """
    Simula canales faltantes en las señales EEG enmascarando aleatoriamente un porcentaje de canales.
    - signals: matriz (N_instantes, N_electrodos)
    - missing_ratio: proporción de canales a enmascarar (por fila)
    Retorna una copia de signals con NaN en los canales faltantes.
    """
    import numpy as np
    rng = np.random.default_rng(random_state)
    signals_masked = signals.copy()
    N, D = signals.shape
    n_missing = max(1, int(D * missing_ratio))
    for i in range(N):
        missing_idx = rng.choice(D, n_missing, replace=False)
        signals_masked[i, missing_idx] = np.nan
    return signals_masked
"""
data_loader.py
Funciones generales para cargar y preprocesar datasets de EEG para el pipeline experimental.
"""

from typing import Tuple, Dict, Any
import numpy as np

# Implementación para MNE Sample Dataset
def load_mne_sample_dataset() -> Dict[str, Any]:
    """
    Carga el MNE Sample Dataset localmente si existe, si no lo descarga.
    Retorna un diccionario con:
      - 'signals': np.ndarray (N_instantes, N_electrodos)
      - 'positions': np.ndarray (N_electrodos, 3)
      - 'info': dict con metadatos
    """
    import mne
    import numpy as np
    import os
    data_path = mne.datasets.sample.data_path(download=False)
    fname_raw = os.path.join(data_path, "MEG", "sample", "sample_audvis_raw.fif")
    if not os.path.exists(fname_raw):
        print("Descargando MNE Sample Dataset...")
        data_path = mne.datasets.sample.data_path(download=True)
        fname_raw = os.path.join(data_path, "MEG", "sample", "sample_audvis_raw.fif")
    raw = mne.io.read_raw_fif(fname_raw, preload=True)
    raw.pick_types(meg=False, eeg=True, stim=False)
    signals = raw.get_data()
    ch_names = raw.info['ch_names']
    montage = raw.get_montage()
    if montage is not None:
        pos_dict = montage.get_positions()['ch_pos']
        positions = np.array([pos_dict[ch] for ch in ch_names if ch in pos_dict])
    else:
        positions = np.zeros((len(ch_names), 3))
    info = {'sfreq': raw.info['sfreq'], 'ch_names': ch_names, 'n_channels': len(ch_names)}
    return {'signals': signals.T, 'positions': positions, 'info': info}

# Ejemplo de función de preprocesamiento
def preprocess_signals(signals: np.ndarray) -> np.ndarray:
    """
    Aplica preprocesamiento estándar a las señales EEG (filtrado, normalización, etc).
    """
    # Implementar según necesidades
    return signals
