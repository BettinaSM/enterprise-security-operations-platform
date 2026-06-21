import streamlit as st

import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.attack_surface_engine import (

    external_assets,

    detect_shadow_it,

    attack_surface_summary
)

require_auth()

st.title(
    "External Exposure Management"
)

summary = attack_surface_summary()

col1, col2 = st.columns(2)

col1.metric(

    "Internet Facing",

    summary["external"]
)

col2.metric(

    "Shadow IT",

    summary["shadow"]
)

st.subheader(
    "External Assets"
)

st.dataframe(

    pd.DataFrame(

        external_assets()

    ),

    use_container_width=True
)

st.subheader(
    "Shadow IT"
)

st.dataframe(

    pd.DataFrame(

        detect_shadow_it()

    ),

    use_container_width=True
)
