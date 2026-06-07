import streamlit as st
import sqlite3
import pandas as pd

from parsers.session_auth import (
    require_auth
)

require_auth()

st.title(
    "Live Security Monitoring"
)

connection = sqlite3.connect(
    "database/security.db"
)

query = """
SELECT *
FROM security_events
ORDER BY id DESC
LIMIT 50
"""

df = pd.read_sql_query(
    query,
    connection
)

st.dataframe(
    df,
    use_container_width=True
)
