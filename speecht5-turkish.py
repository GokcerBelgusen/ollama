from transformers import VitsModel, AutoTokenizer
from IPython.display import Audio
import torch
import soundfile as sf

model = VitsModel.from_pretrained("facebook/mms-tts-tur")
model = model.half()  # Convert model to half precision

tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-tur")

text = "Kara delik, çok güçlü bir yerçekimine sahip olan, ışığın bile kaçamadığı kozmik cisimlerdir. Büyük bir kütlenin çok küçük bir alana sıkışmasıyla oluşurlar. Genellikle devasa yıldızların ömrünün sonuna geldiğinde çökmesiyle meydana gelirler. Kara deliklerin olay ufku adı verilen bir sınırları vardır; bu sınırdan içeri giren hiçbir şey, ışık dahi, dışarı çıkamaz. Kara delikler, evrenin en gizemli ve en yoğun nesnelerinden biridir."

inputs = tokenizer(text, return_tensors="pt")
inputs = inputs.to(torch.float16)

with torch.no_grad():
    output = model(**inputs).waveform

# Define output filename
output_filename = "output-tr.wav"

# Save the generated audio waveform to a file (assuming the waveform is 1D tensor)
sf.write(output_filename, output.squeeze().cpu().numpy(), model.config.sampling_rate)

print(f"Audio saved to {output_filename}")

Audio(output, rate=model.config.sampling_rate)
