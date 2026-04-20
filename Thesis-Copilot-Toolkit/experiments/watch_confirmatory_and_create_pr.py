#!/usr/bin/env python3
"""
Watch confirmatory schedule results and open a PR when complete.
Usage (optional args):
  python watch_confirmatory_and_create_pr.py --schedule experiments/schedules/it01-it50_confirmatory_top_methods.json --branch experiment/final-proposal --base main

Behavior:
 - Polls `results/` for *_stats files for every iteration in the schedule
 - When all expected stats are present, runs `postprocess_and_select.py`
 - Commits local changes (if any), pushes, and tries to create a GitHub PR via `gh`
 - Falls back to printing manual PR instructions if `gh` is not available/authenticated

Be mindful: `gh` must be installed and authenticated for automatic PR creation.
"""

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEDULE = ROOT / "experiments" / "schedules" / "it01-it50_confirmatory_top_methods.json"
RESULTS = ROOT / "results"


def stats_exists_for_key(key: str) -> bool:
    # look for any file in RESULTS containing key and 'stats'
    for f in RESULTS.iterdir():
        if key in f.name and "stats" in f.name:
            return True
    return False


def run(cmd, check=False):
    print("$", " ".join(cmd))
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print(p.stdout)
    if check and p.returncode != 0:
        raise SystemExit(p.returncode)
    return p.returncode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--schedule", type=Path, default=DEFAULT_SCHEDULE)
    parser.add_argument("--branch", type=str, default="experiment/final-proposal")
    parser.add_argument("--base", type=str, default="main")
    parser.add_argument("--poll-interval", type=int, default=30)
    args = parser.parse_args()

    if not args.schedule.exists():
        print("Schedule not found:", args.schedule)
        raise SystemExit(2)

    sched = json.loads(args.schedule.read_text(encoding="utf-8"))
    keys = [it.get("key") for it in sched.get("iterations", []) if it.get("key")]
    if not keys:
        print("No iteration keys found in schedule")
        raise SystemExit(2)

    print(f"Watching for {len(keys)} iteration stats in {RESULTS}")

    # Wait until all keys have stats
    while True:
        missing = [k for k in keys if not stats_exists_for_key(k)]
        if not missing:
            print("All expected stats files present.")
            break
        print(f"{len(missing)} missing (checking again in {args.poll_interval}s). Examples: {missing[:6]}")
        time.sleep(args.poll_interval)

    # Run postprocess
    print("Running postprocess_and_select.py")
    run([sys.executable, str(ROOT / "experiments" / "postprocess_and_select.py")], check=True)

    # Commit any changes
    print("Checking git status")
    run(["git", "checkout", args.branch])
    status_rc = subprocess.run(["git", "status", "--porcelain"], stdout=subprocess.PIPE, text=True)
    if status_rc.stdout.strip():
        print("Local changes found, committing and pushing")
        run(["git", "add", "-A"], check=True)
        run(["git", "commit", "-m", "Auto: update FastICA max_iter + confirmatory results"], check=False)
        run(["git", "push"], check=True)
    else:
        print("No local changes to commit")

    # Try to create PR with gh
    print("Attempting to create PR with gh...")
    gh_ok = subprocess.run(["gh", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0
    title = "Auto: increase FastICA max_iter + confirmatory results"
    body = "Automated PR: changes include FastICA max_iter increase and confirmatory run artifacts. Reviewers: TBD."

    if gh_ok:
        rc = run(["gh", "pr", "create", "--base", args.base, "--head", args.branch, "--title", title, "--body", body])
        if rc == 0:
            print("PR created with gh")
        else:
            print("gh returned non-zero exit code when creating PR")
    else:
        print("`gh` CLI not available or not authenticated. Manual PR instructions below:")
        p = subprocess.run(["git", "config", "--get", "remote.origin.url"], stdout=subprocess.PIPE, text=True)
        remote = p.stdout.strip()
        print("Remote origin:", remote)
        # build a web URL if possible
        if remote.startswith("git@github.com:"):
            repo = remote[len("git@github.com:"):-4]
            print(f"Open: https://github.com/{repo}/pull/new/{args.branch}")
        elif remote.startswith("https://github.com/"):
            repo = remote[len("https://github.com/"):-4]
            print(f"Open: https://github.com/{repo}/pull/new/{args.branch}")
        else:
            print("Create a PR from branch", args.branch, "to", args.base)

    print("Watcher finished.")

if __name__ == '__main__':
    main()
