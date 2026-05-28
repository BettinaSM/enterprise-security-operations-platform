# ---------------------------
# DETECT LATERAL MOVEMENT
# ---------------------------

def detect_lateral_movement(
    logs
):

    findings = []

    keywords = [

        "psexec",
        "wmic",
        "ssh",
        "scp",
        "winrm"
    ]

    for log in logs:

        for keyword in keywords:

            if keyword.lower() in log.lower():

                findings.append({

                    "technique": keyword,
                    "severity": "High",
                    "log": log
                })

    return findings
