import win32com.client as wincl
import webbrowser as wb
import pyautogui as pg
speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your name?")
answer = pg.prompt("Enter your name.")

speak.speak("Hello Jack" + "How was your day?")
day = pg.prompt("Enter how your day was.")

if day == "Good":
    speak.Speak("I am glad to hear that!")

elif day == "Bad":
    speak.Speak("I am sorry to hear that!")

else:
    speak.Speak("Cool! good for you!")


speak.Speak("What kind of video would you like to watch???")
video = pg.prompt("Enter video to watch")
speak.Speak("You want to watch videos about " + video)

wb.open("https://www.youtube.com/results?search_query=" + video)
