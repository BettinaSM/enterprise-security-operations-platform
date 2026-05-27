import streamlit as st
import pandas as pd

from parsers.detection_engine import (
    run_detections
)

from parsers.yaml_detection_engine import (
    run_yaml_detections
)

from parsers.mitre_mapper import (
    map_to_mitre
)

def render_detections(events):

    detections = run_detections(events)

    yaml_detections = run_yaml_detections(events)

    mitre_events = map_to_mitre(events)

    # ---------------------------

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
