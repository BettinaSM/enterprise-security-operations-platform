# --------------------------------
# DEVICE TRUST
# --------------------------------

def evaluate_device(device):

    score = 0

    if device.get(
        "managed",
        False
    ):
        score += 40

    if device.get(
        "encrypted",
        False
    ):
        score += 20

    if device.get(
        "compliant",
        False
    ):
        score += 30

    if device.get(
        "antivirus",
        False
    ):
        score += 10

    if score >= 80:

        level = "Trusted"

    elif score >= 50:

        level = "Partially Trusted"

    else:

        level = "Untrusted"

    return {

        "hostname":
            device.get("hostname"),

        "score":
            score,

        "trust_level":
            level

    }
