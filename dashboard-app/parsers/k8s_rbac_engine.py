from kubernetes import client

from integrations.kubernetes_connector import (
    connect_cluster
)

def get_k8s_roles():

    connect_cluster()

    api = client.RbacAuthorizationV1Api()

    roles = api.list_cluster_role()

    data = []

    for role in roles.items:

        data.append({

            "role":
                role.metadata.name,

            "source":
                "Kubernetes"

        })

    return data
