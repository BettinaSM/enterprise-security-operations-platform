import streamlit as st
import pandas as pd

from parsers.log_parser import (
    read_log,
    count_failed_auth,
    count_critical
)

st.set_page_config(
    page_title="Enterprise Security Operations Platform",
    layout="wide"
)

st.title("Enterprise Security Operations Platform")

st.markdown("""
Unified Security Operations platform covering:

- Linux
- AIX
- Windows
- Kubernetes
- AWS
- Azure
- GCP
- OCI
- IBM Cloud
""")

# Read logs

linux_logs = read_log("agents/linux/auth.log")
falco_logs = read_log("logs/falco-events.log")
aix_logs = read_log("agents/aix/sudo.log")

# Metrics

failed_auth = (
    count_failed_auth(linux_logs)
    + count_failed_auth(aix_logs)
)

critical_alerts = count_critical(falco_logs)

runtime_events = len(falco_logs)

incidents = 2

# Dashboard metrics

col1, col2, col3, col4 = st.columns(4)

col1.metric("Critical Alerts", critical_alerts)
col2.metric("Runtime Threats", runtime_events)
col3.metric("Failed Auth", failed_auth)
col4.metric("Incidents", incidents)

st.divider()

# Environment Coverage

st.subheader("Environment Coverage")

env_data = pd.DataFrame({
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

st.dataframe(env_data, use_container_width=True)

st.divider()

# Runtime Alerts

st.subheader("Runtime Security Alerts")

alerts_df = pd.DataFrame({
    "Severity": [
        "Critical",
        "High",
        "Medium"
    ],
    "Event": [
        "Privileged Container Execution",
        "SSH Brute Force Attempt",
        "Suspicious Runtime Activity"
    ],
    "MITRE": [
        "T1611",
        "T1110",
        "T1059"
    ]
})

st.dataframe(alerts_df, use_container_width=True)

st.divider()

# Raw Events

st.subheader("Recent Runtime Events")

for event in falco_logs:
    st.code(event)

st.divider()

# Architecture

st.subheader("Security Workflow")

st.code("""
Linux / AIX / Windows
        ↓
Cloud Providers
        ↓
Kubernetes Runtime
        ↓
SIEM Correlation
        ↓
Threat Intelligence
        ↓
MITRE ATT&CK Mapping
        ↓
SOC Dashboard
        ↓
Incident Response
""")
