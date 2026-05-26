import streamlit as st
import pandas as pd
import plotly.express as px
import json
import time
import requests

from parsers.rbac_engine import (
    has_permission
)

from parsers.analytics_engine import (
    detection_analytics,
    incident_analytics
)

from parsers.database_engine import (
    create_tables,
    save_incident,
    load_incidents,
    save_detection,
    load_detections
)

from parsers.cve_mapper import (
    enrich_cves
)

from parsers.live_metrics import (
    generate_live_metrics
)

from parsers.auth_engine import authenticate

from parsers.realtime_engine import (
    generate_realtime_event
)

from parsers.threat_feed import (
    load_threat_feed,
    correlate_threat_feed
)

from parsers.correlation_engine import (
    correlate_security_events
)

from parsers.reporting_engine import (
    generate_executive_report
)

from parsers.ioc_matcher import match_ioc

from parsers.ueba_engine import (
    analyze_user_behavior
)

from parsers.threat_scoring import calculate_threat_score

from parsers.threat_intelligence import (
    enrich_iocs
)

from parsers.mitre_mapper import map_to_mitre

from parsers.detection_engine import run_detections

from parsers.risk_engine import calculate_risk_score

from parsers.yaml_detection_engine import (
    run_yaml_detections
)

from parsers.rule_engine import load_rule

from parsers.attack_chain import build_attack_chain

from parsers.incident_manager import (
    generate_incidents
)

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

