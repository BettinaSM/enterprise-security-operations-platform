from fastapi import APIRouter

from parsers.database_engine import (
    load_detections,
    load_security_events
)

router = APIRouter(

    prefix="/detections",

    tags=["Detection Engineering"]

)


@router.get("/")

def detections():

    return {

        "detections":

            load_detections()

    }


@router.get("/events")

def events():

    return {

        "events":

            load_security_events()

    }
