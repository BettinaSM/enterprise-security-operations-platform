import requests

# ---------------------------
# LOAD REMOTE IOCS
# ---------------------------

def load_remote_iocs():

    urls = [

        "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"
    ]

    indicators = []

    for url in urls:

        try:

            response = requests.get(
                url,
                timeout=10
            )

            if response.status_code == 200:

                indicators.extend(
                    response.text.splitlines()
                )

        except Exception:

            pass

    return indicators
