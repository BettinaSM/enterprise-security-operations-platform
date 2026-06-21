from ingestion.queue_manager import (
    dequeue
)

from parsers.normalization_engine import (
    normalize_event
)


def process_pipeline():

    event = dequeue()

    if not event:

        return None

    return normalize_event(

        event["source"],

        event["raw_log"]

    )
