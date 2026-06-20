# --------------------------------
# CVSS CALCULATOR
# --------------------------------

def classify_cvss(score):

    if score >= 9:

        return "Critical"

    elif score >= 7:

        return "High"

    elif score >= 4:

        return "Medium"

    return "Low"


# --------------------------------
# CVSS TO RISK
# --------------------------------

def cvss_to_risk(score):

    return {

        "cvss": score,

        "severity": classify_cvss(score)

    }
