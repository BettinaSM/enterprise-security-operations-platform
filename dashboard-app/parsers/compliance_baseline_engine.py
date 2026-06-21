# ---------------------------
# CIS BASELINE CHECKS
# ---------------------------

def evaluate_baseline(data):

    findings = []

    # ---------------------------
    # ROOT LOGIN
    # ---------------------------

    if data.get(
        "permit_root_login",
        True
    ):

        findings.append({

            "control":
                "SSH Root Login",

            "framework":
                "CIS",

            "severity":
                "High",

            "status":
                "Fail"

        })

    # ---------------------------
    # PASSWORD AUTH
    # ---------------------------

    if data.get(
        "password_authentication",
        True
    ):

        findings.append({

            "control":
                "Password Authentication",

            "framework":
                "CIS",

            "severity":
                "Medium",

            "status":
                "Fail"

        })

    # ---------------------------
    # MFA
    # ---------------------------

    if not data.get(
        "mfa_enabled",
        False
    ):

        findings.append({

            "control":
                "MFA",

            "framework":
                "NIST",

            "severity":
                "High",

            "status":
                "Fail"

        })

    # ---------------------------
    # DORMANT USERS
    # ---------------------------

    if data.get(
        "dormant_accounts",
        0
    ) > 0:

        findings.append({

            "control":
                "Dormant Accounts",

            "framework":
                "ISO27001",

            "severity":
                "Medium",

            "status":
                "Fail"

        })

    return findings

# --------------------------------
# COMPLIANCE SCORE
# --------------------------------

def calculate_compliance_score(

    findings

):

    if not findings:

        return 100

    compliant = len([

        finding

        for finding in findings

        if finding.get(

            "status"

        ) == "Compliant"

    ])

    return round(

        (compliant / len(findings)) * 100,

        2

    )
