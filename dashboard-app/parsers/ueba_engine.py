def analyze_user_behavior(logs):

    findings = []

    suspicious_keywords = [
        "root",
        "sudo",
        "failed",
        "unauthorized",
        "admin"
    ]

    for log in logs:

        for keyword in suspicious_keywords:

            if keyword.lower() in log.lower():

                findings.append({
                    "user_behavior": "Suspicious Activity",
                    "keyword": keyword,
                    "log": log,
                    "risk": "High"
                })

    return findings
