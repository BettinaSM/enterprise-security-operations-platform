import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.identity_lifecycle_engine import (

    find_dormant_accounts,

    find_orphan_accounts,

    find_no_mfa_accounts

)

require_auth()

st.title(
    "Identity Lifecycle Management"
)

tab1, tab2, tab3 = st.tabs([

    "Dormant",

    "Orphan",

    "MFA"

])

with tab1:

    st.dataframe(

        pd.DataFrame(
            find_dormant_accounts()
        )

    )

with tab2:

    st.dataframe(

        pd.DataFrame(
            find_orphan_accounts()
        )

    )

with tab3:

    st.dataframe(

        pd.DataFrame(
            find_no_mfa_accounts()
        )

    )
