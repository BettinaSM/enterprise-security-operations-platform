from parsers.asset_risk_engine import (
    enterprise_asset_risk
)

from parsers.identity_governance import (
    run_identity_governance
)

from parsers.vulnerability_engine import (
    critical_vulnerabilities
)


def calculate_posture():

    posture = 100

    critical_assets = [

        asset

        for asset in enterprise_asset_risk()

        if asset["risk"] == "Critical"

    ]

    posture -= (

        len(critical_assets) * 5

    )

    critical_vulns = critical_vulnerabilities()

    posture -= (

        len(critical_vulns) * 3

    )

    identities = run_identity_governance()

    dormant = len(

        identities.get(

            "dormant_accounts",

            []

        )

    )

    posture -= dormant

    if posture < 0:

        posture = 0

    return {

        "score": posture,

        "critical_assets":

            len(critical_assets),

        "critical_vulnerabilities":

            len(critical_vulns),

        "dormant_accounts":

            dormant

    }
