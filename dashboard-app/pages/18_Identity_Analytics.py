import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.iam_engine import (
    get_local_users
)

from parsers.identity_analytics_engine import (
    analyze_identities
)

require_auth()

st.title(
    "Identity Analytics"
)

analytics = analyze_identities(
    get_local_users()
)

st.dataframe(
    pd.DataFrame(analytics),
    use_container_width=True
)
