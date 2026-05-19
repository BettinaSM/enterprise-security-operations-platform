def detect_suspicious_user_activity(logs):

    suspicious = []

    for log in logs:

        log_lower = log.lower()

        if "root" in log_lower:
            suspicious.append({
                "user": "root",
                "reason": "Privileged account activity"
            })

        if "failed password" in log_lower:
            suspicious.append({
                "user": "unknown",
                "reason": "Multiple failed authentications"
            })

    return suspicious
