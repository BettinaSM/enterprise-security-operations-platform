from utils.logger import log_info
from utils.logger import log_error

import requests
import os
import xml.etree.ElementTree as ET

# -----------------------------------
# QUALYS CONNECTOR
# -----------------------------------

QUALYS_URL = (
    "https://qualysapi.qualys.com/api/2.0/fo/asset/host/vm/detection/"
)


def get_qualys_findings(

    username=None,
    password=None

):

    if not username or not password:

        log_error(
            "Qualys credentials not configured"
        )

        return []

    try:

        response = requests.get(

            QUALYS_URL,

            auth=(username, password),

            timeout=60

        )

        if response.status_code != 200:

            log_error(

                f"Qualys API Error: {response.status_code}"

            )

            return []

        return parse_qualys_xml(

            response.text

        )

    except Exception as error:

        log_error(

            f"Qualys connector error: {error}"

        )

        return []


# -----------------------------------
# XML PARSER
# -----------------------------------

def parse_qualys_xml(xml_content):

    findings = []

    try:

        root = ET.fromstring(
            xml_content
        )

        for host in root.iter("HOST"):

            findings.append({

                "hostname":

                    host.findtext(
                        "IP"
                    ),

                "source":

                    "Qualys",

                "status":

                    "Open"

            })

    except Exception as error:

        log_error(

            f"Qualys parser error: {error}"

        )

    return findings
