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

# --------------------------------
# DAILY REPORT
# --------------------------------

from datetime import datetime


def generate_daily_report():

    return {

        "generated_at":
            datetime.utcnow().isoformat(),

        "summary": {

            "detections": 0,
            "incidents": 0,
            "critical_findings": 0,
            "risk_score": 0

        }

    }
