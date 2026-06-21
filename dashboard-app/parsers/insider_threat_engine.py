from parsers.datalake_engine import (
    load_events
)

# --------------------------------
# DETECT
# --------------------------------

def detect_insider_threat():

    events = load_events()

    findings = []

    for event in events:

        text = str(event).lower()

        if (

            "sudo" in text

            or "administrator" in text

            or "root" in text

        ):

            findings.append({

                "type":

                    "Privileged Activity",

                "severity":

                    "High",

                "event":

                    event

            })

        if (

            "wget" in text

            or "curl" in text

            or "scp" in text

        ):

            findings.append({

                "type":

                    "Potential Data Exfiltration",

                "severity":

                    "Critical",

                "event":

                    event

            })

    return findings
