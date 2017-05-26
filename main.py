
import webbrowser
# time module allows us to access different functions
import time

#random 
import random

links_list = []
#Input to get name
name = input("What is your Name? ")

#input for the desired breaks you want
breaks_counter = input('How many breaks do you want to take today? ')
breaks_counter_int = int(breaks_counter)

#timer how long do you want to work in intervals
timer_work = input("How many minutes do you want to work? ")
time_in_seconds = int(timer_work) * 60

timer_break = input("How many minutes do you want to rest? ")
time_break_in_seconds = int(timer_break) * 60


links_list_lenght=len(links_list)
mini_counter = breaks_counter_int

#looping through to add links you might find useful
while(links_list_lenght < breaks_counter_int):
    
    web_link = input(f"Please insert {mini_counter} link to anything you find interesting ")
    links_list.append(web_link)
    links_list_lenght += 1
    mini_counter -= 1


#looping to get time work intervals and also to pick a random link
counter = 0;
while(counter < breaks_counter_int):
    print(f"Its work time {name}")
    time.sleep(time_in_seconds)
    random.shuffle(links_list)
    webbrowser.open(links_list[-1])
    links_list.pop()
    print(f"Its rest time {name}")
    time.sleep(time_break_in_seconds)
    counter+=1

