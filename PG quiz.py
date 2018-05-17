import pyautogui as pg
import time

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

pg.alert("You are..."

#Snow White
if points < 7:
         pg.alert("Snow White")
#Ariel
elif points >=8 and points < 12:
         pg.alert("Ariel")
#Aladdin
elif points >=13 and points < 15:
         pg.alert("Aladdin")
#Mulan
elif points >=16 and points < 20:
         pg.alert("Mulan")
