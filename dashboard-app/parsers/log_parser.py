from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent


def read_log(file_path):

    full_path = BASE_DIR / file_path

    if not full_path.exists():
        return []

    with open(full_path, "r") as file:
        return file.readlines()


def count_failed_auth(lines):

    return sum(
        1 for line in lines
        if "Failed" in line or "failure" in line
    )


def count_critical(lines):

    return sum(
        1 for line in lines
        if "Critical" in line or "HIGH" in line
    )
