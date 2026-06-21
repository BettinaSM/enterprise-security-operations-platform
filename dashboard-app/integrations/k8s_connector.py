import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

K8S_AUDIT_FILE = (

    BASE_DIR /
    "agents" /
    "Kubernetes" /
    "kube-audit.json"

)

# --------------------------------
# LOAD K8S AUDIT
# --------------------------------

def load_k8s_events():

    try:

        with open(

            K8S_AUDIT_FILE,
            "r",
            encoding="utf-8"

        ) as file:

            return json.load(file)

    except Exception:

        return []

# --------------------------------
# K8S IDENTITIES
# --------------------------------

def get_k8s_users():

    events = load_k8s_events()

    users = []

    for event in events:

        users.append({

            "provider": "Kubernetes",

            "username":

                event.get(
                    "user",
                    "unknown"
                )

        })

    return users
