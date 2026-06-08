import hashlib
import json

from pathlib import Path
from datetime import datetime

# ---------------------------
# BASELINE DIRECTORY
# ---------------------------

BASELINE_DIR = (
    Path(__file__).resolve().parent.parent /
    "baseline"
)

BASELINE_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# ---------------------------
# HASH
# ---------------------------

def calculate_hash(content):

    if isinstance(content, (dict, list)):

        content = json.dumps(
            content,
            sort_keys=True
        )

    return hashlib.sha256(
        str(content).encode()
    ).hexdigest()

# ---------------------------
# SAVE BASELINE
# ---------------------------

def save_baseline(name, content):

    baseline_file = (
        BASELINE_DIR /
        f"{name}.json"
    )

    data = {

        "timestamp":
            datetime.utcnow().isoformat(),

        "hash":
            calculate_hash(content),

        "content":
            content
    }

    with open(
        baseline_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            default=str
        )

# ---------------------------
# SAVE SNAPSHOT
# ---------------------------

def save_baseline_snapshot(
    name,
    content
):

    timestamp = datetime.utcnow().strftime(
        "%Y%m%d_%H%M%S"
    )

    snapshot_file = (
        BASELINE_DIR /
        f"{name}_{timestamp}.json"
    )

    data = {

        "timestamp":
            datetime.utcnow().isoformat(),

        "hash":
            calculate_hash(content),

        "content":
            content
    }

    with open(
        snapshot_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            default=str
        )

# ---------------------------
# COMPARE BASELINE
# ---------------------------

def compare_baseline(
    name,
    content
):

    baseline_file = (
        BASELINE_DIR /
        f"{name}.json"
    )

    if not baseline_file.exists():

        return {

            "status":
                "NEW_BASELINE",

            "drift":
                False
        }

    with open(
        baseline_file,
        "r",
        encoding="utf-8"
    ) as file:

        baseline = json.load(file)

    current_hash = calculate_hash(
        content
    )

    drift = (
        current_hash !=
        baseline["hash"]
    )

    return {

        "status":
            "DRIFT_DETECTED"
            if drift
            else "UNCHANGED",

        "drift":
            drift,

        "baseline_hash":
            baseline["hash"],

        "current_hash":
            current_hash
    }
