import streamlit as st

from collectors.linux_collector import (
    collect_linux_logs
)

from collectors.aix_collector import (
    collect_aix_logs
)

from parsers.detection_engine import (
    run_detections
)

from parsers.analytics_engine import (
    detection_analytics,
    incident_analytics
)

from sections.dashboard import (
    render_dashboard
)

from sections.analytics import (
    render_analytics
)

st.title(
    "SOC Operations"
)

linux_logs = collect_linux_logs()

aix_logs = collect_aix_logs()

events = linux_logs + aix_logs

detections = run_detections(
    events
)

detection_stats = detection_analytics()

incident_stats = incident_analytics()

render_dashboard()

render_analytics(
    detection_stats,
    incident_stats
)
