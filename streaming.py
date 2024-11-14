from langchain.callbacks.base import BaseCallbackHandler
from langchain_ollama import OllamaLLM
from pathlib import Path
from openai import OpenAI
import subprocess
import random
import numpy as np
from piper import PiperVoice
import sounddevice as sd
import time

voice = PiperVoice.load('/home/pi/ollama/voice/en_GB-alan-medium.onnx',
        config_path='/home/pi/ollama/voice/en_GB-alan-medium.onnx.json')


class StreamingCallbackHandler(BaseCallbackHandler):
    def __init__(self):
        self.partial_output = ""

    def on_llm_new_token(self, token: str, **kwargs: any) -> None:
        self.partial_output += token
        print(token, end="", flush=True)

llm = OllamaLLM(model="llama3.2", callbacks=[StreamingCallbackHandler()])

question = "Tell me about The extinction of dinosaurs , how it happened ?"

response = llm.invoke(question)

# Create a sounddevice stream  
stream = sd.OutputStream(samplerate=22050, channels=1, dtype='int16')
stream.start()

for audio_bytes in voice.synthesize_stream_raw(response):
    int_data = np.frombuffer(audio_bytes, dtype=np.int16)
    stream.write(int_data)

stream.stop()
stream.close()

exit()

options = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
voice = random.choice(options)

client = OpenAI()

# Ses dosyasının yolunu belirtin
speech_file_path = Path(__file__).parent / "output.mp3"

# OpenAI TTS API'si ile ses dosyasını oluşturun
response = client.audio.speech.create(
    model="tts-1",
    voice=voice,
    input=response
)

# Ses dosyasını dosyaya yazın
response.stream_to_file(speech_file_path)

# MP3 dosyasını mpg123 ile oynatın
subprocess.run([ "mpg123", str(speech_file_path)])

