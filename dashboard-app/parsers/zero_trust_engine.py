import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

POLICY_FILE = (

    BASE_DIR /
    "policies" /
    "zero_trust_policies.json"

)

# --------------------------------
# LOAD POLICIES
# --------------------------------

def load_zero_trust_policies():

    try:

        with open(
            POLICY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []

# --------------------------------
# ZERO TRUST SCORE
# --------------------------------

def calculate_zero_trust_score():

    policies = load_zero_trust_policies()

    enabled = len([

        p

        for p in policies

        if p.get(
            "enabled"
        )

    ])

    total = len(policies)

    if total == 0:

        return 0

    return round(
        (enabled / total) * 100,
        2
    )
