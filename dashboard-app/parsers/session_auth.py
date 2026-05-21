import streamlit as st

def require_auth():

    if "authenticated" not in st.session_state:

        st.warning(
            "Please login first"
        )

        st.stop()

    if not st.session_state["authenticated"]:

        st.warning(
            "Please login first"
        )

        st.stop()
