from parsers.cmdb_engine import (
    load_cmdb
)

# ---------------------------
# EXTERNAL EXPOSURE
# ---------------------------

def external_assets():

    assets = load_cmdb()

    return [

        asset

        for asset in assets

        if asset.get(
            "internet_facing",
            False
        )

    ]

# ---------------------------
# SHADOW IT
# ---------------------------

def detect_shadow_it():

    assets = load_cmdb()

    return [

        asset

        for asset in assets

        if asset.get(
            "owner"
        ) in [

            None,
            "",
            "unknown"

        ]
    ]

# ---------------------------
# SUMMARY
# ---------------------------

def attack_surface_summary():

    exposed = external_assets()

    shadow = detect_shadow_it()

    return {

        "external":

            len(exposed),

        "shadow":

            len(shadow)

    }
