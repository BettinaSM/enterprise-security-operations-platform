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

        if "scp" in text:

            chain.append(

                "Exfiltration"

            )

    return list(

        set(chain)

    )
