from parsers.backup_engine import (
    validate_backups
)


def evaluate_resilience():

    backups = validate_backups()

    results = []

    for backup in backups:

        results.append({

            "component":
                backup["backup"],

            "status":
                backup["status"]

        })

    return results
