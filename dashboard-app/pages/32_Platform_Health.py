import streamlit as st

import pandas as pd

from parsers.healthcheck_engine import (
    run_platform_health
)

from parsers.session_auth import (
    require_auth
)

require_auth()

st.title(
    "Platform Health Monitoring"
)

health = run_platform_health()

df = pd.DataFrame(
    health
)

st.dataframe(

    df,

    use_container_width=True
)

# ---------------------------
# SUMMARY
# ---------------------------

healthy = len(

    df[
        df["Status"] == "Healthy"
    ]
)

total = len(df)

st.metric(

    "Healthy Components",

    f"{healthy}/{total}"
)

# ---------------------------
# ALERTS
# ---------------------------

issues = df[

    df["Status"] != "Healthy"

]

if not issues.empty:

    st.warning(

        "Platform issues detected."

    )

    st.dataframe(

        issues,

        use_container_width=True
    )

else:

    st.success(

        "All platform components healthy."
    )
