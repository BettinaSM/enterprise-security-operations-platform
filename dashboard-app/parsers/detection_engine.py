import json

from pathlib import Path

# ---------------------------
# BASE PATHS
# ---------------------------

CURRENT_FILE = Path(__file__).resolve()

PARSERS_DIR = CURRENT_FILE.parent

DASHBOARD_DIR = PARSERS_DIR.parent

PROJECT_ROOT = DASHBOARD_DIR.parent

RULE_FILE = (
    PROJECT_ROOT
    / "rules"
    / "detection_rules.json"
)

# ---------------------------
# LOAD RULES
# ---------------------------

def load_rules():

    if not RULE_FILE.exists():

        return []

    with open(
        RULE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

# ---------------------------
# DETECTION ENGINE
# ---------------------------

def run_detections(logs):

    rules = load_rules()

    findings = []

    for log in logs:

        for rule in rules:

            keyword = rule.get(
                "keyword",
                ""
            )

            if keyword.lower() in log.lower():

                findings.append({
                    "rule": rule.get("name"),
                    "severity": rule.get("severity"),
                    "log": log
                })

    return findings
