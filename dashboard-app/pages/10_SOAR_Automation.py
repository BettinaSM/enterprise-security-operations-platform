import streamlit as st

from parsers.session_auth import (
    require_auth
)

require_auth()

from sections.soar import (
    render_soar
)

from sections.automation import (
    render_automation
)

st.set_page_config(
    page_title="SOAR Automation",
    page_icon="⚡",
    layout="wide"
)

st.title(
    "⚡ SOAR Automation"
)

tab1, tab2 = st.tabs(
    [
        "SOAR Playbooks",
        "Ansible Automation"
    ]
)

with tab1:

    render_soar()

with tab2:

    render_automation()
