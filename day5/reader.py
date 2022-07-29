import playsound
import os
import random
from gtts import gTTS

def scoutbot_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 100000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def add_text(file_name, x):
    f = open(file_name,"w")
    f.write(x)

string_input = input(":\n")
enter = input("Enter to start.")
scoutbot_speak(string_input)