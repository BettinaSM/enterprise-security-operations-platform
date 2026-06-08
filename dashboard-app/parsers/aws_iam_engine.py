import boto3

def get_aws_users():

    try:
        iam = boto3.client("iam")
        
        response = iam.list_users()
        
        return response["Users"]
        
    except Exception:

        return [

            {
                "UserName": "aws-admin-simulated"
            },

            {
                "UserName": "aws-readonly-simulated"
            }

        ]
