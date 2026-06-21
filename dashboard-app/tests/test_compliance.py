from parsers.compliance_engine import (
    run_compliance
)

def test_compliance():

    results = run_compliance()

    assert isinstance(
        results,
        list
    )
