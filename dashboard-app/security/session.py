import streamlit as st

from datetime import (
    datetime,
    timedelta
)

SESSION_TIMEOUT_MINUTES = 30

# ---------------------------
# CREATE SESSION
# ---------------------------

def create_session(
    username,
    role
):

    st.session_state["authenticated"] = True

    st.session_state["username"] = username

    st.session_state["role"] = role

    st.session_state["last_activity"] = datetime.utcnow()

# ---------------------------
# VALIDATE SESSION
# ---------------------------

def is_authenticated():

    authenticated = st.session_state.get(
        "authenticated",
        False
    )

    if not authenticated:

        return False

    last_activity = st.session_state.get(
        "last_activity"
    )

    if not last_activity:

        return False

    now = datetime.utcnow()

    timeout = timedelta(
        minutes=SESSION_TIMEOUT_MINUTES
    )

    if now - last_activity > timeout:

        logout()

        return False

    st.session_state["last_activity"] = now

    return True

# ---------------------------
# GET ROLE
# ---------------------------

def get_role():

    return st.session_state.get(
        "role",
        "viewer"
    )

# ---------------------------
# GET USERNAME
# ---------------------------

def get_username():

    return st.session_state.get(
        "username",
        "unknown"
    )

# ---------------------------
# LOGOUT
# ---------------------------

def logout():

    st.session_state.clear()
