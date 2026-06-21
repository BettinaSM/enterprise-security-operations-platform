import streamlit as st

import pandas as pd

from services.audit_trail_service import (
    load_audit_events
)

from parsers.session_auth import (
    require_auth
)

require_auth()

st.title(
    "Operational Audit Trail"
)

events = load_audit_events()

if events:

    st.dataframe(

        pd.DataFrame(events),

        use_container_width=True
    )

else:

    st.info(
        "No audit events found."
    )
