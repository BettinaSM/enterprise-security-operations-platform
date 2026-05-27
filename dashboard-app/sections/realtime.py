import streamlit as st
import pandas as pd

from parsers.log_parser import (
    read_log
)

def render_realtime():

    st.subheader(
        "Live Runtime Events"
    )

    falco_logs = read_log(
        "logs/falco-events.log"
    )

    if not falco_logs:

        st.warning(
            "No runtime events detected"
        )

        return

    runtime_df = pd.DataFrame({

        "Event": falco_logs[-10:]

    })

    st.dataframe(
        runtime_df,
        use_container_width=True
    )
