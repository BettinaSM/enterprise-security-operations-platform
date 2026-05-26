from parsers.auth_engine import (
    authenticate
)

def login(
    username,
    password
):

    return authenticate(
        username,
        password
    )
