import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DNS_FILE = (

    BASE_DIR /
    "attack-surface" /
    "domains.json"

)

# --------------------------------
# DOMAINS
# --------------------------------

def load_domains():

    try:

        with open(
            DNS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []
