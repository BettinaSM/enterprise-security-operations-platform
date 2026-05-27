import streamlit as st
from datetime import datetime, timedelta

SESSION_TIMEOUT_MINUTES = 30

# ---------------------------
# CREATE SESSION
# ---------------------------

def create_session(role):

    st.session_state["authenticated"] = True

    st.session_state["role"] = role

# ---------------------------
# VALIDATE SESSION
# ---------------------------

def is_authenticated():

    return st.session_state.get(
        "authenticated",
        False
    )

# ---------------------------
# GET ROLE
# ---------------------------

def get_role():

    return st.session_state.get(
        "role",
        "viewer"
    )

# ---------------------------
# LOGOUT
# ---------------------------

def logout():

    st.session_state.clear()
