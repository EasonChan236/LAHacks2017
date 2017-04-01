#import http.client
import httplib
#import urllib.parse
import urlparse
import json
from xml.etree import ElementTree

# Generate audio function
def generateAudio( content, filename ):
  # Global Constants
  print("Set global constants **")
  apiKey = "a6ea0d90cf4d40a882e330b72ba27c13"
  params = ""
  headers = {"Ocp-Apim-Subscription-Key": apiKey}

# AccessTokenUri = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken";
  print("Access microsoft access token **")
  AccessTokenHost = "api.cognitive.microsoft.com"
  path = "/sts/v1.0/issueToken"

# Connect to server to get the Access Token
  print ("Connect to server to get the Access Token **")
  #conn = http.client.HTTPSConnection(AccessTokenHost)
  conn = httplib.HTTPSConnection(AccessTokenHost)

# post request to the online api file
  print("Make a request **")
  conn.request("POST", path, params, headers)
  response = conn.getresponse()
  print(response.status, response.reason)
  print("Generate request file **")
  data = response.read()
  conn.close()

# decode style and can be used as text style later
# and set style for the data
  accesstoken = data.decode("UTF-8")
  print ("Access Token: " + accesstoken)
  print("Set the access token **")
  body = ElementTree.Element('speak', version='1.0')
  body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
  voice = ElementTree.SubElement(body, 'voice')
  voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
  voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Female')
  voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)')
  voice.text = content

  headers = {"Content-type": "application/ssml+xml", 
    "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3",
    "Authorization": "Bearer " + accesstoken, 
    "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA", 
    "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960", 
    "User-Agent": "TTSForPython"}

# Connect to server to synthesize the wave
  print ("\nConnect to server to synthesize the wave")
  #conn = http.client.HTTPSConnection("speech.platform.bing.com")
  conn = httplib.HTTPSConnection("speech.platform.bing.com")
# Generate Output
  print("********************************************")
  conn.request("POST", "/synthesize", ElementTree.tostring(body), headers)
  response = conn.getresponse()
  print(response.status, response.reason)
  data = response.read()
# Create Output
  print("Generating audio file **")
  with open(filename+".mp3",'wb') as f:
    f.write(data)
  conn.close()
  print("The synthesized wave length: %d" %(len(data)))
  return filename+".mp3"

# content check -- default
print("Call generating audio function **")
if __name__ == "__main__":
  content = """
  Please generate a content for this video, thank you!
  """
  filename = "output"
  generateAudio(content, filename)
