import boto3

def get_aws_users():

    iam = boto3.client("iam")

    response = iam.list_users()

    return response["Users"]
