import subprocess

from pathlib import Path

# ---------------------------
# EXECUTE PLAYBOOK
# ---------------------------

def execute_playbook(
    playbook,
    inventory
):

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

        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }
