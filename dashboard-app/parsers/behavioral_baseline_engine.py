from collections import Counter

from parsers.datalake_engine import (
    load_events
)

# --------------------------------
# USER BASELINE
# --------------------------------

def build_user_baseline(username):

    events = load_events()

    user_events = [

        e

        for e in events

        if e.get(
            "username"
        ) == username

    ]

    hosts = Counter(

        [

            e.get(
                "hostname"
            )

            for e in user_events

        ]

    )

    return {

        "username": username,

        "usual_hosts":

            list(

                hosts.keys()

            )

    }
