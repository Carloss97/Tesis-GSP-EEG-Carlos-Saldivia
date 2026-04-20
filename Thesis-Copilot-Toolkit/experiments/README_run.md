Run instructions for experiments

1) Activate the conda environment `eegrasp` (Windows PowerShell):

   (C:\Users\sarlo\anaconda3\shell\condabin\conda-hook.ps1) ; conda activate eegrasp

2) Generate the final schedule (if not already generated):

   python experiments/generate_it01_it50_final_schedule.py

3) Quick data availability check:

   python experiments/check_data_availability.py

4) Launch the full it01-it50 schedule (this will write artifacts under `Thesis-Copilot-Toolkit/results/`):

   python experiments/run_schedule_pilot.py --schedule experiments/schedules/it01-it50_schedule_final.json

5) To run in background on Windows PowerShell, use the provided `run_full_it01_it50.ps1` script.

Logs and QA reports will be stored in `Thesis-Copilot-Toolkit/results/`.
