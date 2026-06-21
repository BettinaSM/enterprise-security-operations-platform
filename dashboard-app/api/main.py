from fastapi import FastAPI

# --------------------------------
# ROUTERS
# --------------------------------

from api.routers.auth import (
    router as auth_router
)

from api.routers.assets import (
    router as assets_router
)

from api.routers.risk import (
    router as risk_router
)

from api.routers.vulnerabilities import (
    router as vulnerabilities_router
)

from api.routers.identities import (
    router as identities_router
)

from api.routers.incidents import (
    router as incidents_router
)

from api.routers.threat_intel import (
    router as threat_intel_router
)

from api.routers.detections import (
    router as detections_router
)

from api.routers.compliance import (
    router as compliance_router
)

# --------------------------------
# FASTAPI
# --------------------------------

app = FastAPI(

    title="Enterprise Security Operations API",

    version="1.0.0",

    description="""

Enterprise Security Operations Platform API

Capabilities:

- IAM Governance
- Threat Intelligence
- Vulnerability Management
- Risk Management
- Incident Response
- SOC Operations
- Compliance
- Detection Engineering

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
# ROUTERS REGISTRATION
# --------------------------------

app.include_router(
    auth_router
)

app.include_router(
    incidents_router
)

app.include_router(
    detections_router
)

app.include_router(
    threat_intel_router
)

app.include_router(
    assets_router
)

app.include_router(
    risk_router
)

app.include_router(
    vulnerabilities_router
)

app.include_router(
    identities_router
)

app.include_router(
    compliance_router
)
