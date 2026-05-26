import streamlit as st

def render_kpis(
    threat_score,
    threat_severity,
    risk_score,
    risk_level
):

    st.subheader(
        "Security Operations KPIs"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Threat Score",
        threat_score
    )

    col2.metric(
        "Threat Severity",
        threat_severity
    )

    col3.metric(
        "Risk Score",
        risk_score
    )

    col4.metric(
        "Risk Level",
        risk_level
    )

    if threat_severity == "Critical":

        st.error(
            "Critical threat activity identified"
        )

    elif threat_severity == "High":

        st.warning(
            "High threat activity identified"
        )

    else:

        st.success(
            "Environment operating normally"
        )
