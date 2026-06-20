from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent

CMDB_FILE = (
    BASE_DIR /
    "inventory" /
    "cmdb.json"
)

# ---------------------------
# LOAD CMDB
# ---------------------------

def load_cmdb():

    try:

        with open(
            CMDB_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []

# --------------------------------
# SEARCH ASSET
# --------------------------------

def search_asset(keyword):

    keyword = keyword.lower()

    assets = load_cmdb()

    results = []

    for asset in assets:

        values = str(asset).lower()

        if keyword in values:

            results.append(asset)

    return results

# --------------------------------
# GET ASSET BY HOSTNAME
# --------------------------------

def get_asset_by_hostname(hostname):

    for asset in load_cmdb():

        if asset["hostname"] == hostname:

            return asset

    return None

# --------------------------------
# GET ASSET BY CRITICALITY
# --------------------------------

def get_assets_by_criticality(level):

    return [

        asset

        for asset in load_cmdb()

        if asset.get(
            "criticality"
        ) == level
    ]


def count_assets():

    return len(load_cmdb())

# --------------------------------
# GET CRITICAL ASSETS
# --------------------------------

def get_critical_assets():

    return [

        asset

        for asset in load_cmdb()

        if asset.get(
            "criticality"
        ) == "Critical"

    ]

# --------------------------------
# GET INTERNET FACING
# --------------------------------

def get_internet_facing_assets():

    return [

        asset

        for asset in load_cmdb()

        if asset.get(
            "internet_facing",
            False
        )

    ]

# --------------------------------
# GET BY OWNER
# --------------------------------

def get_asset_owners():

    owners = set()

    for asset in load_cmdb():

        owner = asset.get(
            "owner"
        )

        if owner:

            owners.add(owner)

    return list(owners)

# --------------------------------
# FILTER
# --------------------------------

def filter_assets(
    environment=None,
    operating_system=None,
    owner=None
):

    assets = load_cmdb()

    results = []

    for asset in assets:

        if environment:

            if asset.get(
                "environment"
            ) != environment:

                continue

        if operating_system:

            if asset.get(
                "os"
            ) != operating_system:

                continue

        if owner:

            if asset.get(
                "owner"
            ) != owner:

                continue

        results.append(
            asset
        )

    return results
