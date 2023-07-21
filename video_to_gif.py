from moviepy.editor import VideoFileClip
clip = VideoFileClip("cmatrix.mp4")
clip.write_gif("cmatrix.gif")