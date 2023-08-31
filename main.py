"""_Config_
    Import your API KEY, this is the basic config
    
    fOR THIS momente, we don't use a difereten file for a config
"""

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

import youtubeAPI 