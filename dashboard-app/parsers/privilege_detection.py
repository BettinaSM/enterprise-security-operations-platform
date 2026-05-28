CRITICAL_PATTERNS = [

    "ALL=(ALL)",
    "NOPASSWD",
    "wheel",
    "root"
]

# ---------------------------
# DETECT PRIVILEGE RISK
# ---------------------------

def detect_privilege_escalation(
    logs
):

    findings = []

    for log in logs:

        for pattern in CRITICAL_PATTERNS:

            if pattern.lower() in log.lower():

                findings.append({

                    "severity": "Critical",
                    "pattern": pattern,
                    "log": log
                })

    return findings
