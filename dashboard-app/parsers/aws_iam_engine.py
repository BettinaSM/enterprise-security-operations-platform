from integrations.aws_connector import (
    aws_session
)

def get_aws_users():

    session = aws_session()

    iam = session.client("iam")

    users = []

    paginator = iam.get_paginator(
        "list_users"
    )

    for page in paginator.paginate():

        for user in page["Users"]:

            users.append({

                "username":
                    user["UserName"],

                "arn":
                    user["Arn"],

                "created":
                    str(user["CreateDate"]),

                "source":
                    "AWS IAM"

            })

    return users
