import speech_recognition as sr
sr.__version__
r = sr.Recognizer()
# r.recognize_google(audio)
harvard = sr.AudioFile("harvard.wav")
with harvard as source:
    audio = r.record(source)


type(audio)
r.recognize_google(audio)

with harvard as source:
    audio = r.record(source, duration=4)

r.recognize_google(audio)
