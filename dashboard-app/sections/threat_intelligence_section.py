import streamlit as st
import pandas as pd

def render_threat_intelligence(
    enriched_iocs,
    feed_correlations,
    cve_findings
):

    st.subheader(
        "Threat Intelligence Enrichment"
    )

    if enriched_iocs:

        threat_df = pd.DataFrame(
            enriched_iocs
        )

        st.dataframe(
            threat_df,
            use_container_width=True
        )

    else:

        st.success(
            "No malicious IOC enrichment identified"
        )

    # ---------------------------

    st.subheader(
        "External Threat Feed Correlation"
    )

    if feed_correlations:

        feed_df = pd.DataFrame(
            feed_correlations
        )

        st.dataframe(
            feed_df,
            use_container_width=True
        )

    else:

        st.success(
            "No external threat feed matches identified"
        )

    # ---------------------------

    st.subheader(
        "Threat Intelligence CVE Correlation"
    )

    if cve_findings:

        cve_df = pd.DataFrame(
            cve_findings
        )

        st.dataframe(
            cve_df,
            use_container_width=True
        )

    else:

        st.success(
            "No CVE correlations identified"
        )
