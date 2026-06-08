import json

# ---------------------------
# INVENTORY
# ---------------------------

def load_inventory():

    try:

        with open(
            "inventory/assets.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []

# ---------------------------
# SEARCH HOST
# ---------------------------

def get_asset(hostname):

    inventory = load_inventory()

    for asset in inventory:

        if asset.get(
            "hostname"
        ) == hostname:

            return asset

    return None

# ---------------------------
# FILTER BY OS
# ---------------------------

def get_assets_by_os(os_type):

    inventory = load_inventory()

    return [

        asset

        for asset in inventory

        if asset.get(
            "os",
            ""
        ).lower() == os_type.lower()

    ]
