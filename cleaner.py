import os
import json


with open("text/subsfile.txt", 'r', encoding='utf8') as reader:
    with open("text/subsfile-clean.txt", 'w', encoding='utf8') as writer:
        for line in reader:
            line = line.replace('"', ' ').split()
            newline = ""
            for word in line:
                if word[-1] == "." or word[-1] == "!" or word[-1] == "?":
                    writer.write(word[:-1] + " " + word[-1] + "\n")
                elif word[-1] == ",":
                    writer.write(word[:-1] + " , ")
                else:
                    writer.write(word + " ")


#AIzaSyBLIkEV8p16D4gAb7dXv_Dk05dF1oXrpBQ