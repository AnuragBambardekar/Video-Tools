import subprocess

def compress_gif_with_ffmpeg(input_file, output_file, resize_scale=1.0, crf=30):
    # Use subprocess to call ffmpeg command
    subprocess.run([
        'ffmpeg', '-i', input_file,
        '-vf', f'scale=iw*{resize_scale}:ih*{resize_scale}',
        '-c:v', 'gif',
        '-crf', str(crf),
        output_file
    ])

if __name__ == "__main__":
    # Replace 'input.gif' with the path to your input GIF file
    input_file = "cmatrix.gif"

    # Replace 'output_compressed.gif' with the desired output file path
    output_file = "cmatrix-comp.gif"

    # Resize scale (0.5 means half the size, 2.0 means double the size, etc.)
    resize_scale = 0.5

    # crf is the Constant Rate Factor for video, lower values result in higher quality
    # Adjust this value based on your preference (default is 30)
    crf = 30

    compress_gif_with_ffmpeg(input_file, output_file, resize_scale, crf)
