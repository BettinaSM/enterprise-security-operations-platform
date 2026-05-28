import streamlit as st
import pandas as pd
import plotly.express as px

from parsers.mitre_heatmap import (
    build_mitre_heatmap
)

# ---------------------------
# MITRE HEATMAP
# ---------------------------

def render_mitre_heatmap(
    mitre_events
):

    st.subheader(
        "MITRE ATT&CK Heatmap"
    )

    heatmap = build_mitre_heatmap(
        mitre_events
    )

    if not heatmap:

        st.info(
            "No MITRE data available"
        )

        return

    df = pd.DataFrame(
        heatmap
    )

    fig = px.bar(
        df,
        x="Technique",
        y="Count",
        title="MITRE ATT&CK Activity"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
