import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

IBM_ACTIVITY_FILE = (

    BASE_DIR /
    "agents" /
    "ibm-cloud" /
    "activity-tracker.json"

)

# --------------------------------
# LOAD IBM CLOUD EVENTS
# --------------------------------

def load_ibm_cloud_events():

    try:

        with open(

            IBM_ACTIVITY_FILE,
            "r",
            encoding="utf-8"

        ) as file:

            return json.load(file)

    except Exception:

        return []

# --------------------------------
# IBM IAM USERS
# --------------------------------

def get_ibm_iam_users():

    events = load_ibm_cloud_events()

    users = []

    for event in events:

        user = event.get(
            "user",
            "unknown"
        )

        users.append({

            "provider": "IBM Cloud",
            "username": user

        })

    return users
