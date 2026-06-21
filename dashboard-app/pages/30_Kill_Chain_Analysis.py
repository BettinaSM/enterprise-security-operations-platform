import streamlit as st

from parsers.datalake_engine import (
    load_events
)

from parsers.killchain_engine import (
    reconstruct_killchain
)

st.title(

    "Kill Chain Analysis"

)

events = load_events()

chain = reconstruct_killchain(
    events
)

st.write(chain)
