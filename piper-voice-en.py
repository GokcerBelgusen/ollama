# Text-To-Speech Translation with Piper TTS (Stream) and Python 
# TechMakerAI on YouTube

import numpy as np
from piper import PiperVoice
import sounddevice as sd

voice = PiperVoice.load('/home/pi/ollama/voice/en_GB-alan-medium.onnx', 
	config_path='/home/pi/ollama/voice/en_GB-alan-medium.onnx.json')

text = "A black hole is a region of spacetime wherein gravity is so strong that no matter or electromagnetic energy (e.g. light) can escape it. Albert Einstein's theory of general relativity predicts that a sufficiently compact mass can deform spacetime to form a black hole. The boundary of no escape is called the event horizon. A black hole has a great effect on the fate and circumstances of an object crossing it, but it has no locally detectable features according to general relativity. In many ways, a black hole acts like an ideal black body, as it reflects no light. Quantum field theory in curved spacetime predicts that event horizons emit Hawking radiation, with the same spectrum as a black body of a temperature inversely proportional to its mass. This temperature is of the order of billionths of a kelvin for stellar black holes, making it essentially impossible to observe directly. "

# Create a sounddevice stream  
stream = sd.OutputStream(samplerate=22050, channels=1, dtype='int16')
stream.start()

for audio_bytes in voice.synthesize_stream_raw(text):
    int_data = np.frombuffer(audio_bytes, dtype=np.int16)
    stream.write(int_data)

stream.stop()
stream.close()

