########### Python 2.7 #############
import httplib, urllib, urllib2, sys, base64, json

request_url = 'https://westus.api.cognitive.microsoft.com/linguistics/v1.0/analyze'

account_key = '00f808b7911d41d89dbbadbc131c821f'

headers = {
# Request headers
	'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': account_key,
}

input_texts = '{"language" : "en", "analyzerIds" : ["4fa79af1-f22c-408d-98bb-b7d7aeef7f04"], "text" : "Hi, Tom! How are you today?" }'

req = urllib2.Request(request_url, input_texts, headers);

response = urllib2.urlopen(req)
result = response.read()
obj = json.loads(result)
print obj[0]['result']