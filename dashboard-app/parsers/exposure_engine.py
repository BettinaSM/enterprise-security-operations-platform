from parsers.cmdb_engine import (
    load_cmdb
)

from parsers.vulnerability_engine import (
    enrich_vulnerabilities
)

# --------------------------------
# EXPOSURE
# --------------------------------

def calculate_exposure():

    exposure = []

    assets = load_cmdb()

    vulns = enrich_vulnerabilities()

    for asset in assets:

        hostname = asset.get(
            "hostname"
        )

        asset_vulns = [

            vuln

            for vuln in vulns

            if vuln["hostname"] == hostname

        ]

        exposure.append({

            "hostname": hostname,

            "criticality": asset.get(
                "criticality"
            ),

            "vulnerabilities": len(
                asset_vulns
            ),

            "internet_facing":

                asset.get(
                    "internet_facing"
                )

        })

    return exposure
