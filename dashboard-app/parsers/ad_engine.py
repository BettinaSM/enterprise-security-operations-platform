from integrations.ad_connector import (
    ad_connect
)


def get_ad_users():

    try:

        conn = ad_connect()

        if conn is None:

            return []

        conn.search(

            "dc=company,dc=local",

            "(objectClass=user)",

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

                    "AD"

            })

        return users

    except Exception:

        return []
