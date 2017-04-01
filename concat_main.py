def concat(outputVideoName):
    #with open("myfileList.txt") as f:
    #    command = "MP4Box -force-cat "
    #    for line in f:
    #        command += "-cat " + line.strip()
    #    command += "-new " + outputVideoName + ".mp4"
    #os.system(command)
        

    os.system("ffmpeg -f concat -i myfileList.txt -pix_fmt yuv420p " + outputVideoName + ".mp4" + debugFlag())
