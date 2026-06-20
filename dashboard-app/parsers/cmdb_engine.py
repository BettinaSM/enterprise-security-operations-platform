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

    if not CMDB_FILE.exists():

        return []

    with open(
        CMDB_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

# --------------------------------
# GET ASSET
# --------------------------------

def get_asset(hostname):

    assets = load_cmdb()

    for asset in assets:

        if asset.get(
            "hostname"
        ) == hostname:

            return asset

    return {}

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
