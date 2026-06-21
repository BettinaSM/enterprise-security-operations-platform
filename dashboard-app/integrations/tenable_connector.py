import requests

from secrets.secrets_manager import (
    get_secret
)


def get_tenable_findings():

    headers = {

        "X-ApiKeys":

            f"accessKey={get_secret('TENABLE_ACCESS_KEY')};secretKey={get_secret('TENABLE_SECRET_KEY')}"

    }

    response = requests.get(

        "https://cloud.tenable.com/workbenches/vulnerabilities",

        headers=headers

    )

    return response.json()
