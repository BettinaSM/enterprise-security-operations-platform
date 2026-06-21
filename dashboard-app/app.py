import streamlit as st

from parsers.database_engine import (
    create_tables
)

from security.auth import (
    login
)

from security.session import (
    create_session,
    logout,
    is_authenticated
)

from scheduler.scheduler_engine import scheduler

if "scheduler_started" not in st.session_state:

    scheduler.start()

    st.session_state[
        "scheduler_started"
    ] = True
    
# ---------------------------
# DATABASE
# ---------------------------

from database.database import (
    Base,
    engine
)

# cria tabelas automaticamente
Base.metadata.create_all(
    bind=engine
)

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Enterprise Security Operations Platform",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------
# SESSION INIT
# ---------------------------

if "authenticated" not in st.session_state:

    st.session_state["authenticated"] = False

# ---------------------------
# LOGIN
# ---------------------------

if not is_authenticated():

    st.title(
        "🛡️ Enterprise Security Operations Platform"
    )

    st.subheader(
        "Authentication Required"
    )

    username = st.text_input(
        "Username",
        key="login_username"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button(
        "Login",
        key="login_button"
    ):

        role = login(
            username,
            password
        )

        if role:

            from services.audit_trail_service import (
                register_action
            )

            register_action(

                username,

                "User Login"
            )
            
            create_session(
                username,
                role
            )

            st.success(
                f"Authenticated as {role}"
            )

            st.rerun()

        else:

            st.error(
                "Invalid credentials"
            )

    st.stop()

# ---------------------------
# SIDEBAR
# ---------------------------

st.sidebar.title(
    "SOC Navigation"
)

st.sidebar.success(
    f"Authenticated as: {st.session_state['role']}"
)

if st.sidebar.button(
    "Logout",
    key="logout_button"
):

    register_action(

        st.session_state["username"],

        "User Logout"
    )

    logout()

    st.rerun()

# ---------------------------
# LANDING
# ---------------------------

st.title(
    "🛡️ Enterprise Security Operations Platform"
)

st.markdown("""

Select a module from the left sidebar.

Available capabilities:

- SOC Operations
- Threat Intelligence
- Detection Engineering
- Threat Hunting
- Cloud Security
- IAM Governance
- Compliance & Audit
- SOAR Automation
- Live Monitoring
- Executive Reporting

""")
