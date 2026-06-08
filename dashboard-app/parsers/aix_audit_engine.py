import os
import pwd
import grp
import subprocess

# ---------------------------
# USERS
# ---------------------------

def get_aix_users():

    users = []

    for user in pwd.getpwall():

        users.append({

            "username": user.pw_name,
            "uid": user.pw_uid,
            "gid": user.pw_gid,
            "shell": user.pw_shell,
            "source": "AIX"

        })

    return users

# ---------------------------
# GROUPS
# ---------------------------

def get_aix_groups():

    groups = []

    for group in grp.getgrall():

        groups.append({

            "group": group.gr_name,
            "gid": group.gr_gid,
            "members": group.gr_mem

        })

    return groups

# ---------------------------
# ROLES
# ---------------------------

def get_aix_roles():

    try:

        result = subprocess.run(

            ["lsrole"],

            capture_output=True,
            text=True

        )

        return result.stdout.splitlines()

    except:

        role_file = "/etc/security/roles"

        if os.path.exists(role_file):

            return [role_file]

        return []

# ---------------------------
# SUDO
# ---------------------------

def get_aix_sudo():

    sudo_file = "/etc/sudoers"

    if not os.path.exists(sudo_file):

        return []

    entries = []

    with open(sudo_file) as file:

        for line in file:

            line = line.strip()

            if line and not line.startswith("#"):

                entries.append(line)

    return entries

# ---------------------------
# AUDIT
# ---------------------------

def run_aix_audit():

    return {

        "users": get_aix_users(),
        "groups": get_aix_groups(),
        "roles": get_aix_roles()

    }
