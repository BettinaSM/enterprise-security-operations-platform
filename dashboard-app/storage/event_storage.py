import json

from pathlib import Path

EVENT_DB = Path(
    "database/events.json"
)


def save_event(event):

    events = []

    if EVENT_DB.exists():

        with open(EVENT_DB) as f:

            events = json.load(f)

    events.append(event)

    with open(EVENT_DB, "w") as f:

        json.dump(

            events,

            f,

            indent=4

        )
