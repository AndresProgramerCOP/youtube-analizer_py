import json


def readContent(dirpath, file):
    with open(f'{dirpath}{file}', 'r', encoding="utf-8") as file:
        dict = json.load(file)
    return dict
