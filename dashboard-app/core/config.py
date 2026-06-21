import os


class Config:

    DEBUG = os.getenv(

        "DEBUG",

        "False"

    ) == "True"

    ENVIRONMENT = os.getenv(

        "ENVIRONMENT",

        "development"

    )

    LDAP_ENABLED = os.getenv(

        "LDAP_ENABLED",

        "False"

    ) == "True"

    AD_ENABLED = os.getenv(

        "AD_ENABLED",

        "False"

    ) == "True"

    CLOUD_ENABLED = os.getenv(

        "CLOUD_ENABLED",

        "True"

    ) == "True"

    VERSION = "1.0.0"
