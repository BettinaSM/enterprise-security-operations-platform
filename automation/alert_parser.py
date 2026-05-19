def parse_alert(alert):

    severity_map = {
        "Warning": "Medium",
        "Critical": "High"
    }

    for key in severity_map:
        if key in alert:
            return severity_map[key]

    return "Low"


sample_alert = "Critical Privileged container execution detected"

print(parse_alert(sample_alert))
