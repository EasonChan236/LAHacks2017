#!/usr/bin/python
import os
import re
import requests
from subprocess import call
import cog_speech



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
        imgFormat = entry["encodingFormat"]
        if "gif" in imgFormat:
            continue
        if entry["width"] > 4000 or entry["height"] > 4000:
            continue
        try:
            imgr = requests.request('GET', url, timeout=5) #stream = True, found on all tutorials, seems to be fine without it
        except:
            continue
        if imgr.status_code != 200:
            print "failed, firing new requests"
            continue
        else:
	    
            filename = imageName + "." + str(imgFormat)
            print "successful, writing to " + filename
            writeToFile(imgr, filename)
            return filename
    print "Image not found " + searchName


