from parsers.reporting_engine import (
    generate_executive_report
)

def generate_report(
    threat_score,
    risk_level,
    incidents,
    critical_alerts
):

    return generate_executive_report(
        threat_score,
        risk_level,
        incidents,
        critical_alerts
    )
