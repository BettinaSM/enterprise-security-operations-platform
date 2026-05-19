def calculate_threat_score(
    critical_alerts,
    failed_auth,
    cloud_findings_count,
    ioc_matches_count
):

    score = 0

    score += critical_alerts * 25
    score += failed_auth * 5
    score += cloud_findings_count * 20
    score += ioc_matches_count * 30

    if score >= 100:
        severity = "Critical"

    elif score >= 60:
        severity = "High"

    elif score >= 30:
        severity = "Medium"

    else:
        severity = "Low"

    return score, severity
