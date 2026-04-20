# Run full it01-it50 schedule in conda `eegrasp` and tee output to a log file
$log = "Thesis-Copilot-Toolkit\results\it01-it50_run.log"
(C:\Users\sarlo\anaconda3\shell\condabin\conda-hook.ps1) ; conda activate eegrasp ; python experiments/generate_it01_it50_final_schedule.py ; python experiments/check_data_availability.py ; python experiments/run_schedule_pilot.py --schedule experiments/schedules/it01-it50_schedule_final.json --stop-on-error 2>&1 | Tee-Object -FilePath $log
