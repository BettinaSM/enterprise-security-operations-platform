from google.oauth2 import service_account

def gcp_credentials():

    credentials = service_account.Credentials.from_service_account_file(

        "configs/gcp-key.json"

    )

    return credentials
