def correlate_security_events(
    failed_auth,
    critical_alerts,
    cloud_findings,
    ioc_matches
):

    correlations = []

    # Multi-stage attack simulation

    if failed_auth >= 5 and critical_alerts >= 1:

        correlations.append({
            "Correlation": "Possible Initial Access + Execution",
            "Severity": "Critical",
            "MITRE": "T1110 + T1059"
        })

    if len(cloud_findings) >= 1 and len(ioc_matches) >= 1:

        correlations.append({
            "Correlation": "Cloud Compromise + IOC Activity",
            "Severity": "High",
            "MITRE": "T1078"
        })

    if failed_auth >= 10:

        correlations.append({
            "Correlation": "SSH Brute Force Campaign",
            "Severity": "Critical",
            "MITRE": "T1110"
        })

    return correlations
