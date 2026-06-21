import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CONTROLS_DIR = (

    BASE_DIR /
    "controls"

)

# --------------------------------
# LOAD FRAMEWORK
# --------------------------------

def load_framework(framework):

    file_path = (

        CONTROLS_DIR /
        f"{framework}.json"

    )

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []

# --------------------------------
# SCORE
# --------------------------------

def calculate_framework_score(framework):

    controls = load_framework(
        framework
    )

    if not controls:

        return 0

    implemented = len([

        c

        for c in controls

        if c.get(
            "implemented"
        )

    ])

    return round(

        (implemented / len(controls)) * 100,

        2

    )
