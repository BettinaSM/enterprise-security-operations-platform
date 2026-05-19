import json

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

RULES_DIR = BASE_DIR / "rules"


def load_rules():

    with open(
        RULES_DIR / "detection_rules.json",
        "r"
    ) as file:

        return json.load(file)


def run_detections(logs):

    detections = []

    rules = load_rules()

    for log in logs:

        for rule in rules:

            keyword = rule["keyword"]

            if keyword.lower() in log.lower():

                detections.append({
                    "rule": rule["name"],
                    "severity": rule["severity"],
                    "log": log
                })

    return detections
