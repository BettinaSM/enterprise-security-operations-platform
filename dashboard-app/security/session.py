import streamlit as st

def create_session(role):

    st.session_state["authenticated"] = True

    st.session_state["role"] = role

def logout():

    st.session_state.clear()

def is_authenticated():

    return st.session_state.get(
        "authenticated",
        False
    )
