import streamlit as st
import json
import time
import requests

from parsers.session_auth import (
    login_user,
    logout
)

# ---------------------------
# AUTH
# ---------------------------

from parsers.auth_engine import authenticate

from parsers.rbac_engine import (
    has_permission
)

# ---------------------------
# DATABASE
# ---------------------------

from parsers.database_engine import (
    create_tables,
    save_incident,
    save_detection,
    load_incidents,
    load_detections
)

# ---------------------------
# ANALYTICS
# ---------------------------

from parsers.analytics_engine import (
    detection_analytics,
    incident_analytics
)

# ---------------------------
# LOG PARSERS
# ---------------------------

from parsers.log_parser import (
    read_log,
    count_failed_auth,
    count_critical,
    detect_bruteforce
)

from parsers.cloud_parser import (
    load_json_log,
    detect_failed_cloud_login,
    detect_privileged_activity,
    calculate_severity
)

# ---------------------------
# THREAT INTEL
# ---------------------------

from parsers.ioc_matcher import (
    match_ioc
)

from parsers.threat_feed import (
    load_threat_feed,
    correlate_threat_feed
)

from parsers.threat_intelligence import (
    enrich_iocs
)

from parsers.cve_mapper import (
    enrich_cves
)

# ---------------------------
# DETECTIONS
# ---------------------------

from parsers.detection_engine import (
    run_detections
)

from parsers.yaml_detection_engine import (
    run_yaml_detections
)

from parsers.mitre_mapper import (
    map_to_mitre
)

# ---------------------------
# RISK
# ---------------------------

from parsers.risk_engine import (
    calculate_risk_score
)

from parsers.threat_scoring import (
    calculate_threat_score
)

# ---------------------------
# REALTIME
# ---------------------------

from parsers.live_metrics import (
    generate_live_metrics
)

from parsers.realtime_engine import (
    generate_realtime_event
)

# ---------------------------
# UEBA
# ---------------------------

from parsers.ueba_engine import (
    analyze_user_behavior
)

# ---------------------------
# REPORTING
# ---------------------------

from parsers.reporting_engine import (
    generate_executive_report
)

# ---------------------------
# SETTINGS
# ---------------------------

from configs.settings import (
    APP_NAME,
    SIMULATIONS_DIR
)

# ---------------------------
# SECTIONS
# ---------------------------

from sections.kpis import (
    render_kpis
)

from sections.detections import (
    render_detections
)

from sections.threat_intelligence import (
    render_threat_intelligence
)

from sections.compliance import (
    render_compliance
)

from sections.cloud_security import (
    render_cloud_security
)

from sections.analytics import (
    render_analytics
)

from sections.hunting import (
    render_hunting
)

from sections.executive import (
    render_executive_summary
)

from sections.realtime import (
    render_realtime_events
)

# ---------------------------
# STREAMLIT CONFIG
# ---------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------
# AUTHENTICATION
# ---------------------------

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

role = authenticate(
    username,
    password
)

if not role:

    st.warning(
        "Please authenticate to access the platform"
    )

    st.stop()

login_user(role)

st.sidebar.success(
    f"Authenticated as: {role}"
)

st.sidebar.divider()

if st.sidebar.button("Logout"):

    st.session_state.clear()

    st.rerun()

# ---------------------------
# DATABASE INIT
# ---------------------------

create_tables()

# ---------------------------
# HEADER
# ---------------------------

st.title(APP_NAME)

st.markdown("""

Unified Enterprise Security Operations Platform covering:

- Linux
- AIX
- Windows
- AWS
- Azure
- GCP
- OCI
- IBM Cloud
- Kubernetes

""")

# ---------------------------
# LOAD LOGS
# ---------------------------

linux_logs = read_log(
    "agents/linux/auth.log"
)

aix_logs = read_log(
    "agents/aix/sudo.log"
)

falco_logs = read_log(
    "logs/falco-events.log"
)

# ---------------------------
# CLOUD LOGS
# ---------------------------

aws_log = load_json_log(
    "agents/aws/cloudtrail.json"
)

azure_log = load_json_log(
    "agents/azure/entra-signins.json"
)

gcp_log = load_json_log(
    "agents/gcp/audit-logs.json"
)

# ---------------------------
# CLOUD FINDINGS
# ---------------------------

cloud_findings = []

cloud_events = [

    ("AWS", aws_log),
    ("Azure", azure_log),
    ("GCP", gcp_log)

]

