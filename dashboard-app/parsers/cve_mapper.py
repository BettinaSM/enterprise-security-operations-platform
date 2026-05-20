def enrich_cves(iocs):

    findings = []

    simulated_mapping = {

        "185.220.101.1": {
            "cve": "CVE-2024-3094",
            "threat_actor": "UNC5221",
            "malware": "XZ Backdoor",
            "severity": "Critical"
        },

        "malicious-domain.com": {
            "cve": "CVE-2023-23397",
            "threat_actor": "APT29",
            "malware": "Outlook NTLM Leak",
            "severity": "High"
        }
    }

    for ioc in iocs:

        if ioc in simulated_mapping:

            item = simulated_mapping[ioc]

            findings.append({
                "IOC": ioc,
                "CVE": item["cve"],
                "Threat Actor": item["threat_actor"],
                "Malware": item["malware"],
                "Severity": item["severity"]
            })

    return findings
