from moviepy.editor import VideoFileClip, clips_array

length=5

clip1 = VideoFileClip("./images_and_vids/cmatrix3_ffmpeg_resize.mp4").subclip(0,0+length).margin(8)
clip2 = VideoFileClip("./images_and_vids/one_ffmpeg_resize.mp4").subclip(0,0+length).margin(8)
clip3 = VideoFileClip("./images_and_vids/two_ffmpeg_resize.mp4").subclip(0,0+length).margin(8)
clip4 = VideoFileClip("./images_and_vids/three_ffmpeg_resize.mp4").subclip(0,0+length).margin(8)

combined = clips_array([[clip1, clip2],
                        [clip3, clip4]])

combined.write_videofile("./images_and_vids/sideByside.mp4")