import os
import pwd
import grp

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
            "shell": user.pw_shell

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

    sudo_entries = []

    sudo_files = [

        "/etc/sudoers"
    ]

    for path in sudo_files:

        if not os.path.exists(path):

            continue

        try:

            with open(path) as file:

                for line in file:

                    line = line.strip()

                    if line and not line.startswith("#"):

                        sudo_entries.append(line)

        except:

            pass

    return sudo_entries

# ---------------------------
# AUDIT
# ---------------------------

def run_linux_audit():

    return {

        "users": get_linux_users(),
        "groups": get_linux_groups(),
        "sudo": get_linux_sudo()

    }
