import json
import requests

import os
from dotenv import load_dotenv
load_dotenv()

# Variable que guarda en {string}, la api key, de la cuenta google developer
API_KEY = os.getenv('API_KEY')

# hiCE ESTE script porque queria averiguar especificamente en donde se guardan los datos de un video en particular, con el titulo y su duracion.
# yO QU E ESTABA BORRACHO CUANDO ESCRIBI ESTO?

# Este script solo sirve para guardar un video y su informacion a la vez, no aplica para una lista fde video o id

part = "snippet,contentDetails,statistics,status" # Esto lo saco de la API de YouTube, EN EL OTRO SCRIP ESTA COMO UNA LISTA, YO LO TENGO
#COMO UNa cadena de texto, porque solo hace falta tenerlo separados con "," coma.


#Variable que almacena el ID de un unico video, se puede obtener de uns URL de algun video de youtube
id_video = "Z-Lb8CV1k9E"

#---


# FUNCION 1

def get_data_spcific_video(id_video, api_key, part):
    url = f'https://www.googleapis.com/youtube/v3/videos?key={api_key}&id={id_video}&part={part}' #Url de la API, o endpoint
    json_url = requests.get(url)
    data3 = json.loads(json_url.text)
    try: #Aqui extraigo lo que me interesa de todos los datos que me manda el json de la url, con los parametros que le meti
        data3 = {"title": data3['items'][0]['snippet']['localized']['title'],
                "duration": data3['items'][0]['contentDetails']['duration']}
        #Un error aqui todo raro que no se como hacer, van 6 errores, el error era como ya esta sobreescribiendo data,
    except KeyError:
        print('Could not get channel snippet')
        data3 = {}
    return data3

# FUNCION 2

# db, SAVE DATA IN ROM, in format json
def dump_to_json_file(data):
    fused_data = data
    filename = "output\probando" + ".json" #Quiero hacer que el nombrado del archivo JSON sea dinamico, es decir que se obyenga o se ponga el nombre segun el titulo del video y del canala por el cual estoy extrayendo los datos
    with open(filename, 'w') as f:
        json.dump(fused_data, f, indent=4)

    print('file dumped to', filename)
    pass


first = get_data_spcific_video(API_KEY, id_video, part)
print(first)
