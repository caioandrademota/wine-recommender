import json
from pathlib import Path

path = Path(__file__).parent

def read_json(path):
    """
    Reads a json file and returns the data as a dictionary.
    """
    with open(path) as f:
        data = json.load(f)
    return data

def write_json(path, data):
    """
    Writes a dictionary to a json file.
    """
    with open(path, 'w') as f:
        json.dump(data, f)

def get_object():
    return read_json(path / 'wines.json') #objetos avaliados

def get_users():
    return read_json(path / 'users.json') #notas dos objetos