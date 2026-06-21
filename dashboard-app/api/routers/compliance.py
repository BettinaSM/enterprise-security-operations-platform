from fastapi import APIRouter

from parsers.compliance_engine import (
    run_compliance
)

router = APIRouter(
    prefix="/compliance",
    tags=["Compliance"]
)

@router.get("/")

def compliance():

    return run_compliance()
