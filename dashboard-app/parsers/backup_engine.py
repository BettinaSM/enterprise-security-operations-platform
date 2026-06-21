from datetime import datetime


def validate_backups():

    return [

        {
            "backup": "Linux Servers",
            "status": "Success",
            "last_execution": datetime.utcnow().isoformat()
        },

        {
            "backup": "Database",
            "status": "Success",
            "last_execution": datetime.utcnow().isoformat()
        },

        {
            "backup": "Cloud Snapshots",
            "status": "Warning",
            "last_execution": datetime.utcnow().isoformat()
        }

    ]


def backup_summary():

    backups = validate_backups()

    success = len(

        [

            b

            for b in backups

            if b["status"] == "Success"

        ]

    )

    return {

        "total": len(backups),

        "successful": success

    }
