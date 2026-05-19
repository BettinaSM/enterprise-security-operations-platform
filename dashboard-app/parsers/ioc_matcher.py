known_bad_ips = [
    "185.220.101.1"
]


def match_ioc(log_lines):

    matches = []

    for line in log_lines:

        for ip in known_bad_ips:

            if ip in line:

                matches.append(ip)

    return matches
