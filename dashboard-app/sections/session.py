import streamlit as st

def create_session(
    username,
    role
):

    st.session_state["authenticated"] = True
    st.session_state["username"] = username
    st.session_state["role"] = role

def is_authenticated():

    return st.session_state.get(
        "authenticated",
        False
    )

def logout():

    st.session_state.clear()
