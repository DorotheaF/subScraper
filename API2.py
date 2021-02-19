import json

from pyyoutube import Api
import pandas as pd

api = Api(api_key='AIzaSyBLIkEV8p16D4gAb7dXv_Dk05dF1oXrpBQ')

criteria = "fairy tale"
count = 10

list = api.search_by_keywords(q=criteria, return_json = True, count=count, page_token=None)['items']

titles = []
videoIds = []
channelIds = []
contentRating = []
madeForKids = []
license = []
kidVids = pd.DataFrame()

for item in list:
    print(item)
    id = item['id']['videoId']
    video = api.get_video_by_id(video_id=id, return_json= True)
    # print(video)
    kids = video['items'][0]['status']['madeForKids']
    if kids == True:
        titles.append(item['snippet']['title'])
        channelIds.append(item['snippet']['channelTitle'])
        videoIds.append(item['id']['videoId'])
        # contentRating.append(item['contentDetails']['contentRating']['acbRating'])
        madeForKids.append(item['status']['madeForKids'])
        license.append(item['status']['license'])

kidVids['title'] = titles
kidVids['channelId'] = channelIds
kidVids['videoId'] = videoIds
kidVids['subject'] = criteria
# kidVids['contentRating'] = contentRating
kidVids['madeForKids'] = madeForKids
kidVids['license'] = license

print(kidVids.shape)
print(kidVids)