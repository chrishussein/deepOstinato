import os
from midi2audio import FluidSynth

# Change to class

def midi_to_audio(input_path, ouput_path):
    fs = FluidSynth('MuseScore_General.sf2')
    for file in os.listdir(input_path):
        file = file.strip('.mid')
        input_file = os.path.join(input_path, f"{file}.mid")
        output_file = os.path.join(ouput_path, f"{file}.wav")
        fs.midi_to_audio(input_file, output_file)
    return "Conversion completed"
