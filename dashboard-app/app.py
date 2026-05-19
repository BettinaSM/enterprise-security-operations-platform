import streamlit as st
import pandas as pd
import plotly.express as px

from parsers.log_parser import (
    read_log,
    count_failed_auth,
    count_critical
)

st.set_page_config(
    page_title="Enterprise Security Operations Platform",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------
# HEADER
# ---------------------------

st.title("🛡️ Enterprise Security Operations Platform")

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
# READ LOGS
# ---------------------------

linux_logs = read_log("agents/linux/auth.log")
aix_logs = read_log("agents/aix/sudo.log")
falco_logs = read_log("logs/falco-events.log")

# ---------------------------
# METRICS
# ---------------------------

failed_auth = (
    count_failed_auth(linux_logs)
    + count_failed_auth(aix_logs)
)

critical_alerts = count_critical(falco_logs)

runtime_events = len(falco_logs)

incidents = 2

# ---------------------------
# DASHBOARD METRICS
# ---------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Critical Alerts", critical_alerts)
col2.metric("Runtime Threats", runtime_events)
col3.metric("Failed Auth", failed_auth)
col4.metric("Incidents", incidents)

st.divider()

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

mitre_df = pd.DataFrame({
    "Technique": [
        "T1059",
        "T1110",
        "T1611"
    ],
    "Description": [
        "Command Execution",
        "Brute Force",
        "Privilege Escalation"
    ]
})

st.dataframe(mitre_df, use_container_width=True)

st.divider()

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
# LIVE EVENTS
# ---------------------------

st.subheader("Live Runtime Events")

for event in falco_logs:
    st.code(event)

st.divider()

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
