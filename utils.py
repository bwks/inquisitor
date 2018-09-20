import json


def jprint(data, indent=2):
    print(json.dumps(data, indent=indent))
