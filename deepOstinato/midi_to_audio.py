import os
from midi2audio import FluidSynth

# Change to class
fs = FluidSynth('MuseScore_General.sf2')
for filename in os.listdir("midis_composersA_B"):
    filename = filename.strip('.mid')
    print(filename)
    fs.midi_to_audio(f'midis/{filename}.mid', f'raw_data/midi2audio/{filename}.wav')
