def analyze_user_behavior(events):

    findings = []

    failed_logins = 0

    privileged_actions = 0

    suspicious_commands = 0

    for event in events:

        log = event.lower()

        # ---------------------------
        # FAILED AUTHENTICATIONS
        # ---------------------------

        if "failed" in log:

            failed_logins += 1

        # ---------------------------
        # PRIVILEGED ACTIONS
        # ---------------------------

        if (
            "sudo" in log
            or "root" in log
            or "admin" in log
        ):

            privileged_actions += 1

        # ---------------------------
        # SUSPICIOUS COMMANDS
        # ---------------------------

        if (
            "curl" in log
            or "wget" in log
            or "nc " in log
            or "nmap" in log
        ):

            suspicious_commands += 1

    # ---------------------------
    # UEBA LOGIC
    # ---------------------------

    if failed_logins >= 5:

        findings.append({
            "type": "Brute Force Behavior",
            "severity": "High"
        })

    if privileged_actions >= 3:

        findings.append({
            "type": "Suspicious Admin Activity",
            "severity": "Critical"
        })

    if suspicious_commands >= 2:

        findings.append({
            "type": "Potential Insider Threat",
            "severity": "Critical"
        })

    if not findings:

        findings.append({
            "type": "Normal User Behavior",
            "severity": "Low"
        })

    return findings

    # ---------------------------
    # Suspicious Log
    # ---------------------------

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
