from configs.settings import (
    AIX_SUDO_LOG
)

# ---------------------------
# COLLECT AIX LOGS
# ---------------------------

def collect_aix_logs():

    try:

        with open(
            AIX_SUDO_LOG,
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
