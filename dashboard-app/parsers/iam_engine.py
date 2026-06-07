import pwd
import grp

# ---------------------------
# LOCAL USERS
# ---------------------------

def get_local_users():

    users = []

    for user in pwd.getpwall():

        users.append({

            "username": user.pw_name,
            "uid": user.pw_uid,
            "gid": user.pw_gid,
            "home": user.pw_dir,
            "shell": user.pw_shell
        })

    return users

# ---------------------------
# PRIVILEGED USERS
# ---------------------------

def get_privileged_users():

    privileged = []

    for user in pwd.getpwall():

        if user.pw_uid == 0:

            privileged.append(user.pw_name)

    return privileged

# ---------------------------
# GROUPS
# ---------------------------

def get_groups():

    groups = []

    for group in grp.getgrall():

        groups.append({

            "group": group.gr_name,
            "gid": group.gr_gid,
            "members": ",".join(group.gr_mem)
        })

    return groups
