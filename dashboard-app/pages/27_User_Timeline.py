import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.timeline_engine import (
    get_user_timeline
)

require_auth()

st.title(
    "User Timeline"
)

username = st.text_input(
    "Username"
)

if st.button(
    "Search Timeline"
):

    events = get_user_timeline(
        username
    )

    st.dataframe(

        pd.DataFrame(events),

        use_container_width=True
    )
