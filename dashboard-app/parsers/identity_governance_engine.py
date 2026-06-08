from parsers.iam_engine import (
    get_local_users,
    get_groups,
    get_sudo_users
)

from parsers.identity_risk_engine import (
    calculate_identity_risk
)

# ---------------------------
# GOVERNANCE ANALYSIS
# ---------------------------

def analyze_identity_governance():

    users = get_local_users()

    sudo_users = get_sudo_users()

    findings = []

    for user in users:

        username = user.get(
            "username"
        )

        privileged = False

        for entry in sudo_users:

            if username in str(entry):

                privileged = True

                break

        risk = calculate_identity_risk({

            "privileged": privileged,

            "sudo": privileged,

            "failed_logins": 0,

            "mfa_enabled": False

        })

        findings.append({

            "username": username,

            "privileged": privileged,

            "risk_score": risk["score"],

            "risk_level": risk["level"]

        })

    return findings
