def calculate_security_posture(

        compliance,
        vulnerabilities,
        incidents,
        identity_risk):

    score = 100

    score -= vulnerabilities * 2

    score -= incidents * 3

    score -= identity_risk

    score += compliance

    if score < 0:
        score = 0

    return score
