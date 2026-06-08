from parsers.iam_engine import (
    get_local_users,
    get_groups,
    get_sudo_users
)

# ---------------------------
# PRIVILEGED ACCOUNTS
# ---------------------------

def find_privileged_accounts():

    privileged = []

    sudo_entries = get_sudo_users()

    for entry in sudo_entries:

        privileged.append({

            "type": "sudo",
            "account": entry

        })

    return privileged

# ---------------------------
# SERVICE ACCOUNTS
# ---------------------------

def find_service_accounts():

    accounts = []

    for user in get_local_users():

        username = user.get(
            "username",
            ""
        )

        if (

            username.startswith("svc")

            or username.startswith("sa")

            or username.startswith("oracle")

            or username.startswith("db2")

            or username.startswith("ansible")

        ):

            accounts.append(user)

    return accounts

# ---------------------------
# DORMANT USERS
# ---------------------------

def find_dormant_users():

    dormant = []

    for user in get_local_users():

        shell = user.get(
            "shell",
            ""
        )

        if (

            shell == "/sbin/nologin"

            or shell == "/usr/sbin/nologin"

            or shell == "/bin/false"

        ):

            dormant.append(user)

    return dormant

# ---------------------------
# GOVERNANCE SUMMARY
# ---------------------------

def identity_governance_summary():

    return {

        "privileged_accounts":
            find_privileged_accounts(),

        "service_accounts":
            find_service_accounts(),

        "dormant_accounts":
            find_dormant_users()

    }
