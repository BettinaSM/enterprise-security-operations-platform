import streamlit as st
import plotly.express as px

from parsers.analytics_engine import (
    detection_analytics,
    incident_analytics
)

def render_analytics():

    st.subheader(
        "SOC Historical Analytics"
    )

    detection_stats = detection_analytics()

    incident_stats = incident_analytics()

    # ---------------------------

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

    # ---------------------------

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
