from fastapi import APIRouter

from parsers.asset_risk_engine import (
    enterprise_asset_risk
)

router = APIRouter(

    prefix="/risk",

    tags=["Risk"]

)


@router.get("/")

def get_risk():

    return enterprise_asset_risk()
