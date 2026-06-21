from elasticsearch import Elasticsearch

from secrets.secrets_manager import (
    get_secret
)


def get_elastic_client():

    return Elasticsearch(

        get_secret("ELASTIC_URL"),

        basic_auth=(

            get_secret(
                "ELASTIC_USER"
            ),

            get_secret(
                "ELASTIC_PASSWORD"
            )

        )

    )
