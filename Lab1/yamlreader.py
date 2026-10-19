import os

import yaml

with open("secrets.yaml", "r") as file:
    prime_service = yaml.safe_load(file)

os.environ["api_key"] = str(prime_service["api_key"])
