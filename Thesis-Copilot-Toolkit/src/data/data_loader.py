"""
data_loader.py
Funciones generales para cargar y preprocesar datasets de EEG para el pipeline experimental.
"""

from typing import Tuple, Dict, Any, List

import numpy as np
import os

# Global preference: if True, pipeline will require real datasets and will
# not silently fall back to proxies. Set environment variable
# ALWAYS_USE_REAL_DATA=0 to allow proxies as fallback (not recommended).
ALWAYS_USE_REAL_DATA = os.environ.get("ALWAYS_USE_REAL_DATA", "1") not in ("0", "false", "False", "no", "NO")


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

    # Robust handling of missing_ratio: coerce to float, guard NaN/Inf and
    # accept either a fractional ratio (e.g., 0.2) or an absolute count (>1).
    try:
        mratio = float(missing_ratio)
    except Exception:
        mratio = 0.2

    if not np.isfinite(mratio) or mratio <= 0:
        mratio = 0.2

    if mratio >= 1 and mratio <= D:
        # treat as number of channels to remove
        n_missing = max(1, int(round(mratio)))
    else:
        n_missing = max(1, int(round(D * mratio)))

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
    try:
        raw = mne.io.read_raw_gdf(fname, preload=True, verbose=False)
    except OverflowError as exc:
        # Known issue: some GDF event-table encodings trigger an
        # "Python integer ... out of bounds for uint8" OverflowError
        # inside MNE's GDF parser. We surface a clearer message here
        # and point to the diagnostic/patch scripts included in the repo.
        raise RuntimeError(
            "MNE failed parsing GDF (OverflowError).\n"
            "This repository includes diagnostic scripts to inspect and patch MNE:\n"
            "  - experiments/inspect_gdf_header.py  (inspect header & try pyedflib)\n"
            "  - experiments/patch_mne_gdf_event_fix.py (in-memory patch for quick tests)\n"
            "  - experiments/patch_site_mne_gdf.py (apply persistent patch to site-packages)\n"
            "Recommended actions: ensure BCI_IV_2A_PATH points to the downloaded .gdf files,\n"
            "run the inspect script to confirm the file, then apply the in-repo patch if needed.\n"
            "Long-term: submit a targeted fix to the MNE project and revert local patches."
        ) from exc
    except Exception as exc:
        raise RuntimeError(f"Failed reading GDF file '{fname}': {exc}") from exc
    raw.pick('eeg')
    signals = raw.get_data().T
    
    # BCI IV 2A channels have prefixes "EEG-" and sometimes are just numbers.
    # We will rename known ones and assign a standard montage.
    ch_names = raw.info['ch_names']
    mapping = {}
    
    # Approx standard mapping for BCI IV 2A (22 channels)
    # Based on standard BCI IV 2a ELOC
    bci_standard = [
        "Fz", "FC3", "FC1", "FCz", "FC2", "FC4",
        "C5", "C3", "C1", "Cz", "C2", "C4", "C6",
        "CP3", "CP1", "CPz", "CP2", "CP4",
        "P1", "Pz", "P2", "POz"
    ]
    
    for i, ch in enumerate(ch_names):
        if i < len(bci_standard):
            mapping[ch] = bci_standard[i]
        else:
            mapping[ch] = ch.replace('EEG-', '')
            
    raw.rename_channels(mapping)
    ch_names = raw.info['ch_names']
    
    try:
        montage = mne.channels.make_standard_montage('standard_1005')
        raw.set_montage(montage, on_missing='ignore')
        pos_dict = raw.get_montage().get_positions()['ch_pos']
    except Exception:
        montage = mne.channels.make_standard_montage('standard_1005')
        pos_dict = montage.get_positions()['ch_pos']
        
    # Extract positions, replace missing with uniform generic random or zero to avoid NaN
    rng = np.random.default_rng(42)
    pos_list = []
    for ch in ch_names:
        p = pos_dict.get(ch, None)
        if p is None or np.any(np.isnan(p)):
            # fallback generic
            p = rng.normal(size=3)
            p = p / np.linalg.norm(p) * 0.09 # radius 9cm
        pos_list.append(p)
        
    positions = np.array(pos_list)
    info = {
        'sfreq': raw.info['sfreq'],
        'ch_names': ch_names,
        'n_channels': len(ch_names),
        'subject': subject,
        'source': 'real',
        'dataset': 'bci_competition_iv_2a',
    }
    return {'signals': signals, 'positions': positions, 'info': info}

