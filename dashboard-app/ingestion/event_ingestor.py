from parsers.normalization_engine import (
    normalize_event
)


def ingest_event(source, raw_log):

    return normalize_event(
        source,
        raw_log
    )
