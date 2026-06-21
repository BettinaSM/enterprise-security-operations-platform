from parsers.ccm_engine import (
    calculate_framework_score
)

def get_compliance_dashboard():

    return {

        "ISO27001":

            calculate_framework_score(
                "iso27001_controls"
            ),

        "CIS":

            calculate_framework_score(
                "cis_controls"
            ),

        "NIST":

            calculate_framework_score(
                "nist_controls"
            ),

        "PCI":

            calculate_framework_score(
                "pci_dss_controls"
            ),

        "LGPD":

            calculate_framework_score(
                "lgpd_controls"
            )

    }
