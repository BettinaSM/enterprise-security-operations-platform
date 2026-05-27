import json

# ---------------------------
# LOAD THREAT FEED
# ---------------------------

def load_threat_feed(path):

    with open(path, "r") as file:

        return json.load(file)

# ---------------------------
# CORRELATE THREAT FEED
# ---------------------------

def correlate_threat_feed(
    ioc_matches,
    threat_feed
):

    correlations = []

    for ioc in ioc_matches:

        for item in threat_feed:

            if ioc == item.get("indicator"):

                correlations.append({

                    "Indicator": item.get(
                        "indicator",
                        "Unknown"
                    ),

                    "Type": item.get(
                        "type",
                        "Unknown"
                    ),

                    "Severity": item.get(
                        "severity",
                        "Medium"
                    ),

                    "Source": item.get(
                        "source",
                        "Threat Feed"
                    )
                })

    return correlations
