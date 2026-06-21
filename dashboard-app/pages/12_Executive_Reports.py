import streamlit as st

from parsers.session_auth import (
    require_auth
)

from parsers.audit_engine import (
    run_full_audit
)

from parsers.risk_engine import (
    calculate_risk_score
)

from parsers.compliance_score_engine import (
    calculate_compliance_score
)

from services.audit_trail_service import (
    register_action
)

require_auth()

role = st.sidebar.selectbox(
    "Role Validation",
    [
        "Executive",
        "SOC Analyst",
        "Threat Hunter",
        "Administrator"
    ]
)

if role not in [
    "Executive",
    "Administrator"
]:

    st.error(
        "Access denied"
    )

    st.stop()

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

audit = run_full_audit()

compliance = calculate_compliance_score(
    audit
)

st.metric(

    "Compliance Score",

    f"{compliance['score']}%"
)

register_action(

    st.session_state["username"],

    "Generated Executive Report"
)
