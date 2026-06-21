import os

from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv(
    "APP_NAME",
    "Enterprise Security Operations Platform"
)

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development"
)

DEBUG = os.getenv(
    "DEBUG",
    "False"
).lower() == "true"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///security_platform.db"
)

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "change-me"
)

JWT_SECRET = os.getenv(
    "JWT_SECRET",
    "change-me"
)

LDAP_SERVER = os.getenv(
    "LDAP_SERVER"
)

AD_SERVER = os.getenv(
    "AD_SERVER"
)
