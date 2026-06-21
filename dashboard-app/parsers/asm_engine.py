import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ASM_FILE = (

    BASE_DIR /
    "attack-surface" /
    "external_assets.json"

)

# --------------------------------
# LOAD ASM
# --------------------------------

def load_external_assets():

    try:

        with open(
            ASM_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []

# --------------------------------
# INTERNET FACING
# --------------------------------

def get_internet_facing_assets():

    return [

        asset

        for asset in load_external_assets()

        if asset.get(
            "internet_facing"
        )

    ]
