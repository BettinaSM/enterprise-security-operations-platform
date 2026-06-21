from parsers.baseline_engine import (
    compare_baseline
)

from parsers.backup_engine import (
    validate_backups
)

from parsers.incident_engine import (
    load_incidents
)


def calculate_resilience():

    incidents = len(

        load_incidents()

    )

    backups = validate_backups()

    score = 100

    score -= incidents * 2

    if not backups:

        score -= 30

    if score < 0:

        score = 0

    return {

        "score": score,

        "incidents": incidents,

        "backup_status": backups

    }
