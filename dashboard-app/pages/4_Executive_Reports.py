import streamlit as st

st.set_page_config(
    page_title="Executive Reports",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Executive Reporting")

st.success("""

Board-Level Security Reporting Available

Capabilities:

- Enterprise Risk Reporting
- Compliance Reporting
- Threat Intelligence Summaries
- Incident Metrics
- SOC Performance Metrics
- Executive Security KPIs

""")

st.subheader("Executive KPIs")

col1, col2, col3 = st.columns(3)

col1.metric(
    "MTTD",
    "4 min"
)

col2.metric(
    "MTTR",
    "11 min"
)

col3.metric(
    "Detection Coverage",
    "91%"
)
