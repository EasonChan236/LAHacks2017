#!/usr/bin/python
import os
import re
import requests
from subprocess import call


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
    os.system('echo "' +  searchString + '" > textToBeConverted')
    os.system('say -f textToBeConverted -o ' + audio_name)
    video_name = filename + "_out.mp4"
    os.system("echo file \\'" + video_name + "\\' >> myfileList.txt")
    os.system("ffmpeg -loop 1 -f image2 -i " + filename + " -i " + audio_name + " -shortest -pix_fmt yuv420p -vf \"scale=trunc(iw/2)*2:trunc(ih/2)*2\" " + video_name + debugFlag())


def concat(outputVideoName):
    os.system("ffmpeg -f concat -i myfileList.txt -pix_fmt yuv420p " + outputVideoName + ".mp4" + debugFlag())


def generateSentenceVideo(sentence, outputVideoName):
    splitted = re.compile("[\.,]").split(sentence)
    for i, string in enumerate(splitted):
        generateVideo(string, "img" + str(i))
    concat(outputVideoName)

#generateSentenceVideo("The United States of America (USA), commonly known as the United States (U.S.) or America, is a constitutional federal republic composed of 50 states, a federal district, five major self-governing territories, and various possessions.", "output")
content = """
iPhone  is a line of smartphones designed and marketed by Apple Inc. They run Apple's iOS mobile operating system.[15] The first generation iPhone was released on June 29, 2007; the most recent iPhone model is the iPhone 7, which was unveiled at a special event on September 7, 2016.[16][17]
"""

para2="""
The user interface is built around the device's multi-touch screen, including a virtual keyboard. The iPhone has Wi-Fi and can connect to cellular networks. An iPhone can shoot video (though this was not a standard feature until the iPhone 3GS), take photos, play music, send and receive email, browse the web, send and receive text messages, follow GPS navigation, record notes, perform mathematical calculations, and receive visual voicemail.[18] Other functionality, such as video games, reference works, and social networking, can be enabled by downloading mobile apps. As of January 2017, Apple's App Store contained more than 2.2 million applications available for the iPhone and other iOS devices.[19]
"""
generateSentenceVideo(content, "output");
print "Output saved to build/output.mp4"
