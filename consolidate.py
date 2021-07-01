import csv
import os

def clean(foldername, file):
    with open(foldername + "/raw/" + file + "-dirty.txt", 'r', encoding='utf8') as reader:
        with open(foldername + "/" + file + ".txt", 'w', encoding='utf8') as writer:
            for line in reader:
                line = line.replace('"', ' ').replace("'", ' ').replace("♪", ' ').replace("(", ' ').replace(")", ' ').split()  # get rid of quotes in subs
                newline = ""
                for word in line:
                    if word[-1] == "." or word[-1] == "!" or word[-1] == "?":  # separate punctuation and add newlines
                        writer.write(word[:-1] + " " + word[-1] + "\n")
                    elif word[-1] == ",":
                        writer.write(word[:-1] + " , ")
                    else:
                        writer.write(word + " ")


def findUNK(scripts, min_occurances): # makes list of words that are UNK (occur <= x times)
    counts = {}
    for script in scripts:
        for line in script:
            words = line.replace(".", " ").replace(",", " ").replace("?", " ").replace("!", " ").lower().split()
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

    unk_words = [key for key, value in counts.items() if value >= min_occurances]

    print(len(unk_words))

    with open( "unk.txt", 'w', encoding='utf8') as writer:
        for word in unk_words:
            writer.write(word + "\n")

    return unk_words


def postprocess(unk_words, train, valid, test):
    print("processing")
    new_train = []
    new_valid = []
    new_test = []
    for word in unk_words:
        print(word)
        for script in train:
            for line in script:
                new_train.append(line.replace(word, "UNK"))
        for script in valid:
            for line in script:
                new_train.append(line.replace(word, "UNK"))
        for script in test:
            for line in script:
                new_train.append(line.replace(word, "UNK"))

    return new_train, new_valid, new_test


def concat_subs(foldername, folderlist, portion, min_occurences = 1):
    train = []
    valid = []
    test = []
    for folder in folderlist:
        filelist = [os.fsdecode(file) for file in os.listdir(os.getcwd() + "/" + folder + '/assets')] # TODO: shuffle list
        print(folder + str(len(filelist)))
        print(len(filelist))
        i = 0
        for file in filelist:
            with open(folder + '/assets/' + file, 'r', encoding='utf8') as csvFile:
                reader = csv.reader(csvFile)
                if i % portion == portion - 2:
                    for line in reader:
                        valid.append(line)
                elif i % portion == portion - 1:
                    for line in reader:
                        test.append(line)
                else:
                    for line in reader:
                        train.append(line)

            i += 1

    unk_words = findUNK(train+valid+test, min_occurences)
    train, valid, test = postprocess(unk_words, train, valid, test)

    if not os.path.isdir(os.getcwd() + '/' + foldername + "/raw/".format(os.getcwd())):
        os.makedirs(os.getcwd() + '/' + foldername + "/raw/")

    print(len(train))
    print(len(valid))
    print(len(test))

    with open(foldername + "/raw/train-dirty.txt", 'w', encoding='utf8') as writer:
        #for script in train:
        for line in train:
            # print(line)

            writer.write(line + " ")

    with open(foldername + "/raw/valid-dirty.txt", 'w', encoding='utf8') as writer:
        #for script in valid:
        for line in valid:
            # print(line)
            writer.write(line + " ")

    with open(foldername + "/raw/test-dirty.txt", 'w', encoding='utf8') as writer:
        #for script in test:
        for line in test:
            # print(line)
            writer.write(line + " ")

    clean(foldername, "train")
    clean(foldername, "valid")
    clean(foldername, "test")


folderList = ['Prechool_data','Cartoons_data','Fairy-tales_data']
foldername = "copyOver/allsubs1"
concat_subs(foldername, folderList, 8, 1)