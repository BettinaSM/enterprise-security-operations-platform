from fastapi import APIRouter

from parsers.identity_governance import (
    run_identity_governance
)

router = APIRouter(
    prefix="/identity",
    tags=["Identity"]
)

@router.get("/")

def identity():

    return run_identity_governance()
