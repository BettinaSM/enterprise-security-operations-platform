import streamlit as st
import pandas as pd

def render_detections(
    detections,
    yaml_detections,
    mitre_events
):

    st.subheader(
        "Detection Engine Findings"
    )

    if detections:

        detection_df = pd.DataFrame(
            detections
        )

        st.dataframe(
            detection_df,
            use_container_width=True
        )

    else:

        st.success(
            "No active detections identified"
        )

    # ---------------------------

    st.subheader(
        "YAML Detection Rules"
    )

    if yaml_detections:

        yaml_df = pd.DataFrame(
            yaml_detections
        )

        st.dataframe(
            yaml_df,
            use_container_width=True
        )

    else:

        st.success(
            "No YAML detections identified"
        )

    # ---------------------------

    st.subheader(
        "MITRE ATT&CK Coverage"
    )

    mitre_df = pd.DataFrame(
        mitre_events
    )

    st.dataframe(
        mitre_df,
        use_container_width=True
    )
