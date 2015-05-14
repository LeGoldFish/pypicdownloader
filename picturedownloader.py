'''
Batch downloads pictures from the internet.
'''

import os, glob, urllib, shutil, sys

urlFile = "downloadurls.txt"
placeDownloads = "downloaded"
appendCounter = 0

#First time setup.
if not os.path.isfile(urlFile) or not os.path.isdir(placeDownloads):
    open("downloadurls.txt", "a")
    os.mkdir(placeDownloads)
    print("Created required files and dirs, please add URLs in " + urlFile + "and try again.")
    os.system("PAUSE")
    sys.exit()

with open (urlFile, "r+") as tempFile:
    os.chdir(placeDownloads)
    for line in tempFile:
        appendCounter = appendCounter + 1
        urllib.urlretrieve(line, "Picture-" + str(appendCounter)+ ".png")
os.chdir("..")
os.remove(urlFile)
open("downloadurls.txt", "a")
