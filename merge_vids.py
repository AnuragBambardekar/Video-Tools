from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx, CompositeAudioClip

# clips should be of same resolution - do it with ffmpeg to preserve audio

clip1 = VideoFileClip("images_and_vids/one_ffmpeg_resize.mp4").subclip(0,10).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip2 = VideoFileClip("images_and_vids/two_ffmpeg_resize.mp4").subclip(0,20)
clip3 = VideoFileClip("images_and_vids/three_ffmpeg_resize.mp4").subclip(0,20).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip4 = VideoFileClip("images_and_vids/one_ffmpeg_resize.mp4").subclip(0,10).fx(vfx.colorx, 1.5).fx(vfx.lum_contrast, 0, 50, 128)

audio = AudioFileClip("images_and_vids/two_ffmpeg_resize.mp4").fx(afx.audio_fadein, 1)

combined = concatenate_videoclips([clip1, clip2, clip3, clip4])
combined.audio = CompositeAudioClip([audio])
combined.write_videofile("images_and_vids/combined_vfx.mp4")