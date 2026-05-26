USERS = {

    "admin": {
        "password": "admin123",
        "role": "admin"
    },

    "soc": {
        "password": "soc123",
        "role": "soc_analyst"
    },

    "manager": {
        "password": "manager123",
        "role": "manager"
    },

    "exe": {
        "password": "exec123",
        "role": "executive"
    }
}


def authenticate(
    username,
    password
):

    user = USERS.get(username)

    if not user:

        return None

    if user["password"] != password:

        return None

    return user["role"]
