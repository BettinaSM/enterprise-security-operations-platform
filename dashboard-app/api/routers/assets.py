from fastapi import APIRouter

from services.asset_service import (
    get_all_assets,
    find_asset
)

router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)

# ---------------------------
# ALL ASSETS
# ---------------------------

@router.get("/")

def all_assets():

    return get_all_assets()

# ---------------------------
# SEARCH
# ---------------------------

@router.get("/{keyword}")

def search_asset(keyword: str):

    return find_asset(keyword)
