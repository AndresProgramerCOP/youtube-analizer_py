import json


def readContent(dirpath, file):
    """"""
    """_summary_
    Read you need to put directly the route, is not dinamic
    
    arg: dirpath, the obsolutely dir path of the file
    arg: file, de name of the file and their extension.
    """
    with open(f'{dirpath}{file}', 'r', encoding="utf-8") as file:
        dict = json.load(file)
    return dict
