from parsers.cmdb_engine import (
    load_cmdb
)

# --------------------------------
# ASSET RISK
# --------------------------------

def calculate_asset_risk(asset):

    score = 0

    if asset.get(
        "criticality"
    ) == "Critical":

        score += 40

    elif asset.get(
        "criticality"
    ) == "High":

        score += 25

    if asset.get(
        "internet_facing",
        False
    ):

        score += 30

    if asset.get(
        "environment"
    ) == "production":

        score += 20

    if asset.get(
        "os"
    ) in [

        "Windows Server 2008",
        "RHEL 6",
        "AIX 6.1"

    ]:

        score += 20

    if score > 100:

        score = 100

    return {

        "hostname": asset.get(
            "hostname"
        ),

        "score": score,

        "risk": classify(score)
    }

# --------------------------------
# CLASSIFICATION
# --------------------------------

def classify(score):

    if score >= 80:

        return "Critical"

    elif score >= 60:

        return "High"

    elif score >= 30:

        return "Medium"

    return "Low"

# --------------------------------
# ENTERPRISE RISK
# --------------------------------

def enterprise_asset_risk():

    assets = load_cmdb()

    return [

        calculate_asset_risk(asset)

        for asset in assets

    ]
