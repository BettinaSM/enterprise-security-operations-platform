import streamlit as st

# ---------------------------
# DATABASE
# ---------------------------

from parsers.database_engine import (
    create_tables
)

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
# PARSERS
# ---------------------------

from parsers.log_parser import (
    read_log
)

from parsers.detection_engine import (
    run_detections
)

from parsers.yaml_detection_engine import (
    run_yaml_detections
)

from parsers.mitre_mapper import (
    map_to_mitre
)

from parsers.analytics_engine import (
    detection_analytics,
    incident_analytics
)

from parsers.threat_intelligence import (
    enrich_iocs
)

from parsers.threat_feed import (
    load_threat_feed,
    correlate_threat_feed
)

from parsers.cve_mapper import (
    enrich_cves
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
    render_executive_summary
)

from sections.hunting import (
    render_hunting
)

# ---------------------------
# INITIALIZE DATABASE
# ---------------------------

create_tables()

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

    st.title(
        "🛡️ Enterprise Security Operations Platform"
    )

    st.subheader(
        "Authentication Required"
    )

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

events = (
    linux_logs +
    aix_logs
)

# ---------------------------
# IOC DATA
# ---------------------------

ioc_matches = [
    "185.220.101.1",
    "malicious-domain.com"
]

# ---------------------------
# DETECTIONS
# ---------------------------

detections = run_detections(
    events
)

yaml_detections = run_yaml_detections(
    events
)

mitre_events = map_to_mitre(
    events
)

# ---------------------------
# ANALYTICS
# ---------------------------

detection_stats = detection_analytics()

incident_stats = incident_analytics()

# ---------------------------
# CLOUD FINDINGS
# ---------------------------

cloud_findings = [

    {
        "Cloud": "AWS",
        "Finding": "Privileged Activity",
        "Severity": "Critical"
    },

    {
        "Cloud": "Azure",
        "Finding": "Failed Login",
        "Severity": "High"
    }
]

# ---------------------------
# THREAT INTELLIGENCE
# ---------------------------

threat_feed = load_threat_feed(
    "threat-intelligence/threat-feed.json"
)

feed_correlations = correlate_threat_feed(
    ioc_matches,
    threat_feed
)

enriched_iocs = enrich_iocs(
    ioc_matches
)

cve_findings = enrich_cves(
    ioc_matches
)

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
- MITRE ATT&CK Mapping
- Threat Hunting
- Incident Response
- Compliance Monitoring
- Executive Reporting

""")

# ---------------------------
# RENDER SECTIONS
# ---------------------------

render_dashboard()

render_detections(
    detections,
    yaml_detections,
    mitre_events
)

render_threat_intelligence(
    enriched_iocs,
    feed_correlations,
    cve_findings
)

render_realtime()

render_incidents()

render_analytics(
    detection_stats,
    incident_stats
)

render_cloud_security(
    cloud_findings
)

render_compliance()

render_hunting(
    events
)

render_executive_summary()

# ---------------------------
# FOOTER
# ---------------------------

st.divider()

st.caption(
    "Enterprise Security Operations Platform | SOC Engineering Lab"
)
