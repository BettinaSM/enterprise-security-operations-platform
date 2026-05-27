from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Security Operations API"
)

# ---------------------------
# ROOT
# ---------------------------

@app.get("/")

def root():

    return {
        "message": "Enterprise Security Operations API"
    }

# ---------------------------
# TOKEN
# ---------------------------

from security.jwt_handler import (
    generate_token,
    validate_token
)

from parsers.auth_engine import (
    authenticate
)

# ---------------------------
# IOC FEED
# ---------------------------

@app.get("/ioc-feed")

def ioc_feed():

    return {

        "iocs": [

            "185.220.101.1",
            "malicious-domain.com",
            "45.133.1.22"
        ]
    }

# ---------------------------
# INCIDENTS
# ---------------------------

@app.get("/incidents")

def incidents():

    return {

        "incidents": [

            {
                "id": "INC-1001",
                "severity": "Critical",
                "status": "Open"
            },

            {
                "id": "INC-1002",
                "severity": "High",
                "status": "Investigating"
            }
        ]
    }

# ---------------------------
# THREAT FEED
# ---------------------------

@app.get("/threat-feed")

def threat_feed():

    return {

        "threats": [

            {
                "type": "C2",
                "indicator": "malicious-domain.com"
            },

            {
                "type": "Brute Force",
                "indicator": "185.220.101.1"
            }
        ]
    }

# ---------------------------
# LOGIN
# ---------------------------

@app.post("/login")

def login(
    credentials: dict
):

    username = credentials.get(
        "username"
    )

    password = credentials.get(
        "password"
    )

    role = authenticate(
        username,
        password
    )

    if not role:

        return {
            "error": "Invalid credentials"
        }

    token = generate_token(({

        "username": username,
        "role": role

    })

    return {
        "token": token,
        "role": role
    }

# ---------------------------
# PROTECTED ENDPOINT
# ---------------------------

@app.get("/protected")

def protected(
    token: str
):

    payload = validate_token(
        token
    )

    if not payload:

        return {
            "error": "Invalid token"
        }

    return {
        "message": "Authorized",
        "user": payload
    }

# ---------------------------
# DATABASE
# ---------------------------

from parsers.database_engine import (
    load_security_events,
    load_incidents,
    load_detections
)

# ---------------------------
# SECURITY EVENTS
# ---------------------------

@app.get("/security-events")

def security_events():

    events = load_security_events()

    return {
        "events": events
    }

# ---------------------------
# DETECTIONS
# ---------------------------

@app.get("/detections")

def detections():

    detections = load_detections()

    return {
        "detections": detections
    }

# ---------------------------
# INCIDENTS DATABASE
# ---------------------------

@app.get("/incidents-db")

def incidents_db():

    incidents = load_incidents()

    return {
        "incidents": incidents
    }
