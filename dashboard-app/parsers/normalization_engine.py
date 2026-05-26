def normalize_event(

    source,
    raw_log

):

    log = raw_log.lower()

    severity = "Low"

    event_type = "Informational"

    # ---------------------------
    # FAILED AUTH
    # ---------------------------

    if "failed" in log:

        severity = "High"

        event_type = "Failed Authentication"

    # ---------------------------
    # SUDO
    # ---------------------------

    elif "sudo" in log:

        severity = "Medium"

        event_type = "Privileged Command"

    # ---------------------------
    # ROOT
    # ---------------------------

    elif "root" in log:

        severity = "Critical"

        event_type = "Root Activity"

    # ---------------------------
    # NETWORK
    # ---------------------------

    elif "curl" in log or "wget" in log:

        severity = "Critical"

        event_type = "Suspicious Network Activity"

    return {

        "source": source,

        "event_type": event_type,

        "severity": severity,

        "raw_log": raw_log
    }
