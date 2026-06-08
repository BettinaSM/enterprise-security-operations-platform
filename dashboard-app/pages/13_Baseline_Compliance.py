import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.compliance_baseline_engine import (
    evaluate_baseline,
    calculate_compliance_score
)

require_auth()

st.title(
    "Baseline Compliance"
)

sample_data = {

    "permit_root_login": True,
    "password_authentication": True,
    "mfa_enabled": False,
    "dormant_accounts": 5

}

findings = evaluate_baseline(
    sample_data
)

score = calculate_compliance_score(
    findings
)

st.metric(
    "Compliance Score",
    f"{score}%"
)

st.dataframe(
    pd.DataFrame(
        findings
    )
)
