import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.zero_trust_engine import (
    load_zero_trust_policies,
    calculate_zero_trust_score
)

require_auth()

st.title(
    "Zero Trust Architecture"
)

score = calculate_zero_trust_score()

st.metric(

    "Zero Trust Maturity",

    f"{score}%"

)

policies = load_zero_trust_policies()

st.subheader(
    "Policies"
)

st.dataframe(

    pd.DataFrame(
        policies
    ),

    use_container_width=True

)

st.success("""

Implemented Controls:

✔ MFA Enforcement

✔ Conditional Access

✔ Device Compliance

✔ Privileged Access Control

✔ Session Trust Evaluation

✔ Dormant Account Protection

""")
