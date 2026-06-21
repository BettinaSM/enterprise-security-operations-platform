import streamlit as st

import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.compliance_engine import (
    evaluate_controls
)

require_auth()

st.title(
    "Continuous Compliance"
)

results = evaluate_controls()

df = pd.DataFrame(
    results
)

st.dataframe(

    df,

    use_container_width=True
)

for item in results:

    st.metric(

        item["framework"],

        f"{item['score']}%"
    )
