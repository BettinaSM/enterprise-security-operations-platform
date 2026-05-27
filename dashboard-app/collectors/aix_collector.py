from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

AIX_LOG = (
    BASE_DIR /
    "agents" /
    "aix" /
    "sudo.log"
)

def collect_aix_logs():

    if not AIX_LOG.exists():

        return []

    with open(
        AIX_LOG,
        "r"
    ) as file:

        logs = file.readlines()

    return [
        log.strip()
        for log in logs
        if log.strip()
    ]
