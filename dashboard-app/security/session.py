import streamlit as st

# ---------------------------
# CREATE SESSION
# ---------------------------

def create_session(role):

    st.session_state["authenticated"] = True

    st.session_state["role"] = role

# ---------------------------
# CHECK SESSION
# ---------------------------

def is_authenticated():

    return st.session_state.get(
        "authenticated",
        False
    )

# ---------------------------
# LOGOUT
# ---------------------------

def logout():

    st.session_state.clear()
