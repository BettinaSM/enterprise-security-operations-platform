from ldap3 import (
    Server,
    Connection,
    ALL
)

def ldap_connect():

    server = Server(
        "ldap.company.com",
        get_info=ALL
    )

    conn = Connection(
        server,
        user="cn=readonly,dc=company,dc=com",
        password="password",
        auto_bind=True
    )

    return conn
