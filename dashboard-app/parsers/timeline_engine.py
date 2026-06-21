from datetime import datetime

# --------------------------------
# GENERIC TIMELINE
# --------------------------------

def build_timeline(events):

    timeline = []

    for event in events:

        timeline.append({

            "timestamp":

                event.get(
                    "timestamp",
                    datetime.utcnow().isoformat()
                ),

            "event": str(event)

        })

    return timeline


# --------------------------------
# USER TIMELINE
# --------------------------------

def get_user_timeline(username):

    return [

        {

            "timestamp":
                datetime.utcnow().isoformat(),

            "username":
                username,

            "activity":
                "User Login"

        },

        {

            "timestamp":
                datetime.utcnow().isoformat(),

            "username":
                username,

            "activity":
                "Sudo Command"

        }

    ]


# --------------------------------
# HOST TIMELINE
# --------------------------------

def get_host_timeline(hostname):

    return [

        {

            "timestamp":
                datetime.utcnow().isoformat(),

            "hostname":
                hostname,

            "activity":
                "Authentication"

        },

        {

            "timestamp":
                datetime.utcnow().isoformat(),

            "hostname":
                hostname,

            "activity":
                "Configuration Change"

        }

    ]
