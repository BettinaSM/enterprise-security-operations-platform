from utils.logger import log_info
from utils.logger import log_error

import requests
import os

# -----------------------------------
# MICROSOFT DEFENDER CONNECTOR
# -----------------------------------

DEFENDER_URL = (
    "https://api.security.microsoft.com/api/alerts"
)


def get_defender_alerts(token=None):

    if not token:

        log_warning(
            "Microsoft Defender token not configured"
        )

        return []

    headers = {

        "Authorization":
            f"Bearer {token}",

        "Content-Type":
            "application/json"

    }

    try:

        response = requests.get(

            DEFENDER_URL,

            headers=headers,

            timeout=30

        )

        if response.status_code == 200:

            alerts = response.json().get(

                "value",
                []

            )

            log_info(

                f"Collected {len(alerts)} Defender alerts"

            )

            return alerts

        log_error(

            f"Defender API Error: {response.status_code}"

        )

        return []

    except Exception as error:

        log_error(

            f"Defender connector error: {error}"

        )

        return []


# -----------------------------------
# NORMALIZATION
# -----------------------------------

def normalize_defender_alerts():

    alerts = get_defender_alerts()

    normalized = []

    for alert in alerts:

        normalized.append({

            "source":
                "Microsoft Defender",

            "title":
                alert.get(
                    "title"
                ),

            "severity":
                alert.get(
                    "severity"
                ),

            "status":
                alert.get(
                    "status"
                ),

            "timestamp":
                alert.get(
                    "createdTime"
                )

        })

    return normalized
