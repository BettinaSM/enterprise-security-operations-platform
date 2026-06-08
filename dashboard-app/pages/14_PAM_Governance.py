import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.pam_governance_engine import (
    get_privileged_accounts
)

require_auth()

st.title(
    "PAM Governance"
)

accounts = get_privileged_accounts()

st.metric(
    "Privileged Accounts",
    len(accounts)
)

st.dataframe(
    pd.DataFrame(accounts),
    use_container_width=True
)
