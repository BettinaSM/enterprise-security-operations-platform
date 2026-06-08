import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.identity_governance import (
    run_identity_governance
)

from parsers.identity_risk_engine import (
    calculate_identity_risk
)

require_auth()

st.set_page_config(
    page_title="Identity Governance",
    page_icon="👤",
    layout="wide"
)

st.title(
    "Identity Governance"
)

results = run_identity_governance()

for section, data in results.items():

    st.subheader(

        section.replace(
            "_",
            " "
        ).title()

    )

    if isinstance(data, list):

        df = pd.DataFrame(data)

        if (
            section == "privileged_accounts"
            and not df.empty
        ):

            risk_results = []

            for _, row in df.iterrows():

                risk = calculate_identity_risk({

                    "privileged": True,
                    "sudo": True,
                    "failed_logins": 0,
                    "mfa_enabled": False

                })

                risk_results.append({

                    "account": row.iloc[0],
                    "risk_score": risk["score"],
                    "risk_level": risk["level"]

                })

            st.dataframe(
                pd.DataFrame(risk_results),
                use_container_width=True
            )

        else:

            st.dataframe(
                df,
                use_container_width=True
            )
