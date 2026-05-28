from datetime import datetime

# ---------------------------
# BUILD TIMELINE
# ---------------------------

def build_timeline(
    events
):

    timeline = []

    for event in events:

        timeline.append({

            "timestamp": datetime.utcnow().isoformat(),
            "event": str(event)
        })

    return timeline
