import moviepy.editor as mpy

clip1 = mpy.VideoFileClip("./build/img0.jpeg_out.mp4")
clip2 = mpy.VideoFileClip("./build/img5.png_out.mp4")

audio = mpy.AudioFileClip("./build/img0_audio.aiff")
print("audio duration : " + str(audio.duration))
jpeg = mpy.ImageClip("./build/img0.jpeg", duration=audio.duration)
audio.size = jpeg.size

clip = mpy.clips_array([[clip1, clip2]])
clip.write_videofile("output.mp4")


#clip = mpy.AudioFileClip("./build/img0_audio.aiff")

#print(clip.duration)

#final_clip = mpy.concatenate_videoclips([clip1, clip2])
#final_clip.write_videofile("output.mp4")
