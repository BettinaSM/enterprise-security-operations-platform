import pandas as pd

from parsers.database_engine import (
    load_detections,
    load_incidents
)


# ---------------------------
# DETECTION ANALYTICS
# ---------------------------

def detection_analytics():

    detections = load_detections()

    if not detections:

        return pd.DataFrame()

    detection_df = pd.DataFrame(
        detections,
        columns=[
            "ID",
            "Detection Type",
            "Severity",
            "Details"
        ]
    )

    analytics = (
        detection_df["Severity"]
        .value_counts()
        .reset_index()
    )

    analytics.columns = [
        "Severity",
        "Count"
    ]

    return analytics


# ---------------------------
# INCIDENT ANALYTICS
# ---------------------------

def incident_analytics():

    incidents = load_incidents()

    if not incidents:

        return pd.DataFrame()

    incident_df = pd.DataFrame(
        incidents,
        columns=[
            "ID",
            "Severity",
            "Source",
            "Description",
            "Status"
        ]
    )

    analytics = (
        incident_df["Severity"]
        .value_counts()
        .reset_index()
    )

    analytics.columns = [
        "Severity",
        "Count"
    ]

    return analytics