def load_mne_sample_proxy(seed: int = 42) -> Dict[str, Any]:
    """
    Proxy para MNE Sample Dataset (auditory/visual EEG paradigm, 60 canales).
    Genera datos sintéticos con las mismas características estadísticas que el 
    dataset real MNE Sample: 60 canales EEG, 600 Hz, respuestas auditivas/visuales.
    NOTA: Proxy sintético — el dataset real requiere descarga via mne.datasets.sample.
    """
    import numpy as np
    rng = np.random.default_rng(seed=seed)

    n_channels = 60
    sfreq = 600.0
    duration = 30.0
    n_times = int(sfreq * duration)

    t = np.linspace(0, duration, n_times)
    signals = np.zeros((n_times, n_channels))

    for ch in range(n_channels):
        freqs = np.fft.rfftfreq(n_times, d=1/sfreq)
        freqs[0] = 1
        spectrum = rng.normal(0, 1, len(freqs)) / np.sqrt(freqs)
        background = np.fft.irfft(spectrum, n=n_times)

        alpha_freq = rng.uniform(9, 11)
        alpha_amp = rng.uniform(2, 6) * 1e-6

        aud_evoked = np.zeros(n_times)
        stim_times = np.arange(0.5, duration, 0.8)
        for st in stim_times:
            st_idx = int(st * sfreq)
            n1_idx = st_idx + int(0.1 * sfreq)
            p2_idx = st_idx + int(0.2 * sfreq)
            if n1_idx < n_times:
                aud_evoked[max(0, n1_idx-5):min(n_times, n1_idx+5)] -= rng.uniform(1, 3) * 1e-6
            if p2_idx < n_times:
                aud_evoked[max(0, p2_idx-5):min(n_times, p2_idx+5)] += rng.uniform(1, 3) * 1e-6

        signals[:, ch] = (background * 2e-7 +
                          alpha_amp * np.sin(2*np.pi*alpha_freq*t + rng.uniform(0, 2*np.pi)) +
                          aud_evoked)

    angles = np.linspace(0, 2*np.pi, n_channels, endpoint=False)
    elevations = np.linspace(-np.pi/3, np.pi/2, n_channels)
    r_head = 0.09
    positions = np.column_stack([
        r_head * np.cos(elevations) * np.cos(angles),
        r_head * np.cos(elevations) * np.sin(angles),
        r_head * np.sin(elevations)
    ])

    return {
        'signals': signals,
        'positions': positions,
        'info': {
            'sfreq': sfreq,
            'n_channels': n_channels,
            'duration': duration,
            'ch_names': [f'EEG{i+1:03d}' for i in range(n_channels)],
            'source': 'synthetic_proxy',
            'dataset': 'mne_sample_proxy',
            'note': 'Proxy sintético del MNE Sample Dataset. El real requiere mne.datasets.sample.data_path(download=True).'
        }
    }


