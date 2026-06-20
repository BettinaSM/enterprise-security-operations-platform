# ---------------------------
# RISK ENGINE
# ---------------------------

SEVERITY_WEIGHTS = {

    "Low": 5,
    "Medium": 20,
    "High": 50,
    "Critical": 80
}

# ---------------------------
# CALCULATE RISK
# ---------------------------

def calculate_risk_score(

    detections,

    threat_intel=False,

    privileged_activity=False,

    lateral_movement=False,

    baseline_drift=False,

    suspicious_user=False,

    cloud_event=False,

    identity_risk=False

):

    score = 0

    # ---------------------------
    # DETECTIONS
    # ---------------------------

    for detection in detections:

        severity = detection.get(
            "severity",
            "Low"
        )

        score += SEVERITY_WEIGHTS.get(
            severity,
            0
        )

    # ---------------------------
    # THREAT INTEL
    # ---------------------------

    if threat_intel:

        score += 30

    # ---------------------------
    # PRIVILEGED ACTIVITY
    # ---------------------------

    if privileged_activity:

        score += 25

    # ---------------------------
    # LATERAL MOVEMENT
    # ---------------------------

    if lateral_movement:

        score += 40

    # ---------------------------
    # BASELINE DRIFT
    # ---------------------------

    if baseline_drift:

        score += 35

    # ---------------------------
    # UEBA
    # ---------------------------

    if suspicious_user:

        score += 30

    # ---------------------------
    # CLOUD
    # ---------------------------

    if cloud_event:

        score += 20
        
    # ---------------------------
    # IAM
    # ---------------------------

    if identity_risk:

        score += 30
    
    # ---------------------------
    # LIMIT
    # ---------------------------

    if score > 100:

        score = 100

    # ---------------------------
    # LEVEL
    # ---------------------------

    if score >= 90:

        level = "Critical"

    elif score >= 70:

        level = "High"

    elif score >= 40:

        level = "Medium"

    else:

        level = "Low"

    return {

        "score":
            score,
        "level":
            level
    }
