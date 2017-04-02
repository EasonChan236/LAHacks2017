#import http.client
import httplib
#import urllib.parse
import urlparse
import json
from xml.etree import ElementTree
import os



 
# Generate audio function
def generateAudio( content, filename, language, gender):
    print language 
    print gender

    locale = None
    nameMapping = None
    #language = raw_input('What Region? 1.US or 2.IN or 3.UK ')
    if(language == "1"):
        print "if"
        locale = 'en-US'
        nameMapping = 'Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)'

    if(language == "2"):
        print "if"
        locale = 'en-IN'
        nameMapping = 'Microsoft Server Speech Text to Speech Voice (en-IN, Heera, Apollo)'

    if(language == "3"):
        print "if"
        locale = 'en-GB'
        nameMapping = 'Microsoft Server Speech Text to Speech Voice (en-GB, Susan, Apollo)'

    #gender = raw_input('what gender? 1.Female or 2.Male')
    sex = 'Female' 


    if(gender == "2" and language == "1"):
        print "if"
        nameMapping = 'Microsoft Server Speech Text to Speech Voice (en-US, BenjaminRUS)'
        sex = 'Male'

    if(gender == "2" and language == "2"):
        print "if"
        sex = 'Male'
        nameMapping = 'Microsoft Server Speech Text to Speech Voice (en-IN, Ravi, Apollo)'

    if(gender == "2" and language == "3"):
        print "if"
        sex = 'male'
        nameMapping = 'Microsoft Server Speech Text to Speech Voice (en-GB, George, Apollo)'

    # Global Constants
    print("Set global constants **")
    apiKey = "a6ea0d90cf4d40a882e330b72ba27c13"
    params = ""
    headers = {"Ocp-Apim-Subscription-Key": apiKey}

# AcssTokenUri = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken";
    print("Access microsoft access token **")
    AccessTokenHost = "api.cognitive.microsoft.com"
    path = "/sts/v1.0/issueToken"

# Coect to server to get the Access Token
    print ("Connect to server to get the Access Token **")
    #conn = http.client.HTTPSConnection(AccessTokenHost)
    conn = httplib.HTTPSConnection(AccessTokenHost)

# po request to the online api file
    print("Make a request **")
    conn.request("POST", path, params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    print("Generate request file **")
    data = response.read()
    conn.close()

# dede style and can be used as text style later
# anset style for the data
    accesstoken = data.decode("UTF-8")
    print ("Access Token: " + accesstoken)
    print("Set the access token **")
    body = ElementTree.Element('speak', version='1.0')
    body.set('{http://www.w3.org/XML/1998/namespace}lang', locale)
    voice = ElementTree.SubElement(body, 'voice')
    voice.set('{http://www.w3.org/XML/1998/namespace}lang', locale)
    voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Female')
    voice.set('name', nameMapping)
    voice.text = content

    headers = {"Content-type": "application/ssml+xml", 
      "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3",
      "Authorization": "Bearer " + accesstoken, 
      "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA", 
      "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960", 
      "User-Agent": "TTSForPython"}

# Coect to server to synthesize the wave
    print ("\nConnect to server to synthesize the wave")
    #conn = http.client.HTTPSConnection("speech.platform.bing.com")
    conn = httplib.HTTPSConnection("speech.platform.bing.com")
# Gerate Output
    print("********************************************")
    conn.request("POST", "/synthesize", ElementTree.tostring(body), headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
# Crte Output
    print("Generating audio file **")
    with open(filename+".mp3",'wb') as f:
      f.write(data)
    conn.close()
    print("The synthesized wave length: %d" %(len(data)))
    return filename+".mp3"

# content check -- default
if __name__ == "__main__":
     print("Call generating audio function **")
     content = """
     Please generate a content for this video, thank you!
     """
     filename = "output"
     generateAudio(content, filename)
