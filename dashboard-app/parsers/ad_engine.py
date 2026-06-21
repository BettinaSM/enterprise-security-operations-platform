from integrations.ad_connector import (
    ad_connect
)

# --------------------------------
# GET AD USERS
# --------------------------------

def get_ad_users():

    conn = ad_connect()

    if not conn:

        return [

            {
                "username": "administrator",
                "source": "AD-Simulation"
            },

            {
                "username": "svc_backup",
                "source": "AD-Simulation"
            },

            {
                "username": "soc_analyst",
                "source": "AD-Simulation"
            }

        ]

    try:

        conn.search(

            search_base="dc=company,dc=local",

            search_filter="(objectClass=user)",

            attributes=[

                "sAMAccountName"

            ]

        )

        users = []

        for entry in conn.entries:

            users.append({

                "username":

                    str(
                        entry.sAMAccountName
                    ),

                "source":

                    "Active Directory"

            })

        return users

    except Exception as error:

        print(

            f"AD query error: {error}"

        )

        return []

# --------------------------------
# SEARCH USER
# --------------------------------

def search_ad_user(username):

    conn = ad_connect()

    if not conn:

        return []

    try:

        conn.search(

            search_base="dc=company,dc=local",

            search_filter=f"(sAMAccountName={username})",

            attributes=[

                "sAMAccountName",
                "mail",
                "memberOf"

            ]

        )

        results = []

        for entry in conn.entries:

            results.append(

                entry.entry_attributes_as_dict

            )

        return results

    except:

        return []
