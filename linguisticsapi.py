
import requests


class Token:
    def __init__(self, name, isNoun, position):
        self.name = name
        self.isNoun = isNoun
        self.position = position
        
    def __str__(self):
        return self.name + " " + ("Noun " if self.isNoun else "") + str(self.position) + "\n"
    

#Generate sentence from [Tokens]
def toSentence(tokens):
    return " ".join([tk.name for tk in tokens])


def analyze(text):
    linguisticsReqestHeader = {"Ocp-Apim-Subscription-Key":"53999226847740f48d3b934b9ca1fe07"}
    textAPIRequestHeader = {"Ocp-Apim-Subscription-Key":"a726515b428446cfa89cc6520ef03ed5"}
    #reqestHeader = {"Ocp-Apim-Subscription-Key":"00f808b7911d41d89dbbadbc131c821f"}

#GET ANALYZERS
    analysersJson = requests.get("https://westus.api.cognitive.microsoft.com/linguistics/v1.0/analyzers", headers=linguisticsReqestHeader).json()
    analyzerKinds = [a["kind"] for a in analysersJson]
    analyzerIds = [a["id"] for a in analysersJson]
    analyzerDict = dict(zip(analyzerKinds, analyzerIds))
    print analyzerIds

#GET LANGUAGE

    languageQueryBody = {"documents":[{"id":"id", "text":text}]}
    language = requests.post("https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/languages", headers=textAPIRequestHeader, json=languageQueryBody).json()
    print language

#GET ANALYSIS

    analysisRequestBody={"language":language["documents"][0]["detectedLanguages"][0]["iso6391Name"], 
            "analyzerIds": analyzerIds,
            "text":text}
    textAnalysis = requests.post("https://westus.api.cognitive.microsoft.com/linguistics/v1.0/analyze", headers=linguisticsReqestHeader, json=analysisRequestBody).json()

#GET SENTENCES FROM TOKENS
    posTags = [dic for dic in textAnalysis if dic["analyzerId"] == analyzerDict["POS_Tags"]][0]["result"]
    print "POSTAGS : "
    print posTags

    tokens = [dic for dic in textAnalysis if dic["analyzerId"] == analyzerDict["Tokens"]][0]["result"]
    print "TOKENS: "
    print tokens

    gensentences = []

    for i, sentence in enumerate(tokens):
        gensentence = []
        gensentencelength = int(sentence["Len"])
        gensentenceoffset = int (sentence["Offset"])
        for j, token in enumerate(sentence["Tokens"]):
            pos = float(int(token["Offset"]) - gensentenceoffset)  / gensentencelength
            genTk = Token(token["NormalizedToken"], "NN" in posTags[i][j], pos)
            gensentence.append(genTk)
        gensentences.append(gensentence)
    

    print gensentences
    for i in gensentences:
        for j in i:
            print j


    return gensentences

if __name__ == "__main__":
    analyze("""
            
            Hi, How are you. I went to school yesterday.
    """)
