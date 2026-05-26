import streamlit as st
import plotly.express as px

def render_analytics(
    detection_stats,
    incident_stats
):

    st.subheader(
        "SOC Historical Analytics"
    )

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
