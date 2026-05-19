import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Enterprise Security Operations Platform",
    layout="wide"
)

st.title("Enterprise Security Operations Platform")

st.markdown("""
Multi-environment Security Operations monitoring platform
covering Linux, AIX, Windows, Kubernetes and Multi-Cloud environments.
""")

# Metrics

col1, col2, col3, col4 = st.columns(4)

col1.metric("Critical Alerts", "4")
col2.metric("Runtime Threats", "7")
col3.metric("Failed Auth", "23")
col4.metric("Incidents", "2")

st.divider()

# Environment coverage

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

# Alerts

st.subheader("Security Alerts")

alerts = pd.DataFrame({
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

st.dataframe(alerts, use_container_width=True)

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
