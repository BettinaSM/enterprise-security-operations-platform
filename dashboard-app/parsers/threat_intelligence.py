THREAT_FEED = {

    "185.220.101.1": {
        "type": "TOR Exit Node",
        "severity": "Critical",
        "confidence": "High"
    },

    "45.155.205.233": {
        "type": "C2 Infrastructure",
        "severity": "Critical",
        "confidence": "High"
    },

    "103.245.228.12": {
        "type": "Botnet",
        "severity": "High",
        "confidence": "Medium"
    }
}

def enrich_iocs(iocs):

    enriched = []

    for ioc in iocs:

        if ioc in THREAT_FEED:

            entry = THREAT_FEED[ioc]

            enriched.append({
                "IOC": ioc,
                "Threat Type": entry["type"],
                "Severity": entry["severity"],
                "Confidence": entry["confidence"]
            })

    return enriched
