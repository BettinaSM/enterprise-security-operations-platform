from parsers.identity_risk_engine import (
    calculate_identity_risk
)

def test_identity_risk():

    identity = {

        "privileged": True,
        "sudo": True

    }

    result = calculate_identity_risk(
        identity
    )

    assert result["score"] > 0
