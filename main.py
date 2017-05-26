#webbrowser is a module that allows python to open a web browser
import webbrowser
# time module allows us to access different functions
import time

youtube_video = "https://www.youtube.com/watch?v=1Wh8RzcQZr4"


breaks_counter = input('How many breaks do you want to take today? ')
breaks_counter_int = int(breaks_counter)

counter = 0;
while(counter < breaks_counter_int):
    time.sleep(120)
    webbrowser.open(youtube_video)
    counter+=1

