import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

RULE_FILE = (
    BASE_DIR
    / "rules"
    / "detection_rules.json"
)

def load_rules():

    with open(
        RULE_FILE,
        "r"
    ) as file:

        return json.load(file)

def run_detections(logs):

    rules = load_rules()

    findings = []

    for log in logs:

        for rule in rules:

            keyword = rule.get("keyword")

            if keyword.lower() in log.lower():

                findings.append({
                    "rule": rule.get("name"),
                    "severity": rule.get("severity"),
                    "log": log
                })

    return findings
