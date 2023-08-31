"""sumary_line
Coloca aqui cualquier URL de un video, la idea no es complicar al usuario para que coloqe un ID de un video si no solamente el link
esto es para que se parezca Como las aplicaciones que estoy usando para tomar bibliografia del video

Keyword arguments:
argument -- description
Return: return_description
"""


url_vidyt = "https://www.youtube.com/watch?v=M90aTPMZdJI"
part = "snippet,contentDetails,statistics"





from files.readfile import readContent

"""_read and see datae_
This test is only for json, storage rom, adn let you see the data storaged
"""
def see_data():
      a = readContent("output/", "probando.json") # * Remember to changue the dir path adn de the name file

      # * IF the youtube api, changued, need to fix
      publishedAt = a['items'][0]['snippet']['publishedAt']
      duration = a['items'][0]['contentDetails']['duration']
      channel_title = a['items'][0]['snippet']['channelTitle']
      link = url_vidyt
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


LYT = "https://www.youtube.com/watch?v=mfjpijMwIp8"
print(LYT[32:], len(LYT[32:]), len(LYT))


b = good_len(LYT)
print(b)