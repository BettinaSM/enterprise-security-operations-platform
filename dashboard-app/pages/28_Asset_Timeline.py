import streamlit as st
import pandas as pd

from parsers.insider_threat_engine import (
    detect_insider_threat
)

st.title(

    "Insider Threat Detection"

)

st.dataframe(

    pd.DataFrame(

        detect_insider_threat()

    ),

    use_container_width=True

)
