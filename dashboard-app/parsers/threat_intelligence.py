def enrich_iocs(iocs):

    enriched = []

    malicious_iocs = {
        "185.220.101.1": {
            "type": "TOR Exit Node",
            "risk": "Critical",
            "country": "Unknown"
        },

        "192.168.1.200": {
            "type": "Internal Recon",
            "risk": "Medium",
            "country": "Internal"
        },

        "evil-admin.com": {
            "type": "Malicious Domain",
            "risk": "High",
            "country": "RU"
        }
    }

    for ioc in iocs:

        if ioc in malicious_iocs:

            data = malicious_iocs[ioc]

            enriched.append({
                "ioc": ioc,
                "type": data["type"],
                "risk": data["risk"],
                "country": data["country"]
            })

    return enriched
