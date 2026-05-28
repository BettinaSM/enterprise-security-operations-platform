import os
import streamlit as st

from ansible.ansible_runner import (
    run_playbook
)

# ---------------------------
# ENTERPRISE AUDIT
# ---------------------------

def render_enterprise_audit():

    st.subheader(
        "Enterprise Audit Engine"
    )

    audit_type = st.selectbox(

        "Audit Type",

        [

            "User Audit",
            "Group Audit",
            "Sudoers Audit"
        ]
    )

    # ---------------------------

    if audit_type == "User Audit":

        target_user = st.text_input(
            "Target User"
        )

        if st.button(
            "Execute User Audit",
            key="user_audit_button"
        ):

            os.environ["TARGET_USER"] = (
                target_user
            )

            result = run_playbook(
                "user_audit.yml"
            )

            st.code(
                result["stdout"]
            )

    # ---------------------------

    elif audit_type == "Group Audit":

        target_group = st.text_input(
            "Target Group"
        )

        if st.button(
            "Execute Group Audit",
            key="group_audit_button"
        ):

            os.environ["TARGET_GROUP"] = (
                target_group
            )

            result = run_playbook(
                "group_audit.yml"
            )

            st.code(
                result["stdout"]
            )

    # ---------------------------

    elif audit_type == "Sudoers Audit":

        keyword = st.text_input(
            "Privilege Keyword"
        )

        if st.button(
            "Execute Sudoers Audit",
            key="sudoers_audit_button"
        ):

            os.environ["TARGET_KEYWORD"] = (
                keyword
            )

            result = run_playbook(
                "sudoers_audit.yml"
            )

            st.code(
                result["stdout"]
            )