for provider, event in cloud_events:

    if not event:
        continue

    if detect_failed_cloud_login(event):

        cloud_findings.append({

            "Cloud": provider,
            "Finding": "Failed Authentication",
            "Severity": calculate_severity(event)

        })

    if detect_privileged_activity(event):

        cloud_findings.append({

            "Cloud": provider,
            "Finding": "Privileged Activity",
            "Severity": "Critical"

        })

        save_incident(
            "Critical",
            provider,
            "Privileged cloud activity detected",
            "Open"
        )

# ---------------------------
# IOC MATCHING
# ---------------------------

ioc_matches = match_ioc(
    linux_logs
)

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
# DETECTIONS
# ---------------------------

detections = run_detections(

    linux_logs +
    aix_logs +
    falco_logs

)

yaml_detections = run_yaml_detections(

    linux_logs +
    aix_logs +
    falco_logs

)

mitre_events = map_to_mitre(

    linux_logs +
    aix_logs +
    falco_logs

)

# ---------------------------
# SAVE DETECTIONS
# ---------------------------

for detection in detections:

    save_detection(

        detection.get(
            "Detection",
            "Unknown"
        ),

        detection.get(
            "Severity",
            "Medium"
        ),

        str(detection)

    )

# ---------------------------
# UEBA
# ---------------------------

ueba_findings = analyze_user_behavior(

    linux_logs +
    aix_logs +
    falco_logs

)

# ---------------------------
# METRICS
# ---------------------------

failed_auth = (
    count_failed_auth(linux_logs)
    +
    count_failed_auth(aix_logs)
)

critical_alerts = count_critical(
    falco_logs
)

# ---------------------------
# THREAT SCORE
# ---------------------------

threat_score, threat_severity = calculate_threat_score(

    critical_alerts,
    failed_auth,
    len(cloud_findings),
    len(ioc_matches)

)

# ---------------------------
# RISK SCORE
# ---------------------------

risk_score, risk_level = calculate_risk_score(
    detections
)

# ---------------------------
# REPORT
# ---------------------------

report_file = generate_executive_report(

    threat_score,
    risk_level,
    len(cloud_findings),
    critical_alerts

)

# ---------------------------
# RENDER SECTIONS
# ---------------------------

render_kpis(

    threat_score,
    threat_severity,
    risk_score,
    risk_level

)

render_cloud_security(
    cloud_findings
)

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

render_realtime_events(
    falco_logs
)

render_hunting(

    linux_logs +
    aix_logs +
    falco_logs

)

# ---------------------------
# ANALYTICS
# ---------------------------

detection_stats = detection_analytics()

incident_stats = incident_analytics()

render_analytics(

    detection_stats,
    incident_stats

)

# ---------------------------
# COMPLIANCE
# ---------------------------

if has_permission(
    role,
    "compliance"
):

    render_compliance()

# ---------------------------
# EXECUTIVE
# ---------------------------

if has_permission(
    role,
    "executive"
):

    render_executive_summary()

# ---------------------------
# BRUTEFORCE ALERT
# ---------------------------

if detect_bruteforce(
    linux_logs
):

    st.error(
        "Potential SSH brute force attack detected"
    )

# ---------------------------
# LIVE METRICS
# ---------------------------

st.subheader(
    "Live SOC Metrics"
)

metrics_placeholder = st.empty()

for _ in range(3):

    metrics = generate_live_metrics()

    with metrics_placeholder.container():

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Critical Alerts",
            metrics["critical_alerts"]
        )

        col2.metric(
            "Runtime Threats",
            metrics["runtime_threats"]
        )

        col3.metric(
            "Failed Auth",
            metrics["failed_auth"]
        )

        col4.metric(
            "Incidents",
            metrics["incidents"]
        )

    time.sleep(0.5)

# ---------------------------
# REALTIME EVENTS
# ---------------------------

st.subheader(
    "Real-Time Security Events"
)

for _ in range(3):

    realtime_event = generate_realtime_event()

    severity = realtime_event["severity"]

    if severity == "Critical":

        st.error(realtime_event)

    elif severity == "High":

        st.warning(realtime_event)

    elif severity == "Medium":

        st.info(realtime_event)

    else:

        st.success(realtime_event)

# ---------------------------
# DOWNLOAD REPORT
# ---------------------------

st.subheader(
    "Executive Security Report"
)

with open(
    report_file,
    "rb"
) as pdf_file:

    st.download_button(

        label="Download Executive PDF Report",

        data=pdf_file,

        file_name="executive_security_report.pdf",

        mime="application/pdf"

    )
