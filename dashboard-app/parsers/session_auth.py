import streamlit as st

from datetime import (
    datetime,
    timedelta
)

SESSION_TIMEOUT_MINUTES = 30

# ---------------------------
# VALIDATE SESSION
# ---------------------------

def validate_session():

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

    session_age = now - last_activity

    if session_age > timedelta(
        minutes=SESSION_TIMEOUT_MINUTES
    ):

        logout()

        return False

    st.session_state[
        "last_activity"
    ] = now

    return True

# ---------------------------
# REQUIRE AUTH
# ---------------------------

def require_auth():

    if not validate_session():

        st.warning(
            "Session expired. Please login again."
        )

        st.stop()

# ---------------------------
# LOGIN USER
# ---------------------------

def login_user(role):

    st.session_state[
        "authenticated"
    ] = True

    st.session_state[
        "role"
    ] = role

    st.session_state[
        "last_activity"
    ] = datetime.utcnow()

# ---------------------------
# LOGOUT
# ---------------------------

def logout():

    for key in list(
        st.session_state.keys()
    ):

        del st.session_state[key]
