from parsers.database_engine import (
    save_detection,
    load_detections
)

def save_detection_repository(
    detection_type,
    severity,
    details
):

    save_detection(
        detection_type,
        severity,
        details
    )

def load_detections_repository():

    return load_detections()
