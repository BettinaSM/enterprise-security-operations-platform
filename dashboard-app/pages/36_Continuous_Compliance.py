import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.compliance_engine import (
    run_compliance
)

require_auth()

st.title(
    "Continuous Compliance"
)

results = run_compliance()

for framework in results:

    st.subheader(

        framework["framework"]

    )

    st.metric(

        "Score",

        f"{framework['score']}%"

    )

    st.dataframe(

        pd.DataFrame(

            framework["controls"]

        ),

        use_container_width=True

    )
