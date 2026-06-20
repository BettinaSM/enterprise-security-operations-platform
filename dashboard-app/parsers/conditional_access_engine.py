# --------------------------------
# CONDITIONAL ACCESS
# --------------------------------

def evaluate_access(identity):

    decision = "Allow"

    reasons = []

    if not identity.get(
        "mfa_enabled",
        False
    ):

        decision = "Deny"

        reasons.append(
            "MFA not enabled"
        )

    if identity.get(
        "dormant",
        False
    ):

        decision = "Deny"

        reasons.append(
            "Dormant account"
        )

    if identity.get(
        "risk_score",
        0
    ) >= 80:

        decision = "Deny"

        reasons.append(
            "High identity risk"
        )

    return {

        "user":
            identity.get(
                "username"
            ),

        "decision":
            decision,

        "reasons":
            reasons

    }
