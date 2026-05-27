from configs.settings import (
    SIMULATION_MODE,
    LINUX_LOG,
    LINUX_LOG_PATH
)

# ---------------------------
# COLLECT LINUX LOGS
# ---------------------------

def collect_linux_logs():

    log_file = (
        LINUX_LOG
        if SIMULATION_MODE
        else LINUX_LOG_PATH
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
            f"collector_error: {error}"
        ]
