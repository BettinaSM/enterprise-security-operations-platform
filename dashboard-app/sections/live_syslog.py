import streamlit as st

from collectors.syslog_collector import (
    start_syslog_listener,
    receive_syslog_event
)

# ---------------------------
# LIVE SYSLOG
# ---------------------------

def render_live_syslog():

    st.subheader(
        "Live Syslog Monitoring"
    )

    if st.button(
        "Start Syslog Listener",
        key="start_syslog"
    ):

        sock = start_syslog_listener()

        st.success(
            "Syslog listener started on UDP 5140"
        )

        event = receive_syslog_event(
            sock
        )

        st.code(event)
