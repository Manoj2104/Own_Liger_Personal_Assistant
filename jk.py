import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import pywhatkit
import pyautogui
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate",200)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !,I am your assistant. How can i help you ")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !,I am your assistant. How can i help you ")

    else:
        speak("Good Evening  !,I am your assistant. How can i help you ")



def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        if 'liger' in query:
            query = query.replace('liger', '')
            print(f"User said: {query}\n")



    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")


        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('assistant6515@gmail.com', 'Manoj@2104')
    server.sendmail('assistant6515@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()

    while True:
        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command        if 'wikipedia' in query:

        if 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'play' in query or 'song' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)


        elif 'siri' in query:
            speak('Sorry I am not siri, I am your Liger assistant')
            print('Sorry I am not siri, I am your Liger assistant')

        elif 'google' in query:
            speak('Sorry I am not google, I am your Liger assistant')
            print('Sorry I am not google, I am your Liger assistant')

        elif 'alexa' in query:
            speak('Sorry I am not alexa, I am your Liger assistant')
            print('Sorry I am not alexa, I am your Liger assistant')



        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening Google\n")
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            speak("opening Gmail\n")
            webbrowser.open("gmail.com")

        elif 'open facebook' in query:
            speak("opening facebook\n")
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            speak("opening instagram \n")
            webbrowser.open("instagram.com")


        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\Shadow_Mano\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'open photo' in query or "open gallery" in query:
            speak("opening photo")
            # music_dir = "G:\\Song"
            photo_dir = "C:\\Users\\Shadow_Mano\\Pictures"
            photo = os.listdir(photo_dir)
            print(photo)


        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            print("I am fine, Thank you")
            speak("What about you, I think, your always ultimate ")
            print("What about you, I think your always ultimate ")

        elif 'fine' in query or "good" in query:
            speak("Yes i known, your always ultimate")
            print("Yes i known, your always ultimate")

        elif 'not fine' in query or "not good" in query:
            speak("Don't worry about failure; you only have to be right once.")
            print("Don't worry about failure; you only have to be right once.")
        
        elif "open" in query:
            from Dictapp import openappweb
            openappweb(query)

        elif "close" in query:
            from Dictapp import closeappweb
            closeappweb(query)

        elif 'hi' in query or "hello" in query:
            speak("Hi there.If if you're in the mood for something, musical, that's a little classical,just say play song")
            print("Hi there.If if you're in the mood for something, musical, that's a little classical,just say play song")


        elif "who are you" in query:
            speak("I am your virtual assistant created by Manoj")
            print("I am your virtual assistant created by Manoj")

        elif "who are you doing" in query:
            speak("I'm thinking in riddles! join in and ask me for one.")
            print("I'm thinking in riddles! join in and ask me for one.")

        elif "did you eat" in query:
            speak("while i appreciate great food, my good taste is better reflected in the compay i keep")
            print("while i appreciate great food, my good taste is better reflected in the compay i keep")

        elif "I love you" in query:
            speak("That's really nice, thanks")
            print("That's really nice, thanks")


        elif "who i am" in query or "Who am i" in query:
            speak("If you talk then definitely your human.")
            print("If you talk then definitely your human.")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak('Liger')
            print("My friends call me,Liger")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Liger from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Liger Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open('Liger.txt', 'w')
            speak(" Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("Liger.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'news' in query:

            try:
                jsonObj = urlopen(
'https://newsapi.org/v2/everything?q=tesla&from=2022-12-22&sortBy=publishedAt&apiKey=8b67177780fd4bb08e7ec4d205e5b365')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))

        elif "send message " in query:
            # You need to create an account on Twilio to use this service
            account_sid = 'AC4354b9af24392b25340189ce6a9c09a9'
            auth_token = 'USbb9607433c1482c0cf323e13ddbaf56f'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body=takeCommand(),
                from_='Sender No',
                to='Receiver No'
            )

            print(message.sid)


        elif 'what' in query:

            client = wolframalpha.Client("UH54WQ-895PPQ895A")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif 'how' in query:

            client = wolframalpha.Client("UH54WQ-895PPQ895A")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif 'where' in query:

            client = wolframalpha.Client("UH54WQ-895PPQ895A")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif 'when' in query:

            client = wolframalpha.Client("UH54WQ-895PPQ895A")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "1cf7847e2378fab42d6778a04c7ba380"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")
        


        elif 'calculate' in query:

            client = wolframalpha.Client("UH54WQ-895PPQ895A")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")


       
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('The current time is' + time)
            print(time)
        elif 'date' in query:
            date = datetime.datetime.now().strftime('%d-%m-%Y')
            speak('The current date is' + date)
            print(date)
        elif 'day' in query:
            day = datetime.datetime.now().strftime('%A')
            speak('The current day is' + day)
            print(day)

    # elif "" in query:
    # Command go here
    # For adding more commands


