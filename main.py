from config import API_KEY
from youtubeAPI.requestVideo import get_data_spcific_video


id_video = "M90aTPMZdJI"
part = "snippet,contentDetails,statistics"

a = get_data_spcific_video(id_video, API_KEY, part)
print(a)


