from azure.identity import (
    ClientSecretCredential
)

def entra_credential():

    credential = ClientSecretCredential(

        tenant_id="",

        client_id="",

        client_secret=""

    )

    return credential
