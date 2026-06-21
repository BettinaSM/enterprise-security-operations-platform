from integrations.aws_connector import collect_aws

from integrations.azure_connector import collect_azure

from integrations.gcp_connector import collect_gcp


def collect_cloud_assets():

    return {

        "aws": collect_aws(),

        "azure": collect_azure(),

        "gcp": collect_gcp()

    }
