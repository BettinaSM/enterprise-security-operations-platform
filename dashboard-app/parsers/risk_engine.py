def calculate_risk(event):

    score = 0

    severity = event.get("severity", "")

    if severity == "Critical":
        score += 50

    elif severity == "High":
        score += 30

    elif severity == "Medium":
        score += 15

    source = event.get("source", "").lower()

    if "azure" in source:
        score += 10

    if "aws" in source:
        score += 10

    if "falco" in source:
        score += 20

    if "privilege" in event.get("event", "").lower():
        score += 25

    return score
