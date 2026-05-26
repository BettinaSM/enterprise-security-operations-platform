import streamlit as st
import pandas as pd

def render_cloud_security(
    cloud_findings
):

    st.subheader(
        "Cloud Security Findings"
    )

    if cloud_findings:

        cloud_df = pd.DataFrame(
            cloud_findings
        )

        st.dataframe(
            cloud_df,
            use_container_width=True
        )

    else:

        st.success(
            "No cloud findings identified"
        )
