import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

x = np.linspace(0, 2 * np.pi, 200)

# duration of the video
duration = 20

fig, ax = plt.subplots()

# method to get frames
def make_frame(t):
    # clear
    ax.clear()

    # compute frequency
    frequency = 1 + t * 2  # Changing frequency over time

    # plotting sine wave
    ax.plot(x, np.sin(frequency * x), lw=3)
    ax.set_ylim(-1.5, 1.5)

    # returning numpy image
    return mplfig_to_npimage(fig)

# creating animation
animation = VideoClip(make_frame, duration=duration)

output_file = "sine_wave_animation.mp4"
animation.write_videofile(output_file, fps=20)

print(f"Animation saved as {output_file}")
