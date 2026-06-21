import json
from pathlib import Path

EVENT_FILE = (
    Path(__file__).resolve().parent.parent /
    "data" /
    "normalized_events.json"
)

EVENT_FILE.parent.mkdir(
    exist_ok=True
)

def save_events(events):

    with open(
        EVENT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            events,
            file,
            indent=4
        )


def load_events():

    try:

        with open(
            EVENT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []
