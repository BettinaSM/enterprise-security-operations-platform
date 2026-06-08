from parsers.identity_risk_engine import (
    calculate_identity_risk
)

def analyze_identities(users):

    results = []

    for user in users:

        risk = calculate_identity_risk(user)

        results.append({

            "username":
                user.get(
                    "username"
                ),

            "risk":
                risk["level"],

            "score":
                risk["score"]

        })

    return results
