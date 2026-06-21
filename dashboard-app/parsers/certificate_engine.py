import json

from pathlib import Path

from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

CERT_FILE = (

    BASE_DIR /
    "attack-surface" /
    "certificates.json"

)

# --------------------------------
# CERTIFICATES
# --------------------------------

def load_certificates():

    try:

        with open(
            CERT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []

# --------------------------------
# EXPIRING CERTIFICATES
# --------------------------------

def get_expiring_certificates():

    findings = []

    today = datetime.now()

    for cert in load_certificates():

        expiration = datetime.strptime(

            cert["expires"],
            "%Y-%m-%d"

        )

        remaining = (

            expiration - today

        ).days

        if remaining <= 90:

            findings.append({

                **cert,

                "days_remaining": remaining

            })

    return findings
