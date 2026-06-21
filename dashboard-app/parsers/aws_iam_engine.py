from integrations.aws_connector import (
    aws_connect
)


def get_aws_users():

    client = aws_connect()

    if not client:

        return []

    try:

        response = client.list_users()

        return [

            {

                "username":
                    user["UserName"],

                "source":
                    "AWS IAM"

            }

            for user in response["Users"]

        ]

    except:

        return []
