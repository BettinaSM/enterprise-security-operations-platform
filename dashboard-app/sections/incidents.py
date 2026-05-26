import streamlit as st
import pandas as pd

from services.incident_service import (
    get_all_incidents
)

def render_incidents():

    st.subheader(
        "SOC Case Management"
    )

    incidents = get_all_incidents()

    if incidents:

        incident_df = pd.DataFrame(
            incidents,
            columns=[
                "ID",
                "Severity",
                "Source",
                "Description",
                "Status",
                "Created At"
            ]
        )

        st.dataframe(
            incident_df,
            use_container_width=True
        )

    else:

        st.info(
            "No incidents stored"
        )
