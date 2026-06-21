import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_LAKE = (

    BASE_DIR /
    "datalake" /
    "normalized"

)

DATA_LAKE.mkdir(

    parents=True,

    exist_ok=True

)

# --------------------------------
# INGEST
# --------------------------------

def ingest_event(event):

    file_path = (

        DATA_LAKE /
        "events.json"

    )

    events = []

    if file_path.exists():

        with open(

            file_path,

            "r",

            encoding="utf-8"

        ) as file:

            events = json.load(file)

    events.append(event)

    with open(

        file_path,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            events,

            file,

            indent=4

        )

# --------------------------------
# LOAD
# --------------------------------

def load_events():

    file_path = (

        DATA_LAKE /
        "events.json"

    )

    if not file_path.exists():

        return []

    with open(

        file_path,

        "r",

        encoding="utf-8"

    ) as file:

        return json.load(file)
