import os
import librosa as lr
import numpy as np

def filter_audio(path, max_size=40_000_000, min_size=10_000_000):
    """Function that filters the audio files to keep the ones with the required lenght only"""
    audio = []
    for file in os.scandir(path):
        if os.stat(file).st_size < max_size and os.stat(file).st_size > min_size:     #os.stat(file).st_size
            file, sr = lr.load(file)
            audio.append(np.array(file))
    return audio
