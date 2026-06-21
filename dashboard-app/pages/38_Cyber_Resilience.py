import streamlit as st

from parsers.resilience_engine import (
    calculate_resilience
)

from parsers.session_auth import (
    require_auth
)

require_auth()

st.title(
    "Cyber Resilience Dashboard"
)

resilience = calculate_resilience()

st.metric(

    "Cyber Resilience Score",

    f"{resilience['score']}%"
)

st.metric(

    "Registered Incidents",

    resilience["incidents"]
)

st.metric(

    "Backup Status",

    str(

        resilience["backup_status"]

    )
)
