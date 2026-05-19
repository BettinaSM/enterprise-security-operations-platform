import yaml
from pathlib import Path

RULES_DIR = (
    Path(__file__)
    .resolve()
    .parent.parent.parent
    / "detections"
    / "rules"
)

def load_rules():

    rules = []

    for file in RULES_DIR.glob("*.yml"):

        with open(file, "r") as stream:

            rule = yaml.safe_load(stream)

            rules.append(rule)

    return rules

def run_yaml_detections(logs):

    detections = []

    rules = load_rules()

    for rule in rules:

        for log in logs:

            for pattern in rule["patterns"]:

                if pattern.lower() in log.lower():

                    detections.append({

                        "title": rule["title"],
                        "severity": rule["severity"],
                        "pattern": pattern,
                        "log": log,
                        "mitre": ", ".join(rule["mitre"])
                    })

    return detections
