import streamlit as st
import pandas as pd

from parsers.ctem_engine import (
    run_ctem_analysis
)

from parsers.session_auth import (
    require_auth
)

require_auth()

st.title(
    "Exposure Management"
)

results = run_ctem_analysis()

df = pd.DataFrame(
    results
)

st.dataframe(
    df,
    use_container_width=True
)

st.subheader(
    "Top Exposed Assets"
)

st.bar_chart(

    df.set_index(
        "hostname"
    )["exposure_score"]

)
