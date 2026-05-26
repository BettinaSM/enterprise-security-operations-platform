import streamlit as st

def render_hunting(
    logs
):

    st.subheader(
        "Threat Hunting Console"
    )

    hunt_term = st.text_input(
        "Hunt indicators"
    )

    if hunt_term:

        matches = []

        for log in logs:

            if hunt_term.lower() in log.lower():

                matches.append(log)

        if matches:

            st.success(
                f"{len(matches)} matches found"
            )

            for match in matches:

                st.code(match)

        else:

            st.warning(
                "No matching events found"
            )
