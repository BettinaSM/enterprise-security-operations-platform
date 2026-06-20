import streamlit as st
import pandas as pd

from parsers.cmdb_engine import (
    load_cmdb,
    search_asset,
    count_assets
)

st.title(
    "Enterprise CMDB"
)

assets = load_cmdb()

col1, col2 = st.columns(2)

col1.metric(
    "Total Assets",
    count_assets()
)

col2.metric(
    "Critical Assets",

    len([

        x

        for x in assets

        if x["criticality"] == "Critical"
    ])
)

keyword = st.text_input(
    "Search Asset"
)

if keyword:

    results = search_asset(
        keyword
    )

    st.dataframe(
        pd.DataFrame(results),
        use_container_width=True
    )

else:

    st.dataframe(
        pd.DataFrame(assets),
        use_container_width=True
    )
