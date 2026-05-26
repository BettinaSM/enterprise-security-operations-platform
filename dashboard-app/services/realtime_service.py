from parsers.realtime_engine import (
    generate_realtime_event
)

from parsers.live_metrics import (
    generate_live_metrics
)

def get_live_event():

    return generate_realtime_event()

def get_live_metrics():

    return generate_live_metrics()
