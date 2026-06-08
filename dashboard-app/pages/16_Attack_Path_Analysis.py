import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.attack_path_engine import (
    build_attack_paths
)

require_auth()

st.title(
    "Attack Path Analysis"
)

paths = build_attack_paths()

st.dataframe(
    pd.DataFrame(paths),
    use_container_width=True
)
