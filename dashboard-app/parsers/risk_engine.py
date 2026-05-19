def calculate_risk_score(detections):

    score = 0

    for detection in detections:

        severity = detection.get(
            "severity",
            "Low"
        )

        if severity == "Critical":

            score += 40

        elif severity == "High":

            score += 25

        elif severity == "Medium":

            score += 10

        else:

            score += 5

    if score >= 80:

        level = "Critical"

    elif score >= 50:

        level = "High"

    elif score >= 20:

        level = "Medium"

    else:

        level = "Low"

    return score, level
