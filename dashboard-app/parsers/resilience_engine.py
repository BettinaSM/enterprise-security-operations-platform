from parsers.backup_engine import (
    validate_backups
)

# --------------------------------
# RESILIENCE SCORE
# --------------------------------

def calculate_resilience():

    backups = validate_backups()

    total = len(backups)

    successful = len([

        backup

        for backup in backups

        if backup["status"] == "Success"

    ])

    score = (

        round(
            successful / total * 100,
            2
        )

        if total > 0

        else 0

    )

    return {

        "score": score,

        "successful": successful,

        "total": total

    }


# --------------------------------
# RESILIENCE DETAILS
# --------------------------------

def evaluate_resilience():

    return validate_backups()
