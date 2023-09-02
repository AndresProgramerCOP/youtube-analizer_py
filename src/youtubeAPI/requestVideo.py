import json as j
import requests as r

"""Este script solo sirve para guardar un video y su informacion a la vez, no aplica para una lista de video o id"""
# FUNCION 1, entiendo
def get_data_video(id_video, api_key, part):
    # Url de la API, o endpoint
    url = f'https://www.googleapis.com/youtube/v3/videos?key={api_key}&id={id_video}&part={part}'
    json = r.get(url)
    data0 = j.loads(json.text)
    return data0

# FUNCION 2
def storage_to_json_file(data):
    """SAVE and persist DATA IN ROM, in format json"""
    a = data
    b = str(a["items"][0]["snippet"]["title"])
    c = b.replace("|", "-").replace(" ", "_")
    filename = f'output\{c}.json'
    with open(filename, 'w') as f:
        j.dump(a, f, indent=2)
    print('file dumped to', filename)
