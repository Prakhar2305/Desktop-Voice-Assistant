# from pip import main
import pyttsx3  # Used for speaking the output from the device
import speech_recognition as sr  # Used for recognising the speech and returning a string output
import pyaudio
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')   # Engine consists of the voices which we further take and helps in speaking as well
voices = engine.getProperty('voices')
# print(voices[1].id)   We can print the voice id using this 
voices = engine.setProperty('voice', voices[1].id) # currently we have 2 ids for voices which can be used and using set property we set a voice

def speak(audio):
    engine.say(audio)   # Used for saying the audio and audio here is a string 
    engine.runAndWait() # Must use function.. Audio doesn't work without using this function

def greet():
    h = int(datetime.datetime.now().hour)
    if(h>=0 and h<12):
        speak("Good Morning")
    elif(h>=12 and h<16):
        speak("Good Afternoon")
    elif(h>=16 and h<20):
        speak("Good Evening")    
    else:
        speak("Good Night")

    speak("Hey there, I am Jarvis but the better version.")  


def take_command():
    # Used for taking an audio input from the user and converts it to a string
    r = sr.Recognizer()   
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thershold = 1 # Seconds of non-speaking time before an audio is considered complete. 
        r.energy_thershold = 500 # Minimum amount of audio energy required for the audio to be heard
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please..")
        return "None"
    return query

if __name__ == "__main__":
    greet()
    speak("I am a dekstop voice assistant.")
    while True:
        query = take_command().lower()

        if "wikipedia" in query:
            speak("Searching in wikipedia...")
            query = query.replace("wikipedia", "")
            answer = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(answer)
            speak(answer)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open leetcode" in query:
            webbrowser.open("leetcode.com")    
