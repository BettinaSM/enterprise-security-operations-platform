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
