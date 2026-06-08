from datetime import datetime

def generate_access_review(users):

    results = []

    for user in users:

        results.append({

            "username":
                user.get(
                    "username"
                ),

            "last_review":
                datetime.now().strftime(
                    "%Y-%m-%d"
                ),

            "review_status":
                "Pending"

        })

    return results
