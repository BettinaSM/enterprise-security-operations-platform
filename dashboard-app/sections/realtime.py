import streamlit as st
import pandas as pd
import time

from parsers.realtime_engine import (
    generate_realtime_event
)

# ---------------------------
# REALTIME SECTION
# ---------------------------

def render_realtime():

    st.subheader(
        "Real-Time Security Monitoring"
    )

    # ---------------------------
    # LIVE EVENTS
    # ---------------------------

    live_placeholder = st.empty()

    for _ in range(5):

        realtime_event = generate_realtime_event()

        event_df = pd.DataFrame([
            realtime_event
        ])

        with live_placeholder.container():

            severity = realtime_event.get(
                "severity",
                "Low"
            )

            if severity == "Critical":

                st.error("Critical security event detected")

            elif severity == "High":

                st.warning("High severity event detected")

            elif severity == "Medium":

                st.info("Medium severity event detected")

            else:

                st.success("Low severity event detected")

            st.dataframe(
                event_df,
                use_container_width=True
            )

        time.sleep(1)
