from collections import Counter

# ---------------------------
# MITRE HEATMAP
# ---------------------------

def build_mitre_heatmap(
    mitre_events
):

    techniques = []

    for event in mitre_events:

        technique = event.get(
            "technique",
            "Unknown"
        )

        techniques.append(
            technique
        )

    counts = Counter(
        techniques
    )

    return [

        {
            "Technique": k,
            "Count": v
        }

        for k, v in counts.items()
    ]
