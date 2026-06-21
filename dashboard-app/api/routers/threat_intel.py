from fastapi import APIRouter

router = APIRouter(

    prefix="/threat-intel",

    tags=["Threat Intelligence"]

)


@router.get("/ioc-feed")

def ioc_feed():

    return {

        "iocs": [

            "185.220.101.1",

            "malicious-domain.com",

            "45.133.1.22"

        ]

    }


@router.get("/threat-feed")

def threat_feed():

    return {

        "threats": [

            {

                "type": "C2",

                "indicator":
                    "malicious-domain.com"

            },

            {

                "type":
                    "Brute Force",

                "indicator":
                    "185.220.101.1"

            }

        ]

    }
