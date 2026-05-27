from pathlib import Path

# ---------------------------
# BASE PATH
# ---------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# LOG PATHS
# ---------------------------

LINUX_AUTH_LOG = (
    BASE_DIR /
    "agents" /
    "linux" /
    "auth.log"
)

# ---------------------------
# LOAD LINUX AUTH LOGS
# ---------------------------

def collect_linux_logs():

    if not LINUX_AUTH_LOG.exists():

        return []

    with open(
        LINUX_AUTH_LOG,
        "r"
    ) as file:

        logs = file.readlines()

    return [
        log.strip()
        for log in logs
        if log.strip()
    ]
