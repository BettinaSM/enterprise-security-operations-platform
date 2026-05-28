import socket

# ---------------------------
# SYSLOG SERVER
# ---------------------------

SYSLOG_PORT = 5140

# ---------------------------
# START SYSLOG LISTENER
# ---------------------------

def start_syslog_listener():

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    sock.bind(
        ("0.0.0.0", SYSLOG_PORT)
    )

    return sock

# ---------------------------
# RECEIVE EVENTS
# ---------------------------

def receive_syslog_event(
    sock
):

    try:

        data, addr = sock.recvfrom(
            65535
        )

        return {

            "source_ip": addr[0],
            "event": data.decode(
                errors="ignore"
            )
        }

    except Exception as error:

        return {

            "error": str(error)
        }
