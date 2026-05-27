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

            if ioc == item.get("ioc"):

                correlations.append({

                    "IOC": item.get(
                        "ioc",
                        "Unknown"
                    ),

                    "Type": item.get(
                        "type",
                        "Unknown"
                    ),

                    "Threat": item.get(
                        "threat",
                        "Unknown"
                    ),

                    "Threat Actor": item.get(
                        "threat_actor",
                        "Unknown"
                    ),

                    "Severity": item.get(
                        "severity",
                        item.get(
                            "reputation",
                            "Medium"
                        )
                    ),

                    "Campaign": item.get(
                        "campaign",
                        "Unknown"
                    )
                })

    return correlations
