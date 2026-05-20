import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cloud Security",
    page_icon="☁️",
    layout="wide"
)

st.title("☁️ Cloud Security Monitoring")

cloud_df = pd.DataFrame({

    "Cloud": [
        "AWS",
        "Azure",
        "GCP",
        "OCI",
        "IBM Cloud"
    ],

    "Threats": [
        4,
        2,
        1,
        3,
        0
    ],

    "Risk Level": [
        "High",
        "Medium",
        "Low",
        "High",
        "Low"
    ]
})

st.dataframe(
    cloud_df,
    use_container_width=True
)

st.subheader("Cloud IAM Risks")

iam_df = pd.DataFrame({

    "Cloud": [
        "AWS",
        "Azure",
        "OCI"
    ],

    "Issue": [
        "Excessive IAM Permissions",
        "Legacy Authentication",
        "Privileged Policy Drift"
    ],

    "Severity": [
        "Critical",
        "High",
        "High"
    ]
})

st.dataframe(
    iam_df,
    use_container_width=True
)
