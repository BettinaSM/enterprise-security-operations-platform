import streamlit as st

from security.session import (
    is_authenticated
)

def require_auth():

    if not is_authenticated():

        st.warning(
            "Please authenticate"
        )

        st.stop()
