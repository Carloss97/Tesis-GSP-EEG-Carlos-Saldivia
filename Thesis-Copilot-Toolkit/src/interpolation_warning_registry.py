"""Centralized in-memory registry for interpolation warning classification."""

from __future__ import annotations

from collections import defaultdict
from threading import Lock
from typing import Any, Dict, List


_LOCK = Lock()
_RECORDS: List[Dict[str, Any]] = []


def clear_registry() -> None:
    with _LOCK:
        _RECORDS.clear()


def record_warning(
    method: str,
    warning_code: str,
    message: str,
    severity: str,
    decision: str,
    context: Dict[str, Any] | None = None,
) -> None:
    with _LOCK:
        _RECORDS.append(
            {
                "method": str(method),
                "warning_code": str(warning_code),
                "message": str(message),
                "severity": str(severity),
                "decision": str(decision),
                "context": context or {},
            }
        )


def summarize_registry(reset: bool = False) -> List[Dict[str, Any]]:
    with _LOCK:
        records = list(_RECORDS)
        if reset:
            _RECORDS.clear()

    grouped: Dict[tuple[str, str, str, str], Dict[str, Any]] = defaultdict(dict)
    for rec in records:
        key = (
            rec["method"],
            rec["warning_code"],
            rec["severity"],
            rec["decision"],
        )
        if not grouped[key]:
            grouped[key] = {
                "method": rec["method"],
                "warning_code": rec["warning_code"],
                "severity": rec["severity"],
                "decision": rec["decision"],
                "count": 0,
                "sample_message": rec["message"],
            }
        grouped[key]["count"] += 1

    return sorted(grouped.values(), key=lambda x: (x["method"], x["warning_code"], x["decision"]))
