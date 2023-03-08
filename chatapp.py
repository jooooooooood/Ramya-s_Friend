import speech_recognition as sr
import openai
from gtts import gTTS
import os
from playsound import playsound

# Initialize the OpenAI API
openai.api_key = "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"

# Initialize the recognizer class from the speech_recognition library
r = sr.Recognizer()

# Function to transcribe audio input from the microphone
def transcribe_audio():
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, None)

    # Transcribe the audio
    transcribed_text = r.recognize_google(audio)
    return transcribed_text

def speak_response(response):
    tts = gTTS(response)
    tts.save("ada_response.mp3")

    # Hardcoded the path name here,, fix later
    playsound("C:/Users/mclar/Downloads/OpenAI_API/ada_response.mp3")

# Continuously prompt the user for input
while True:
    # Transcribe audio input
    user_input = transcribe_audio()
    if (user_input == 'exit' or user_input == 'goodbye'):
        break 

    # Generate a response using the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{user_input}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.95,
    ).get("choices")[0].get("text")

    print(f"Ada: {response}")
    speak_response(response)
