import streamlit as st
import pandas as pd

from parsers.timeline_engine import (
    get_user_timeline
)

username = st.text_input(

    "Username"

)

if username:

    st.dataframe(

        pd.DataFrame(

            get_user_timeline(
                username
            )

        )

    )
