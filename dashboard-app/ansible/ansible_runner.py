import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

INVENTORY_FILE = (
    BASE_DIR /
    "inventory" /
    "inventory.ini"
)

PLAYBOOK_DIR = (
    BASE_DIR /
    "playbooks"
)

REPORT_DIR = (
    BASE_DIR /
    "reports" /
    "ansible-output"
)

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# ---------------------------
# RUN PLAYBOOK
# ---------------------------

def run_playbook(
    playbook_name
):

    playbook_path = (
        PLAYBOOK_DIR /
        playbook_name
    )

    command = [

        "ansible-playbook",

        "-i",
        str(INVENTORY_FILE),

        str(playbook_path)
    ]

    result = subprocess.run(

        command,

        capture_output=True,
        text=True
    )

    return {

        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }
