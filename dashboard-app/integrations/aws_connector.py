try:

    import boto3

except:

    boto3 = None


def aws_connect():

    if not boto3:

        return None

    try:

        return boto3.client(

            "iam",

            region_name="us-east-1"

        )

    except:

        return None
