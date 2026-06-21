from parsers.cmdb_engine import (
    load_cmdb
)

from parsers.asset_risk_engine import (
    enterprise_asset_risk
)

from parsers.vulnerability_engine import (
    enrich_vulnerabilities
)

# --------------------------------
# CTEM ANALYSIS
# --------------------------------

def run_ctem_analysis():

    assets = load_cmdb()

    vulnerabilities = enrich_vulnerabilities()

    asset_risks = {

        asset["hostname"]: asset

        for asset in enterprise_asset_risk()
    }

    results = []

    for asset in assets:

        hostname = asset.get(
            "hostname"
        )

        vuln_count = len([

            vuln

            for vuln in vulnerabilities

            if vuln.get(
                "hostname"
            ) == hostname

        ])

        critical_vulns = len([

            vuln

            for vuln in vulnerabilities

            if (

                vuln.get(
                    "hostname"
                ) == hostname

                and

                vuln.get(
                    "severity"
                ) == "Critical"

            )

        ])

        risk = asset_risks.get(
            hostname,
            {}
        )

        exposure = (

            risk.get(
                "score",
                0
            )

            +

            (critical_vulns * 15)

        )

        if exposure > 100:

            exposure = 100

        results.append({

            "hostname": hostname,

            "criticality": asset.get(
                "criticality"
            ),

            "internet_facing": asset.get(
                "internet_facing"
            ),

            "vulnerabilities": vuln_count,

            "critical_vulnerabilities": critical_vulns,

            "exposure_score": exposure

        })

    return sorted(

        results,

        key=lambda x: x["exposure_score"],

        reverse=True
    )
