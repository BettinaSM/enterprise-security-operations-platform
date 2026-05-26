from parsers.database_engine import (
    save_incident,
    load_incidents
)

def save_incident_repository(
    severity,
    source,
    description,
    status
):

    save_incident(
        severity,
        source,
        description,
        status
    )

def load_incidents_repository():

    return load_incidents()
