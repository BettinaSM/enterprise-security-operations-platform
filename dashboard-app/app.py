import streamlit as st

# ---------------------------
# SECURITY
# ---------------------------

from security.auth import login

from security.session import (
    create_session,
    logout,
    is_authenticated
)

# ---------------------------
# SECTIONS
# ---------------------------

from sections.dashboard import (
    render_dashboard
)

from sections.detections import (
    render_detections
)

from sections.threat_intelligence import (
    render_threat_intelligence
)

from sections.realtime import (
    render_realtime
)

from sections.incidents import (
    render_incidents
)

from sections.analytics import (
    render_analytics
)

from sections.cloud_security import (
    render_cloud_security
)

from sections.compliance import (
    render_compliance
)

from sections.executive import (
    render_executive
)

from sections.hunting import (
    render_hunting
)

# ---------------------------
# PARSERS
# ---------------------------

from parsers.log_parser import (
    read_log
)

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Enterprise SOC Platform",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------
# SESSION VALIDATION
# ---------------------------

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# ---------------------------
# LOGIN SCREEN
# ---------------------------

if not is_authenticated():

    st.title("🛡️ Enterprise Security Operations Platform")

    st.subheader("Authentication Required")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        role = login(
            username,
            password
        )

        if role:

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

if st.sidebar.button("Logout"):

    logout()

    st.rerun()

# ---------------------------
# LOAD LOGS
# ---------------------------

linux_logs = read_log(
    "agents/linux/auth.log"
)

aix_logs = read_log(
    "agents/aix/sudo.log"
)

events = linux_logs + aix_logs

# ---------------------------
# IOC DATA
# ---------------------------

ioc_matches = [
    "185.220.101.1"
]

# ---------------------------
# RENDER SECTIONS
# ---------------------------

render_dashboard()

render_detections(events)

render_threat_intelligence(
    ioc_matches,
    "threat-intelligence/threat-feed.json"
)

render_realtime()

render_incidents()

render_analytics()

render_cloud_security()

render_compliance()

render_hunting()

render_executive()
