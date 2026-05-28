import streamlit as st

from soar.response_engine import (
    block_linux_user
)

# ---------------------------
# SOAR SECTION
# ---------------------------

def render_soar():

    st.subheader(
        "SOAR Automation"
    )

    username = st.text_input(
        "Target User"
    )

    if st.button(
        "Block Linux User",
        key="block_linux_user"
    ):

        result = block_linux_user(
            username
        )

        if result["success"]:

            st.success(
                "User blocked successfully"
            )

            st.code(
                result["output"]
            )

        else:

            st.error(
                result["error"]
            )
