import streamlit as st
import pandas as pd
import json

from pathlib import Path

from parsers.session_auth import (
    require_auth
)

require_auth()

from configs.settings import (
    THREAT_FEED
)

st.set_page_config(
    page_title="Threat Intelligence",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Threat Intelligence")

from configs.settings import (
    THREAT_FEED
)

with open(
    THREAT_FEED,
    "r"
) as file:

    threat_feed = json.load(file)

feed_df = pd.DataFrame(threat_feed)

st.dataframe(
    feed_df,
    use_container_width=True
)
