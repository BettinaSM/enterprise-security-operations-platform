import yaml

def load_rule(path):

    with open(path, "r") as file:

        return yaml.safe_load(file)
