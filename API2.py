import json

from pyyoutube import Api
import pandas as pd

api = Api(api_key='AIzaSyBLIkEV8p16D4gAb7dXv_Dk05dF1oXrpBQ')

criteria = "fairy tale"
count = 100 # why does count 1 return no results

allVids = api.search_by_keywords(q=criteria, return_json = True, count=count, page_token=None)['items']
#TODO close caption, english

titles = []
videoIds = []
channelIds = []
contentRating = []
madeForKids = []
license = []
kidVids = pd.DataFrame()

for entry in allVids:
    ID = ""
    for key in entry['id']:  # not sure why ['id']['videoId'] doesn't work
        if key == 'videoId':
            ID = entry['id'][key]
    print(ID)
    if ID !="":
        video = api.get_video_by_id(video_id=ID, return_json= True)
        #print(video['items'][0]['status']['madeForKids'])
        kids = video['items'][0]['status']['madeForKids']
        if kids == True:
            #print(video['items'][0]['snippet']['title'])
            titles.append(video['items'][0]['snippet']['title'])
            channelIds.append(video['items'][0]['snippet']['channelTitle'])
            videoIds.append(ID)
            # # contentRating.append(item['contentDetails']['contentRating']['acbRating'])
            madeForKids.append(video['items'][0]['status']['madeForKids'])
            license.append(video['items'][0]['status']['license'])

kidVids['title'] = titles
kidVids['channelId'] = channelIds
kidVids['videoId'] = videoIds
kidVids['subject'] = criteria
# kidVids['contentRating'] = contentRating
kidVids['madeForKids'] = madeForKids
kidVids['license'] = license # Is this the correct license to use?

print(kidVids.shape)
print(kidVids)

kidVids.to_csv(path_or_buf="Fairy-tales_data/vids.csv", index=False)

