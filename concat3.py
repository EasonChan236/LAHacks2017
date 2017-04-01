import os
os.chdir('build')
def concat(outputVideoName):
    os.system("ffmpeg -f concat -i myfileList.txt  -pix_fmt yuv420p " + outputVideoName + ".mp4")

concat("output")
