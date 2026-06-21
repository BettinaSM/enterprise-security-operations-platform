from ldap3 import Server
from ldap3 import Connection
from ldap3 import ALL

from utils.logger import log_error


def ad_connect():

    try:

        server = Server(

            "ldap.company.com",

            get_info=ALL

        )

        connection = Connection(

            server,

            user="svc_soc",

            password="password",

            auto_bind=False

        )

        return connection

    except Exception as error:

        log_error(

            f"AD Connection Error: {error}"

        )

        return None
