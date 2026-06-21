import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.datalake_engine import (
    load_events
)

require_auth()

st.title(

    "Security Data Lake"

)

events = load_events()

st.metric(

    "Stored Events",

    len(events)

)

st.dataframe(

    pd.DataFrame(events),

    use_container_width=True

)
