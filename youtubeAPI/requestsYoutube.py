import json
import requests
from tqdm import tqdm

class YTstats:
    """ Este script trae toda la informacion de un canal de yotube
    Una sola clase que contiene todas las funciones, para este caso solo son 7 funciones
    """
    def __init__(self, api_key, channel_id): #Constructor
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_data = None

#FUNCION 1 de 7 que ejecuta todo.
    def extract_all(self):
        self.get_channel_statistics() #Aqui se llama a la funcion 2.
        self.get_channel_video_data() #Aqui se llama a la funcion 3.

#FUNCION 2 de 7, funcion sencillas  15 lienas de codigo,
# ESTA FUNCION EN LO personal no me gusta hace riudo en los datos, se puede guardar en otro json aparte y listo  O como otro objeto json dentro de los mismo objeto json
#Devuelve 2 datos
    def get_channel_statistics(self):
        """Extract the basic channel statistics"""
        print('get channel YouTube statistics and information')
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics,snippet&id={self.channel_id}&key={self.api_key}'
        pbar = tqdm(total=1) #Varaible que se crea para crear la barra de progreso interactiva

        json_url = requests.get(url) #Json obtenido de la url,
        data = json.loads(json_url.text)
        try:
            data = {"channel_statistic": data['items'][0]['statistics'], "data_information": data['items'][0]['snippet']}  #Creo un diccionario personalizado, que tiene 2 claves.
        except KeyError:
            print('Could not get channel statistics and information')
            data = {}

        self.channel_statistics = data
        pbar.update()
        pbar.close()
        return data # Agrego los datos (en forma de diccionario) a la variable del constructor que creo.

#FUNCION 3 de 7, esta funcion llama a 2 funciones que estan debajo suyo, la (4) y (5)
    def get_channel_video_data(self):
        "Extract all video information of the channel"
        print('get the videos data of the channel YouTube specified')
        channel_videos, channel_playlists = self._get_channel_content(limit=50) #Esta llama a la funcion (5)

        #parts = ["snippet", "statistics", "contentDetails", "topicDetails", etc etc]
        parts = ["snippet", "statistics", "contentDetails"] #Aqui defino que informacion quiero obtener del canal
        for video_id in tqdm(channel_videos): #esta linea no la entiendo
            for part in parts: # Ojo aqqui, cambien la funcion 4
                data = self._get_single_video_data(video_id, part) # Aqui se llama al a funcion (4)
                channel_videos[video_id].update(data)

        self.video_data = channel_videos
        return channel_videos

#FUNCION 4 de 7
    def _get_single_video_data(video_id, part, api_key):
        """
        Extract further information for a single video
        parts can be: 'snippet', 'statistics', 'contentDetails', 'topicDetails'
        """
        #Aqui se usa la nueva url que incluye el  nuva nueva ruta la cual es  "/videos"
        url = f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        print(data)
        # try:
        #     data = data['items'][0][part] #Para que es esto?
        # except KeyError as e:
        #     print(f'Error! Could not get {part} part of data: \n{data}')
        #     data = dict() # hace un diccionario vacio si hay error en la peticion de datos
        return data

#FUNCION 5 de 7 _get_channel_content -----------------------------------------------------
    #Devuelve 2 valores, 2 enteros, 1 contiene todos los videos en total y el otro todas las listas de reproducicon total de canal
    def _get_channel_content(self, limit=None, check_all_pages=True):
        """
        Extract all videos and playlists, can check all available search pages
        channel_videos = videoId: title, publishedAt
        channel_playlists = playlistId: title, publishedAt
        return channel_videos, channel_playlists
        """
        url = f"https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=snippet,id&order=date"
        if limit is not None and isinstance(limit, int):
            url += "&maxResults=" + str(limit)

        vid, pl, npt = self._get_channel_content_per_page(url) #Aqui se llama la funcion 6, que recibe los tres datos que esta arroja
        idx = 0
        while(check_all_pages and npt is not None and idx < 10):
            nexturl = url + "&pageToken=" + npt
            next_vid, next_pl, npt = self._get_channel_content_per_page(
                nexturl)
            vid.update(next_vid)
            pl.update(next_pl)
            idx += 1

        return vid, pl

#FUNCION 6 de 7, esta funcion devuelve 3 datos
    def _get_channel_content_per_page(self, url):
        """
        Extract all videos and playlists per page
        return channel_videos, channel_playlists, nextPageToken
        """
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_videos = dict()
        channel_playlists = dict()
        if 'items' not in data:
            print('Error! Could not get correct channel data!\n', data)
            return channel_videos, channel_videos, None

        nextPageToken = data.get("nextPageToken", None)

        item_data = data['items']
        for item in item_data:
            try:
                kind = item['id']['kind']
                published_at = item['snippet']['publishedAt'] #Este esta bien con respecto a las respuesta json
                title = item['snippet']['title'] #Este tambien esta bien
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_videos[video_id] = {'publishedAt': published_at, 'title': title}
                elif kind == 'youtube#playlist':
                    playlist_id = item['id']['playlistId']
                    channel_playlists[playlist_id] = {'publishedAt': published_at, 'title': title}
            except KeyError as e:
                print('Error! Could not extract data from item:\n', item)

        return channel_videos, channel_playlists, nextPageToken

#FUNCION 7 de 7,
# En esta funcion no se hace llamado a ninguna otra funcion o metodos de teceros. o importados, se usan 3 variablesm 1 if,  1 sentencia
# with [...] as [...]:
    def dump_to_json(self):
        """Dumps channel statistics and video data in a single json file"""
        if self.channel_statistics is None or self.video_data is None:
            print(
                'data is missing!\nCall get_channel_statistics() and get_channel_video_data() first!')
            return

        fused_data = {"id_channel":self.channel_id,  "prueba":self.channel_statistics, "video_data": self.video_data}

        channel_title = self.video_data.popitem()[1].get(
            'channelTitle', self.channel_id)
        channel_title = channel_title.replace(" ", "_").lower()
        filename = 'output/'+ channel_title + '.json' # Variable que crea el nombre para el archivo json que s eva a crear
        with open(filename, 'w') as f:
            json.dump(fused_data, f, indent=4)

        print('file dumped to', filename)
