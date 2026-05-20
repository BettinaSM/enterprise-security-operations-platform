import jwt
import datetime

SECRET_KEY = "enterprise-security-platform"


# ---------------------------
# GENERATE TOKEN
# ---------------------------

def generate_token(
    username,
    role
):

    payload = {

        "username": username,
        "role": role,

        "exp": (
            datetime.datetime.utcnow()
            + datetime.timedelta(hours=8)
        )
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return token


# ---------------------------
# VALIDATE TOKEN
# ---------------------------

def validate_token(
    token
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return payload

    except Exception:

        return None
