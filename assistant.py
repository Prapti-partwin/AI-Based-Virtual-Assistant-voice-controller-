# assistant.py
import os
import time
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Setup TTS engine (pyttsx3)
tts_engine = pyttsx3.init()
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Setup speech recognizer
recognizer = sr.Recognizer()

def listen_from_mic(timeout=5, phrase_time_limit=7):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        print("Listening...")
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None
    except sr.RequestError as e:
        print("Speech service error:", e)
        return None

# ⭐ UPDATED GPT FUNCTION (new API + new model)
def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    
    except Exception as e:
        print("GPT error:", e)
        return "Sorry, an error occurred."

def main():
    speak("Hello! I am your assistant. Say 'exit' to quit.")
    
    while True:
        user_text = listen_from_mic()
        if not user_text:
            continue
        
        if user_text.lower() in ("exit", "quit", "goodbye"):
            speak("Goodbye!")
            break

        reply = ask_gpt(user_text)
        print("Assistant:", reply)
        speak(reply)
        time.sleep(0.3)

if __name__ == "__main__":
    main()
