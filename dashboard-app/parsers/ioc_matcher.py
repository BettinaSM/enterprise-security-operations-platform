from parsers.ioc_auto_ingest import (
    load_remote_iocs
)

# ---------------------------
# STATIC IOCS
# ---------------------------

STATIC_IOCS = [

    "185.220.101.1",
    "malicious-domain.com"
]

# ---------------------------
# LOAD IOCS
# ---------------------------

def load_all_iocs():

    remote_iocs = load_remote_iocs()

    return list(

        set(

            STATIC_IOCS +
            remote_iocs
        )
    )

# ---------------------------
# MATCH IOCS
# ---------------------------

def match_ioc(
    log_lines
):

    matches = []

    indicators = load_all_iocs()

    for line in log_lines:

        for indicator in indicators:

            if indicator in line:

                matches.append({

                    "ioc": indicator,
                    "log": line,
                    "severity": "Critical"
                })

    return matches
