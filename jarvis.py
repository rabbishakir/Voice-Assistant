import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import webbrowser
import subprocess
import random
import wikipedia

# loggin configuration

LOG_DIR = "Logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)



def speak(text):
    """
    This function converts text to voice
    
    :param 
        text
    :retun 
        voice
    """
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print("user said", query)
    except Exception as e:
        print(e)

    return query


speak("Hello Sir, My Name is jervis. I am your personal assistant")

while True:
    query = takeCommand()
    
    if query is None:
        continue
    
    if "exit" in query or "quit" in query or "stop" in query:
        speak("Goodbye Sir")
        logging.info("Assistant stopped by user")
        break
    
    print(f"Repeating: {query}")
    speak(query)
    logging.info(f"Repeated: {query}")



