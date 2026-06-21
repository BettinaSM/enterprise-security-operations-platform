import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.resilience_engine import (
    calculate_resilience,
    evaluate_resilience
)

require_auth()

st.title(
    "Cyber Resilience"
)

metrics = calculate_resilience()

col1, col2 = st.columns(2)

col1.metric(
    "Resilience Score",
    f"{metrics['score']}%"
)

col2.metric(
    "Successful Backups",
    f"{metrics['successful']}/{metrics['total']}"
)

st.divider()

st.subheader(
    "Backup Validation"
)

st.dataframe(

    pd.DataFrame(
        evaluate_resilience()
    ),

    use_container_width=True
)
