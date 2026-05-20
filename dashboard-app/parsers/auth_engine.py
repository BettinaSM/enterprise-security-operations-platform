def authenticate(username, password):

    users = {

        "admin": {
            "password": "admin123",
            "role": "Administrator"
        },

        "analyst": {
            "password": "soc123",
            "role": "SOC Analyst"
        },

        "hunter": {
            "password": "hunt123",
            "role": "Threat Hunter"
        },

        "executive": {
            "password": "exec123",
            "role": "Executive"
        }
    }

    user = users.get(username)

    if user and user["password"] == password:

        return user["role"]

    return None
