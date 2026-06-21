from fastapi import APIRouter

from parsers.database_engine import (
    load_detections
)

router = APIRouter(
    prefix="/detections",
    tags=["Detections"]
)

@router.get("/")

def detections():

    return load_detections()
