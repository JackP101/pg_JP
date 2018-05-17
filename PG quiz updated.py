import pyautogui as pg
import time
import webbrowser
points = 0

# Question

answer = pg.prompt(
"""
Where do you want to live

a)Kingdom
b)Atlantis
c)Arabia
d)China

"""
    )

# Give Points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# Question

answer = pg.prompt(
"""
What trait do you describe yourself as

a)Lonely
b)Singer
c)Royal
d)Brave

"""
    )

# Give Points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# Question

answer = pg.prompt(
"""
What do you like to do

a)Sing
b)Swim
c)Steal
d)Fight

"""
    )

# Give Points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

    # Question

answer = pg.prompt(
"""
Whats your favorite pet

a)Birds
b)Fish
c)Tiger
d)Dragon

"""
    )

# Give Points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

#END OF SURVEY

pg.alert("You are...")

#Snow White
if points < 7:
    pg.alert("Snow White")
    webbrowser.open("https://lumiere-a.akamaihd.net/v1/images/character_princess_snowwhite_b6c31f4d.jpeg?region=0,0,563,300")
#Ariel
elif points >=8 and points < 12:
    pg.alert("Ariel")
    webbrowser.open("https://img.buzzfeed.com/buzzfeed-static/static/2015-05/11/19/enhanced/webdr10/original-28143-1431385856-44.jpg?downsize=715:*&output-format=auto&output-quality=auto")
#Aladdin
elif points >=13 and points < 15:
    pg.alert("Aladdin")
    webbrowser.open("https://lumiere-a.akamaihd.net/v1/images/image_3ed34004.jpeg")
#Mulan
elif points >=16 and points < 20:
    pg.alert("Mulan")
    webbrowser ("https://cdn.movieweb.com/img.news.tops/NE9LwGuMQ68Tda_2_b/Mulan-Disney-Remake-New-Release-Date-2019-Live.jpg")
