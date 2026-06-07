import streamlit as st
import pandas as pd

from parsers.iam_engine import (
    get_local_users,
    get_privileged_users,
    get_groups
)

st.title(
    "IAM Governance"
)

# ---------------------------
# USERS
# ---------------------------

users = get_local_users()

users_df = pd.DataFrame(
    users
)

st.subheader(
    "Local Users"
)

st.dataframe(
    users_df,
    use_container_width=True
)

# ---------------------------
# PRIVILEGED
# ---------------------------

privileged = get_privileged_users()

st.subheader(
    "Privileged Accounts"
)

st.write(
    privileged
)

# ---------------------------
# GROUPS
# ---------------------------

groups = get_groups()

groups_df = pd.DataFrame(
    groups
)

st.subheader(
    "Groups"
)

st.dataframe(
    groups_df,
    use_container_width=True
)
