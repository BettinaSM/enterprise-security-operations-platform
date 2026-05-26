import streamlit as st
import pandas as pd

def render_realtime_events(
    falco_logs
):

    st.subheader(
        "Live Runtime Events"
    )

    runtime_df = pd.DataFrame({

        "Event": falco_logs[-10:]

    })

    st.dataframe(
        runtime_df,
        use_container_width=True
    )
