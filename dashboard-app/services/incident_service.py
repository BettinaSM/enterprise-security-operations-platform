from repositories.incidents_repository import (
    save_incident_repository,
    load_incidents_repository
)

def create_incident(
    severity,
    source,
    description,
    status="Open"
):

    save_incident_repository(
        severity,
        source,
        description,
        status
    )

def get_all_incidents():

    return load_incidents_repository()
