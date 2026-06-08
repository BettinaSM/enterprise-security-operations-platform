from datetime import datetime

# ---------------------------
# IDENTITY RISK SCORE
# ---------------------------

def calculate_identity_risk(identity):

    score = 0

    # ---------------------------
    # PRIVILEGED
    # ---------------------------

    if identity.get(
        "privileged",
        False
    ):

        score += 40

    # ---------------------------
    # SUDO
    # ---------------------------

    if identity.get(
        "sudo",
        False
    ):

        score += 25

    # ---------------------------
    # FAILED LOGINS
    # ---------------------------

    failed_logins = identity.get(
        "failed_logins",
        0
    )

    score += min(
        failed_logins * 2,
        20
    )

    # ---------------------------
    # DORMANT
    # ---------------------------

    if identity.get(
        "dormant",
        False
    ):

        score += 15

    # ---------------------------
    # SERVICE ACCOUNT
    # ---------------------------

    if identity.get(
        "service_account",
        False
    ):

        score += 10

    # ---------------------------
    # MFA
    # ---------------------------

    if identity.get(
        "mfa_disabled",
        False
    ):

        score += 30

    # ---------------------------
    # SHARED ACCOUNT
    # ---------------------------

    if identity.get(
        "shared_account",
        False
    ):

        score += 25

    # ---------------------------
    # ORPHAN ACCOUNT
    # ---------------------------

    if identity.get(
        "orphan_account",
        False
    ):

        score += 35

    # ---------------------------
    # EXCESSIVE PRIVILEGES
    # ---------------------------

    if identity.get(
        "excessive_privileges",
        False
    ):

        score += 40
    
    # ---------------------------
    # RISK LEVEL
    # ---------------------------

    if score >= 80:

        level = "Critical"

    elif score >= 60:

        level = "High"

    elif score >= 30:

        level = "Medium"

    else:

        level = "Low"

    return {

        "score": score,
        "level": level

    }
