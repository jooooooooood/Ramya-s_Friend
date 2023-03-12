import speech_recognition as sr
import openai
from gtts import gTTS
from playsound import playsound
import os

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
    response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": user_input}
  ]
)
    print(f"Ada: {response.choices[0].message.content}")
    speak_response(response.choices[0].message.content)

