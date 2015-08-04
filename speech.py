import speech_recognition as sr
from subfunction import *
from time import sleep

r = sr.Recognizer()
r.energy_threshold = 5000
#call(["playerctl", "play-pause"])
cont = 1
inp = 0
while(cont!=0):
     with sr.Microphone() as source:
          r.adjust_for_ambient_noise(source)
          speak("Ask me something")
          sleep(1)
          print("I'm listening actively now")# use the defanult microphone as the audio source
          audio = r.listen(source,10)                   # listen for the first phrase and extract it into audio data
          print("I finished listening")
     
     try:
          a = r.recognize(audio)
          cont = recognize(a,inp)
          inp = cont
          print("You said " + a)    # recognize speech using Google Speech Recognition
     except LookupError:                            # speech is unintelligible
          speak("Could not understand audio")
#call(["playerctl", "play-pause"])


