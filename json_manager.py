"""Gestiona la lectura y escritura de los datos en un archivo .json
"""
import json
import os

def read_json():
    """Lee o crea un archivo json en caso de que no exista

    Returns:
        list: Notas almacenadas, ordenadas por corte
    """
    if not os.path.isfile('data/data.json'):
        with open('data/data.json', 'w') as f:
            json.dump([], f)
    with open('data/data.json', 'r') as f:
        data = json.load(f)
    return data


def write_json(data):
    """Escribe los datos en un archivo .json

    Args:
        data (list): Notas a almacenar
    """
    with open('data/data.json', 'w') as f:
        json.dump(data, f)