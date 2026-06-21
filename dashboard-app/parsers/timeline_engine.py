from datetime import datetime

# ---------------------------
# GENERIC TIMELINE
# ---------------------------

def build_timeline(events):

    timeline = []

    for event in events:

        timeline.append({

            "timestamp":

                event.get(
                    "timestamp",
                    datetime.utcnow().isoformat()
                ),

            "event":

                str(event)

        })

    return timeline

# --------------------------------
# USER TIMELINE
# --------------------------------

def get_user_timeline(

    events,
    username

):

    return [

        event

        for event in events

        if event.get(
            "username"
        ) == username

    ]

# --------------------------------
# HOST TIMELINE
# --------------------------------

def get_host_timeline(

    events,
    hostname

):

    return [

        event

        for event in events

        if event.get(
            "hostname"
        ) == hostname

    ]
