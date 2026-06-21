import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

OCI_AUDIT_FILE = (

    BASE_DIR /
    "agents" /
    "oracle-cloud" /
    "activity-tracker.json"

)

# --------------------------------
# LOAD OCI EVENTS
# --------------------------------

def load_oci_events():

    try:

        with open(

            OCI_AUDIT_FILE,
            "r",
            encoding="utf-8"

        ) as file:

            return json.load(file)

    except Exception:

        return []

# --------------------------------
# OCI USERS
# --------------------------------

def get_oci_users():

    events = load_oci_events()

    users = []

    for event in events:

        users.append({

            "provider": "OCI",

            "username":

                event.get(
                    "principalName",
                    "unknown"
                )

        })

    return users
