# --------------------------------
# EVENTS CORRELATION
# --------------------------------

def correlate_security_events(
    failed_auth,
    critical_alerts,
    cloud_findings,
    ioc_matches
):

    correlations = []

    # Multi-stage attack simulation

    if failed_auth >= 5 and critical_alerts >= 1:

        correlations.append({
            "Correlation": "Possible Initial Access + Execution",
            "Severity": "Critical",
            "MITRE": "T1110 + T1059"
        })

    if len(cloud_findings) >= 1 and len(ioc_matches) >= 1:

        correlations.append({
            "Correlation": "Cloud Compromise + IOC Activity",
            "Severity": "High",
            "MITRE": "T1078"
        })

    if failed_auth >= 10:

        correlations.append({
            "Correlation": "SSH Brute Force Campaign",
            "Severity": "Critical",
            "MITRE": "T1110"
        })

    return correlations
# --------------------------------
# USER CORRELATION
# --------------------------------

def correlate_user_activity(events):

    findings = []

    failed = 0

    privileged = 0

    lateral = 0

    for event in events:

        text = str(event).lower()

        if "failed" in text:

            failed += 1

        if (

            "sudo" in text
            or "administrator" in text
            or "root" in text

        ):

            privileged += 1

        if (

            "psexec" in text
            or "winrm" in text
            or "ssh" in text

        ):

            lateral += 1

    if (

        failed >= 5

        and privileged >= 1

    ):

        findings.append({

            "Correlation":

                "Compromised Privileged Identity",

            "Severity":

                "Critical"

        })

    if lateral >= 3:

        findings.append({

            "Correlation":

                "Possible Lateral Movement Campaign",

            "Severity":

                "Critical"

        })

    return findings
