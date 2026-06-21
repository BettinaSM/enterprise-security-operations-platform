import requests

from secrets.secrets_manager import (
    get_secret
)

QRADAR_URL = get_secret(
    "QRADAR_URL"
)

QRADAR_TOKEN = get_secret(
    "QRADAR_TOKEN"
)


def get_offenses():

    headers = {

        "SEC":

            QRADAR_TOKEN

    }

    try:

        response = requests.get(

            f"{QRADAR_URL}/api/siem/offenses",

            headers=headers

        )

        return response.json()

    except Exception as error:

        return []
