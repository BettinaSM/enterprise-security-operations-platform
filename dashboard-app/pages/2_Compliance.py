import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Compliance Dashboard",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Compliance Dashboard")

# ---------------------------
# COMPLIANCE OVERVIEW
# ---------------------------

compliance_df = pd.DataFrame({

    "Framework": [
        "ISO 27001",
        "NIST",
        "PCI-DSS",
        "CIS Controls",
        "SOC2"
    ],

    "Status": [
        "Compliant",
        "Partial",
        "In Review",
        "Compliant",
        "Partial"
    ],

    "Coverage": [
        92,
        81,
        74,
        89,
        78
    ]
})

st.dataframe(
    compliance_df,
    use_container_width=True
)

# ---------------------------
# COMPLIANCE HEATMAP
# ---------------------------

st.subheader("Compliance Coverage")

fig = px.bar(
    compliance_df,
    x="Framework",
    y="Coverage",
    title="Compliance Framework Coverage"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------
# EXECUTIVE RISK OVERVIEW
# ---------------------------

st.subheader("Executive Risk Overview")

risk_df = pd.DataFrame({

    "Area": [
        "Cloud Security",
        "IAM",
        "Endpoint Security",
        "Kubernetes",
        "Threat Detection"
    ],

    "Risk": [
        "Medium",
        "High",
        "Low",
        "Critical",
        "Medium"
    ]
})

st.dataframe(
    risk_df,
    use_container_width=True
)

# ---------------------------
# AUDIT STATUS
# ---------------------------

st.subheader("Audit Readiness")

audit_df = pd.DataFrame({

    "Audit": [
        "Internal Audit",
        "External Audit",
        "PCI Assessment",
        "SOC2 Review"
    ],

    "Status": [
        "Ready",
        "In Progress",
        "Scheduled",
        "Ready"
    ]
})

st.dataframe(
    audit_df,
    use_container_width=True
)
