from config import API_KEY
from youtubeAPI.requestVideo import get_data_video, format_data, storage_to_json_file
from files.readfile import readContent

id_video = "M90aTPMZdJI"
part = "snippet,contentDetails,statistics"

a = readContent("output/","probando.json")

# b = format_data(a)
# print(a['items'][0]['kind'], type(a))

print(a)
