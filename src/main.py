"""_Config_
    Import your API KEY, this is the basic config
    
    fOR THIS moment, we don't use a difereten file for a config
"""

from time import time
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')


def count_elapsed_time(f):
    """
    Decorator.
    Execute the function and calculate the elapsed time.
    Print the result to the standard output.
    """
    def wrapper():
        # Start counting.
        start_time = time()
        # Take the original function's return value.
        ret = f()
        # Calculate the elapsed time.
        elapsed_time = time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        return ret

    return wrapper


@count_elapsed_time
def main():
    from youtubeAPI.requestsYoutube import YTstats

    ch_id = 'UCbXgNpp0jedKWcQiULLbDTA'
    yt = YTstats(api_key=API_KEY, channel_id=ch_id)
    yt.extract_all()
    yt.dump_to_json()  # dumps to .json
    
    return print("Se ejecuto el programa, todo salio bien?")


main()
