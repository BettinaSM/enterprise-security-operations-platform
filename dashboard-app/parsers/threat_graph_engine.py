from collections import defaultdict

# --------------------------------
# BUILD THREAT GRAPH
# --------------------------------

def build_threat_graph(events):

    graph = defaultdict(list)

    for event in events:

        if not isinstance(event, dict):

            continue

        username = event.get(
            "username",
            "unknown"
        )

        hostname = event.get(
            "hostname",
            "unknown"
        )

        source_ip = event.get(
            "ip",
            "unknown"
        )

        cloud = event.get(
            "cloud",
            None
        )

        # User -> Host

        if username != "unknown":

            graph[username].append(hostname)

        # Host -> IP

        if hostname != "unknown":

            graph[hostname].append(source_ip)

        # User -> Cloud

        if cloud:

            graph[username].append(cloud)

    return dict(graph)


# --------------------------------
# USER RELATIONSHIP
# --------------------------------

def get_user_relationships(

    graph,
    username

):

    return graph.get(
        username,
        []
    )


# --------------------------------
# HOST RELATIONSHIP
# --------------------------------

def get_host_relationships(

    graph,
    hostname

):

    return graph.get(
        hostname,
        []
    )


# --------------------------------
# RISKY IDENTITIES
# --------------------------------

def find_highly_connected_identities(graph):

    findings = []

    for node, relations in graph.items():

        if len(relations) >= 5:

            findings.append({

                "identity": node,

                "connections": len(relations),

                "risk": "High"

            })

    return findings
