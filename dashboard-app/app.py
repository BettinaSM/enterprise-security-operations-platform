import streamlit as st
import pandas as pd
import plotly.express as px
import json
import time

from pathlib import Path

from parsers.ioc_matcher import match_ioc

from parsers.threat_scoring import calculate_threat_score

from parsers.mitre_mapper import map_to_mitre

from parsers.detection_engine import run_detections

from parsers.risk_engine import calculate_risk_score

from parsers.yaml_detection_engine import (
    run_yaml_detections
)

from parsers.rule_engine import load_rule

from parsers.attack_chain import build_attack_chain

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
# BASE PATHS
# ---------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

SIMULATIONS_DIR = BASE_DIR / "simulations"

RULES_DIR = BASE_DIR / "detections" / "sigma"

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

st.title("🛡️ Unified Enterprise Security Operations Platform")

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

# ---------------------------
# IOC MATCHING
# ---------------------------

ioc_matches = match_ioc(linux_logs)

mitre_events = map_to_mitre(
    linux_logs + aix_logs + falco_logs
)

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

risk_score, risk_level = calculate_risk_score(
    detections
)

if ioc_matches:

    st.warning(
        f"Known malicious IOC detected: {', '.join(ioc_matches)}"
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

attack_chain = build_attack_chain(
    failed_auth,
    cloud_findings,
    ioc_matches,
    critical_alerts
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
# DASHBOARD METRICS
# ---------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Critical Alerts", critical_alerts)
col2.metric("Runtime Threats", runtime_events)
col3.metric("Failed Auth", failed_auth)
col4.metric("Incidents", incidents)

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
# COMPLIANCE DASHBOARD
# ---------------------------

st.subheader("Compliance Overview")

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

st.subheader("SOAR Automated Actions")

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

with open(
    SIMULATIONS_DIR / "realtime-events.json",
    "r"
) as file:

    realtime_events = json.load(file)

for event in realtime_events:

    severity = event["severity"]

    if severity == "Critical":

        st.error(event)

    elif severity == "High":

        st.warning(event)

    else:

        st.info(event)

    time.sleep(0.1)

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
# EXECUTIVE SUMMARY
# ---------------------------

st.subheader("Executive Security Summary")

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
