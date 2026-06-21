from fastapi import APIRouter

from security.jwt_handler import (
    generate_token,
    validate_token
)

from parsers.auth_engine import (
    authenticate
)

router = APIRouter(

    prefix="/auth",

    tags=["Authentication"]

)


@router.post("/login")

def login(credentials: dict):

    username = credentials.get(
        "username"
    )

    password = credentials.get(
        "password"
    )

    role = authenticate(

        username,

        password

    )

    if not role:

        return {

            "error":
                "Invalid credentials"

        }

    token = generate_token({

        "username": username,

        "role": role

    })

    return {

        "token": token,

        "role": role

    }


@router.get("/validate")

def validate(token: str):

    payload = validate_token(
        token
    )

    if not payload:

        return {

            "error":
                "Invalid token"

        }

    return payload
