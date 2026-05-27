import streamlit as st
import pandas as pd

from parsers.cloud_parser import (
    load_json_log,
    detect_failed_cloud_login,
    detect_privileged_activity,
    calculate_severity
)

def render_cloud_security():

    aws_log = load_json_log(
        "agents/aws/cloudtrail.json"
    )

    azure_log = load_json_log(
        "agents/azure/entra-signins.json"
    )

    gcp_log = load_json_log(
        "agents/gcp/audit-logs.json"
    )

    oci_log = load_json_log(
        "agents/oracle-cloud/oci-audit.json"
    )

    ibm_log = load_json_log(
        "agents/ibm-cloud/activity-tracker.json"
    )

    cloud_findings = []

    cloud_events = [

        ("AWS", aws_log),
        ("Azure", azure_log),
        ("GCP", gcp_log),
        ("OCI", oci_log),
        ("IBM Cloud", ibm_log)

    ]

    for provider, event in cloud_events:

        if not event:
            continue

        if detect_failed_cloud_login(event):

            cloud_findings.append({

                "Cloud": provider,
                "Finding": "Failed Authentication",
                "Severity": calculate_severity(event)

            })

        if detect_privileged_activity(event):

            cloud_findings.append({

                "Cloud": provider,
                "Finding": "Privileged Activity",
                "Severity": "Critical"

            })

    # ---------------------------

    st.subheader(
        "Cloud Security Findings"
    )

    if cloud_findings:

        cloud_df = pd.DataFrame(
            cloud_findings
        )

        st.dataframe(
            cloud_df,
            use_container_width=True
        )

    else:

        st.success(
            "No cloud findings identified"
        )