st.set_page_config(
    page_title="Unified Enterprise Security Operations Platform",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------
# AUTHENTICATION
# ---------------------------

st.sidebar.subheader("Authentication")

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

create_tables()

st.sidebar.success(
    f"Authenticated as: {role}"
)

st.session_state["authenticated"] = True
st.session_state["role"] = role

# ---------------------------
# BASE PATHS
# ---------------------------

from configs.settings import (
    APP_NAME,
    SIMULATIONS_DIR,
    RULES_DIR
)

# ---------------------------
# HEADER
# ---------------------------

st.sidebar.title("SOC Navigation")

st.sidebar.markdown("""
## Security Monitoring
- Dashboard
- Runtime Security
- Cloud Security
- Threat Intelligence

## Detection Engineering
- MITRE ATT&CK
- IOC Matching
- Threat Scoring
- Attack Simulation

## Incident Response
- Incident Timeline
- Incident Drilldown
- SOAR Automation

## Governance
- Compliance Dashboard
- Executive Summary
""")

st.title(APP_NAME)

st.markdown("""
Unified Security Operations monitoring platform covering:

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
# FILTERS
# ---------------------------

severity_filter = st.sidebar.selectbox(
    "Filter Severity",
    ["All", "Critical", "High", "Medium"]
)

# ---------------------------
# READ LOGS
# ---------------------------

linux_logs = read_log("agents/linux/auth.log")
aix_logs = read_log("agents/aix/sudo.log")
falco_logs = read_log("logs/falco-events.log")

# ---------------------------
# CLOUD LOGS
# ---------------------------

aws_log = load_json_log("agents/aws/cloudtrail.json")
azure_log = load_json_log("agents/azure/entra-signins.json")
gcp_log = load_json_log("agents/gcp/audit-logs.json")
oci_log = load_json_log("agents/oracle-cloud/oci-audit.json")
ibm_log = load_json_log("agents/ibm-cloud/activity-tracker.json")


# ---------------------------
# SECURITY KPIs
# ---------------------------

st.subheader("Security Operations KPIs")

kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

kpi_col1.metric(
    "Mean Time To Detect",
    "4 min"
)

kpi_col2.metric(
    "Mean Time To Respond",
    "11 min"
)

kpi_col3.metric(
    "Detection Coverage",
    "91%"
)

# ---------------------------
# CLOUD DETECTIONS
# ---------------------------

cloud_findings = []

cloud_events = [
    ("AWS", aws_log),
    ("Azure", azure_log),
    ("GCP", gcp_log),
    ("OCI", oci_log),
    ("IBM Cloud", ibm_log)
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

ioc_matches = match_ioc(linux_logs)

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

mitre_events = map_to_mitre(
    linux_logs + aix_logs + falco_logs
)

detections = run_detections(
    linux_logs +
    aix_logs +
    falco_logs
)

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

yaml_detections = run_yaml_detections(
    linux_logs +
    aix_logs +
    falco_logs
)

risk_score, risk_level = calculate_risk_score(
    detections
)

ueba_findings = analyze_user_behavior(
    linux_logs +
    aix_logs +
    falco_logs
)

if ioc_matches:

    st.warning(
        f"Known malicious IOC detected: {', '.join(ioc_matches)}"
    )

for ioc in ioc_matches:

    save_detection(
        "IOC Match",
        "High",
        ioc
    )
    
# ---------------------------
# SECURITY EVENTS
# ---------------------------

with open(
    SIMULATIONS_DIR / "security-events.json",
    "r"
) as file:

    security_events = json.load(file)

filtered_events = []

for event in security_events:

    if severity_filter == "All":

        filtered_events.append(event)

    elif event["severity"] == severity_filter:

        filtered_events.append(event)

# ---------------------------
# METRICS
# ---------------------------

failed_auth = (
    count_failed_auth(linux_logs)
    + count_failed_auth(aix_logs)
)

critical_alerts = count_critical(falco_logs)

runtime_events = len(falco_logs)

incidents = len(cloud_findings)

# ---------------------------
# ATTACK CHAIN
# ---------------------------

incidents_data = generate_incidents()

attack_chain = build_attack_chain(
    failed_auth,
    cloud_findings,
    ioc_matches,
    critical_alerts
)

correlations = correlate_security_events(
    failed_auth,
    critical_alerts,
    cloud_findings,
    ioc_matches
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

report_file = generate_executive_report(
    threat_score,
    risk_level,
    incidents,
    critical_alerts
)

# ---------------------------
# ATTACK CHAIN VISUALIZATION
# ---------------------------

st.subheader("Attack Chain Progression")

if attack_chain:

    for step in attack_chain:

        st.warning(step)

else:

    st.success(
        "No active attack chain identified"
    )

# ---------------------------
# EVENT CORRELATION ENGINE
# ---------------------------

st.subheader("SIEM Correlation Engine")

if correlations:

    correlation_df = pd.DataFrame(
        correlations
    )

    st.dataframe(
        correlation_df,
        use_container_width=True
    )

else:

    st.success(
        "No correlated attack patterns identified"
    )

# ---------------------------
# THREAT PRIORITY
# ---------------------------

st.subheader("Threat Priority Assessment")

score_col1, score_col2 = st.columns(2)

score_col1.metric(
    "Threat Score",
    threat_score
)

score_col2.metric(
    "Threat Severity",
    threat_severity
)

if threat_severity == "Critical":

    st.error("Critical threat level detected")

elif threat_severity == "High":

    st.warning("High threat activity identified")

elif threat_severity == "Medium":

    st.info("Medium threat activity")

else:

    st.success("Low threat activity")


# ---------------------------
# AUTOMATED DETECTIONS
# ---------------------------

if detect_bruteforce(linux_logs):

    st.error("Potential SSH brute force attack detected")

# ---------------------------
# LIVE DASHBOARD METRICS
# ---------------------------

st.subheader("Live SOC Metrics")

metrics_placeholder = st.empty()

for _ in range(5):

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

st.divider()

st.subheader("Enterprise Risk Assessment")

risk_col1, risk_col2 = st.columns(2)

risk_col1.metric(
    "Enterprise Risk Score",
    risk_score
)

risk_col2.metric(
    "Enterprise Risk Level",
    risk_level
)

if risk_level == "Critical":

    st.error(
        "Critical enterprise-wide security exposure"
    )

elif risk_level == "High":

    st.warning(
        "High enterprise security risk identified"
    )

elif risk_level == "Medium":

    st.info(
        "Moderate enterprise security risk"
    )

else:

    st.success(
        "Enterprise environment operating normally"
    )
    
# ---------------------------
# ALERT SEVERITY CHART
# ---------------------------

st.subheader("Alert Severity Distribution")

severity_df = pd.DataFrame({
    "Severity": ["Critical", "High", "Medium"],
    "Count": [4, 7, 12]
})

fig = px.bar(
    severity_df,
    x="Severity",
    y="Count",
    title="Security Alerts"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------------------
# ENVIRONMENT COVERAGE
# ---------------------------

st.subheader("Environment Coverage")

env_df = pd.DataFrame({
    "Environment": [
        "Linux",
        "AIX",
        "Windows",
        "AWS",
        "Azure",
        "GCP",
        "OCI",
        "IBM Cloud",
        "Kubernetes"
    ],
    "Monitoring": [
        "Enabled",
        "Enabled",
        "Enabled",
        "Enabled",
        "Enabled",
        "Enabled",
        "Enabled",
        "Enabled",
        "Enabled"
    ]
})

st.dataframe(env_df, use_container_width=True)

st.divider()

# ---------------------------
# MITRE MAPPING
# ---------------------------

st.subheader("MITRE ATT&CK Coverage")

mitre_df = pd.DataFrame(mitre_events)

st.dataframe(
    mitre_df,
    use_container_width=True
)

st.divider()

# ---------------------------
# MITRE DISTRIBUTION
# ---------------------------

mitre_chart = pd.DataFrame({
    "Technique": [
        "T1059",
        "T1110",
        "T1611",
        "T1078"
    ],
    "Events": [
        7,
        12,
        4,
        6
    ]
})

mitre_fig = px.bar(
    mitre_chart,
    x="Technique",
    y="Events",
    title="MITRE ATT&CK Techniques"
)

st.plotly_chart(mitre_fig, use_container_width=True)

# ---------------------------
# DETECTION ENGINE
# ---------------------------

st.subheader("Detection Engine Findings")

if detections:

    detection_df = pd.DataFrame(detections)

    st.dataframe(
        detection_df,
        use_container_width=True
    )

else:

    st.success(
        "No active detections identified"
    )

# ---------------------------
# YAML Detection Rules
# ---------------------------

st.subheader("YAML Detection Rules")

if yaml_detections:

    yaml_df = pd.DataFrame(
        yaml_detections
    )

    st.dataframe(
        yaml_df,
        use_container_width=True
    )

else:

    st.success(
        "No YAML detections identified"
    )

# ---------------------------
# DETECTION-AS-CODE
# ---------------------------

st.subheader("Detection-as-Code Rule")

rule = load_rule(
    RULES_DIR / "linux_bruteforce.yml"
)

st.json(rule)

# ---------------------------
# UEBA ANALYTICS
# ---------------------------

st.subheader("User & Entity Behavior Analytics")

if ueba_findings:

    ueba_df = pd.DataFrame(
        ueba_findings
    )

    st.dataframe(
        ueba_df,
        use_container_width=True
    )

else:

    st.success(
        "No anomalous behavior identified"
    )

# ---------------------------
# COMPLIANCE DASHBOARD
# ---------------------------

if has_permission(
    role,
    "compliance"
):

    st.subheader(
        "Compliance Overview"
    )

    compliance_df = pd.DataFrame({
        "Framework": [
            "ISO 27001",
            "NIST",
            "CIS Controls",
            "PCI-DSS"
        ],
        "Status": [
            "Compliant",
            "Partial",
            "Compliant",
            "In Review"
        ],
        "Coverage": [
            "92%",
            "81%",
            "89%",
            "74%"
        ]
    })

    st.dataframe(
        compliance_df,
        use_container_width=True
    )

# ---------------------------
# API THREAT FEED
# ---------------------------

api_threats = []

try:

    response = requests.get(
        "http://127.0.0.1:8000/threat-feed",
        timeout=5
    )

    if response.status_code == 200:

        api_data = response.json()

        api_threats = api_data.get(
            "threats",
            []
        )

except Exception:

    api_threats = []

# ---------------------------
# LIVE API THREAT FEED
# ---------------------------

st.subheader("Live API Threat Feed")

if api_threats:

    api_df = pd.DataFrame(
        api_threats
    )

    st.dataframe(
        api_df,
        use_container_width=True
    )

else:

    st.warning(
        "Threat feed API unavailable"
    )

# ---------------------------
# THREAT INTELLIGENCE
# ---------------------------

st.subheader("Threat Intelligence Enrichment")

if enriched_iocs:

    threat_df = pd.DataFrame(
        enriched_iocs
    )

    st.dataframe(
        threat_df,
        use_container_width=True
    )

else:

    st.success(
        "No malicious IOC enrichment identified"
    )

# ---------------------------
# THREAT FEED CORRELATION
# ---------------------------

st.subheader("External Threat Feed Correlation")

if feed_correlations:

    feed_df = pd.DataFrame(
        feed_correlations
    )

    st.dataframe(
        feed_df,
        use_container_width=True
    )

else:

    st.success(
        "No external threat feed matches identified"
    )

# ---------------------------
# CVE ENRICHMENT
# ---------------------------

st.subheader("Threat Intelligence CVE Correlation")

if cve_findings:

    cve_df = pd.DataFrame(
        cve_findings
    )

    st.dataframe(
        cve_df,
        use_container_width=True
    )

else:

    st.success(
        "No CVE correlations identified"
    )

# ---------------------------
# CLOUD SECURITY EVENTS
# ---------------------------

st.subheader("Cloud Security Findings")

if cloud_findings:

    cloud_df = pd.DataFrame(cloud_findings)

    st.dataframe(cloud_df, use_container_width=True)

else:

    st.info("No cloud findings detected")

# ---------------------------
# Kubernetes Runtime Security
# ---------------------------

st.subheader("Kubernetes Runtime Security")

with open(
    SIMULATIONS_DIR / "k8s-runtime.json",
    "r"
) as file:

    k8s_alerts = json.load(file)

k8s_df = pd.DataFrame(k8s_alerts)

st.dataframe(
    k8s_df,
    use_container_width=True
)

# ---------------------------
# ASSET CRITICALITY
# ---------------------------

st.subheader("Enterprise Asset Criticality")

with open(
    SIMULATIONS_DIR / "assets.json",
    "r"
) as file:

    asset_data = json.load(file)

asset_df = pd.DataFrame(asset_data)

st.dataframe(
    asset_df,
    use_container_width=True
)

# ---------------------------
# INCIDENT TIMELINE
# ---------------------------

st.subheader("Incident Timeline")

timeline_df = pd.DataFrame({
    "Time": [
        "10:15",
        "10:20",
        "10:22",
        "10:30"
    ],
    "Event": [
        "Failed SSH attempts detected",
        "Falco runtime alert",
        "SIEM correlation",
        "Container isolated"
    ]
})

st.table(timeline_df)

st.divider()

# ---------------------------
# SOC CASE MANAGEMENT
# ---------------------------

st.subheader("SOC Case Management")

db_incidents = load_incidents()

incident_cases_df = pd.DataFrame(
    db_incidents,
    columns=[
        "ID",
        "Severity",
        "Source",
        "Description",
        "Status"
    ]
)

st.dataframe(
    incident_cases_df,
    use_container_width=True
)

# ---------------------------
# INCIDENT RESPONSE METRICS
# ---------------------------

st.subheader("Incident Response Metrics")

metric_col1, metric_col2, metric_col3 = st.columns(3)

metric_col1.metric(
    "Open Incidents",
    "12"
)

metric_col2.metric(
    "Escalated Cases",
    "4"
)

metric_col3.metric(
    "SLA Compliance",
    "94%"
)

# ---------------------------
# INCIDENT DRILLDOWN
# ---------------------------

st.subheader("Incident Drilldown")

incident_df = pd.DataFrame({
    "Incident ID": [
        "INC-1001",
        "INC-1002",
        "INC-1003"
    ],
    "Severity": [
        "Critical",
        "High",
        "Medium"
    ],
    "Environment": [
        "Kubernetes",
        "Linux",
        "AWS"
    ],
    "Status": [
        "Open",
        "Investigating",
        "Contained"
    ]
})

selected_incident = st.selectbox(
    "Select Incident",
    incident_df["Incident ID"]
)

filtered_incident = incident_df[
    incident_df["Incident ID"] == selected_incident
]

st.dataframe(
    filtered_incident,
    use_container_width=True
)

# ---------------------------
# SOAR ACTIONS
# ---------------------------

if has_permission(
    role,
    "soar"
):

    st.subheader(
        "SOAR Automated Actions"
    )

    soar_df = pd.DataFrame({
        "Action": [
            "Block IOC",
            "Disable User",
            "Isolate Container",
            "Create Incident Ticket"
        ],
        "Status": [
            "Executed",
            "Pending",
            "Executed",
            "Executed"
        ]
    })

    st.dataframe(
        soar_df,
        use_container_width=True
    )

# ---------------------------
# LIVE EVENTS
# ---------------------------

st.subheader("Live Runtime Events")

for event in falco_logs[-10:]:
    st.code(event)

st.divider()

# ---------------------------
# LIVE EVENT STREAM
# ---------------------------

st.subheader("Real-Time Security Events")

live_placeholder = st.empty()

for _ in range(3):

    realtime_event = generate_realtime_event()

    with live_placeholder.container():

        severity = realtime_event["severity"]

        if severity == "Critical":

            st.error(realtime_event)

        elif severity == "High":

            st.warning(realtime_event)

        elif severity == "Medium":

            st.info(realtime_event)

        else:

            st.success(realtime_event)

    time.sleep(0.5)

# ---------------------------
# THREAT HUNTING CONSOLE
# ---------------------------

st.subheader("Threat Hunting Console")

hunt_term = st.text_input(
    "Hunt for indicators, users, IPs or commands"
)

hunt_results = []

all_hunt_data = (
    linux_logs
    + aix_logs
    + falco_logs
)

if hunt_term:

    for log in all_hunt_data:

        if hunt_term.lower() in log.lower():

            hunt_results.append(log)

    if hunt_results:

        st.success(
            f"{len(hunt_results)} hunting matches identified"
        )

        for result in hunt_results:

            st.code(result)

    else:

        st.warning(
            "No matching threat hunting results"
        )

# ---------------------------
# SIEM SEARCH
# ---------------------------

st.subheader("SIEM Event Search")

search_term = st.text_input(
    "Search security events"
)

if search_term:

    matching_events = []

    for event in falco_logs[-10:]:

        if search_term.lower() in event.lower():

            matching_events.append(event)

    if matching_events:

        st.success(
            f"{len(matching_events)} matching events found"
        )

        for match in matching_events:

            st.code(match)

    else:

        st.warning("No matching events found")

# ---------------------------
# SIEM EVENTS
# ---------------------------

st.subheader("SIEM Event Correlation")

events_df = pd.DataFrame(filtered_events)

st.dataframe(
    events_df,
    use_container_width=True
)

# ---------------------------
# EXECUTIVE PDF REPORT
# ---------------------------

st.subheader("Executive Security Report")

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

# ---------------------------
# HISTORICAL DETECTIONS
# ---------------------------

st.subheader(
    "Historical Detection Repository"
)

historical_detections = load_detections()

if historical_detections:

    historical_df = pd.DataFrame(
        historical_detections,
        columns=[
            "ID",
            "Detection Type",
            "Severity",
            "Details"
        ]
    )

    st.dataframe(
        historical_df,
        use_container_width=True
    )

else:

    st.info(
        "No historical detections stored"
    )

# ---------------------------
# REAL SOC ANALYTICS
# ---------------------------

st.subheader(
    "SOC Historical Analytics"
)

detection_stats = detection_analytics()

incident_stats = incident_analytics()

if not detection_stats.empty:

    detection_fig = px.bar(
        detection_stats,
        x="Severity",
        y="Count",
        title="Historical Detection Severity"
    )

    st.plotly_chart(
        detection_fig,
        use_container_width=True
    )

if not incident_stats.empty:

    incident_fig = px.pie(
        incident_stats,
        names="Severity",
        values="Count",
        title="Incident Severity Distribution"
    )

    st.plotly_chart(
        incident_fig,
        use_container_width=True
    )

# ---------------------------
# EXECUTIVE SUMMARY
# ---------------------------

if has_permission(
    role,
    "executive"
):

    st.subheader(
        "Executive Security Summary"
    )

    st.success("""
    Enterprise monitoring coverage active across:

- Linux / Unix / AIX
- Windows
- Kubernetes
- AWS
- Azure
- GCP
- OCI
- IBM Cloud

Threat detection pipelines operational.

MITRE ATT&CK coverage enabled.

IOC monitoring active.

SOAR integrations simulated successfully.
    """)

# ---------------------------
# SECURITY ARCHITECTURE
# ---------------------------

st.subheader("Enterprise Security Workflow")

st.code("""
Linux / AIX / Windows
        ↓
AWS / Azure / GCP / OCI / IBM Cloud
        ↓
Kubernetes Runtime Monitoring
        ↓
SIEM Correlation Engine
        ↓
Threat Intelligence Enrichment
        ↓
MITRE ATT&CK Mapping
        ↓
SOC Dashboard
        ↓
Incident Response
        ↓
SOAR Automation
""")

# ---------------------------
# ATTACK SIMULATION
# ---------------------------

st.subheader("Attack Simulation")

with open(
    SIMULATIONS_DIR / "attack-simulation.json",
    "r"
) as file:

    attack_data = json.load(file)

attack_df = pd.DataFrame(attack_data)

st.dataframe(
    attack_df,
    use_container_width=True
)

# ---------------------------
# COMPLIANCE Executive Risk Overview
# ---------------------------

st.subheader("Executive Risk Overview")

executive_df = pd.DataFrame({
    "Area": [
        "Cloud Security",
        "Endpoint Security",
        "IAM",
        "Kubernetes",
        "Threat Detection"
    ],
    "Risk Level": [
        "Medium",
        "High",
        "Low",
        "Critical",
        "Medium"
    ]
})

st.dataframe(
    executive_df,
    use_container_width=True
)


# ---------------------------
# COMPLIANCE Heatmap
# ---------------------------

st.subheader("Compliance Heatmap")

compliance_chart = pd.DataFrame({
    "Framework": [
        "ISO27001",
        "NIST",
        "PCI-DSS",
        "CIS"
    ],
    "Coverage": [
        92,
        81,
        74,
        89
    ]
})

heatmap = px.bar(
    compliance_chart,
    x="Framework",
    y="Coverage",
    title="Compliance Coverage"
)

st.plotly_chart(
    heatmap,
    use_container_width=True
)

# ---------------------------
# SOC Analyst Queue
# ---------------------------

st.subheader("SOC Analyst Queue")

soc_queue = pd.DataFrame({
    "Ticket": [
        "SOC-1001",
        "SOC-1002",
        "SOC-1003"
    ],
    "Priority": [
        "Critical",
        "High",
        "Medium"
    ],
    "Owner": [
        "Tier 2",
        "Tier 1",
        "Threat Hunting"
    ],
    "Status": [
        "Investigating",
        "Open",
        "Escalated"
    ]
})

st.dataframe(
    soc_queue,
    use_container_width=True
)
