from fastapi import APIRouter

from parsers.database_engine import (
    load_incidents
)

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)

@router.get("/")

def incidents():

    return load_incidents()
