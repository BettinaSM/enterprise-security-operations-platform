import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.asset_risk_engine import (
    enterprise_asset_risk
)

require_auth()

st.title(
    "Enterprise Asset Risk"
)

risk = enterprise_asset_risk()

st.dataframe(

    pd.DataFrame(risk),

    use_container_width=True

)
