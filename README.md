## recording

Open and run timelapse-taper.py

press r to start recording

optional: press r to stop recording

press q to quit the video feed

## To convert stills into a video

cd capture/2021-07-29_09-23-44
ffmpeg -r 60 -f image2 -pattern_type glob -i 'img*.jpg' -s 640x480 -vcodec libx264 ../timelapse-2021-07-29_09-23-44.mp4
