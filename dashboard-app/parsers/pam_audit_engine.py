# ---------------------------
# PRIVILEGED ACCESS AUDIT
# ---------------------------

from parsers.iam_engine import (

    get_sudo_users,
    get_groups

)

# ---------------------------
# DISCOVER PRIVILEGED
# ---------------------------

def discover_privileged_access():

    findings = []

    # ---------------------------
    # SUDO
    # ---------------------------

    for entry in get_sudo_users():

        findings.append({

            "platform": "Linux/AIX",
            "type": "SUDO",
            "entry": entry

        })

    # ---------------------------
    # GROUPS
    # ---------------------------

    privileged_groups = [

        "sudo",
        "wheel",
        "root",
        "adm",
        "system"

    ]

    for group in get_groups():

        if group.get(

            "group"

        ) in privileged_groups:

            findings.append({

                "platform": "Unix",
                "type": "PRIVILEGED_GROUP",
                "group": group["group"],
                "members": group["members"]

            })

    return findings

# ---------------------------
# RISK SUMMARY
# ---------------------------

def privileged_summary():

    findings = discover_privileged_access()

    return {

        "total_privileged_findings": len(findings),

        "risk": (

            "Critical"

            if len(findings) > 10

            else "Medium"

        )

    }
