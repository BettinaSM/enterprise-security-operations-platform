import streamlit as st

def require_auth():

    authenticated = st.session_state.get(
        "authenticated",
        False
    )

    if not authenticated:

        st.warning(
            "Please login first"
        )

        st.stop()
