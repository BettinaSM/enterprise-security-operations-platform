from pathlib import Path

REAL_LOGS = [

    "/var/log/auth.log",
    "/var/log/secure",
    "/var/log/messages"

]

def collect_linux_real_logs():

    collected = []

    for log_path in REAL_LOGS:

        path = Path(log_path)

        if path.exists():

            try:

                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as file:

                    lines = file.readlines()[-100:]

                    collected.extend([
                        line.strip()
                        for line in lines
                        if line.strip()
                    ])

            except Exception as error:

                collected.append(
                    f"linux_real_collector_error: {error}"
                )

    return collected
