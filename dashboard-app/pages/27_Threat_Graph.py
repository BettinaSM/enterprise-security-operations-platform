import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.threat_graph_engine import (

    build_threat_graph,
    find_highly_connected_identities

)

from collectors.linux_collector import (
    collect_linux_logs
)

from collectors.aix_collector import (
    collect_aix_logs
)

require_auth()

st.title(
    "Threat Graph Analysis"
)

events = []

events.extend(

    [

        {

            "username": "root",

            "hostname": "linux01",

            "ip": "10.10.10.1"

        },

        {

            "username": "socadmin",

            "hostname": "linux02",

            "ip": "10.10.10.2"

        },

        {

            "username": "Administrator",

            "hostname": "win01",

            "ip": "10.10.10.3"

        }

    ]

)

graph = build_threat_graph(
    events
)

st.subheader(
    "Threat Relationships"
)

st.json(graph)

st.subheader(
    "Highly Connected Identities"
)

st.dataframe(

    pd.DataFrame(

        find_highly_connected_identities(
            graph
        )

    ),

    use_container_width=True

)
