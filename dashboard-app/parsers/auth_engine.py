USERS = {

    "admin": {
        "password": "admin123",
        "role": "admin"
    },

    "analyst": {
        "password": "soc123",
        "role": "analyst"
    },

    "manager": {
        "password": "manager123",
        "role": "manager"
    },

    "readonly": {
        "password": "view123",
        "role": "readonly"
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
