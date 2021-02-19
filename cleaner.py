import os
import json

folder = os.fsencode('jsons')

filenames = [os.fsdecode(file) for file in os.listdir(folder)\
             if os.fsdecode(file).endswith(".json")]

#print(filenames)

with open("text/subsfile.txt", 'w') as writer:
    for file in filenames:
        print(file)
        with open("jsons/" + file) as reader:
            tree = json.load(reader)
            events = tree["events"]
            subtitles = []
            #extract the text
            for element in events:
                print(element["segs"][0]["utf8"])
                writer.write(element["segs"][0]["utf8"] + " ")



#AIzaSyBLIkEV8p16D4gAb7dXv_Dk05dF1oXrpBQ