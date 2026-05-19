import json


def load_rules():

    with open(
        "rules/detection_rules.json",
        "r"
    ) as file:

        return json.load(file)


def run_detections(events):

    rules = load_rules()

    detections = []

    for event in events:

        event_str = str(event).lower()

        for rule in rules:

            if rule["keyword"] in event_str:

                detections.append({
                    "rule": rule["name"],
                    "severity": rule["severity"],
                    "mitre": rule["mitre"],
                    "event": event
                })

    return detections
