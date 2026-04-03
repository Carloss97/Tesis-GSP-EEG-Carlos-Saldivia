"""
data_loader.py
Funciones generales para cargar y preprocesar datasets de EEG para el pipeline experimental.
"""

from typing import Tuple, Dict, Any, List

import numpy as np


# Simulación de canales faltantes (enmascaramiento aleatorio)
def simulate_missing_channels(signals: np.ndarray, missing_ratio: float = 0.1, random_state: int = 42) -> np.ndarray:
    """
    Simula canales faltantes en las señales EEG enmascarando aleatoriamente un porcentaje de canales.
    - signals: matriz (N_instantes, N_electrodos)
    - missing_ratio: proporción de canales a enmascarar (por fila)
    Retorna una copia de signals con NaN en los canales faltantes.
    """
    rng = np.random.default_rng(random_state)
    signals_masked = signals.copy()
    N, D = signals.shape
    n_missing = max(1, int(D * missing_ratio))
    for i in range(N):
        missing_idx = rng.choice(D, n_missing, replace=False)
        signals_masked[i, missing_idx] = np.nan
    return signals_masked

# Simulación de canales faltantes (enmascaramiento sistemático)
def simulate_missing_channels_systematic(signals: np.ndarray, missing_indices: List[int]) -> np.ndarray:
    """
    Simula canales faltantes en las señales EEG enmascarando sistemáticamente los canales indicados.
    - signals: matriz (N_instantes, N_electrodos)
    - missing_indices: lista de índices de canales a enmascarar (por ejemplo, [0, 3, 7])
    Retorna una copia de signals con NaN en los canales seleccionados.
    """
    signals_masked = signals.copy()
    N, D = signals.shape
    for idx in missing_indices:
        if idx < 0 or idx >= D:
            raise ValueError(f"Índice de canal fuera de rango: {idx}")
        signals_masked[:, idx] = np.nan
    return signals_masked


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

# Implementación para PhysioNet EEG Motor Movement/Imagery Dataset (EEGMMIDB)
def load_physionet_eegmmidb(subject: int = 1, run: int = 1) -> Dict[str, Any]:
    """
    Carga un sujeto y run del PhysioNet EEGMMIDB usando mne.datasets.eegbci.
    Retorna un diccionario con 'signals', 'positions', 'info'.
    """
    import mne
    import numpy as np
    # Descargar y cargar datos
    eegbci = mne.datasets.eegbci
    runs = [run]
    raw_fnames = eegbci.load_data(subject, runs)
    raw = mne.io.read_raw_edf(raw_fnames[0], preload=True)
    raw.pick_types(eeg=True, meg=False)
    signals = raw.get_data()
    ch_names = raw.info['ch_names']
    montage = mne.channels.make_standard_montage('standard_1005')
    raw.set_montage(montage)
    pos_dict = montage.get_positions()['ch_pos']
    positions = np.array([pos_dict[ch] if ch in pos_dict else np.zeros(3) for ch in ch_names])
    info = {'sfreq': raw.info['sfreq'], 'ch_names': ch_names, 'n_channels': len(ch_names), 'subject': subject, 'run': run}
    return {'signals': signals.T, 'positions': positions, 'info': info}

# Implementación para dataset sintético propio
def load_synthetic_eeg(n_channels: int = 16, n_times: int = 1000, random_state: int = 42) -> Dict[str, Any]:
    """
    Genera un dataset sintético de EEG con posiciones y señales conocidas.
    Retorna un diccionario con 'signals', 'positions', 'info'.
    """
    import numpy as np
    rng = np.random.default_rng(random_state)
    # Señales sintéticas: suma de senos y ruido
    t = np.linspace(0, 1, n_times)
    signals = np.array([np.sin(2 * np.pi * f * t) + 0.1 * rng.normal(size=n_times) for f in rng.uniform(8, 12, n_channels)])
    signals = signals.T  # (n_times, n_channels)
    # Posiciones sintéticas en círculo 2D
    theta = np.linspace(0, 2 * np.pi, n_channels, endpoint=False)
    positions = np.stack([np.cos(theta), np.sin(theta), np.zeros_like(theta)], axis=1)
    info = {'sfreq': n_times, 'ch_names': [f'Ch{i+1}' for i in range(n_channels)], 'n_channels': n_channels, 'synthetic': True}
    return {'signals': signals, 'positions': positions, 'info': info}

# Implementación para BCI Competition IV Dataset 2a
def load_bci_competition_iv_2a(subject: int = 1) -> Dict[str, Any]:
    """
    Carga el dataset BCI Competition IV 2a para un sujeto.
    Retorna un diccionario con 'signals', 'positions', 'info'.
    """
    import mne
    import numpy as np
    import os
    # El usuario debe descargar manualmente los archivos .gdf y colocarlos en una carpeta conocida
    data_dir = os.environ.get('BCI_IV_2A_PATH', './datasets/BCI_IV_2a/')
    fname = os.path.join(data_dir, f'A{subject:02d}T.gdf')
    if not os.path.exists(fname):
        raise FileNotFoundError(f"Archivo {fname} no encontrado. Descargue el dataset y defina BCI_IV_2A_PATH.")
    raw = mne.io.read_raw_gdf(fname, preload=True)
    raw.pick_types(eeg=True, meg=False)
    signals = raw.get_data()
    ch_names = raw.info['ch_names']
    montage = mne.channels.make_standard_montage('standard_1005')
    raw.set_montage(montage)
    pos_dict = montage.get_positions()['ch_pos']
    positions = np.array([pos_dict[ch] if ch in pos_dict else np.zeros(3) for ch in ch_names])
    info = {'sfreq': raw.info['sfreq'], 'ch_names': ch_names, 'n_channels': len(ch_names), 'subject': subject}
    return {'signals': signals.T, 'positions': positions, 'info': info}

# Ejemplo de función de preprocesamiento
def preprocess_signals(signals: np.ndarray) -> np.ndarray:
    """
    Aplica preprocesamiento estándar a las señales EEG (filtrado, normalización, etc).
    """
    # Implementar según necesidades
    return signals
