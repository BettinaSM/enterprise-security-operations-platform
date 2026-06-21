import streamlit as st

from parsers.session_auth import (
    require_auth
)

from parsers.posture_engine import (
    calculate_posture
)

require_auth()

st.title(
    "Security Posture"
)

posture = calculate_posture()

st.metric(

    "Enterprise Security Score",

    f"{posture['score']}%"
)

col1, col2, col3 = st.columns(3)

col1.metric(

    "Critical Assets",

    posture["critical_assets"]
)

col2.metric(

    "Critical Vulnerabilities",

    posture["critical_vulnerabilities"]
)

col3.metric(

    "Dormant Accounts",

    posture["dormant_accounts"]
)

if posture["score"] >= 80:

    st.success(
        "Security posture healthy"
    )

elif posture["score"] >= 50:

    st.warning(
        "Security posture requires attention"
    )

else:

    st.error(
        "Security posture critical"
    )
