import streamlit as st

role = st.sidebar.selectbox(
    "Role Validation",
    [
        "SOC Analyst",
        "Threat Hunter",
        "Executive",
        "Administrator"
    ]
)

if role not in [
    "Threat Hunter",
    "Administrator"
]:

    st.error(
        "Access denied"
    )

    st.stop()

st.set_page_config(
    page_title="Threat Hunting",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Threat Hunting Console")

hunt_term = st.text_input(
    "Search indicators, IPs, users or commands"
)

sample_logs = [

    "Failed SSH login from 185.220.101.1",
    "sudo privilege escalation detected",
    "Falco container escape attempt",
    "AWS root login detected",
    "OCI IAM policy modified"
]

results = []

if hunt_term:

    for log in sample_logs:

        if hunt_term.lower() in log.lower():

            results.append(log)

if results:

    st.success(
        f"{len(results)} matching events identified"
    )

    for result in results:

        st.code(result)

else:

    st.info(
        "No threat hunting matches identified"
    )
