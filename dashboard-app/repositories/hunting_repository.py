from parsers.database_engine import (
    save_hunting_query,
    load_hunting_queries
)

def save_hunt_query_repository(
    query,
    analyst
):

    save_hunting_query(
        query,
        analyst
    )

def load_hunt_queries_repository():

    return load_hunting_queries()
