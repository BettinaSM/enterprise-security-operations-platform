from fastapi import APIRouter

from parsers.vulnerability_engine import (
    enrich_vulnerabilities
)

router = APIRouter(

    prefix="/vulnerabilities",

    tags=["Vulnerabilities"]

)


@router.get("/")

def get_vulnerabilities():

    return enrich_vulnerabilities()
