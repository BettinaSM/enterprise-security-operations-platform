from fastapi import FastAPI

from api.routers import (
    assets,
    risk,
    vulnerabilities,
    identities,
    auth,
    incidents,
    threat_intel,
    detections
)

app = FastAPI(

    title="Enterprise Security Operations API",

    version="1.0.0",

    description="""

    Enterprise Security Operations Platform API

    Capabilities:

    - IAM
    - Threat Intelligence
    - Vulnerability Management
    - Risk Management
    - Incident Response
    - SOC Operations

    """

)

# --------------------------------
# ROOT
# --------------------------------

@app.get("/")

def root():

    return {

        "message":
            "Enterprise Security Operations API",

        "version":
            "1.0.0"

    }


# --------------------------------
# ROUTERS
# --------------------------------

app.include_router(
    auth.router
)

app.include_router(
    incidents.router
)

app.include_router(
    detections.router
)

app.include_router(
    threat_intel.router
)

app.include_router(
    assets.router
)

app.include_router(
    risk.router
)

app.include_router(
    vulnerabilities.router
)

app.include_router(
    identities.router
)
