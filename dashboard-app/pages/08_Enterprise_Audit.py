import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.audit_engine import (
    run_full_audit,
    audit_user,
    audit_group,
    audit_sudo,
    audit_service_accounts
)

from parsers.identity_governance import (
    identity_governance_summary
)

from parsers.cmdb_engine import (
    get_asset_by_hostname
)

require_auth()

st.title(
    "Enterprise Audit Engine"
)

audit_type = st.selectbox(

    "Audit Type",

    [

        "Full Audit",
        
        "User Audit",
        
        "Group Audit",
        
        "Sudo Audit",
        
        "Service Accounts",

        "Identity Governance"

    ]
)

# ---------------------------
# FULL AUDIT
# ---------------------------

if audit_type == "Full Audit":

    results = run_full_audit()

    for section, data in results.items():

        st.subheader(
            section.replace("_", " ").title()
        )

        try:

            st.dataframe(
                pd.DataFrame(data)
            )

        except:

            st.write(data)
            
# ---------------------------
# USER AUDIT
# ---------------------------

elif audit_type == "User Audit":

    username = st.text_input(
        "Username"
    )

    if st.button(
        "Run User Audit",
        key="audit_user_btn"
    ):

        st.dataframe(
            pd.DataFrame(
                audit_user(username)
            )
        )

# ---------------------------
# GROUP AUDIT
# ---------------------------

elif audit_type == "Group Audit":

    group_name = st.text_input(
        "Group",
        key="audit_group"
    )

    if st.button(
        "Run Group Audit",
        key="audit_group_btn"
    ):

        st.dataframe(
            pd.DataFrame(
                audit_group(group_name)
            )
        )

# ---------------------------
# SUDO AUDIT
# ---------------------------

elif audit_type == "Sudo Audit":

    st.dataframe(
        pd.DataFrame(
            audit_sudo(),
            columns=["sudo_entry"]
        )
    )

# ---------------------------
# SERVICE ACCOUNTS
# ---------------------------

elif audit_type == "Service Accounts":

    st.dataframe(
        pd.DataFrame(
            audit_service_accounts()
        )
    )

# ---------------------------
# GOVERNANCE
# ---------------------------

elif audit_type == "Identity Governance":

    results = identity_governance_summary()

    for section, data in results.items():

        st.subheader(
            section.replace(
                "_",
                " "
            ).title()
        )

        st.dataframe(
            pd.DataFrame(data)
        )

# ---------------------------
# TARGET HOSTNAME
# ---------------------------

target = st.text_input(
    "Target Hostname"
)

if target:

    asset = get_asset_by_hostname(
        target
    )

    st.write(asset)
