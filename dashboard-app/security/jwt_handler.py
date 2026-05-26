import jwt

SECRET = "enterprise-secret"

def generate_token(payload):

    return jwt.encode(
        payload,
        SECRET,
        algorithm="HS256"
    )

def validate_token(token):

    return jwt.decode(
        token,
        SECRET,
        algorithms=["HS256"]
    )
