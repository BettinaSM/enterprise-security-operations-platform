import os
import pwd
import grp
import subprocess

# ---------------------------
# USERS
# ---------------------------

def get_linux_users():

    users = []

    for user in pwd.getpwall():

        users.append({

            "username": user.pw_name,
            "uid": user.pw_uid,
            "gid": user.pw_gid,
            "shell": user.pw_shell,
            "source": "Linux"

        })

    return users

# ---------------------------
# GROUPS
# ---------------------------

def get_linux_groups():

    groups = []

    for group in grp.getgrall():

        groups.append({

            "group": group.gr_name,
            "gid": group.gr_gid,
            "members": group.gr_mem

        })

    return groups

# ---------------------------
# SUDO
# ---------------------------

def get_linux_sudo():

    entries = []

    sudo_files = [

        "/etc/sudoers"

    ]

    sudoers_d = "/etc/sudoers.d"

    if os.path.exists(sudoers_d):

        for file in os.listdir(sudoers_d):

            sudo_files.append(
                f"{sudoers_d}/{file}"
            )

    for path in sudo_files:

        if not os.path.exists(path):

            continue

        try:

            with open(path) as file:

                for line in file:

                    line = line.strip()

                    if (

                        line
                        and not line.startswith("#")

                    ):

                        entries.append(line)

        except:

            pass

    return entries

# ---------------------------
# LAST LOGINS
# ---------------------------

def get_last_logins():

    try:

        result = subprocess.run(

            ["last", "-n", "20"],

            capture_output=True,
            text=True

        )

        return result.stdout.splitlines()

    except:

        return []

# ---------------------------
# SERVICES
# ---------------------------

def get_running_services():

    try:

        result = subprocess.run(

            [
                "systemctl",
                "list-units",
                "--type=service",
                "--state=running"
            ],

            capture_output=True,
            text=True

        )

        return result.stdout.splitlines()

    except:

        return []

# ---------------------------
# AUDIT
# ---------------------------

def run_linux_audit():

    return {

        "users": get_linux_users(),
        "groups": get_linux_groups(),
        "sudo": get_linux_sudo(),
        "last_logins": get_last_logins(),
        "services": get_running_services()

    }
