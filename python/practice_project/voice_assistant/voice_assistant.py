# Project 14
# Voice Assistant AI - Step 1
# Text to Speech Assistant

import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

print("🎤 Voice Assistant Started")

speak("Hello Sandeep, I am your voice assistant.")

speak("Today we are starting Project 14.")

speak("This project will help you learn speech AI.")