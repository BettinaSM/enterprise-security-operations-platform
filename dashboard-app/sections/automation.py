import streamlit as st

from services.ansible_service import (
    execute_playbook
)

# ---------------------------
# AUTOMATION SECTION
# ---------------------------

def render_automation():

    st.subheader(
        "SOAR Automation"
    )

    playbook = st.selectbox(

        "Playbook",

        [

            "collect_logs.yml",
            "users_audit.yml",
            "sudoers_audit.yml"

        ]
    )

    if st.button(
        "Execute Playbook"
    ):

        result = execute_playbook(

            f"ansible/playbooks/{playbook}",

            "ansible/inventory/inventory.ini"
        )

        st.code(
            result["stdout"]
        )

        if result["stderr"]:

            st.error(
                result["stderr"]
            )
