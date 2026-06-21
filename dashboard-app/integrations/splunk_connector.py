import requests

from secrets.secrets_manager import (
    get_secret
)

SPLUNK_URL = get_secret(
    "SPLUNK_URL"
)

SPLUNK_TOKEN = get_secret(
    "SPLUNK_TOKEN"
)


def search_splunk(query):

    headers = {

        "Authorization":

            f"Bearer {SPLUNK_TOKEN}"

    }

    payload = {

        "search": query

    }

    try:

        response = requests.post(

            f"{SPLUNK_URL}/services/search/jobs",

            headers=headers,

            data=payload

        )

        return response.json()

    except Exception as error:

        return {

            "error": str(error)

        }
