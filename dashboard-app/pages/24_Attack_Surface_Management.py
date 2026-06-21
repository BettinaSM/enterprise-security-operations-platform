import streamlit as st
import pandas as pd

from parsers.session_auth import (
    require_auth
)

from parsers.asm_engine import (
    get_internet_facing_assets
)

from parsers.certificate_engine import (
    get_expiring_certificates
)

from parsers.shadow_it_engine import (
    detect_shadow_it
)

from parsers.dns_inventory_engine import (
    load_domains
)

require_auth()

st.title(
    "Attack Surface Management"
)

tab1, tab2, tab3, tab4 = st.tabs([

    "External Assets",
    "Certificates",
    "DNS Inventory",
    "Shadow IT"

])

with tab1:

    st.dataframe(

        pd.DataFrame(
            get_internet_facing_assets()
        ),

        use_container_width=True

    )

with tab2:

    st.dataframe(

        pd.DataFrame(
            get_expiring_certificates()
        ),

        use_container_width=True

    )

with tab3:

    st.dataframe(

        pd.DataFrame(
            load_domains()
        ),

        use_container_width=True

    )

with tab4:

    st.dataframe(

        pd.DataFrame(
            detect_shadow_it()
        ),

        use_container_width=True

    )
