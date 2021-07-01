import pandas as pd
import os
from pyyoutube import Api
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
DEVELOPER_KEY ='<YOUR KEY HERE>' # TODO: conf file or env file or something to hide the key

api = Api(api_key=DEVELOPER_KEY)


def get_authenticated_service():
    # flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    # credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION,  developerKey=DEVELOPER_KEY ) #, credentials = credentials)


# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
    good_kwargs = {}
    if kwargs is not None:
        for key, value in kwargs.items():
            if value:
                good_kwargs[key] = value
    return good_kwargs


def youtube_keyword(client, **kwargs):
    kwargs = remove_empty_kwargs(**kwargs)
    response = client.search().list(
        **kwargs
        ).execute()
    return response


def youtube_search(criteria, max_res, client):
    # create lists and empty dataframe
    titles = []
    videoIds = []
    channelIds = []
    contentRating = []
    madeForKids = []
    license = []
    resp_df = pd.DataFrame()
    token = None
    while len(titles) < max_res:  #TODO: if token fails, throw warning but save
        if max_res >= 50:
            mR = 50
        else:
            mR = max_res
        print("adding videos to " + str(len(titles)))
        response = youtube_keyword(client,  #TODO: language english
                                   part='id,snippet',
                                   maxResults=mR,
                                   q=criteria,
                                   videoCaption='closedCaption',
                                   type='video',
                                   key=DEVELOPER_KEY,
                                   pageToken=token)

        #print(response)

        for item in response['items']:
            ID = item['id']['videoId']
            video = api.get_video_by_id(video_id=ID, return_json=True)
            kids = video['items'][0]['status']['madeForKids']
            if kids == True: #TODO: check if has eng subs file
                #print(video['items'][0]['snippet']['title'])
                titles.append(video['items'][0]['snippet']['title'])
                channelIds.append(video['items'][0]['snippet']['channelTitle'])
                videoIds.append(ID)
                # # contentRating.append(item['contentDetails']['contentRating']['acbRating'])
                madeForKids.append(video['items'][0]['status']['madeForKids'])
                license.append(video['items'][0]['status']['license'])

        token = response['nextPageToken'] #TODO: check if there is a next page
        #print(token)

    resp_df['title'] = titles
    resp_df['channelId'] = channelIds
    resp_df['videoId'] = videoIds
    resp_df['subject'] = criteria
    # resp_df['contentRating'] = contentRating
    resp_df['madeForKids'] = madeForKids
    # resp_df['license'] = license

    return resp_df

