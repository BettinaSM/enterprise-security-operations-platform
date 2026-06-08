def get_k8s_roles():

    return [

        {
            "role": "cluster-admin",
            "namespace": "default"
        },

        {
            "role": "view",
            "namespace": "dev"
        }

    ]
