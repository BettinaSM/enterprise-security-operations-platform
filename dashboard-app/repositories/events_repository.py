from parsers.database_engine import (
    connect_db
)

import pandas as pd

def load_security_events():

    connection = connect_db()

    df = pd.read_sql_query(
        """
        SELECT * FROM security_events
        ORDER BY id DESC
        LIMIT 100
        """,
        connection
    )

    connection.close()

    return df
