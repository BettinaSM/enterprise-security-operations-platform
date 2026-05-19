MITRE_MAPPINGS = {
    "failed ssh": {
        "technique": "T1110",
        "name": "Brute Force"
    },

    "sudo": {
        "technique": "T1548",
        "name": "Abuse Elevation Control Mechanism"
    },

    "privileged": {
        "technique": "T1068",
        "name": "Privilege Escalation"
    },

    "createuser": {
        "technique": "T1136",
        "name": "Create Account"
    },

    "kubectl exec": {
        "technique": "T1059",
        "name": "Command Execution"
    }
}


def map_to_mitre(events):

    mapped = []

    for event in events:

        event_str = str(event).lower()

        for keyword, mitre_data in MITRE_MAPPINGS.items():

            if keyword in event_str:

                mapped.append({
                    "event": event,
                    "technique": mitre_data["technique"],
                    "name": mitre_data["name"]
                })

    return mapped
