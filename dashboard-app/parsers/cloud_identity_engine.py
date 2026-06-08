from parsers.aws_iam_engine import (
    get_aws_users
)

from parsers.azure_iam_engine import (
    get_entra_users
)

from parsers.gcp_iam_engine import (
    get_gcp_users
)

# ---------------------------
# CLOUD IDENTITIES
# ---------------------------

def get_all_cloud_identities():

    return {

        "aws":
            get_aws_users(),

        "azure":
            get_entra_users(),

        "gcp":
            get_gcp_users()

    }

# ---------------------------
# SEARCH
# ---------------------------

def search_cloud_identity(
    username
):

    findings = []

    for user in get_aws_users():

        if username.lower() in str(user).lower():

            findings.append({

                "provider": "AWS",
                "details": user

            })

    for user in get_entra_users():

        if username.lower() in str(user).lower():

            findings.append({

                "provider": "Azure",
                "details": user

            })

    for user in get_gcp_users():

        if username.lower() in str(user).lower():

            findings.append({

                "provider": "GCP",
                "details": user

            })

    return findings
