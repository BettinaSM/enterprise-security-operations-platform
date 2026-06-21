import requests

def load_otx_feed(api_key):

    headers = {
        "X-OTX-API-KEY": api_key
    }

    url = (
        "https://otx.alienvault.com/api/v1/indicators/export"
    )

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        return response.json()

    except:

        return []
