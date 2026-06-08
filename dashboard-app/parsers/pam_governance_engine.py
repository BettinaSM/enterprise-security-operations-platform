from parsers.iam_engine import (
    get_sudo_users
)

# ---------------------------
# PAM FINDINGS
# ---------------------------

def get_privileged_accounts():

    findings = []

    sudo_entries = get_sudo_users()

    for entry in sudo_entries:

        findings.append({

            "account": entry,
            "source": "sudoers",
            "risk": "High"

        })

    return findings
