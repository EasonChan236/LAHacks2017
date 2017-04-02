import re
import os
import argparse
import bingImageAPI
import linguisticsapi
import concat_main
import cog_speech
#import splitPointGenerator #generateSplit


parser = argparse.ArgumentParser()
parser.add_argument("-v", help="increase output verbosity")
args = parser.parse_args()

def debugFlag():
    if(args.v):
        return " 2> /dev/null "
    else:
        return ""

def generateVideo(searchString, imageName, language, sex):
    print "GENERATING " + searchString
    filename = bingImageAPI.request(searchString, imageName)
    if filename is None:
        print "Error in creating " + searchString
        return
#this will get reassigned
    audio_name = imageName + "_audio.aiff"
    #os.system('echo "' +  searchString + '" > textToBeConverted')
    #os.system('say -f textToBeConverted -o ' + audio_name)

#create new audio name
    audio_name = cog_speech.generateAudio(searchString, audio_name, language, sex)
    createAudioFromImageAndAudio(filename, audio_name)

#file name is the image file name. audio name is the audio file name
def createAudioFromImageAndAudio(filename, audio_name):
    video_name = filename + "_out.m4v"
    os.system("echo file '" + video_name + "' >> myfileList.txt")
    os.system("ffmpeg -loop 1 -f image2 -i " + filename + " -i " + audio_name + " -shortest -f mpeg -pix_fmt yuv420p -vf \"scale=trunc(iw/2)*2:trunc(ih/2)*2\" " + video_name + debugFlag())


#language : 1. US, 2. IN, 3. UK Sex 1. Female, 2.Male
def generateSentenceVideo(sentence, outputVideoName, language, sex):
    os.system('rm -rf build')
    os.system('mkdir build')
    os.chdir('build')

    sentence = re.sub(r'\([^\)]*\)', '', sentence)
    sentence = re.sub(r'\[[^\]]*\]', '', sentence)
    sentence = re.sub(r'\{[^\}]*\}', '', sentence)
    splitted = re.compile(r'[\.,]').split(sentence)
    for i in range(0, len(splitted)):
        splitted[i] = re.sub(r'[^A-Za-z0-9]+',' ', splitted[i])
        splitted[i] = re.sub(r'[^\x00-\x7F]+',' ', splitted[i])
    
    print splitted 
    try:
        for i, string in enumerate(splitted):
            generateVideo(string, "img" + str(i), language, sex)
        concat_main.concat(outputVideoName)
    except:
        os.chdir('..')
	raise

if __name__ == "__main__" :
#    generateSentenceVideo("The United States of America (USA), commonly known as the United States (U.S.) or America, is a constitutional federal republic composed of 50 states, a federal district, five major self-governing territories, and various possessions.", "output")
    content = """
    Microsoft Windows (or simply Windows) is a metafamily of graphical operating systems developed, marketed, and sold by Microsoft. It consists of several families of operating systems, each of which cater to a certain sector of the computing industry with the OS typically associated with IBM PC compatible architecture. Active Windows families include Windows NT, Windows Embedded and Windows Phone; these may encompass subfamilies, e.g. Windows Embedded Compact (Windows CE) or Windows Server. Defunct Windows families include Windows 9x; Windows 10 Mobile is an active product, unrelated to the defunct family Windows Mobile.

    """

    generateSentenceVideo(content, "output", "1", "1");
    print "Output saved to build/output.mp4"
