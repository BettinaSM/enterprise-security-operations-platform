from fastapi import APIRouter

from parsers.vulnerability_engine import (
    enrich_vulnerabilities,
    critical_vulnerabilities
)

router = APIRouter(
    prefix="/vulnerabilities",
    tags=["Vulnerabilities"]
)

@router.get("/")

def vulnerabilities():

    return enrich_vulnerabilities()

@router.get("/critical")

def critical():

    return critical_vulnerabilities()
