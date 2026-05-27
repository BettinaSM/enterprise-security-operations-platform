from parsers.cloud_parser import load_json_log

def collect_cloud_logs():

    return {

        "aws": load_json_log(
            "agents/aws/cloudtrail.json"
        ),

        "azure": load_json_log(
            "agents/azure/entra-signins.json"
        ),

        "gcp": load_json_log(
            "agents/gcp/audit-logs.json"
        )
    }
