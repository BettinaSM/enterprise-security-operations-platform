import streamlit as st

import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.risk_register_engine import (
    enterprise_risk_register
)

require_auth()

st.title(
    "Enterprise Risk Register"
)

risks = enterprise_risk_register()

df = pd.DataFrame(
    risks
)

st.dataframe(

    df,

    use_container_width=True
)

critical = len(

    df[
        df["risk"] == "Critical"
    ]
)

st.metric(

    "Critical Risks",

    critical
)
