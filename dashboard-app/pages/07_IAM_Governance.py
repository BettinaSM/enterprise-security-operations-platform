import streamlit as st
import pandas as pd


from parsers.session_auth import (
    require_auth
)

require_auth()

from parsers.iam_engine import (
    get_local_users,
    get_privileged_users,
    get_groups
)

from parsers.ldap_engine import (
    get_ldap_users
)

from parsers.ad_engine import (
    get_ad_users
)

from parsers.aws_iam_engine import (
    get_aws_users
)

from parsers.azure_iam_engine import (
    get_entra_users
)

from parsers.gcp_iam_engine import (
    get_gcp_users
)

from parsers.k8s_rbac_engine import (
    get_k8s_roles
)

st.title(
    "IAM Governance"
)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([

    "Local",
    "LDAP",
    "AD",
    "Cloud",
    "Kubernetes"

])

with tab1:

    st.subheader(
        "Local Users"
    )

    users = get_local_users()

    st.dataframe(
        pd.DataFrame(
            users
        ),
        use_container_width=True
    )

    st.subheader(
        "Privileged Accounts"
    )

    privileged = get_privileged_users()

    st.write(
        privileged
    )

    st.subheader(
        "Groups"
    )

    groups = get_groups()

    st.dataframe(
        pd.DataFrame(
            groups
        ),
        use_container_width=True
    )

with tab2:

    st.dataframe(
        pd.DataFrame(
            get_ldap_users()
        )
    )

with tab3:

    st.dataframe(
        pd.DataFrame(
            get_ad_users()
        )
    )

with tab4:

    cloud_users = (

        get_aws_users()
        +
        get_entra_users()
        +
        get_gcp_users()

    )

    st.dataframe(
        pd.DataFrame(
            cloud_users
        )
    )

with tab5:

    st.dataframe(
        pd.DataFrame(
            get_k8s_roles()
        )
    )

with tab6:

    st.subheader(
        "Service Accounts"
    )

    st.write(
        get_service_accounts()
    )
