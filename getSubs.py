import csv

import pandas as pd
import os
import webvtt


def get_all_ccs(videos):
    base_url = 'https://www.youtube.com/watch?v='
    lang = "en"
    for vid in videos:
        url = base_url + vid
        cmds = ["youtube-dl", "--skip-download", "--write-sub", "--sub-lang", lang, url]
        os.system(" ".join(cmds))


def convert_vtt(filepath, filenames):
    #create an assets subfolder if one does not yet exist
    if not os.path.isdir(os.getcwd() + '/' + filepath + '/assets'.format(os.getcwd())):
        os.makedirs(filepath + '/assets')
    #extract the text and times from the vtt file
    for file in filenames:
        captions = webvtt.read(file)
        text_time = pd.DataFrame()
        text_time['text'] = [caption.text for caption in captions]
        text_time['start'] = [caption.start for caption in captions]
        text_time['stop'] = [caption.end for caption in captions]
        print(text_time['text'])
        text_time['text'].to_csv(filepath + '/assets/{}.csv'.format(file[:-4].replace(" ", "")), index=False) #quoting=csv.QUOTE_NONE, index=False, header=False, escapechar='') #-4 to remove '.vtt'
        #remove files from local drive
        os.remove(file)


def concat_subs(filepath, filelist):
    subs = []
    for file in filelist:
        with open(filepath + '/assets/' + file, 'r', encoding='utf8') as csvFile:
            reader = csv.reader(csvFile)
            for line in reader:
                subs.append(line)

    if not os.path.isdir(os.getcwd() + '/' + filepath + '/text'.format(os.getcwd())):
        os.makedirs(os.getcwd() + '/' + filepath + '/text')

    with open(filepath + "/text/subsfile.txt", 'w', encoding='utf8') as writer:
        for script in subs:
            for line in script:
                # print(line)
                writer.write(line + " ")


def clean(filepath):
    with open(filepath + "/text/subsfile.txt", 'r', encoding='utf8') as reader:
        with open(filepath + "/text/subsfile-clean.txt", 'w', encoding='utf8') as writer:
            for line in reader:
                line = line.replace('"', ' ').replace("'", ' ').split()  # get rid of quotes in subs
                newline = ""
                for word in line:
                    if word[-1] == "." or word[-1] == "!" or word[-1] == "?":  # separate punctuation and add newlines
                        writer.write(word[:-1] + " " + word[-1] + "\n")
                    elif word[-1] == ",":
                        writer.write(word[:-1] + " , ")
                    else:
                        writer.write(word + " ")


# # kidsVids = pd.read_csv(filepath_or_buffer="vids.csv")
# # print(kidsVids.head())
# #
# # get_all_ccs(kidsVids['videoId'])
#
# filenames_vtt = [os.fsdecode(file) for file in os.listdir(os.getcwd()) if os.fsdecode(file).endswith(".vtt")]
# print(filenames_vtt[:2])
# convert_vtt(filenames_vtt)
#
#
# filelist = [os.fsdecode(file) for file in os.listdir(os.getcwd()+'/assets')]
# concat_subs(filelist)
# clean()
