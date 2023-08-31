"""sumary_line
Coloca aqui cualquier URL de un video, la idea no es complicar al usuario para que coloqe un ID de un video si no solamente el link
esto es para que se parezca Como las aplicaciones que estoy usando para tomar bibliografia del video

Keyword arguments:
argument -- description
Return: return_description
"""

part = "snippet,contentDetails,statistics"


from files.readfile import readContent

"""_read and see datae_
This test is only for json, storage rom, adn let you see the data storaged
"""
def see_data(link_yt):
      a = readContent("output/", "probando.json") # * Remember to changue the dir path adn de the name file

      # * IF the youtube api, changued, need to fix
      publishedAt = a['items'][0]['snippet']['publishedAt']
      duration = a['items'][0]['contentDetails']['duration']
      channel_title = a['items'][0]['snippet']['channelTitle']
      link = link_yt
      id_video = a['items'][0]['id']
      video_title = a['items'][0]['snippet']['title']
      views = a['items'][0]['statistics']['viewCount']
      likeCount = a['items'][0]['statistics']['likeCount']
      tags = a['items'][0]['snippet']['tags']

      print(id_video, duration, channel_title, channel_title,
            publishedAt, views, likeCount, tags)
      return True


def good_len(link_youtube):
    if len(link_youtube[32:]) < 11:
        return False
    else:
        return link_youtube[32:]
    # todo for more case when the link is more longuer


from youtubeAPI.requestVideo import get_data_video, storage_to_json_file
from main import API_KEY

id_yt = good_len("https://www.youtube.com/watch?v=aQmF57RRKKw")
API_KEY
data = get_data_video(id_video=id_yt, api_key=API_KEY, part="snippet")

storage_to_json_file(data)


