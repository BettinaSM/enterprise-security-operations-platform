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

from parsers.yaml_detection_engine import (
    run_yaml_detections
)

from parsers.mitre_mapper import (
    map_to_mitre
)

from sections.detections import (
    render_detections
)

from sections.mitre_heatmap import (
    render_mitre_heatmap
)

st.title(
    "Detection Engineering"
)

events = (
    collect_linux_logs() +
    collect_aix_logs()
)

detections = run_detections(
    events
)

yaml_detections = run_yaml_detections(
    events
)

mitre_events = map_to_mitre(
    events
)

render_detections(
    detections,
    yaml_detections,
    mitre_events
)

render_mitre_heatmap(
    mitre_events
)
