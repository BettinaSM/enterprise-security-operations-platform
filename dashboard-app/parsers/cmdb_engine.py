import json

# ---------------------------
# LOAD CMDB
# ---------------------------

def load_cmdb():

    try:

        with open(
            "inventory/cmdb.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []

# ---------------------------
# SEARCH
# ---------------------------

def get_asset_relationships(hostname):

    cmdb = load_cmdb()

    return [

        item

        for item in cmdb

        if item.get(
            "hostname"
        ) == hostname

    ]
