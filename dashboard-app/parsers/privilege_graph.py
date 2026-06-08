from parsers.iam_engine import (
    get_groups,
    get_sudo_users
)

# ---------------------------
# PRIVILEGE GRAPH
# ---------------------------

def build_privilege_graph(username):

    graph = []

    graph.append(

        f"User -> {username}"

    )

    for group in get_groups():

        if username in group.get(
            "members",
            []
        ):

            graph.append(

                f"{username} -> {group['group']}"

            )

    for sudo in get_sudo_users():

        if username in sudo:

            graph.append(

                f"{username} -> SUDO"

            )

    return graph
