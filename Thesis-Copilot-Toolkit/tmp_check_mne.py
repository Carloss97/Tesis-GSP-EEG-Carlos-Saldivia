import sys
try:
    import mne
except Exception as e:
    print('MNE_IMPORT_FAIL:', e)
    sys.exit(2)
try:
    p = mne.datasets.sample.data_path(download=False)
    print('MNE_INSTALLED: True')
    print('DATA_PATH:' + str(p))
    sys.exit(0)
except Exception as e:
    print('DATA_NOT_PRESENT:', e)
    try:
        print('Attempting download (may take several minutes)...')
        p = mne.datasets.sample.data_path(download=True)
        print('DOWNLOADED:' + str(p))
        sys.exit(0)
    except Exception as e2:
        print('DOWNLOAD_FAILED:', e2)
        sys.exit(3)
