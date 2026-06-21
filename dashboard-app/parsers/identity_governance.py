from datetime import datetime
from collections import Counter

from parsers.iam_engine import (
    get_local_users,
    get_groups,
    get_sudo_users,
    get_service_accounts
)

from parsers.iam_engine import (
    get_privileged_users
)

# ---------------------------
# DORMANT ACCOUNTS
# ---------------------------

def find_dormant_accounts(users):

    findings = []

    for user in users:

        if user.get(
            "last_login_days",
            0
        ) > 90:

            findings.append({

                "username":
                    user["username"],

                "issue":
                    "Dormant Account",

                "severity":
                    "High"

            })

    return findings

# ---------------------------
# SERVICE ACCOUNTS
# ---------------------------

def find_service_accounts():

    findings = []

    for account in get_service_accounts():

        findings.append({

            "username":
                account,

            "issue":
                "Service Account",

            "severity":
                "Medium"

        })

    return findings

# ---------------------------
# PRIVILEGED ACCOUNTS
# ---------------------------

def find_privileged_accounts():

    findings = []

    sudo_entries = get_sudo_users()

    for entry in sudo_entries:

        findings.append({

            "entry":
                entry,

            "issue":
                "Privileged Access",

            "severity":
                "Critical"

        })

    return findings

# ---------------------------
# DUPLICATE ACCOUNTS
# ---------------------------

def find_duplicate_accounts(users):

    usernames = [

        user["username"]

        for user in users

    ]

    duplicates = [

        name

        for name, count

        in Counter(
            usernames
        ).items()

        if count > 1

    ]

    return duplicates

# ---------------------------
# EMPTY GROUPS
# ---------------------------

def find_empty_groups():

    findings = []

    for group in get_groups():

        if len(

            group.get(
                "members",
                []
            )

        ) == 0:

            findings.append({

                "group":
                    group["group"],

                "issue":
                    "Empty Group"

            })

    return findings

# ---------------------------
# FULL GOVERNANCE AUDIT
# ---------------------------

def run_identity_governance():

    users = get_local_users()

    return {

        "dormant_accounts":
            find_dormant_accounts(users),

        "service_accounts":
            find_service_accounts(),

        "privileged_accounts":
            get_privileged_users(),

        "duplicate_accounts":
            find_duplicate_accounts(users),

        "empty_groups":
            find_empty_groups()

    }

# ---------------------------
# GOVERNANCE SUMMARY
# ---------------------------

def identity_governance_summary():

    results = run_identity_governance()

    return {

        "total":

            len(results),

        "privileged":

            len([

                x

                for x in results

                if x.get(
                    "privileged",
                    False
                )

            ])

    }
