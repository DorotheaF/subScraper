import os
import pandas as pd

import youtubeAPI
import getSubs

# Takes search terms and returns csv file of appropriate videos
def getSomeVids(searchTerms, maxSearchQuantity, directory, fileTitle):
    client = youtubeAPI.get_authenticated_service()
    vidsList = youtubeAPI.youtube_search(searchTerms, maxSearchQuantity, client)

    print(vidsList.shape)
    print(vidsList.head())

    if not os.path.isdir('{}/' + directory.format(os.getcwd())):
        os.makedirs(directory)

    vidsList.to_csv(path_or_buf=directory + "/" + fileTitle, index=False)


# takes list of videos and returns vtt files, moves files to assets  folder and converts to txt
def getSomeSubs(directory, fileTitle):
    vidsList = pd.read_csv(filepath_or_buffer=directory + "/" + fileTitle)
    print(vidsList.head())

    getSubs.get_all_ccs(vidsList['videoId'])

    filenames_vtt = [os.fsdecode(file) for file in os.listdir(os.getcwd()) if os.fsdecode(file).endswith(".vtt")]
    print(filenames_vtt[:2])
    getSubs.convert_vtt(directory, filenames_vtt)


def cleanTheSubs(directory):
    filelist = [os.fsdecode(file) for file in os.listdir(os.getcwd() + "/" + primaryTopic + '/assets')]
    getSubs.concat_subs(primaryTopic, filelist)
    getSubs.clean(primaryTopic)



# VARIABLES:
searchTerms = '[green]'  # i.e '[kids, cartoons]'. Find videos fulfilling all terms.
maxSearchQuantity = 5  # how many videos you want to find.
# If you get nextPageToken error, change this number to the largest one output in the terminal
primaryTopic = "Green"  # what (new) directory you want the subs to be stored in
listFileTitle = "videoList.csv"
searchForVids = True
getVidSubs = True
concatAndClean = True

if searchForVids:
    print("Searching for " + str(maxSearchQuantity) + " videos with topic(s): " + searchTerms)
    getSomeVids(searchTerms, maxSearchQuantity, primaryTopic, listFileTitle)

if getVidSubs:
    print("Getting subs for videos with topic " + primaryTopic)
    getSomeSubs(primaryTopic, listFileTitle)

if concatAndClean:
    cleanTheSubs(primaryTopic)

