import requests


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
#print r.text.encode('utf-8')
#    print r.json()
    jcontent = r.json()
    #print [value["name"] for value in jcontent["value"]]
    #print jcontent
    #print jcontent["weSearchUrl"]
    for i, entry in enumerate(jcontent["value"]):
        url = entry["contentUrl"]
        print "Requesting " + str(url)
        imgr = requests.request('GET', url) #stream = True, found on all tutorials, seems to be fine without it
        if imgr.status_code != 200:
            print "failed, firing new requests"
            continue
        else:
            filename = imageName + "." + str(entry["encodingFormat"])
            print "successful, writing to " + filename
            writeToFile(imgr, filename)
            break
    else:
        print "Image not found " + searchName


request("iPhone", "image00003")
