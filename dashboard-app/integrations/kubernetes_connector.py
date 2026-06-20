from kubernetes import config

def connect_cluster():

    config.load_kube_config()
