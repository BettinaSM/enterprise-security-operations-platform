import requests

from secrets.secrets_manager import (
    get_secret
)


def get_hosts():

    token = get_secret(
        "CROWDSTRIKE_TOKEN"
    )

    headers = {

        "Authorization":

            f"Bearer {token}"

    }

    response = requests.get(

        "https://api.crowdstrike.com/devices/queries/devices/v1",

        headers=headers

    )

    return response.json()
