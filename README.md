# ANALIZE CHANNELS OF YOYTUBE

 (YouTube Statistics)
This program let you bulk the "main" data about a chanell youtube or single video, playlists and.

Get Data like duration of video, title, channel, data at publish

Use this scrip o program, sotfware, for obtain data about a unique url, video of yotube.
You need put de id vide in the variable `id_video`  the id video is after the "<https://www.youtube.com/watch?v>=" in a link of video.

This is a scripting software

from: [youtube-analyzer](https://github.com/patrickloeber/youtube-analyzer)
Extract youtube statistics of a channel. Uses the YouTube Data API.
It extracts channel statistics like viewCount, subscriberCount, and videoCount. It further extracts statistics for each video, like title, description, viewCount, likeCount, duration and much more...

## install

```shell
git clone 

pipenv shell

pipenv install
```

## configure

```shell
.env

API_KEY=<your api key>
```

### API KEY - GOOGLE CONSOLE

You need to make your own API_KEY

**<https://console.cloud.google.com/>**

<https://developers.google.com/youtube/v3/getting-started>

<https://console.developers.google.com/>

You need a Google Account to access the Google API Console, request an API key, and register your application.

Create a project in the Google Developers Console and obtain authorization credentials so your application can submit API requests.

After creating your project, make sure the YouTube Data API is one of the services that your application is registered to use:

Go to the API Console and select the project that you just registered. Visit the Enabled APIs page. In the list of APIs, make sure the status is ON for the YouTube Data API v3.

## USAGE

Changue some variables

```shell
python main.py
```

## RELATIONATED

The inspiration about this program was:

<https://github.com/python-engineer/youtube-analyzer>

See this playlist tutorial

[YouTube Data API - Python Tutorials](https://www.youtube.com/playlist?list=PLqnslRFeH2UpC8EqlF2aax9A-VLiPDwxP)
