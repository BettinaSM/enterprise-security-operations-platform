from parsers.asset_risk_engine import (
    enterprise_asset_risk
)

# ---------------------------
# ENTERPRISE RISK
# ---------------------------

def enterprise_risk_register():

    risks = []

    for asset in enterprise_asset_risk():

        risks.append({

            "asset":

                asset["hostname"],

            "risk":

                asset["risk"],

            "score":

                asset["score"]

        })

    return risks
