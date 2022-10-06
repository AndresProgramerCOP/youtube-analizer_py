from re import A
from youtubeAPI.youtube_statistics import YTstats as yt

import os
from dotenv import load_dotenv
load_dotenv()

# Variable que guarda en {string}, la api key, de la cuenta google developer
API_KEY = os.getenv('API_KEY')


#------------------------------------------------------------------------------------------------------------------
#PythonIA_id_YTChannel = "UC8B7LR70zfRE1zbESFkyyzQ"
#ayt = yt(API_KEY, PythonIA_id_YTChannel)
#------------------------------------------------------------------------------------------------------------------

video_id = "M90aTPMZdJI"
part = "snippet,contentDetails,statistics"

a = yt._get_single_video_data(video_id=video_id, part = part, api_key=API_KEY)



print(a)