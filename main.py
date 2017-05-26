#webbrowser is a module that allows python to open a web browser
import webbrowser
# time module allows us to access different functions
import time

#random 
import random

youtube_videos = ["https://www.youtube.com/watch?v=1Wh8RzcQZr4","https://www.youtube.com/watch?v=ssRIHxNV8Ls","https://www.youtube.com/watch?v=geqVuYmo8Y0"]


breaks_counter = input('How many breaks do you want to take today? ')
breaks_counter_int = int(breaks_counter)

counter = 0;
while(counter < breaks_counter_int):
    time.sleep(2)
    random.shuffle(youtube_videos)
    webbrowser.open(youtube_videos[0])
    counter+=1

