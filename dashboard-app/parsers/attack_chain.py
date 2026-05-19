def build_attack_chain(
    failed_auth,
    cloud_findings,
    ioc_matches,
    critical_alerts
):

    chain = []

    if failed_auth > 3:

        chain.append(
            "Initial Access - SSH Brute Force"
        )

    if cloud_findings:

        chain.append(
            "Valid Accounts - Cloud Login"
        )

    if critical_alerts > 0:

        chain.append(
            "Privilege Escalation"
        )

    if ioc_matches:

        chain.append(
            "Command and Control Activity"
        )

    return chain
