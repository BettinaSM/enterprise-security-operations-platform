from azure.identity import ClientSecretCredential

from msgraph import GraphServiceClient

from secrets.secrets_manager import (
    get_secret
)


def get_sentinel_client():

    credential = ClientSecretCredential(

        tenant_id=get_secret(
            "AZURE_TENANT_ID"
        ),

        client_id=get_secret(
            "AZURE_CLIENT_ID"
        ),

        client_secret=get_secret(
            "AZURE_CLIENT_SECRET"
        )

    )

    return credential
