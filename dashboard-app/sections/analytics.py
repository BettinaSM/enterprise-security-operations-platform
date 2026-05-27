```python
import streamlit as st
import plotly.express as px
import pandas as pd

# ---------------------------
# ANALYTICS SECTION
# ---------------------------

def render_analytics(
    detection_stats,
    incident_stats
):

    st.subheader(
        "SOC Historical Analytics"
    )

    # ---------------------------
    # DETECTION ANALYTICS
    # ---------------------------

    st.markdown(
        "### Detection Severity Distribution"
    )

    if detection_stats is not None and not detection_stats.empty:

        detection_fig = px.bar(
            detection_stats,
            x="Severity",
            y="Count",
            title="Detection Severity Overview"
        )

        st.plotly_chart(
            detection_fig,
            use_container_width=True
        )

        st.dataframe(
            detection_stats,
            use_container_width=True
        )

    else:

        st.info(
            "No detection analytics available"
        )

    # ---------------------------
    # INCIDENT ANALYTICS
    # ---------------------------

    st.markdown(
        "### Incident Severity Distribution"
    )

    if incident_stats is not None and not incident_stats.empty:

        incident_fig = px.pie(
            incident_stats,
            names="Severity",
            values="Count",
            title="Incident Severity Overview"
        )

        st.plotly_chart(
            incident_fig,
            use_container_width=True
        )

        st.dataframe(
            incident_stats,
            use_container_width=True
        )

    else:

        st.info(
            "No incident analytics available"
        )
```
