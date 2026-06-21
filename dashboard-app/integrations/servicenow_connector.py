import requests

from secrets.secrets_manager import (
    get_secret
)

SN_URL = get_secret(
    "SERVICENOW_URL"
)

SN_USER = get_secret(
    "SERVICENOW_USER"
)

SN_PASSWORD = get_secret(
    "SERVICENOW_PASSWORD"
)


def create_incident(

    short_description,

    description,

    severity="2"

):

    payload = {

        "short_description":
            short_description,

        "description":
            description,

        "severity":
            severity

    }

    try:

        response = requests.post(

            f"{SN_URL}/api/now/table/incident",

            auth=(

                SN_USER,

                SN_PASSWORD

            ),

            json=payload,

            timeout=20

        )

        return response.json()

    except Exception as error:

        return {

            "error": str(error)

        }
