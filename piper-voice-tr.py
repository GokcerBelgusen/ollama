# Text-To-Speech Translation with Piper TTS (Stream) and Python 
# TechMakerAI on YouTube

import numpy as np
from piper import PiperVoice
import sounddevice as sd

voice = PiperVoice.load('/home/pi/ollama/voice/tr_TR-dfki-medium.onnx', 
	config_path='/home/pi/ollama/voice/tr_TR_dfki_medium_tr_TR-dfki-medium.onnx.json')

# Configure sounddevice buffer size and latency
sd.default.blocksize = 8192  # Set a larger block size to reduce underruns
sd.default.latency = 'low'   # Use low latency for real-time playback


text = "Kara delik, çok güçlü bir yerçekimine sahip olan, ışığın bile kaçamadığı kozmik cisimlerdir. Büyük bir kütlenin çok küçük bir alana sıkışmasıyla oluşurlar. Genellikle devasa yıldızların ömrünün sonuna geldiğinde çökmesiyle meydana gelirler. Kara deliklerin olay ufku adı verilen bir sınırları vardır; bu sınırdan içeri giren hiçbir şey, ışık dahi, dışarı çıkamaz. Kara delikler, evrenin en gizemli ve en yoğun nesnelerinden biridir."

# Create a sounddevice stream  
stream = sd.OutputStream(samplerate=22050, channels=1, dtype='int16')
stream.start()

for audio_bytes in voice.synthesize_stream_raw(text):
    int_data = np.frombuffer(audio_bytes, dtype=np.int16)
    stream.write(int_data)

stream.stop()
stream.close()

