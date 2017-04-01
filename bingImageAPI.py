#!/usr/bin/python
import os
import re
import requests
from subprocess import call
import cog_speech


os.system('rm -rf build')
os.system('mkdir build')
os.chdir('build')

def writeToFile(r, path):
    with open(path, 'wb') as f:
        for chunk in r:
            f.write(chunk)

#r = requests.request('GET', "https://api.cognitive.microsoft.com/bing/v5.0/images/search?q=fef", headers={"Ocp-Apim-Subscription-Key":"0a3b4839-c160-4992-be13-ad16c3db1184"})
def request(searchName, imageName):
    print "Processing " + searchName
    qencode = {"q": searchName}
    r = requests.request('GET', "https://api.cognitive.microsoft.com/bing/v5.0/images/search",params=qencode,
            headers={"Ocp-Apim-Subscription-Key":"4697f61aecec45ff866e01ee82b4a982"})
    print r.status_code
    if r.status_code != 200 :
        print "Error in request "
        print r.json()
        return None
#print r.text.encode('utf-8')
#    print r.json()
    jcontent = r.json()
    #print [value["name"] for value in jcontent["value"]]
    #print jcontent
    #print jcontent["weSearchUrl"]
    for i, entry in enumerate(jcontent["value"]):
        url = entry["contentUrl"]
        print "Requesting " + str(url)
        try:
            imgr = requests.request('GET', url) #stream = True, found on all tutorials, seems to be fine without it
        except:
            continue
        if imgr.status_code != 200:
            print "failed, firing new requests"
            continue
        else:
            filename = imageName + "." + str(entry["encodingFormat"])
            print "successful, writing to " + filename
            writeToFile(imgr, filename)
            return filename
    print "Image not found " + searchName

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", help="increase output verbosity")
args = parser.parse_args()

def debugFlag():
    if(args.v):
        return " 2> /dev/null "
    else:
        return ""

def generateVideo(searchString, imageName):
    filename = request(searchString, imageName)
    if filename is None:
        print "Error in creating " + searchString
        return
    audio_name = imageName + "_audio.aiff"
    #os.system('echo "' +  searchString + '" > textToBeConverted')
    #os.system('say -f textToBeConverted -o ' + audio_name)
#create new audio name
    audio_name = cog_speech.generateAudio(searchString, audio_name)
    video_name = filename + "_out.m4v"
    os.system("echo file '" + video_name + "' >> myfileList.txt")
    os.system("ffmpeg -loop 1 -f image2 -i " + filename + " -i " + audio_name + " -shortest -f mpeg -pix_fmt yuv420p -vf \"scale=trunc(iw/2)*2:trunc(ih/2)*2\" " + video_name + debugFlag())


def concat(outputVideoName):
    #with open("myfileList.txt") as f:
    #    command = "MP4Box -force-cat "
    #    for line in f:
    #        command += "-cat " + line.strip()
    #    command += "-new " + outputVideoName + ".mp4"
    #os.system(command)
        

    os.system("ffmpeg -f concat -i myfileList.txt -pix_fmt yuv420p " + outputVideoName + ".mp4" + debugFlag())


def generateSentenceVideo(sentence, outputVideoName):
    splitted = re.compile("[\.,]").split(sentence)
    for i, string in enumerate(splitted):
        generateVideo(string, "img" + str(i))
    concat(outputVideoName)

#generateSentenceVideo("The United States of America (USA), commonly known as the United States (U.S.) or America, is a constitutional federal republic composed of 50 states, a federal district, five major self-governing territories, and various possessions.", "output")
content = """
Microsoft Windows (or simply Windows) is a metafamily of graphical operating systems developed, marketed, and sold by Microsoft. It consists of several families of operating systems, each of which cater to a certain sector of the computing industry with the OS typically associated with IBM PC compatible architecture. Active Windows families include Windows NT, Windows Embedded and Windows Phone; these may encompass subfamilies, e.g. Windows Embedded Compact (Windows CE) or Windows Server. Defunct Windows families include Windows 9x; Windows 10 Mobile is an active product, unrelated to the defunct family Windows Mobile.

Microsoft introduced an operating environment named Windows on November 20, 1985, as a graphical operating system shell for MS-DOS in response to the growing interest in graphical user interfaces (GUIs).[4] Microsoft Windows came to dominate the world's personal computer (PC) market with over 90% market share, overtaking Mac OS, which had been introduced in 1984. Apple came to see Windows as an unfair encroachment on their innovation in GUI development as implemented on products such as the Lisa and Macintosh (eventually settled in court in Microsoft's favor in 1993). On PCs, Windows is still the most popular operating system. However, in 2014, Microsoft admitted losing the majority of the overall operating system market to Android,[5] because of the massive growth in sales of Android smartphones. In 2014, the number of Windows devices sold was less than 25% that of Android devices sold. This comparison however may not be fully relevant, as the two operating systems traditionally target different platforms.

As of September 2016, the most recent version of Windows for PCs, tablets, smartphones and embedded devices is Windows 10. The most recent versions for server computers is Windows Server 2016. A specialized version of Windows runs on the Xbox One game console.[6]
"""
generateSentenceVideo(content, "output");
print "Output saved to build/output.mp4"
