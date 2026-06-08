import json
import subprocess

from configs.settings import (
    WINDOWS_LOG
)

# ---------------------------
# USERS
# ---------------------------

def get_windows_users():

    try:

        result = subprocess.run(

            [

                "powershell",
                "-Command",
                "Get-LocalUser | Select Name"

            ],

            capture_output=True,
            text=True

        )

        return result.stdout.splitlines()

    except:

        return []

# ---------------------------
# LOCAL ADMINS
# ---------------------------

def get_local_admins():

    try:

        result = subprocess.run(

            [

                "powershell",
                "-Command",
                "Get-LocalGroupMember Administrators"

            ],

            capture_output=True,
            text=True

        )

        return result.stdout.splitlines()

    except:

        return []

# ---------------------------
# EVENTS
# ---------------------------

def get_windows_events():

    try:

        with open(
            WINDOWS_LOG,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []

# ---------------------------
# AUDIT
# ---------------------------

def run_windows_audit():

    return {

        "users": get_windows_users(),
        "local_admins": get_local_admins(),
        "events": get_windows_events()

    }
