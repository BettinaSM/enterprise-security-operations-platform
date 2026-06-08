import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.identity_governance import (
    run_identity_governance
)

require_auth()

st.title(
    "Identity Governance"
)

results = run_identity_governance()

for section, data in results.items():

    st.subheader(

        section.replace(
            "_",
            " "
        ).title()

    )

    st.dataframe(
        pd.DataFrame(data)
    )
