import json

from pathlib import Path

from datetime import datetime

AUDIT_FILE = (
    Path(__file__).resolve().parent.parent /
    "audit" /
    "audit_trail.json"
)

AUDIT_FILE.parent.mkdir(
    exist_ok=True
)

if not AUDIT_FILE.exists():

    with open(
        AUDIT_FILE,
        "w"
    ) as file:

        json.dump([], file)


def register_action(

    username,
    action,
    source="SOC Platform"

):

    entry = {

        "timestamp":
            datetime.utcnow().isoformat(),

        "username":
            username,

        "action":
            action,

        "source":
            source
    }

    with open(
        AUDIT_FILE,
        "r"
    ) as file:

        data = json.load(file)

    data.append(entry)

    with open(
        AUDIT_FILE,
        "w"
    ) as file:

        json.dump(

            data,

            file,

            indent=4
        )


def load_audit_events():

    with open(
        AUDIT_FILE,
        "r"
    ) as file:

        return json.load(file)
