import json


def load_threat_feed(path):

    with open(path, "r") as file:

        return json.load(file)


def correlate_threat_feed(
    ioc_matches,
    feed_data
):

    findings = []

    for ioc in ioc_matches:

        for item in feed_data:

            if ioc == item["ioc"]:

                findings.append({
                    "IOC": ioc,
                    "Type": item["type"],
                    "Threat Actor": item["threat_actor"],
                    "Campaign": item["campaign"],
                    "Reputation": item["reputation"]
                })

    return findings
