import streamlit as st
import pandas as pd
import json

from pathlib import Path

st.set_page_config(
    page_title="Threat Intelligence",
    page_icon="🧠",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SIMULATIONS_DIR = BASE_DIR / "simulations"

st.title("🧠 Threat Intelligence")

with open(
    SIMULATIONS_DIR / "threat-feed.json",
    "r"
) as file:

    feed = json.load(file)

feed_df = pd.DataFrame(feed)

st.dataframe(
    feed_df,
    use_container_width=True
)
