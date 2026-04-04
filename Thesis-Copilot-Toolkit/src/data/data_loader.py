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
def load_physionet_eegmmidb(subject: int = 1, run: int = 4) -> Dict[str, Any]:
    """
    Carga un sujeto y run del PhysioNet EEGMMIDB.
    Busca primero en la ruta local EEGBCI_LOCAL_PATH (relativa o absoluta),
    luego intenta descarga online como fallback.
    run=4 corresponde a motor imagery (manos izquierda/derecha).
    Retorna un diccionario con 'signals', 'positions', 'info'.
    """
    import mne
    import numpy as np
    import os

    local_root = os.environ.get(
        'EEGBCI_LOCAL_PATH',
        os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'datasets', 'MNE-eegbci-data')
    )
    local_root = os.path.realpath(local_root)

    fname_local = os.path.join(
        local_root, 'files', 'eegmmidb', '1.0.0',
        f'S{subject:03d}', f'S{subject:03d}R{run:02d}.edf'
    )

    if os.path.exists(fname_local):
        raw_fname = fname_local
    else:
        # Fallback: attempt online download via MNE
        try:
            eegbci = mne.datasets.eegbci
            raw_fnames = eegbci.load_data(subject, [run])
            raw_fname = raw_fnames[0]
        except Exception as exc:
            raise FileNotFoundError(
                f"No se encontró el archivo local '{fname_local}' y la descarga falló: {exc}"
            ) from exc

    raw = mne.io.read_raw_edf(raw_fname, preload=True, verbose=False)
    raw.pick('eeg')
    # Normalise channel names for montage matching
    mne.datasets.eegbci.standardize(raw)
    montage = mne.channels.make_standard_montage('standard_1005')
    try:
        raw.set_montage(montage, on_missing='ignore')
    except Exception:
        pass
    signals = raw.get_data().T  # (n_times, n_channels)
    ch_names = raw.info['ch_names']
    try:
        pos_dict = raw.get_montage().get_positions()['ch_pos']
        positions = np.array([pos_dict[ch] if ch in pos_dict else np.zeros(3) for ch in ch_names])
    except Exception:
        montage2 = mne.channels.make_standard_montage('standard_1005')
        pos_dict = montage2.get_positions()['ch_pos']
        positions = np.array([pos_dict.get(ch, np.zeros(3)) for ch in ch_names])

    info = {
        'sfreq': raw.info['sfreq'],
        'ch_names': ch_names,
        'n_channels': len(ch_names),
        'subject': subject,
        'run': run,
        'source': 'real',
        'dataset': 'physionet_eegmmidb',
        'local_file': raw_fname,
    }
    return {'signals': signals, 'positions': positions, 'info': info}

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
BCI_IV_2A_PROXY_NOTE = (
    "BCI Competition IV Dataset 2a (.gdf) requires manual download from "
    "https://www.bbci.de/competition/iv/. "
    "Files not found in BCI_IV_2A_PATH. "
    "This dataset is formally declared as PROXY/NOT AVAILABLE for this run. "
    "Any results referencing bci_competition_iv_2a in this context are excluded "
    "from strong empirical claims."
)

def load_bci_competition_iv_2a(subject: int = 1) -> Dict[str, Any]:
    """
    Carga el dataset BCI Competition IV 2a para un sujeto.
    Retorna un diccionario con 'signals', 'positions', 'info'.
    NOTA: Requiere descarga manual desde https://www.bbci.de/competition/iv/
    Si los archivos no están presentes, lanza FileNotFoundError con instrucciones.
    """
    import mne
    import numpy as np
    import os
    data_dir = os.environ.get('BCI_IV_2A_PATH', './datasets/BCI_IV_2a/')
    fname = os.path.join(data_dir, f'A{subject:02d}T.gdf')
    if not os.path.exists(fname):
        raise FileNotFoundError(
            f"Archivo {fname} no encontrado. "
            f"Descargue el BCI Competition IV 2a dataset desde "
            f"https://www.bbci.de/competition/iv/ y defina BCI_IV_2A_PATH. "
            f"Nota proxy: {BCI_IV_2A_PROXY_NOTE}"
        )
    raw = mne.io.read_raw_gdf(fname, preload=True, verbose=False)
    raw.pick('eeg')
    signals = raw.get_data().T
    ch_names = raw.info['ch_names']
    try:
        montage = mne.channels.make_standard_montage('standard_1005')
        raw.set_montage(montage, on_missing='ignore')
        pos_dict = raw.get_montage().get_positions()['ch_pos']
    except Exception:
        montage = mne.channels.make_standard_montage('standard_1005')
        pos_dict = montage.get_positions()['ch_pos']
    positions = np.array([pos_dict.get(ch, np.zeros(3)) for ch in ch_names])
    info = {
        'sfreq': raw.info['sfreq'],
        'ch_names': ch_names,
        'n_channels': len(ch_names),
        'subject': subject,
        'source': 'real',
        'dataset': 'bci_competition_iv_2a',
    }
    return {'signals': signals, 'positions': positions, 'info': info}

# Ejemplo de función de preprocesamiento
def preprocess_signals(signals: np.ndarray) -> np.ndarray:
    """
    Aplica preprocesamiento estándar a las señales EEG (filtrado, normalización, etc).
    """
    # Implementar según necesidades
    return signals
