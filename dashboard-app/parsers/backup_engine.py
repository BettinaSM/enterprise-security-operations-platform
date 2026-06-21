from datetime import datetime

# --------------------------------
# BACKUP STATUS
# --------------------------------

def get_backup_status():

    return [

        {

            "asset":
                "srv-ad01",

            "status":
                "Success",

            "last_backup":
                datetime.utcnow().isoformat()

        },

        {

            "asset":
                "srv-db01",

            "status":
                "Success",

            "last_backup":
                datetime.utcnow().isoformat()

        },

        {

            "asset":
                "srv-web01",

            "status":
                "Failed",

            "last_backup":
                datetime.utcnow().isoformat()

        }

    ]

# --------------------------------
# BACKUP COVERAGE
# --------------------------------

def backup_coverage():

    backups = get_backup_status()

    protected = len(

        [

            x

            for x in backups

            if x["status"] == "Success"

        ]

    )

    total = len(backups)

    return round(

        protected / total * 100,

        2

    )
