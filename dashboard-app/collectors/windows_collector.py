import json

from configs.settings import (
    SIMULATION_MODE,
    WINDOWS_LOG
)

# ---------------------------
# WINDOWS COLLECTOR
# ---------------------------

def collect_windows_logs():

    if SIMULATION_MODE:

        try:

            with open(
                WINDOWS_LOG,
                "r",
                encoding="utf-8"
            ) as file:

                events = json.load(file)

            return events

        except Exception as error:

            return [
                {
                    "error": str(error)
                }
            ]

    # ---------------------------
    # REAL WINDOWS COLLECTION
    # ---------------------------

    return [
        {
            "message": "Real Windows collection not configured yet"
        }
    ]
