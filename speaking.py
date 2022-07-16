from gtts import gTTS
import os
#For gTTS, TEXT to Speking
#For OS, saving on the system


def speaking():
    speak=gTTS(text="Welcome to SIRI Prototype",lang='en',slow=False)
    speak.save("deneme.mp3")
    os.system("deneme.mp3")
speaking()
