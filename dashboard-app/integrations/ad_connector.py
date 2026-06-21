from dotenv import load_dotenv

import os

try:

    from ldap3 import (

        Server,
        Connection,
        ALL

    )

except:

    Server = None
    Connection = None

load_dotenv()

LDAP_SERVER = os.getenv(
    "LDAP_SERVER"
)

LDAP_USER = os.getenv(
    "LDAP_USER"
)

LDAP_PASSWORD = os.getenv(
    "LDAP_PASSWORD"
)

LDAP_ENABLED = os.getenv(
    "LDAP_ENABLED",
    "False"
)


# --------------------------------
# AD CONNECTION
# --------------------------------

def ad_connect():

    if LDAP_ENABLED != "True":

        return None

    if not Server:

        return None

    try:

        server = Server(

            LDAP_SERVER,

            get_info=ALL

        )

        conn = Connection(

            server,

            user=LDAP_USER,

            password=LDAP_PASSWORD,

            auto_bind=True

        )

        return conn

    except Exception as error:

        print(

            f"LDAP connection error: {error}"

        )

        return None


# --------------------------------
# SEARCH USER
# --------------------------------

def search_user(username):

    conn = ad_connect()

    if not conn:

        return []

    try:

        conn.search(

            search_base="DC=company,DC=com",

            search_filter=f"(sAMAccountName={username})",

            attributes=[

                "cn",
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


# --------------------------------
# GET GROUP MEMBERS
# --------------------------------

def get_group_members(group_name):

    conn = ad_connect()

    if not conn:

        return []

    try:

        conn.search(

            search_base="DC=company,DC=com",

            search_filter=f"(cn={group_name})",

            attributes=["member"]

        )

        members = []

        for entry in conn.entries:

            members.extend(

                entry.member.values

            )

        return members

    except:

        return []


# --------------------------------
# TEST CONNECTION
# --------------------------------

def test_connection():

    conn = ad_connect()

    return conn is not None
