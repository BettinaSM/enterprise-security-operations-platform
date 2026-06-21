def prioritize(detection):

    severity = detection.get(
        "severity",
        "Low"
    )

    mapping = {

        "Critical": 1,

        "High": 2,

        "Medium": 3,

        "Low": 4

    }

    return mapping.get(
        severity,
        4
    )
