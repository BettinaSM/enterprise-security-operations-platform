def hunt_logs(
    hunt_term,
    logs
):

    findings = []

    for log in logs:

        if hunt_term.lower() in log.lower():

            findings.append(log)

    return findings
