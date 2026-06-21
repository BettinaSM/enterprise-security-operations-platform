from datetime import datetime

# --------------------------------
# NORMALIZE EVENT
# --------------------------------

def normalize_event(

    source,
    raw_log

):

    log = str(raw_log).lower()

    severity = "Low"

    event_type = "Informational"

    username = "unknown"

    hostname = "unknown"

    ip = "unknown"

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

    elif (

        "curl" in log
        or "wget" in log
        or "scp" in log
        or "nc " in log

    ):

        severity = "Critical"

        event_type = "Suspicious Network Activity"

    # ---------------------------
    # GENERIC FIELDS
    # ---------------------------

    if isinstance(raw_log, dict):

        username = raw_log.get(

            "username",

            raw_log.get(
                "user",
                "unknown"
            )
        )

        hostname = raw_log.get(

            "hostname",

            raw_log.get(
                "host",
                "unknown"
            )
        )

        ip = raw_log.get(

            "ip",

            raw_log.get(
                "source_ip",
                "unknown"
            )
        )

    return {

        "timestamp":

            datetime.utcnow().isoformat(),

        "source":

            source,

        "username":

            username,

        "hostname":

            hostname,

        "ip":

            ip,

        "event_type":

            event_type,

        "severity":

            severity,

        "raw_log":

            str(raw_log)

    }
