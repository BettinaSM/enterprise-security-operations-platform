import json
import subprocess

from configs.settings import (
    WINDOWS_LOG
)

# ---------------------------
# USERS
# ---------------------------

def get_windows_users():

    return [

        {
            "username": "Administrator"
        }
    ]

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
        "events": get_windows_events()

    }
