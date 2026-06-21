import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

EVIDENCE_DIR = (

    BASE_DIR /
    "evidence"

)

EVIDENCE_DIR.mkdir(

    parents=True,

    exist_ok=True

)

# --------------------------------
# SAVE EVIDENCE
# --------------------------------

def save_evidence(

    framework,

    evidence

):

    file_path = (

        EVIDENCE_DIR /
        f"{framework}.json"

    )

    with open(

        file_path,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            evidence,

            file,

            indent=4

        )
