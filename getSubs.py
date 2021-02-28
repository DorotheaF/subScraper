import pandas as pd
import os
import webvtt

def get_all_ccs(videos):
    base_url = 'https://www.youtube.com/watch?v='
    lang="en"
    for vid in videos:
        url = base_url + vid
        cmds = ["youtube-dl","--skip-download","--write-sub",
               "--sub-lang",lang,url]
        os.system(" ".join(cmds))


def convert_vtt(filenames):
    #create an assets folder if one does not yet exist
    if os.path.isdir('{}/assets'.format(os.getcwd())) == False:
        os.makedirs('assets')
    #extract the text and times from the vtt file
    for file in filenames:
        captions = webvtt.read(file)
        text_time = pd.DataFrame()
        text_time['text'] = [caption.text for caption in captions]
        text_time['start'] = [caption.start for caption in captions]
        text_time['stop'] = [caption.end for caption in captions]
        print(text_time['text'])
        text_time['text'].to_csv('assets/{}.csv'.format(file[:-4].replace(" ", "")), quoting=csv.QUOTE_NONE, index=False, header=False) #-4 to remove '.vtt'
        #remove files from local drive
        os.remove(file)


def concat_subs(filelist):
    subs = pd.DataFrame
    for file in filelist:
        text = pd.read_csv('assets/' + file)
        subs.append(text)
    subs.to_csv(path_or_buf="text/subsfile.csv", index=False)



# kidsVids = pd.read_csv(filepath_or_buffer="vids.csv")
# print(kidsVids.head())
#
# get_all_ccs(kidsVids['videoId'])
#
# filenames_vtt = [os.fsdecode(file) for file in os.listdir(os.getcwd()) if os.fsdecode(file).endswith(".vtt")]
# print(filenames_vtt[:2])
# convert_vtt(filenames_vtt)


filelist = [os.fsdecode(file) for file in os.listdir(os.getcwd()+'/assets')]
concat_subs(filelist)