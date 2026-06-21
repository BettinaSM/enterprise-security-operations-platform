import streamlit as st

from parsers.datalake_engine import (
    load_events
)

from parsers.kill_chain_engine import (
    reconstruct_killchain
)

from parsers.session_auth import (
    require_auth
)

require_auth()

st.title(
    "Kill Chain Analysis"
)

events = load_events()

if not events:

    st.warning(
        "No events found in Security Data Lake"
    )

else:

    chain = reconstruct_killchain(
        events
    )

    st.write(chain)
