# Video to GIF

**In Windows 11, you can screen-record using the snippet tool**

This script demonstrates how to use the MoviePy library to convert a video file into an animated GIF. It specifically takes a video file named "cmatrix.mp4" and converts it into a GIF named "cmatrix.gif". The resulting GIF will be an animated version of the original video, suitable for sharing and embedding in various platforms.

## Notes

The script will take some time to process the video and create the GIF, depending on the length and complexity of the original video. Please be patient during the conversion process.

You can adjust various parameters in the MoviePy library to customize the GIF creation process, such as frame rate, duration, and resolution.

# Compress a GIF

This script demonstrates how to compress a GIF file using FFmpeg, a powerful multimedia framework. The compression process reduces the file size of the GIF while maintaining acceptable visual quality. By default, it uses a Constant Rate Factor (CRF) value of 30, but you can adjust it to your preference.

To run this script, you need to have the following library/tool installed:

FFmpeg: FFmpeg is a command-line tool used for handling multimedia data, including video and audio. It includes various codecs, filters, and formats, making it an excellent choice for processing multimedia files.

### Before running, you may edit the following parameters

input_file: Replace "cmatrix.gif" with the path to your input GIF file that you want to compress.

output_file: Replace "cmatrix-comp.gif" with the desired output file path for the compressed GIF.

resize_scale: Adjust this value to resize the GIF. For example, a value of 0.5 will reduce the size by half, while 2.0 will double the size. If you don't want to resize the GIF, set it to 1.0.

crf: The Constant Rate Factor (CRF) is a quality-based value for video compression. Lower values result in higher quality but larger file sizes. Adjust this value based on your preference (default is 30).