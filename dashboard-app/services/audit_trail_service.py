import json

from datetime import datetime

AUDIT_FILE = "audit/audit_trail.json"


def register_action(

    user,

    action

):

    entry = {

        "timestamp":
            datetime.utcnow().isoformat(),

        "user":
            user,

        "action":
            action
    }

    try:

        with open(

            AUDIT_FILE,

            "r"

        ) as file:

            data = json.load(file)

    except:

        data = []

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
