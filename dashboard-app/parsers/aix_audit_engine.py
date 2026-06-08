import os
import pwd
import grp

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
            "shell": user.pw_shell

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
# RBAC
# ---------------------------

def get_aix_roles():

    roles = []

    role_file = "/etc/security/roles"

    if os.path.exists(role_file):

        roles.append(role_file)

    return roles

# ---------------------------
# AUDIT
# ---------------------------

def run_aix_audit():

    return {

        "users": get_aix_users(),
        "groups": get_aix_groups(),
        "roles": get_aix_roles()

    }
