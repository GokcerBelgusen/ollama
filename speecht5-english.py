from transformers import VitsModel, AutoTokenizer
from IPython.display import Audio
import torch
import soundfile as sf

model = VitsModel.from_pretrained("facebook/mms-tts-eng")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")

text = "A black hole is a region of spacetime wherein gravity is so strong that no matter or electromagnetic energy (e.g. light) can escape it. Albert Einstein's theory of general relativity predicts that a sufficiently compact mass can deform spacetime to form a black hole. The boundary of no escape is called the event horizon. A black hole has a great effect on the fate and circumstances of an object crossing it, but it has no locally detectable features according to general relativity. In many ways, a black hole acts like an ideal black body, as it reflects no light. Quantum field theory in curved spacetime predicts that event horizons emit Hawking radiation, with the same spectrum as a black body of a temperature inversely proportional to its mass. This temperature is of the order of billionths of a kelvin for stellar black holes, making it essentially impossible to observe directly."

inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    output = model(**inputs).waveform

# Define output filename
output_filename = "output-en.wav"

# Save the generated audio waveform to a file (assuming the waveform is 1D tensor)
sf.write(output_filename, output.squeeze().cpu().numpy(), model.config.sampling_rate)

print(f"Audio saved to {output_filename}")

Audio(output, rate=model.config.sampling_rate)
