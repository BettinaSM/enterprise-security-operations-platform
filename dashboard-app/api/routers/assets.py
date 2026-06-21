from fastapi import APIRouter

from parsers.cmdb_engine import (
    load_cmdb
)

router = APIRouter(

    prefix="/assets",

    tags=["Assets"]

)


@router.get("/")

def get_assets():

    return load_cmdb()
