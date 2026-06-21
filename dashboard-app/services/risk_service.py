from parsers.risk_engine import (

    calculate_risk_score

)


def calculate_enterprise_risk(

    detections,

    **kwargs

):

    return calculate_risk_score(

        detections,

        **kwargs
    )
