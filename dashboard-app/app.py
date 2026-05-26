import streamlit as st

from security.auth import (
    login
)

from security.session import (
    create_session,
    logout
)

from sections.dashboard import (
    render_dashboard
)

from sections.detections import (
    render_detections
)

from sections.threat_intel import (
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

from parsers.log_parser import (
    read_log
)

st.set_page_config(
    page_title="Enterprise SOC",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------
# AUTH
# ---------------------------

st.sidebar.title(
    "Authentication"
)

username = st.sidebar.text_input(
    "Username"
)

password = st.sidebar.text_input(
    "Password",
    type="password"
)

role = login(
    username,
    password
)

if not role:

    st.warning(
        "Please authenticate"
    )

    st.stop()

create_session(role)

st.sidebar.success(
    f"Authenticated as: {role}"
)

if st.sidebar.button("Logout"):

    logout()

    st.rerun()

# ---------------------------
# LOAD EVENTS
# ---------------------------

linux_logs = read_log(
    "agents/linux/auth.log"
)

aix_logs = read_log(
    "agents/aix/sudo.log"
)

events = (
    linux_logs +
    aix_logs
)

ioc_matches = [
    "185.220.101.1"
]

# ---------------------------
# RENDER UI
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
