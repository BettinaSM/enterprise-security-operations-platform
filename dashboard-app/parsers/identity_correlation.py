from parsers.iam_engine import (
    get_local_users
)

from parsers.ldap_engine import (
    get_ldap_users
)

from parsers.ad_engine import (
    get_ad_users
)

# ---------------------------
# IDENTITY SEARCH
# ---------------------------

def correlate_identity(username):

    results = {

        "local": [],
        "ldap": [],
        "ad": []

    }

    for user in get_local_users():

        if user.get(
            "username"
        ) == username:

            results["local"].append(user)

    for user in get_ldap_users():

        if user.get(
            "username"
        ) == username:

            results["ldap"].append(user)

    for user in get_ad_users():

        if user.get(
            "username"
        ) == username:

            results["ad"].append(user)

    return results
