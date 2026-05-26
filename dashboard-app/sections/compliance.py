import streamlit as st
import pandas as pd

def render_compliance():

    st.subheader(
        "Compliance Overview"
    )

    compliance_df = pd.DataFrame({

        "Framework": [
            "ISO 27001",
            "NIST",
            "PCI-DSS",
            "CIS"
        ],

        "Status": [
            "Compliant",
            "Partial",
            "In Review",
            "Compliant"
        ],

        "Coverage": [
            "92%",
            "81%",
            "74%",
            "89%"
        ]
    })

    st.dataframe(
        compliance_df,
        use_container_width=True
    )
