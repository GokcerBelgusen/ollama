import pyttsx3

# Initialize with 'espeak' driver explicitly
engine = pyttsx3.init()
engine.say("Welcome!")
engine.runAndWait()
