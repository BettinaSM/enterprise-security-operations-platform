import subprocess
from pathlib import Path
import shutil

# ---------------------------
# EXECUTE PLAYBOOK
# ---------------------------

def execute_playbook(
    playbook,
    inventory
):

    if not shutil.which(
        "ansible-playbook",
    ):

        return {
            "stdout": "",
            "stderr":
                "Ansible not installed",
            "returncode": 1
        }

    command = [
        "ansible-playbook",
        playbook,
        "-i",
        inventory
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return {
        "stdout":
            result.stdout,
        "stderr":
            result.stderr,
        "returncode":
            result.returncode
    }
