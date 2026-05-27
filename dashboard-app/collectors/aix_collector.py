from configs.settings import (
    SIMULATION_MODE,
    AIX_LOG,
    AIX_LOG_PATH
)

# ---------------------------
# COLLECT AIX LOGS
# ---------------------------

def collect_aix_logs():

    log_file = (
        AIX_LOG
        if SIMULATION_MODE
        else AIX_LOG_PATH
    )

    try:

        with open(
            log_file,
            "r",
            encoding="utf-8"
        ) as file:

            logs = file.readlines()

        return [
            log.strip()
            for log in logs
            if log.strip()
        ]

    except Exception as error:

        return [
            f"aix_collector_error: {error}"
        ]
