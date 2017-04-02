#http://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
import urllib
import videoGenerationAPI
import html2text
import requests
import nltk
from bs4 import BeautifulSoup

def generateVideoFromURL(url, outpufilename, language, sex):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

# kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

# get text
    text = soup.get_text()

# break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
    text = '\n'.join(chunk for i, chunk in enumerate(chunks) if chunk and i < 40)

    videoGenerationAPI.generateSentenceVideo(text, "output", language, sex)

if __name__ == "__main__":
    generateVideoFromURL("https://en.wikipedia.org/wiki/User_talk:169.232.218.22", "output", "1", "1")
