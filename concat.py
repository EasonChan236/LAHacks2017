import os

os.chdir("build")

def concat(outputVideoName):
    with open("myfileList.txt") as f:
        command = "MP4Box -force-cat "
        for line in f:
            command += " -cat " + line.strip()
        command += " -new " + outputVideoName + ".mp4"
    print command
    os.system(command)

concat("output.txt");
