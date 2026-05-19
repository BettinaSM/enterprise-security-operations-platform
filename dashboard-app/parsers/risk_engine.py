def calculate_risk_score(detections):

    score = 0

    for detection in detections:

        severity = detection["severity"]

        if severity == "Critical":
            score += 40

        elif severity == "High":
            score += 25

        elif severity == "Medium":
            score += 10

    if score >= 100:
        return score, "Critical"

    elif score >= 60:
        return score, "High"

    elif score >= 30:
        return score, "Medium"

    return score, "Low"
