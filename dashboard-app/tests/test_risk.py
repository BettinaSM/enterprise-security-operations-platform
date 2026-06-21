from parsers.risk_engine import (
    calculate_risk_score
)

def test_risk_engine():

    detections = [

        {
            "severity": "Critical"
        }

    ]

    risk = calculate_risk_score(
        detections
    )

    assert risk["score"] > 0
