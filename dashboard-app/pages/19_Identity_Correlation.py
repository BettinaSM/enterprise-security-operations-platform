import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.identity_correlation import (
    correlate_identity
)

require_auth()

st.title(
    "Identity Correlation"
)

username = st.text_input(
    "Username"
)

if st.button(
    "Search Identity"
):

    results = correlate_identity(
        username
    )

    for source, data in results.items():

        st.subheader(
            source.upper()
        )

        if data:

            st.dataframe(
                pd.DataFrame(data)
            )

        else:

            st.info(
                "No records found"
            )
