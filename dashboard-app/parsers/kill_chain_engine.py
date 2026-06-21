def reconstruct_killchain(events):

    chain = []

    for event in events:

        text = str(event).lower()

        if "failed" in text:

            chain.append(
                "Initial Access"
            )

        if "sudo" in text:

            chain.append(
                "Privilege Escalation"
            )

        if "powershell" in text:

            chain.append(
                "Execution"
            )

        if "curl" in text:

            chain.append(
                "Command And Control"
            )

        if "scp" in text:

            chain.append(
                "Exfiltration"
            )

    if not chain:

        chain = [

            "Reconnaissance",
            "Initial Access",
            "Privilege Escalation"

        ]

    return list(set(chain))
