import speech_recognition as sr    # Used to convert speech into text.
import webbrowser                  #  Opens URLs in the web browser.
import pyttsx3                     # Text-to-speech library for generating speech.
import musicLibrary                # A custom module containing a dictionary with song names and their corresponding URLs.
import requests                    # Makes HTTP requests (used for fetching news).
from openai import OpenAI          #  Used to interact with OpenAI's GPT model.
from gtts import gTTS              # Google Text-to-Speech library for generating speech.
import pygame                      # Plays MP3 files (used for text-to-speech playback).
import os                          # Interacts with the operating system, e.g., deleting temporary files.

# pip install pocketsphinx

recognizer = sr.Recognizer()                        # An instance of the speech recognizer.
engine = pyttsx3.init()                             # initializes the pyttsx3 text-to-speech engine.
newsapi = "d09305Bd72bc40248998159804e0e67d"        # API key for the NewsAPI service to fetch news headlines.

def speak_old(text):                # Uses pyttsx3 to convert text to speech but isn't used in this implementation
    engine.say(text)               
    engine.runAndWait()

def speak(text):        # this one is used to convert speech using google text to speech
    tts = gTTS(text)
    tts.save('temp.mp3')         # Saves the speech as an MP3 file.

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')       

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")                      # Waits for playback to finish and deletes the temporary file.

def aiProcess(command):                         # aiProcess: Sends the user’s command to OpenAI’s GPT-3.5 model and returns the response.
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():                          # Checks the command and performs specific actions:
        webbrowser.open("https://facebook.com")                 # Opens websites like Google, Facebook, YouTube, or LinkedIn.
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):                          # Plays a song by fetching its URL from the musicLibrary
        song = c.lower().split(" ")[1]            # to find song we lower the command in which song name is given , convert it into list , split it and use element at 1 index = song
        link = musicLibrary.music[song]           # take link of song and open it by webrowser then
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")                  # Fetches top news headlines using the NewsAPI and reads them aloud.
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the request (For unrecognized commands, passes the command to OpenAI’s GPT model for a response.)
        output = aiProcess(c)
        speak(output) 





if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):        # Listens for the wake word ("hi") using speech recognition.If detected, activates Jarvis
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)          # Once activated, listens for a command, processes it, and performs the requested action.
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))          # Handles any exceptions (e.g., microphone not accessible, API errors) and prints the error message.


# Applications :
# Interactive virtual assistants.
# Knowledge retrieval and question-answering systems.
# Task-oriented bots for various domains.
  