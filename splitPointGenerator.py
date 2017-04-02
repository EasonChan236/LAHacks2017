#!/usr/bin/python
import os
#import mad
outputFileName = []
time = 0
def generateSplit( audioFileName, arrayOfSplitPoints ):
    # total time of the music file
    os.system("soxi -D " + audioFileName + ".mp3 > time.txt")
    with open("time.txt", "r") as f:
	#for line in f:
	time = f.read()
        os.system("rm time.txt")
    #mf = mad.MadFile(audioFileName)
    track_length_in_milliseconds = time
    # firt video time of
    videoTimeFirst = float(track_length_in_milliseconds) * arrayOfSplitPoints[0]
    # keep track of the precious time
    previousTime = videoTimeFirst
       
    for index,_ in enumerate(arrayOfSplitPoints):
      if index == 0:
        #os.system("ffmpeg -i '" + audioFileName + "'.mp3 -f segment -segment_time '" + str(videoTimeFirst) + "' -c copy '" + audioFileName + str(index) + "'.mp3")
	os.system("ffmpeg -ss " + str(0) + " -t " + str(videoTimeFirst) + " -i " + audioFileName + ".mp3 out" + str(index) + ".mp3")
	#outputFileName[index] = audioFileName + str(index) + ".mp3"
	outputFileName.append("out" + str(index) + ".mp3")
      #elif index == (len(arrayOfSplitPoints) - 1):
       # videoTime = track_length_in_milliseconds * arrayOfSplitPoints[index]
        #tempTime = videoTime	
	#prev = previousTime
        #videoTime = videoTime - previousTime
        #previousTime = tempTime	
	#outputFileName.append("out" + str(index) + ".mp3")
	#os.system("ffmpeg -ss " + str(prev) + " -i " + audioFileName + ".mp3 out" + str(index) + ".mp3")
      else: 
	print("index " + str(index))
	print("array " + str(arrayOfSplitPoints[index]))
        videoTime = float(track_length_in_milliseconds) * arrayOfSplitPoints[index]
        tempTime = videoTime	
	prev = previousTime
        videoTime = videoTime - previousTime
        previousTime = tempTime	
	#outputFileName[index] = audioFileName + str(index) + ".mp3"
	outputFileName.append("out" + str(index) + ".mp3")
        #os.system("ffmpeg -i '" + audioFileName + str((index - 1)) + "'.mp3 -f segment -segment_time '" + str(videoTime) + "' -c copy '" + audioFileName + str(index) + "'.mp3")
	os.system("ffmpeg -ss " + str(prev) + " -t " + str(videoTime) + " -i " + audioFileName + ".mp3 out" + str(index) + ".mp3")
    return outputFileName

generateSplit( "img0_audio.aiff", [0.25, 0.5] )
