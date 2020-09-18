import pyttsx3  # pip install
import datetime
import speech_recognition as sr # pip  install
import wikipedia  # pip install
import webbrowser
import os
import smtplib
import time
import subprocess

# if using python>3.8 then pyaudio won't work use this
# pip install pipwin
# pipwin install pyaudio
typ = 0
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
	time.sleep(1)
	engine.say(audio)
	engine.runAndWait()

asstntname ="Max"
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(f"I am {asstntname}")


def giveHelp():
    speak("I can search on google, stackoverflow, open youtube, open This PC")

def changevoice(typ):
    if typ == 0:
        typ = 1
    else:
        typ = 0
        engine.setProperty('voice', voices[typ].id)



# microphone input from user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising... ")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please..")
        print("None")
        query = takeCommand()
    return query
count = 0

if __name__ == "__main__":

    wishMe()
    

    speak("To know what can I do say help else,")
    while True:
        if count > 0:
            speak("If you want I can change my voice type, to change say change voice")
            count = 0
        time.sleep(1)
        speak("Give command or say quit")
        try:
            query = takeCommand().lower()
        except:
            exit()

        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')


        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            speak("Enter the location of file")
            music_dir =input()
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'How are you' in query:
        	speak("I am fine")
        	speak("How are you")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is:{strTime}")

        elif 'help' in query:
            giveHelp()

        elif 'shutdown system' in query: 
            speak("Hold On a Sec ! Your system is on its way to shut down") 
            subprocess.call('shutdown / p /f') 

        elif 'change name' in query:
        	speak("What would you like to call me")
        	usrname = takeCommand()

        elif 'quit' in query:
            exit()

        elif 'open my pc' in query:
            Path = "This PC"
            os.system("explorer.exe  file:")

        elif 'change voice' in query:
            changevoice(typ)
            count += 1
        time.sleep(2)
