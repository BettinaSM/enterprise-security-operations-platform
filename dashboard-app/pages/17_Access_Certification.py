import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.iam_engine import (
    get_local_users
)

from parsers.access_certification_engine import (
    generate_access_review
)

require_auth()

st.title(
    "Access Certification"
)

reviews = generate_access_review(
    get_local_users()
)

st.dataframe(
    pd.DataFrame(reviews),
    use_container_width=True
)
