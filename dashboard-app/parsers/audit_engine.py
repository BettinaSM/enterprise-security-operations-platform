from parsers.iam_engine import (
    get_local_users,
    get_groups,
    get_sudo_users,
    get_service_accounts
)

from parsers.ldap_engine import (
    get_ldap_users
)

from parsers.ad_engine import (
    get_ad_users
)

from parsers.aws_iam_engine import (
    get_aws_users
)

from parsers.azure_iam_engine import (
    get_entra_users
)

from parsers.gcp_iam_engine import (
    get_gcp_users
)

from parsers.k8s_rbac_engine import (
    get_k8s_roles
)

# ---------------------------
# COMPLETE AUDIT
# ---------------------------

def run_full_audit():

    return {

        "local_users":
            get_local_users(),

        "groups":
            get_groups(),

        "sudo_users":
            get_sudo_users(),

        "service_accounts":
            get_service_accounts(),

        "ldap_users":
            get_ldap_users(),

        "ad_users":
            get_ad_users(),

        "aws_users":
            get_aws_users(),

        "entra_users":
            get_entra_users(),

        "gcp_users":
            get_gcp_users(),

        "kubernetes_roles":
            get_k8s_roles()

    }

# ---------------------------
# AUDIT BY USER
# ---------------------------

def audit_user(username):

    findings = []

    # ---------------------------
    # LOCAL USERS
    # ---------------------------

    for user in get_local_users():

        if user.get(
            "username"
        ) == username:

            findings.append({

                "source": "Local",
                "details": user

            })

    # ---------------------------
    # LDAP
    # ---------------------------

    for user in get_ldap_users():

        if user.get(
            "username"
        ) == username:

            findings.append({

                "source": "LDAP",
                "details": user

            })

    # ---------------------------
    # AD
    # ---------------------------

    for user in get_ad_users():

        if user.get(
            "username"
        ) == username:

            findings.append({

                "source": "AD",
                "details": user

            })

    return findings
