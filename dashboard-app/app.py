import streamlit as st

# ---------------------------
# SECURITY
# ---------------------------

from security.auth import (
    login
)

from security.session import (
    create_session,
    logout,
    is_authenticated
)

# ---------------------------
# DATABASE
# ---------------------------

from parsers.database_engine import (
    create_tables
)

# ---------------------------
# COLLECTORS
# ---------------------------

from collectors.linux_collector import (
    collect_linux_logs
)

from collectors.aix_collector import (
    collect_aix_logs
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

from sections.compliance import (
    render_compliance
)

from sections.cloud_security import (
    render_cloud_security
)

from sections.hunting import (
    render_hunting
)

from sections.executive import (
    render_executive
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
# INITIALIZE DATABASE
# ---------------------------

create_tables()

# ---------------------------
# SIDEBAR
# ---------------------------

st.sidebar.title(
    "Enterprise SOC Platform"
)

# ---------------------------
# AUTHENTICATION
# ---------------------------

if not is_authenticated():

    st.sidebar.subheader(
        "Authentication"
    )

    username = st.sidebar.text_input(
        "Username"
    )

    password = st.sidebar.text_input(
        "Password",
        type="password"
    )

    if st.sidebar.button("Login"):

        role = login(
            username,
            password
        )

        if role:

            create_session(role)

            st.sidebar.success(
                f"Authenticated as: {role}"
            )

            st.rerun()

        else:

            st.sidebar.error(
                "Invalid credentials"
            )

    st.warning(
        "Please authenticate to access the platform"
    )

    st.stop()

# ---------------------------
# ACTIVE SESSION
# ---------------------------

role = st.session_state.get(
    "role",
    "analyst"
)

st.sidebar.success(
    f"Authenticated as: {role}"
)

if st.sidebar.button("Logout"):

    logout()

    st.rerun()

# ---------------------------
# NAVIGATION
# ---------------------------

section = st.sidebar.radio(
    "SOC Navigation",
    [
        "Dashboard",
        "Detections",
        "Threat Intelligence",
        "Real-Time Monitoring",
        "Incidents",
        "Analytics",
        "Compliance",
        "Cloud Security",
        "Threat Hunting",
        "Executive"
    ]
)

# ---------------------------
# LOAD SECURITY EVENTS
# ---------------------------

linux_logs = collect_linux_logs()

aix_logs = collect_aix_logs()

events = (
    linux_logs +
    aix_logs
)

# ---------------------------
# IOC SIMULATION
# ---------------------------

ioc_matches = [
    "185.220.101.1",
    "192.168.100.50"
]

# ---------------------------
# HEADER
# ---------------------------

st.title(
    "🛡️ Enterprise Security Operations Platform"
)

st.markdown("""
Unified SOC platform providing:

- Linux Monitoring
- AIX Monitoring
- Threat Intelligence
- SIEM Correlation
- UEBA Analytics
- MITRE ATT&CK Mapping
- Threat Hunting
- Incident Response
- Compliance Monitoring
- Executive Reporting
""")

# ---------------------------
# ROUTING
# ---------------------------

if section == "Dashboard":

    render_dashboard()

elif section == "Detections":

    render_detections(events)

elif section == "Threat Intelligence":

    render_threat_intelligence(
        ioc_matches,
        "threat-intelligence/threat-feed.json"
    )

elif section == "Real-Time Monitoring":

    render_realtime()

elif section == "Incidents":

    render_incidents()

elif section == "Analytics":

    render_analytics()

elif section == "Compliance":

    render_compliance(role)

elif section == "Cloud Security":

    render_cloud_security()

elif section == "Threat Hunting":

    render_hunting(events)

elif section == "Executive":

    render_executive()

# ---------------------------
# FOOTER
# ---------------------------

st.divider()

st.caption(
    "Enterprise Security Operations Platform | SOC Engineering Lab"
)
