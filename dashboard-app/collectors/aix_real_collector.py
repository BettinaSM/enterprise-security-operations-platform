from pathlib import Path

AIX_LOGS = [

    "/var/adm/sulog",
    "/var/adm/ras/syslog.caa",
    "/var/adm/messages"

]

def collect_aix_real_logs():

    collected = []

    for log_path in AIX_LOGS:

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
                    f"aix_real_collector_error: {error}"
                )

    return collected
