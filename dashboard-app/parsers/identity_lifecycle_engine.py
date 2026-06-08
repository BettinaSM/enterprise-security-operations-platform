from parsers.iam_engine import (
    get_local_users
)

# ---------------------------
# DORMANT ACCOUNTS
# ---------------------------

def find_dormant_accounts():

    findings = []

    for user in get_local_users():

        findings.append({

            "username":
                user["username"],

            "status":
                "Dormant"

        })

    return findings

# ---------------------------
# ORPHAN ACCOUNTS
# ---------------------------

def find_orphan_accounts():

    findings = []

    for user in get_local_users():

        if user.get(
            "manager"
        ) is None:

            findings.append({

                "username":
                    user["username"],

                "risk":
                    "Orphan Account"

            })

    return findings

# ---------------------------
# NO MFA
# ---------------------------

def find_no_mfa_accounts():

    findings = []

    for user in get_local_users():

        findings.append({

            "username":
                user["username"],

            "mfa":
                False

        })

    return findings