def load_bci_competition_proxy(subject: int = 1, session: str = 'T') -> Dict[str, Any]:
    """
    Proxy para BCI Competition IV Dataset 2a (motor imagery EEG, 22 canales).
    Genera datos sintéticos con las mismas características que el dataset real:
    22 canales EEG, 250 Hz, motor imagery 4 clases (mano izq, mano der, pies, lengua).
    9 sujetos disponibles (subject=1-9), 2 sesiones (T=training, E=evaluation).
    NOTA: Proxy sintético — el dataset real requiere descarga manual desde
    https://www.bbci.de/competition/iv/
    """
    import numpy as np
    seed = subject * 17 + (0 if session == 'T' else 100)
    rng = np.random.default_rng(seed=seed)

    n_channels = 22
    sfreq = 250.0
    duration = 300.0
    n_times = int(sfreq * duration)

    t = np.linspace(0, duration, n_times)
    signals = np.zeros((n_times, n_channels))

    mu_amp = rng.uniform(5, 15) * 1e-6
    beta_amp = rng.uniform(3, 10) * 1e-6

    for ch in range(n_channels):
        freqs = np.fft.rfftfreq(n_times, d=1/sfreq)
        freqs[0] = 1
        spectrum = rng.normal(0, 1, len(freqs)) / np.sqrt(freqs)
        background = np.fft.irfft(spectrum, n=n_times)

        mu_freq = rng.uniform(9, 12)
        beta_freq = rng.uniform(18, 26)
        laterality = 1.0 if ch < 11 else -1.0
        class_label = rng.integers(0, 4)
        class_effect = laterality * [1, -1, 0.5, 0.3][class_label] * 0.5

        signals[:, ch] = (background * 3e-7 +
                          mu_amp * (1 - class_effect * 0.3) * np.sin(2*np.pi*mu_freq*t + rng.uniform(0, 2*np.pi)) +
                          beta_amp * 0.5 * np.sin(2*np.pi*beta_freq*t + rng.uniform(0, 2*np.pi)) +
                          rng.normal(0, 2e-6, n_times))

    bci2a_positions_2d = np.array([
        [-0.5, 0.8], [0, 0.8], [0.5, 0.8],
        [-0.75, 0.5], [-0.3, 0.5], [0, 0.5], [0.3, 0.5], [0.75, 0.5],
        [-1.0, 0], [-0.5, 0], [0, 0], [0.5, 0], [1.0, 0],
        [-0.75, -0.5], [-0.3, -0.5], [0, -0.5], [0.3, -0.5], [0.75, -0.5],
        [-0.5, -0.8], [0, -0.8], [0.5, -0.8], [0, -1.0],
    ])[:n_channels]

    r_head = 0.09
    norm = np.sqrt(bci2a_positions_2d[:, 0]**2 + bci2a_positions_2d[:, 1]**2).max()
    positions = np.column_stack([
        r_head * bci2a_positions_2d[:, 0] / norm,
        r_head * bci2a_positions_2d[:, 1] / norm,
        r_head * np.sqrt(np.maximum(0, 1 - (bci2a_positions_2d[:, 0]**2 + bci2a_positions_2d[:, 1]**2) / norm**2))
    ])

    ch_names = ['F3', 'Fz', 'F4', 'FC3', 'FC1', 'FCz', 'FC2', 'FC4',
                'C5', 'C3', 'Cz', 'C4', 'C6', 'CP3', 'CP1', 'CPz',
                'CP2', 'CP4', 'P3', 'Pz', 'P4', 'Oz'][:n_channels]

    return {
        'signals': signals,
        'positions': positions,
        'info': {
            'sfreq': sfreq,
            'n_channels': n_channels,
            'duration': duration,
            'ch_names': ch_names,
            'source': 'synthetic_proxy',
            'dataset': 'bci_competition_iv_2a_proxy',
            'subject': subject,
            'session': session,
            'note': 'Proxy sintético del BCI Competition IV 2a. El real requiere descarga manual desde https://www.bbci.de/competition/iv/'
        }
    }


# Ejemplo de función de preprocesamiento
def preprocess_signals(signals: np.ndarray) -> np.ndarray:
    """
    Aplica preprocesamiento estándar a las señales EEG (filtrado, normalización, etc).
    """
    # Implementar según necesidades
    return signals
