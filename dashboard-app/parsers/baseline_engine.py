import hashlib
import json

from pathlib import Path

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

def calculate_hash(
    content
):

    return hashlib.sha256(
        content.encode()
    ).hexdigest()

# ---------------------------
# SAVE BASELINE
# ---------------------------

def save_baseline(
    name,
    content
):

    baseline_file = (
        BASELINE_DIR /
        f"{name}.json"
    )

    data = {

        "hash": calculate_hash(content),
        "content": content
    }

    with open(
        baseline_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
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
            "status": "NEW_BASELINE"
        }

    with open(
        baseline_file,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    current_hash = calculate_hash(
        content
    )

    if current_hash != data["hash"]:

        return {
            "status": "DRIFT_DETECTED"
        }

    return {
        "status": "UNCHANGED"
    }
