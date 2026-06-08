def calculate_compliance_score(audit):

    score = 100

    if audit.get("sudo_users"):

        score -= 5

    if audit.get("service_accounts"):

        score -= 5

    if len(audit.get("local_users", [])) > 50:

        score -= 10

    if score < 0:

        score = 0

    return {

        "score": score
    }
