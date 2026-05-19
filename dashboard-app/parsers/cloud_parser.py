import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def load_json_log(file_path):

    full_path = BASE_DIR / file_path

    if not full_path.exists():
        return None

    with open(full_path, "r") as file:
        return json.load(file)


def detect_failed_cloud_login(event):

    event_str = str(event)

    keywords = [
        "Failed authentication",
        "failure",
        "failed",
        "Unauthorized"
    ]

    return any(
        keyword.lower() in event_str.lower()
        for keyword in keywords
    )


def detect_privileged_activity(event):

    event_str = str(event)

    keywords = [
        "CreateUser",
        "system:admin",
        "privileged",
        "Administrator"
    ]

    return any(
        keyword.lower() in event_str.lower()
        for keyword in keywords
    )
