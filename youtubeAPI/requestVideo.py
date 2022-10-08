import json
import requests

# Este script solo sirve para guardar un video y su informacion a la vez, no aplica para una lista fde video o id

# FUNCION 1

def get_data_spcific_video(id_video, api_key, part):
    # Url de la API, o endpoint
    url = f'https://www.googleapis.com/youtube/v3/videos?key={api_key}&id={id_video}&part={part}'
    json_url = requests.get(url)
    data0 = json.loads(json_url.text)
    return data0


def format_data(data1):
    """ Format and select data, with custom json"""
    try:  
        data1 = {"title": data1['items'][0]['snippet']['localized']['title'],
                    "duration": data1['items'][0]['contentDetails']['duration']}
        #Un error aqui todo raro que no se como hacer, van 6 errores, el error era como ya esta sobreescribiendo data,
    except KeyError:
        print('Could not get channel snippet')
        data1 = {}


# FUNCION 2

def storage_to_json_file(data):
    """SAVE and persist DATA IN ROM, in format json"""
    fused_data = data
    filename = "output\probando" + ".json" #Quiero hacer que el nombrado del archivo JSON sea dinamico, es decir que se obyenga o se ponga el nombre segun el titulo del video y del canala por el cual estoy extrayendo los datos
    with open(filename, 'w') as f:
        json.dump(fused_data, f, indent=4)

    print('file dumped to', filename)
    pass
