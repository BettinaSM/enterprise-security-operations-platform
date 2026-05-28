from collections import Counter

# ---------------------------
# UEBA ENGINE
# ---------------------------

SUSPICIOUS_COMMANDS = [

    "curl",
    "wget",
    "nc ",
    "nmap",
    "scp",
    "psexec",
    "wmic"
]

PRIVILEGED_KEYWORDS = [

    "sudo",
    "root",
    "admin",
    "wheel"
]

# ---------------------------
# ANALYZE USER BEHAVIOR
# ---------------------------

def analyze_user_behavior(
    events
):

    findings = []

    failed_logins = 0

    privileged_actions = 0

    suspicious_commands = 0

    user_activity = []

    # ---------------------------
    # PROCESS EVENTS
    # ---------------------------

    for event in events:

        log = str(event).lower()

        # failed auth

        if (

            "failed" in log
            or "authentication failure" in log

        ):

            failed_logins += 1

        # privileged actions

        for keyword in PRIVILEGED_KEYWORDS:

            if keyword in log:

                privileged_actions += 1

        # suspicious commands

        for command in SUSPICIOUS_COMMANDS:

            if command in log:

                suspicious_commands += 1

        # track users

        words = log.split()

        for word in words:

            if "user" in word:

                user_activity.append(word)

    # ---------------------------
    # USER FREQUENCY
    # ---------------------------

    counter = Counter(
        user_activity
    )

    anomalous_users = []

    for user, count in counter.items():

        if count > 10:

            anomalous_users.append({

                "user": user,
                "count": count
            })

    # ---------------------------
    # UEBA RULES
    # ---------------------------

    if failed_logins >= 5:

        findings.append({

            "type": "Brute Force Behavior",
            "severity": "High"
        })

    if privileged_actions >= 3:

        findings.append({

            "type": "Suspicious Privileged Activity",
            "severity": "Critical"
        })

    if suspicious_commands >= 2:

        findings.append({

            "type": "Potential Lateral Movement",
            "severity": "Critical"
        })

    if anomalous_users:

        findings.append({

            "type": "Anomalous User Activity",
            "severity": "High",
            "users": anomalous_users
        })

    # ---------------------------
    # NORMAL
    # ---------------------------

    if not findings:

        findings.append({

            "type": "Normal Behavior",
            "severity": "Low"
        })

    return findings
