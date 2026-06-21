import streamlit as st

from parsers.session_auth import (
    require_auth
)

from parsers.datalake_engine import (
    load_events
)

from parsers.kill_chain_engine import (
    reconstruct_killchain
)

require_auth()

st.title(
    "Kill Chain Analysis"
)

events = load_events()

chain = reconstruct_killchain(
    events
)

if chain:

    for stage in chain:

        st.success(stage)

else:

    st.info(
        "No kill chain identified."
    )
