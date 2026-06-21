from ldap3 import (
    Server,
    Connection,
    ALL
)

from utils.logger import (
    log_warning
)

LDAP_SERVER = "ldap.company.com"

def ldap_connect():

    try:

        server = Server(
            LDAP_SERVER,
            get_info=ALL
        )

        conn = Connection(
            server,
            auto_bind=True
        )

        return conn

    except Exception as error:

        log_warning(
            f"LDAP unavailable: {error}"
        )

        return None
