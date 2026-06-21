from fastapi import APIRouter

from parsers.identity_governance import (
    run_identity_governance
)

router = APIRouter(

    prefix="/identities",

    tags=["Identity"]

)


@router.get("/")

def get_identities():

    return run_identity_governance()
