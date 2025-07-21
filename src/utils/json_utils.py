import json

class JsonUtilsException(Exception):
    pass


def read_json_file(path:str) -> dict:
    if ".json" not in path:
        raise JsonUtilsException("Not a valid type of file")
    with open(path, 'r') as f:
        value = json.load(f)
    if not value:
        raise JsonUtilsException("Json file empty")
    return value
