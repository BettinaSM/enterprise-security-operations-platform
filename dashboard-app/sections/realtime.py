import streamlit as st
import pandas as pd

from parsers.realtime_engine import (
    generate_realtime_event
)

def render_realtime():

    st.subheader(
        "Real-Time Security Monitoring"
    )

    realtime_events = []

    for _ in range(10):

        event = generate_realtime_event()

        realtime_events.append(event)

    realtime_df = pd.DataFrame(
        realtime_events
    )

    st.dataframe(
        realtime_df,
        use_container_width=True
    )

    st.subheader(
        "Live Runtime Events"
    )

    for event in realtime_events:

        severity = event.get(
            "severity",
            "Low"
        )

        if severity == "Critical":

            st.error(event)

        elif severity == "High":

            st.warning(event)

        elif severity == "Medium":

            st.info(event)

        else:

            st.success(event)
    )
