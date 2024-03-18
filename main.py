# -*- coding: utf-8 -*-

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Simba' in command:
                command = command.replace('Simba', '')
                print(command)

    except:
        command = "Microphone Failed"
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    song = command.replace('play', '')
    if "play" in command:
        talk("playing" + song)
        print(song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("the time is now " + time)
    elif "google" in command:
        wiki = command.replace('google', '')
        try:
                    info = wikipedia.summary(wiki, 2)
        except:info = "Could not find any information on wikipedia on " + wiki
        print(info)
        talk(info)
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)        
    else:
        talk("Sorry, I didn't catch that.")
        
while True:
    run_alexa()
print("done")