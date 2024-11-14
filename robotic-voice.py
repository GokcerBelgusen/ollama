import pyaudio
import pyttsx3
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Configure engine to use pyaudio as the output
engine.setProperty('rate', 110)  # Set desired speech rate

# Configure pyaudio to output to Bluetooth device index 5
device_index = 5  # Replace with the correct Bluetooth device index

# Initialize PyAudio and open a stream for Bluetooth output
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=24000, output=True, output_device_index=device_index)

def on_audio_output(audio):
    # Write audio data directly to the Bluetooth stream
    stream.write(audio)

# Use callback to send audio data to Bluetooth device
engine.connect("finished-utterance", lambda name, completed: stream.stop_stream())
engine.say("A black hole is a region of spacetime where gravity is so strong that nothing, not even light and other electromagnetic waves, is capable of possessing enough energy to escape it.")
engine.runAndWait()

time.sleep(20)

# Close the stream and terminate PyAudio
stream.close()
p.terminate()

