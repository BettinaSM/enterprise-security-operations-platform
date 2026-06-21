import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.compliance_dashboard_engine import (
    get_compliance_dashboard
)

from parsers.control_testing_engine import (
    execute_control_tests
)

require_auth()

st.title(

    "Continuous Control Monitoring"

)

dashboard = get_compliance_dashboard()

st.subheader(

    "Framework Scores"

)

st.dataframe(

    pd.DataFrame(

        dashboard.items(),

        columns=[

            "Framework",

            "Score"

        ]

    ),

    use_container_width=True

)

st.subheader(

    "Automated Control Tests"

)

st.dataframe(

    pd.DataFrame(

        execute_control_tests()

    ),

    use_container_width=True

)
