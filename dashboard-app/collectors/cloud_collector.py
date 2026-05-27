from configs.settings import (
    SIMULATION_MODE
)

from parsers.cloud_parser import (
    load_json_log
)

# ---------------------------
# CLOUD COLLECTOR
# ---------------------------

def collect_cloud_logs():

    if SIMULATION_MODE:

        return {

            "aws": load_json_log(
                "agents/aws/cloudtrail.json"
            ),

            "azure": load_json_log(
                "agents/azure/entra-signins.json"
            ),

            "gcp": load_json_log(
                "agents/gcp/audit-logs.json"
            ),

            "oci": load_json_log(
                "agents/oracle-cloud/oci-audit.json"
            ),

            "ibm": load_json_log(
                "agents/ibm-cloud/activity-tracker.json"
            )
        }

    # ---------------------------
    # REAL CLOUD COLLECTION
    # ---------------------------

    return {

        "aws": [],
        "azure": [],
        "gcp": [],
        "oci": [],
        "ibm": []
    }
