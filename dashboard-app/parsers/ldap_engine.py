from integrations.ldap_connector import (
    ldap_connect
)

def get_ldap_users():

    conn = ldap_connect()

    conn.search(

        "dc=company,dc=com",

        "(objectClass=person)",

        attributes=["cn"]

    )

    users = []

    for entry in conn.entries:

        users.append({

            "username": str(entry.cn),
            "source": "LDAP"

        })

    return users
