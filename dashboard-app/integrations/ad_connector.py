from ldap3 import Server, Connection

def ad_connect():

    server = Server(
        "ad.company.local"
    )

    conn = Connection(

        server,

        user="administrator@company.local",

        password="password",

        auto_bind=True

    )

    return conn
