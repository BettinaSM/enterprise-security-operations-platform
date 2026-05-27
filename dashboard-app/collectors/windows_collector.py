import json

from configs.settings import (
    SIMULATION_MODE,
    WINDOWS_LOG,
    REAL_WINDOWS_LOG
)

# ---------------------------
# WINDOWS COLLECTOR
# ---------------------------

def collect_windows_logs():

    log_source = (
        WINDOWS_LOG
        if SIMULATION_MODE
        else REAL_WINDOWS_LOG
    )

    try:

        path = Path(log_source)

        if not path.exists():

            return [
                {
                    "error": f"log_not_found: {log_source}"
                }
            ]

        with open(
            path,
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
