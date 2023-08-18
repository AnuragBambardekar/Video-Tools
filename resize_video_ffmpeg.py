import subprocess
import cv2

input_video_path = "images_and_vids/cmatrix3.mp4"
output_video_path = "images_and_vids/cmatrix3_ffmpeg_resize.mp4"

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Get the original video's width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Input Video Resolution: {width},{height}")

new_width = 1280
new_height = 720

ffmpeg_cmd = [
    "ffmpeg",
    "-i", input_video_path,
    "-vf", f"scale={new_width}:{new_height}",
    "-c:a", "copy",
    output_video_path
]

# Run the ffmpeg command
subprocess.run(ffmpeg_cmd)
