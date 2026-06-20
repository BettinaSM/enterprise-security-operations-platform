from datetime import datetime

# --------------------------------
# SESSION TRUST
# --------------------------------

def evaluate_session(session):

    score = 100

    if session.get(
        "impossible_travel",
        False
    ):

        score -= 40

    if session.get(
        "privileged_session",
        False
    ):

        score -= 10

    if session.get(
        "anonymous_ip",
        False
    ):

        score -= 30

    if session.get(
        "tor",
        False
    ):

        score -= 30

    if score < 0:

        score = 0

    return {

        "user":
            session.get("user"),

        "score":
            score,

        "trusted":
            score >= 60

    }
