import yaml

def load_secrets():

    with open(
        "configs/secrets.yaml"
    ) as file:

        return yaml.safe_load(file)
