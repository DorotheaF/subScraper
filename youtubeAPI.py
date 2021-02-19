import pandas as pd
import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
CLIENT_SECRETS_FILE = "client_secret_962900755501-cv74i754qsq0u6l8hmvt4ga80bvfaa4e.apps.googleusercontent.com.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)


# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
    good_kwargs = {}
    if kwargs is not None:
        for key, value in kwargs.items():
            if value:
                good_kwargs[key] = value
    return good_kwargs


client = get_authenticated_service()

def youtube_keyword(client, **kwargs):
    kwargs = remove_empty_kwargs(**kwargs)
    response = client.search().list(
        **kwargs
        ).execute()
    return response


def youtube_search(criteria, max_res):
    # create lists and empty dataframe
    titles = []
    videoIds = []
    channelIds = []
    contentRating = []
    madeForKids = []
    license = []
    resp_df = pd.DataFrame()

    while len(titles) < max_res:
        token = None
        response = youtube_keyword(client,
                                   part='id,snippet',
                                   maxResults=50,
                                   q=criteria,
                                   videoCaption='closedCaption',
                                   type='video',
                                   videoDuration='long',
                                   pageToken=token)

        print(response)

        for item in response['items']:
            titles.append(item['snippet']['title'])
            channelIds.append(item['snippet']['channelTitle'])
            videoIds.append(item['id']['videoId'])
            # contentRating.append(item['contentDetails']['contentRating']['acbRating'])
            # madeForKids.append(item['status']['madeForKids'])
            # license.append(item['status']['license'])

        token = response['nextPageToken']

    resp_df['title'] = titles
    resp_df['channelId'] = channelIds
    resp_df['videoId'] = videoIds
    resp_df['subject'] = criteria
    # resp_df['contentRating'] = contentRating
    # resp_df['madeForKids'] = madeForKids
    # resp_df['license'] = license

    return resp_df

kidVids = youtube_search('[kids]',10)
print(kidVids.shape)
print(kidVids.head())