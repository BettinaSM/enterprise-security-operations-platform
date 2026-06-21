from parsers.cmdb_engine import (
    load_cmdb
)

# --------------------------------
# EXTERNAL EXPOSURE
# --------------------------------

def find_exposed_assets():

    assets = load_cmdb()

    findings = []

    for asset in assets:

        if asset.get(

            "internet_exposed",

            False

        ):

            findings.append({

                "hostname":

                    asset.get(
                        "hostname"
                    ),

                "ip":

                    asset.get(
                        "ip"
                    ),

                "criticality":

                    asset.get(
                        "criticality"
                    ),

                "owner":

                    asset.get(
                        "owner"
                    ),

                "risk":

                    "High"

            })

    return findings
