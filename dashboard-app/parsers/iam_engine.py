import os
import pwd
import grp
import platform

# ---------------------------
# PLATFORM
# ---------------------------

OS_TYPE = platform.system().lower()

# ---------------------------
# LOCAL USERS
# ---------------------------

def get_local_users():

    if OS_TYPE == "windows":

        return get_windows_users()

    return get_unix_users()

# ---------------------------
# UNIX USERS
# ---------------------------

def get_unix_users():

    users = []

    for user in pwd.getpwall():

        users.append({

            "username": user.pw_name,
            "uid": user.pw_uid,
            "gid": user.pw_gid,
            "shell": user.pw_shell,
            "source": "Local"

        })

    return users

# ---------------------------
# WINDOWS USERS
# ---------------------------

def get_windows_users():

    return [

        {
            "username": "Administrator",
            "source": "Local"
        }

    ]

# ---------------------------
# GROUPS
# ---------------------------

def get_groups():
    
    if OS_TYPE == "windows":

        return []

    groups = []

    for group in grp.getgrall():

        groups.append({

            "group": group.gr_name,
            "gid": group.gr_gid,
            "members": group.gr_mem
        })

    return groups

# ---------------------------
# SUDO USERS
# ---------------------------

def get_sudo_users():

    sudo_users = []

    sudo_files = [

        "/etc/sudoers"

    ]

    for file_path in sudo_files:

        if not os.path.exists(file_path):

            continue

        try:

            with open(file_path) as file:

                for line in file:

                    line = line.strip()

                    if (

                        line
                        and not line.startswith("#")

                    ):

                        sudo_users.append(line)

        except:

            pass

    return sudo_users
